
import string
import serial
import time
from threading import Thread,Lock,Condition
from .drive import DriveTask,LMCPidControlTypes
import logging
from .errors import LMCCommandError,LMCCommunicationError
from enum import Enum

class LMCEventType(Enum):
    """Enum for types of events that the LMC may post"""
    READY = "ready" # LMC is fully initialized and ready to receive commands

    # drive results
    DRIVE_SUCCESS = "d_success"
    DRIVE_FAILED = "d_failed"
    DRIVE_SPLINE_AT_POINT = "d_spoint"
    DRIVE_REJECTED = "d_rejected"

    SYS_FAILURE = "sysfail" # The LMC has a problem from which it cannot recover, and is unable to drive or localize

class LMCParameters(Enum):
    """Enum for parameter variables that can be read/set from the LMC using the 'get' and 'set' commands"""
    SEND_STATUS = "sendstatus" # values: 1 (st messages are sent continuously) or 0 (no status messages are sent)
    COLLISIONS_ENABLED = "coll" # values: 1 (enabled) or 0 (disabled)
    LASER_POSE_ENABLED = "lcpose" # values: 1 (enabled) or 0 (disabled)
    WEIGHT = "weight" # value: weight in kg (float)
    MOMENT_OF_INERTIA = "momin" # value: moment of inertia in (Nm/s/s/rad) (float)

class LMCStatus:
    """
    Class encapsulating the LMC's current status, as received by the LMC status messages
    """
    def __init__(self, message:list[str]) -> None:
        pass #TODO

class LMCConnection:
    """
    Class handling the serial connection between control computer and LMC
    Responsibilities include:
    - Spawn a thread for LMC communication and provide a thread-safe interface
    - initial connection establishment and link check
    - automatic reconnection in case of link break
    - keeping track of the currently run command and prevent sending two commands at the same time
    - basic parsing of incoming messages:
        - ok messages: split return value list and provide to caller
        - error messages: split error message and throw appropriate exception
        - evt and st messages: forward to appropriate callback
    - providing functions for composing all commands programatically
    """

    # Timeout for synchronous commands (waiting for a response from LMC)
    commandResponseTimeout = 0.5

    # The logger instance to log messages to (needs to be provided)
    logger:logging.Logger = None

    # Device to connect to (passed to serial_for_url)
    device:string = None

    # The serial connection object
    conn:serial.Serial = None

    # reader thread
    readerThread:Thread = None

    # variable telling the connection has been started (may not do certain things afterwards)
    isInitialized = False

    # various threading locks and inter-thread messaging
    RTSyncSignallingLock:Lock = None # Lock for inter-thread communication between readerThread and synchronous commands
    RTSyncSignallingCV:Condition = None # Condition variable for this
    # This CV guards the following variables:
    commandResponse:list[str] = None # The response of the last command executed
    isConnected = False # Whether the LMC connection is active
    connectionFault = None # an unrecoverable connection fault has occured (variable holds last exception)

    syncCommandLock:Lock = None # prevents multiple threads from issuing commands simultaneously

    # current LMC status
    lmcStatusLock:Lock = None
    lmcStatus:LMCStatus = None

    # callback functions
    # registered callbacks for status messages
    statusCallbacks = None
    # registered callbacks for events
    eventCallbacks = None

    def __init__(self, device:string = "/dev/LMC", logger:logging.Logger = None):
        self.device = device
        # init threading stuff
        self.RTSyncSignallingLock = Lock()
        self.RTSyncSignallingCV = Condition(self.RTSyncSignallingLock);
        self.syncCommandLock = Lock()
        self.lmcStatusLock = Lock()
        if logger is not None:
            self.logger = logger
        else:
            self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        strh = logging.StreamHandler()
        strh.setLevel(logging.DEBUG)
        self.logger.addHandler(strh)

        self.statusCallbacks = [];
        self.eventCallbacks = [];

        self.logger.info("LMC communication created (device "+self.device+")")
        self.conn = serial.serial_for_url(self.device, do_not_open = True)

    def startConnection(self):
        """
        Start the LMC communication interface and connect to the LMC
        Callbacks must be registered before calling this function
        """
        # Reset reader thread variables
        with self.RTSyncSignallingCV:
            if self.isConnected:
                raise RuntimeError("Cannot re-start already connected LMC Connection")
            self.connectionFault = None
            self.commandResponse = None
            self.isConnected = False
        if self.conn.isOpen:
            self.conn.close()
        self.logger.info("Starting LMC connection...")
        self.readerThread = Thread(target=self.readerThreadMain, name="LMC Reader Thread", daemon=True)
        self.readerThread.start()
        # wait until connection is established
        with self.RTSyncSignallingCV:
            while not self.isConnected and self.connectionFault is None:
                self.RTSyncSignallingCV.wait()
            if self.connectionFault is not None:
                raise LMCCommunicationError("LMC connection couldn't be started:"+str(self.connectionFault))
        self.isInitialized = True

    
    def addStatusCallback(self, callback):
        """
        Add a callback function that is called whenever the LMC posts a Status message
        Callback function signature is: callback(lmcStatus: LMCStatus)
        Must be called before initAndConnect()
        Be aware that the callback functions get called from the LMC reader thread!
        """
        if self.isInitialized:
            raise RuntimeError("Cannot add callbacks to already started LMC Connection")
        self.statusCallbacks.append(callback)
    def addEventCallback(self, callback):
        """
        Add a callback function that is called whenever the LMC posts an Event
        Callback function signature is: callback(evtType: LMCEventType, evtData: List of Strings)
        Must be called before initAndConnect()
        Be aware that the callback functions get called from the LMC reader thread!
        """
        if self.isInitialized:
            raise RuntimeError("Cannot add callbacks to already started LMC Connection")
        self.eventCallbacks.append(callback)

    def getParameter(self, param:LMCParameters):
        """Retrieve a parameter from the LMC"""
        answer = self.syncCommand(f"get {param.value}")
        return answer[0]

    def setParameter(self, param:LMCParameters, value):
        """Set a parameter on the LMC"""
        self.syncCommand(f"set {param.value} {value}")
        return

    def issueDriveTask(self, driveTask:DriveTask):
        """
        Issues the given DriveTask to the LMC.
        Does not await the completion of the drive task
        """
        driveTask.execute(self)
        return

    def setPidParameters(self, controlType:LMCPidControlTypes, kr:float, ti:float, td:float, frict_offset:float = 0):
        """
        Set the PID parameters of the given PID control
        Kr, Ti, Td: TODO
        frict_offset: Unit is N for translational, Nm for rotational controls, ignored for current control
        """
        self.syncCommand(f"setpid {controlType.value} {kr} {ti} {td} {frict_offset}")

    def setKanayamaGain(self, tang:float, norm:float, rot:float):
        """
        Set the parameters of the Kanayama algorithm
        Details: TODO
        """
        self.syncCommand(f"setkanayama {tang} {norm} {rot}")

    def setOdometryCalibration(self, left_radius:float, right_radius:float, wheel_dist:float):
        """
        Set the odometry calibration values (wheel radii and distance)
        Units are mm
        """
        self.syncCommand(f"setodometry {left_radius} {right_radius} {wheel_dist}")

    def getLmcStatus(self):
        """
        Get the current LMC status, as received by the last status message from the LMC
        """
        with self.lmcStatusLock:
            status = self.lmcStatus
        return status

    def fetchLmcStatus(self):
        """
        Synchronously fetch the LMC status (using st command)
        """
        #TODO implement on LMC side
        st = self.syncCommand("st")
        status = LMCStatus(st)
        # update status var
        with self.lmcStatusLock:
            self.lmcStatus = status
        return status

    def syncCommand(self, command:str, timeout:float = 2):
        """
        Sends the given command to the LMC and blocks until an answer is received.
        If the answer is 'ok', returns a list of strings representing the returned values
        If the answer is 'err', raises an exception
        """
        if not self.isInitialized:
            raise RuntimeError("LMC Connection is not started (call startConnection() first)")
        with self.syncCommandLock: # only one command at a time!
            # wait for reader thread availability (do not attempt things during reconnection)
            with self.RTSyncSignallingCV: # acquire the condition variable
                # check if the connection is severed
                if self.connectionFault is not None:
                    raise LMCCommunicationError("LMC connection has fault:"+str(self.connectionFault))
                if not self.isConnected:
                    raise LMCCommunicationError("LMC is not connected, call startConnection() first!")
                try:
                    # write the command on the wire
                    self.conn.write(command.encode('ascii') + b'\n')
                except serial.SerialException as e:
                    self.logger.warning("syncCommand: Sending command failed: "+str(e))
                    raise LMCCommunicationError("syncCommand: Serial connection error: "+str(e))
                # wait for an answer
                self.commandResponse = None # we have the lock, so this is safe to do
                while self.commandResponse is None \
                        and self.connectionFault is None:
                    # If the condition variable wait times out, throw an error
                    notimeout = self.RTSyncSignallingCV.wait(timeout)
                    if not notimeout:
                        raise LMCCommunicationError("syncCommand: Response timed out!")
                # A connection breakage cause a wakeup
                if self.connectionFault is not None:
                    raise LMCCommunicationError("LMC connection has fault:"+str(self.connectionFault))
                # now the command response is in the commandResponse variable. We have the RTSyncSignallingCV lock again, so this is thread safe.
                cmdResponse = self.commandResponse
                # If it is an error, then throw it
                if cmdResponse[0] == "err":
                    raise LMCCommandError(cmdResponse[1])
                # otherwise, return OK to the caller
                return cmdResponse[1:]

    def readerThreadMain(self):
        """
        Main function of the reader thread
        The reader thread reads the replies, events and status messages of the LMC
        """
        # aquire the sync lock, so that other threads to not attempt to start commands during reconnection
        try:
            self.conn.open()
            # Connection self test, run an echo command
            # remove nonsense from the wire and turn off statuses temporarily
            self.conn.write("\n\n\n".encode('ascii'))
            # wait a moment for LMC to process it
            time.sleep(0.2)
            self.conn.read_all() # empty buffer
            #self.conn.write("version\n".encode('ascii'))
            #line = self.conn.readline().decode('ascii')
            #if line.startswith("ok"):
            #    self.logger.info("LMC reports version: "+line)
            #else:
            #    raise RuntimeError(f"LMC version check failed, got '{line}'")
            # successful
        except Exception as e:
            self.logger.critical(f"Connecting to LMC failed : {str(e)}")
            with self.RTSyncSignallingCV:
                self.connectionFault = e
                self.RTSyncSignallingCV.notify_all()
            return
        # The connection was successful. Make LMC available to syncCommand and enter read loop
        self.logger.info("LMC connected successfully!")
        with self.RTSyncSignallingCV:
            self.isConnected = True
            self.RTSyncSignallingCV.notify_all()
        try:
            while True:
                # inner loop: continuous read
                self.logger.debug("LMC Reader Thread: Now entering blocking read")
                pkt = self.conn.read_until(b'\n')
                pktstr = pkt.decode('ascii', 'replace')
                self.logger.debug("LMC Reader Thread: received packet: "+pktstr)
                pktsplit = pktstr.split()
                #branch depending on message type
                if pktsplit[0] == "ok" or pktsplit[0] == "err":
                    # Command response
                    self.logger.debug("LMC Reader Thread: Signaling command response")
                    with self.RTSyncSignallingCV:
                        self.commandResponse = pktsplit
                        self.connectionBroken = None # no error
                        self.RTSyncSignallingCV.notify_all()
                    self.logger.debug("LMC Reader Thread: Response Event signaled")
                elif pktsplit[0] == "evt":
                    self.logger.info("LMC event received: "+pktstr)
                    for cb in self.eventCallbacks:
                        cb(pktsplit[1:])
                elif pktsplit[0] == "st":
                    status = LMCStatus(pktsplit[1:])
                    # update status variable
                    with self.lmcStatusLock:
                        self.lmcStatus = status
                    # call callbacks
                    for cb in self.statusCallbacks:
                        cb(status)
                else:
                    self.logger.warning("Unknown answer opcode received from lmc: "+pktstr)
            # end inner loop
        except serial.SerialException as e:
            self.logger.critical(f"LMC Connection lost: {str(e)}")
            # If a synchronous command is already in the making, we need to wake it up
            with self.RTSyncSignallingCV:
                self.connectionFault = e
                self.commandResponse = None
                self.isConnected = False
                self.RTSyncSignallingCV.notify_all()
            # reader thread exits
                
                

