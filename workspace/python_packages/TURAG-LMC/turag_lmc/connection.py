# TURAG-LMC: Python package to interface with the TURAG drive platform controller (LMC)
# Copyright (C) 2022-2023 TURAG e.V.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import string
import serial
import time
import typing
from threading import Thread, Lock, Condition
from .drive import DriveTask, LMCPidControlTypes
from .status import LMCStatus
import logging
from enum import Enum
import queue


class LMCError(Exception):
    """
    General superclass for errors related to the LMC communication
    """

    pass


class LMCCommunicationError(LMCError):
    """
    Errors regarding the communication link between Host and LMC, e.g. an IO error or link break
    """

    pass


class LMCCommandError(LMCError):
    """
    Errors in command execution (invalid/out of range values, missing parameters etc.)
    Corresponds to "err" messages from the LMC.
    """

    pass


class LMCEventType(Enum):
    """Enum for types of events that the LMC may post"""

    READY = "ready"  # LMC is fully initialized and ready to receive commands

    # drive results
    DRIVE_SUCCESS = "d_success"
    DRIVE_FAILED = "d_failed"
    DRIVE_SPLINE_AT_POINT = "d_spoint"
    DRIVE_REJECTED = "d_rejected"

    SYS_FAILURE = "sysfail"  # The LMC has a problem from which it cannot recover, and is unable to drive or localize


class LMCParameters(Enum):
    """Enum for parameter variables that can be read/set from the LMC using the 'get' and 'set' commands"""

    # (not implemented yet) SEND_STATUS = "sendstatus" # values: 1 (st messages are sent continuously) or 0 (no status messages are sent)
    COLLISIONS_ENABLED = "coll"  # values: 1 (enabled) or 0 (disabled)
    LASER_POSE_ENABLED = "lcpose"  # values: 1 (enabled) or 0 (disabled)
    WEIGHT = "weight"  # value: weight in kg (float)
    MOMENT_OF_INERTIA = "momin"  # value: moment of inertia in (Nm/s/s/rad) (float)


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
    logger: logging.Logger = None

    # Device to connect to (passed to serial_for_url)
    device: string = None

    # The serial connection object
    conn: serial.Serial = None

    # reader thread
    readerThread: Thread = None

    # various threading locks and inter-thread messaging
    RTSyncSignallingLock: Lock = None  # Lock for inter-thread communication between readerThread and synchronous commands
    RTSyncSignallingCV: Condition = None  # Condition variable for this
    # This CV guards the following variables:
    commandResponse: list = None  # The response of the last command executed
    isConnected = False  # Whether the LMC connection is active
    connectionFault = None  # an unrecoverable connection fault has occured (variable holds last exception)

    syncCommandLock: Lock = (
        None  # prevents multiple threads from issuing commands simultaneously
    )

    eventQueue: queue.Queue = None

    # current LMC status
    # not needed right now, because LMC doesn't actively send status.
    # lmcStatusLock:Lock = None
    # lmcStatus:LMCStatus = None

    def __init__(self, device: string = "/dev/LMC", logger: logging.Logger = None):
        """
        Create a new LMC Connection. This just creates the object, the connection must be explicitly established using startConnection().
        Parameters:
        device: the path or identifier of the device to connect to. See the pyserial documentation for possible formats (serial.serial_for_url()).
        logger: The python Logger instance to use to log LMC messages. If not provided, a default logger will be created that prints to stderr with log level INFO.
        """
        self.device = device
        # init threading stuff
        self.RTSyncSignallingLock = Lock()
        self.RTSyncSignallingCV = Condition(self.RTSyncSignallingLock)
        self.syncCommandLock = Lock()
        self.lmcStatusLock = Lock()
        self.eventQueue = queue.Queue()
        if logger is not None:
            self.logger = logger
        else:
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.DEBUG)
            strh = logging.StreamHandler()
            strh.setLevel(logging.INFO)
            self.logger.addHandler(strh)
        self.conn = serial.serial_for_url(self.device, do_not_open=True)
        self.logger.info("LMC communication created (device " + self.device + ")")

    def startConnection(self):
        """
        (Re-)Start the LMC communication interface and connect to the LMC
        This function must be called after creating the LMCConnection object to connect.

        In case of a link break or other I/O error on the serial link, the interface will stop to work and throw LMCCommunicationErrors
        You can then call startConnection() again to try to reconnect

        This function does not return until a connection is established and the protocol version of the LMC has been confirmed ('version' command).
        If one of these steps fail, this function throws an LMCCommunicationError.
        """
        with self.syncCommandLock:  # we may not enter this while a sync command is being executed
            # Reset reader thread variables
            with self.RTSyncSignallingCV:
                if self.isConnected:
                    raise RuntimeError(
                        "Cannot re-start already connected LMC Connection"
                    )
                self.connectionFault = None
                self.commandResponse = None
                self.isConnected = False
            if self.conn.isOpen:
                self.conn.close()
            self.logger.info("Starting LMC connection...")
            self.readerThread = Thread(
                target=self.readerThreadMain, name="LMC Reader Thread", daemon=True
            )
            self.readerThread.start()
            # wait until connection is established
            with self.RTSyncSignallingCV:
                while not self.isConnected and self.connectionFault is None:
                    self.RTSyncSignallingCV.wait()
                if self.connectionFault is not None:
                    raise LMCCommunicationError(
                        "LMC connection couldn't be started:"
                        + str(self.connectionFault)
                    )

    def getParameter(self, param: LMCParameters):
        """Retrieve a parameter from the LMC"""
        answer = self.syncCommand(f"get {param.value}")
        return answer[0]

    def setParameter(self, param: LMCParameters, value):
        """Set a parameter on the LMC"""
        self.syncCommand(f"set {param.value} {value}")
        return

    def issueDriveTask(self, driveTask: DriveTask):
        """
        Issues the given DriveTask to the LMC.

        A DriveTask is a driving action that the LMC can execute in one go, for example:
        * Drive continuously with a constant velocity (DriveConstantVelocityTask)
        * Drive a certain distance (DriveDistanceTask)
        * Drive to a pose (using the internal odometry) (DrivePoseTask)
        * Drive along a spline of multiple points (DriveSplineTask)

        This function returns immediately after the LMC has accepted the new drive task. It does not block for its completion.

        The completion and result of a drive task is signalled by the DRIVE_ family of events, using the event mechanism (see getNextPendingEvent()).

        Issuing a DriveTask cancels any other active drive task that the LMC may be running at this time. If a queue of drive tasks is required, you need to implement it yourself.
        For example, to drive a triangle (while NOT using a spline), you need to issue 3 DrivePoseTasks in total and, before sending the next one, wait until the DRIVE_SUCCESS event is received.
        Note: As only exception a spline, although comprised of multiple points, is one atomic drive action.
        """
        driveTask.execute(self)
        return

    def setPidParameters(
        self,
        controlType: LMCPidControlTypes,
        kr: float,
        ti: float,
        td: float,
        frict_offset: float = 0,
    ):
        """
        Set the PID parameters of the given PID control
        Kr, Ti, Td: TODO
        frict_offset: Unit is N for translational, Nm for rotational controls, ignored for current control
        """
        self.syncCommand(f"setpid {controlType.value} {kr} {ti} {td} {frict_offset}")

    def setKanayamaGain(self, tang: float, norm: float, rot: float):
        """
        Set the parameters of the Kanayama algorithm
        Details: TODO
        """
        self.syncCommand(f"setkanayama {tang} {norm} {rot}")

    def setOdometryCalibration(
        self, left_radius: float, right_radius: float, wheel_dist: float
    ):
        """
        Set the odometry calibration values (wheel radii and distance)
        Units are mm
        """
        self.syncCommand(f"setodometry {left_radius} {right_radius} {wheel_dist}")

    def fetchLmcStatus(self, extended: bool = False):
        """
        Fetch the current LMC status from the LMC
        The Status contains the operation state and current pose.
        When the "extended" parameter is True, the status also contains information about encoder distance, velocity, force, motor currents and PWM. See the LMCStatus class for more info.
        """
        if extended:
            st = self.syncCommand("stx")
        else:
            st = self.syncCommand("st")
        try:
            return LMCStatus(st)
        except Exception as e:
            raise LMCCommandError("Could not parse LMC status", e)

    def syncCommand(self, command: str, timeout: float = 2):
        """
        Sends the given raw command to the LMC and blocks until an answer is received.
        If the answer is 'ok', returns a list of strings representing the returned values
        If the answer is 'err', raises an LMCCommandException containing the error information.
        """
        with self.syncCommandLock:  # only one command at a time!
            # wait for reader thread availability (do not attempt things during reconnection)
            with self.RTSyncSignallingCV:  # acquire the condition variable
                # check if the connection is severed
                if self.connectionFault is not None:
                    raise LMCCommunicationError(
                        "LMC connection has fault:" + str(self.connectionFault)
                    )
                if not self.isConnected:
                    raise LMCCommunicationError(
                        "LMC is not connected, call startConnection() first!"
                    )
                try:
                    # write the command on the wire
                    self.logger.info("[Host->LMC] " + command)
                    self.conn.write(command.encode("ascii") + b"\n")
                except serial.SerialException as e:
                    self.logger.warning(
                        "syncCommand: Sending command failed: " + str(e)
                    )
                    raise LMCCommunicationError(
                        "syncCommand: Serial connection error: " + str(e)
                    )
                # wait for an answer
                self.commandResponse = None  # we have the lock, so this is safe to do
                while self.commandResponse is None and self.connectionFault is None:
                    # If the condition variable wait times out, throw an error
                    notimeout = self.RTSyncSignallingCV.wait(timeout)
                    if not notimeout:
                        raise LMCCommunicationError("syncCommand: Response timed out!")
                # A connection breakage cause a wakeup
                if self.connectionFault is not None:
                    raise LMCCommunicationError(
                        "LMC connection has fault:" + str(self.connectionFault)
                    )
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
        try:
            self.conn.open()
            # Connection self test, run an echo command
            # remove nonsense from the wire and turn off statuses temporarily
            self.conn.write("\n\n\n".encode("ascii"))
            # wait a moment for LMC to process it
            time.sleep(0.2)
            self.conn.read_all()  # empty buffer
            # for this call only, set the timeout
            self.conn.timeout = 2.0
            self.logger.info("[Host->LMC] version")
            self.conn.write("version\n".encode("ascii"))
            line = self.conn.readline().decode("ascii")
            self.logger.info("[LMC->Host] " + line)
            if line.startswith("ok"):
                self.logger.info("LMC reports version: " + line)
            else:
                # timeout will fall into this line as well
                raise RuntimeError(f"LMC version check failed, got '{line}'")
            # reset the timeout
            self.conn.timeout = None
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
                pkt = self.conn.read_until(b"\n")
                pktstr = pkt.decode("ascii", "replace")
                self.logger.info("[LMC->Host] " + pktstr)
                pktsplit = pktstr.split()

                # branch depending on message type
                if pktsplit[0] == "ok" or pktsplit[0] == "err":
                    # Command response
                    self.logger.debug("LMC Reader Thread: Signaling command response")
                    with self.RTSyncSignallingCV:
                        self.commandResponse = pktsplit
                        self.connectionBroken = None  # no error
                        self.RTSyncSignallingCV.notify_all()
                    self.logger.debug("LMC Reader Thread: Response Event signaled")

                elif pktsplit[0] == "evt":
                    self.logger.info("LMC event received: " + pktstr)
                    # parse the event type
                    evttypestr = pktsplit[1]
                    try:
                        evttype = LMCEventType(evttypestr)
                        # puts a tuple of (evttype, evtdata)
                        self.logger.debug(
                            "Adding event to queue: type="
                            + str(evttype)
                            + " data="
                            + str(pktsplit[2:])
                        )
                        self.eventQueue.put((evttype, pktsplit[2:]))
                    except ValueError:
                        self.logger.warning(
                            "Unknown event type received from lmc: " + pktstr
                        )
                #                elif pktsplit[0] == "st":
                #                    status = LMCStatus(pktsplit[1:])
                #                    # update status variable
                #                    with self.lmcStatusLock:
                #                        self.lmcStatus = status
                #                    # call callbacks
                #                    for cb in self.statusCallbacks:
                #                        cb(status)
                else:
                    self.logger.warning(
                        "Unknown answer opcode received from lmc: " + pktstr
                    )
            # end inner loop
        except Exception as e:
            self.logger.critical(f"LMC Connection lost: {str(e)}")
            # If a synchronous command is already in the making, we need to wake it up
            with self.RTSyncSignallingCV:
                self.connectionFault = e
                self.commandResponse = None
                self.isConnected = False
                # connection must be closed so linux can reassign the device file
                self.conn.close()
                self.RTSyncSignallingCV.notify_all()
            # reader thread exits

    # event queue
    def hasPendingEvent(self) -> bool:
        """
        Returns true if the LMC has sent an event that has not been processed by the host yet.

        The host code needs to regularily poll for events from the LMC. It is suggested that you include code similar to the following into your main loop:
        ```
        while lmc.hasPendingEvent():
            evtType, evtData = lmc.getNextPendingEvent()
            if evtType == LMCEventType.DRIVE_SUCCESS:
                ... handle the event ...
        ```
        """
        return not self.eventQueue.empty()

    def getNextPendingEvent(self) -> tuple():
        """
        Returns the next pending event from the LMC event queue.
        Returns a tuple of evtType, evtData
        evtType: the LMCEventType of the event
        evtData: additional data, currently only used for DRIVE_SPLINE_AT_POINT; int(evtData[0]) = index of point in spline path that has been reached.
        removed annotation: -> tuple(LMCEventType, typing.List[str])

        Returns (None,None) if no event is pending.

        Note: according to python's Queue docs, Queue.get may return nothing despite the queue being not empty (hasPendingEvent() is True).
        """
        try:
            return self.eventQueue.get(block=False)
        except queue.Empty:
            return (None, None)

    def waitForNextEvent(self, timeout=None) -> tuple():
        """
        Waits for and returns the next event from the LMC. If an event is already pending, returns it immediately, else blocks until an event is sent by the LMC.

        The optional "timeout" parameter can be used to specify a timeout in seconds. If the timeout expires, (None,None) is returned

        Returns a tuple of evtType, evtData
        evtType: the LMCEventType of the event
        evtData: additional data, currently only used for DRIVE_SPLINE_AT_POINT; int(evtData[0]) = index of point in spline path that has been reached.
        removed annotation: -> tuple(LMCEventType, typing.List[str])
        """
        try:
            return self.eventQueue.get(timeout=timeout)
        except queue.Empty:
            return (None, None)
