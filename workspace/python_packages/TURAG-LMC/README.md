# TURAG LMC Client Interface

This is a Python3 module to communicate with the TURAG drive platform (LMC) over a USB CDC link. It handles:
* Connection establishment and recovery
* Executing commands on the LMC, such as starting drive tasks or setting parameters
* Fetching and parsing LMC status messages
* Accepting and providing Events from the LMC via a polling mechanism

Please note that the LMC provides two CDC endpoints. This library needs to connect to the first endpoint (CMD), the second endpoint (LOG) is reserved for the debug log and needs to be accessed using the TURAG Console. This may change in the future.

## Example
```
from turag_lmc import *

lmc = LMCConnection("/dev/ttyACM0") # create the connection object
lmc.startConnection() # connect to the LMC

# Set up parameters (the values are examples only!)
lmc.setParameter(LMCParameters.WEIGHT, 20)
lmc.setPidParameters(LMCPidControlTypes.TRANS_DIST, ...)
lmc.setOdometryCalibration(42.36, 42.43, 19.8)

while True:
    # handle LMC events
    while lmc.hasPendingEvent():
        evtType, evtData = lmc.getNextPendingEvent()
        ... handle the event ...
    # get LMC status (e.g. pose)
    status = lmc.fetchLmcStatus()

    ... implement your control logic here ...

    # issue a drive command to the LMC
    dt = DrivePoseTask(Pose(123,456,78), DR.RAMP_SLOW)
    lmc.issueDriveTask(dt)