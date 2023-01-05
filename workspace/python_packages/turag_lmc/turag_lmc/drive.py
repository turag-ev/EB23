from enum import Enum,IntFlag

class LMCDriveFlags(IntFlag):
    """
    Drive flags for drive-to-pose actions. Combine using bitwise OR
    """
    FORWARD = 0         # Dummy, no flags set
    BACKWARD = 1        # Robot will drive backwards
    LONG_TURN_START = 2 # Spline only: Robot will do a long turn at the start of the path (whatever that means)
    LONG_TURN_END = 4   # Spline only: Robot will do a long turn at the end of the path (whatever that means)
    KANAYAMA = 8        # Single pose only: enable the Kanayama regulation (robot corrects path automatically; always enabled for Spline)


class LMCPidControlTypes(Enum):
    """
    Control type values for the PID regulation values
    setpid <control_type> <Kr> <Ti> <Td> <frict_offset/Nm>
    Control Types:
        trans_dist    (PID::CONTROL_DISTANCE) # frict_offset in N
        rot_dist       (PID::CONTROL_ANGLE)  # frict_offset in Nm
        trans_vel (PID::CONTROL_TRANSLATION) # frict_offset in N
        rot_vel    (PID::CONTROL_ROTATION)  # frict_offset in Nm
        current       (PID::CONTROL_FORCE)    # frict_offset is ignored for this PID (please provide a dummy value)
    """
    TRANS_DIST = "trans_dist"       # Translational distance regulation (PID::CONTROL_DISTANCE)
    ROT_DIST = "rot_dist"           # Rotational distance (angle) regulation (PID::CONTROL_ANGLE)
    TRANS_VEL = "trans_vel"         # Translational velocity regulation (PID::CONTROL_TRANSLATION)
    ROT_VEL = "rot_vel"             # Rotational velocity regulation (PID::CONTROL_ROTATION)
    CURRENT = "current"             # Current regulation (PID::CONTROL_FORCE)


# Note: This class SHOULD be replaced by the common Pose class from the main TURAG code
class Pose:
    """
    Class to represent a pose with x and y position (in mm) and angle (in degrees)
    """
    ANY_ANGLE = None # constant for "any angle" in pose
    x = 0 # X position (mm)
    y = 0 # Y position (mm)
    _angle = 0 # angle in degrees

    def __init__(self, x=0, y=0, angle=ANY_ANGLE, lmcMessage:str=None):
        if lmcMessage is not None:
            sp = lmcMessage.split(",")
            try:
                self.x = int(sp[0])
                self.y = int(sp[1])
                if sp[2] == "x":
                    self.angle = self.ANY_ANGLE
                else:
                    self.angle = int(sp[2])
            except TypeError:
                raise TypeError("Invalid LMC Pose Message: "+lmcMessage)
        else:
            self.x = x
            self.y = y
            self.angle = angle

    def getAngle(self):
        return self._angle
    
    def setAngle(self, ang):
        self._angle = ang #TODO

    angle = property(getAngle, setAngle)

    def toLmcMessage(self):
        if self.angle == self.ANY_ANGLE:
            return str(self.x)+","+str(self.y)+",x"
        else:
            return str(self.x)+","+str(self.y)+","+str(self.angle)

class DriveRamp:
    """
    Class encapsulating the maximum velocities and accelerations the robot will use
    In a real setup, there will be a number of predefined ramps globally defined
    (e.g. RAMP_SLOW, RAMP_FAST)
    Note: not all values are used for all drive tasks!
    """

    v_max = 0 # m/s
    a_max = 0 # m/s^2
    ang_v_max = 0 # rad/s
    ang_a_max = 0 # rad/s^2
    def __init__(self, v_max = 0, a_max = 0, ang_v_max = 0, ang_a_max = 0) -> None:
        """
        v_max = ? m/s         # velocity
        a_max = ? m/s^2       # acceleration
        ang_v_max = ? rad/s   # angular velocity
        ang_a_max = ? rad/s^2 # angular acceleration
        Note: the deceleration is hardcoded into LMC code
        """
        self.v_max = v_max
        self.a_max = a_max
        self.ang_v_max = ang_v_max
        self.ang_a_max = ang_a_max

class DR:
    # default drive ramps from old systemcontrol
    #                       m/s  m/s^2 rad/s rad/s^2
    RAMP_SLOW   = DriveRamp(0.3, 1.0,  2.4,   7.2)
    RAMP_MEDIUM = DriveRamp(0.6, 1.0,  4.8,  14.4)
    RAMP_FAST   = DriveRamp(1.0, 1.5,  6.0,  18.0)

    ramp_dict = {
        "slow": RAMP_SLOW,
        "medium": RAMP_MEDIUM,
        "fast": RAMP_FAST
    }
    # TODO: please delete when you define drive ramps elsewhere


class DriveTask:
    """
    Base class for drive tasks
    Please use the subclasses for actual things
    """
    # DriveTask at least defines the ramp as common property
    ramp = None
    def __init__(self, ramp:DriveRamp) -> None:
        self.ramp = ramp
    
    def execute(self, conn):
        """
        Start the drive task on the provided LMCConnection
        """
        conn.syncCommand(self._toLmcMessage())

    def _toLmcMessage(self):
        raise NotImplementedError("DriveTask base class has no implementation for _toLmcMessage")

"""
Note: all of these can be retrieved with get too

Collisions enabled
set coll <1/0>

LC (laser scanner) pose enabled
set lcpose <1/0>

set weight <weight/kg>
set momin <moment_of_inertia/(Nm/s/s/rad)

--------

The following drive task messages exist:
(format is <param/unit>)

-- constant velocity drive
drive vel <linear/m/s> <angular/rad/s>

-- drive translational/rotational using only the velocity control (no distance regulation)
drive trans_vel <dist/mm> <vmax/m/s> <amax/m/s²> # Construct a velocity ramp that results in the provided drive distance and drive it (without further distance control)
drive rot_vel <angle/rad> <ang_vmax/m/s> <ang_amax/m/s²> # Same for rotational

-- relative drive commands (using distance control)
drive dist <dist/mm> <vmax/m/s> <amax/m/s>
drive angle <angle> <ang_vmax/rad/s> <ang_amax/rad/s²>
-- pose driving command
drive pose <target pose> <drive_flags*> <vmax/m/s> <amax/m/s> <ang_vmax/rad/s> <ang_amax/rad/s²>

-- drive spline: subcommands since we might exceed the max command length otherwise
drive spline add <pose> # add a point to the current spline
drive spline clear # clear the current spline
drive spline go <drive_flags*> <vmax/m/s> <amax/m/s> <ang_vmax/rad/s> <ang_amax/rad/s²> # start driving the current spline
-- force commands
drive force <force/N> <torque/Nm>
drive force_ha <force/N>  # Drive force with holding angle
-- stop and misc commands
drive release # release motors
drive estop # emergency stop
drive softstop # soft stop
drive pwm <left*> <right*> # Arguments are PWM duty cycles (range 0.0f to 1.0f)
drive square <square_size/mm> <direction CW=-1 CCW=1> <vmax/m/s> <amax/m/s> <ang_vmax/rad/s> <ang_amax/rad/s²>


-- set PID and odometry params (not drive commands)
setpid <control_type> <Kr> <Ti> <Td> <frict_offset/Nm>
# where control_type is:
    trans_dist    (PID::CONTROL_DISTANCE) # frict_offset in N
    rot_dist       (PID::CONTROL_ANGLE)  # frict_offset in Nm
    trans_vel (PID::CONTROL_TRANSLATION) # frict_offset in N
    rot_vel    (PID::CONTROL_ROTATION)  # frict_offset in Nm
    current       (PID::CONTROL_FORCE)    # frict_offset is ignored for this PID (please provide a dummy value)

setkanayama <tang> <norm> <rot>

setodometry <left_radius/mm> <right_radius/mm> <wheel_distance/mm>

*Drive Flags: use bitwise OR of LMCDriveFlags
"""

class DriveConstantVelocityTask(DriveTask):
    """
    Drive with constant linear and angular velocities
    v_linear unit: m/s
    v_angular unit: rad/s
    """
    def __init__(self, v_linear:float, v_angular:float):
        self.v_linear = v_linear
        self.v_angular = v_angular
    def _toLmcMessage(self):
        return "drive vel %s %s" % (self.v_linear, self.v_angular)

class DriveTransVelTask(DriveTask):
    """
    Drive forward using the velocity regulation only
    Length is the total area under the velocity ramp (used only for ramp calculation)
    length unit: m
    """
    def __init__(self, length:float, ramp:DriveRamp):
        super().__init__(ramp)
        self.length = length
    def _toLmcMessage(self):
        return "drive trans_vel %s %s %s" % (self.length, self.ramp.v_max, self.ramp.a_max)
class DriveRotVelTask(DriveTask):
    """
    Rotate bot using the velocity regulation only
    Angle is the total area under the angular velocity ramp (used only for ramp calculation)
    angle unit: rad
    """
    def __init__(self, angle:float, ramp:DriveRamp):
        super().__init__(ramp)
        self.angle = angle
    def _toLmcMessage(self):
        return "drive rot_vel %s %s %s" % (self.angle, self.ramp.ang_v_max, self.ramp.ang_a_max)

class DriveDistanceTask(DriveTask):
    """
    Drive forward for a fixed length
    length unit: m
    """
    def __init__(self, length:float, ramp:DriveRamp):
        super().__init__(ramp)
        self.length = length
    def _toLmcMessage(self):
        return "drive dist %s %s %s" % (self.length, self.ramp.v_max, self.ramp.a_max)

class DriveAngleTask(DriveTask):
    """
    Rotate bot by a fixed relative angle
    angle unit: rad
    """
    def __init__(self, angle:float, ramp:DriveRamp):
        super().__init__(ramp)
        self.angle = angle
    def _toLmcMessage(self):
        return "drive angle %s %s %s" % (self.angle, self.ramp.ang_v_max, self.ramp.ang_a_max)

class DrivePoseTask(DriveTask):
    """
    Drive bot to a given pose (using its internal odometry)
    Sequence: turn towards correct pose, drive to target pose, rotate to target angle
    If pose angle is ANY_ANGLE, final turn is omitted

    Drive flags applicable:
    BACKWARD: robot drives backwards
    KANAYAMA: enable the Kanayama algorithm (continuously corrects path alignment, should usually be enabled)
    """
    def __init__(self, target:Pose, drive_flags:int, ramp:DriveRamp):
        super().__init__(ramp)
        self.target = target
        self.drive_flags = drive_flags
    def _toLmcMessage(self):
        return "drive pose %s %d %s %s %s %s" % (self.target.toLmcMessage(), self.drive_flags, self.ramp.v_max, self.ramp.a_max, self.ramp.ang_v_max, self.ramp.ang_a_max)

class DriveSplineTask(DriveTask):
    """
    Drive along the given poses (pose_list), following a spline

    Drive flags applicable:
    BACKWARD: robot drives backwards
    LONG_TURN_START: ??TODO
    LONG_TURN_END: ??TODO
    Note: KANAYAMA flag is ignored and is always enabled
    """
    def __init__(self, pose_list:list[Pose], drive_flags:int, ramp:DriveRamp):
        super().__init__(ramp)
        self.pose_list = pose_list
        self.drive_flags = drive_flags
    
    def execute(self, conn):
        """
        Start the drive task on the provided LMCConnection
        DriveSplineTask overrides because it needs multiple commands
        """
        # 1. clear spline path
        conn.syncCommand("drive spline clear")
        # 2. send each point
        for pose in self.pose_list:
            conn.syncCommand(f"drive spline add {pose.toLmcMessage()}")
        # 3. start the spline
        conn.syncCommand(self._toLmcMessage())
    
    def _toLmcMessage(self):
        return "drive spline go %d %s %s %s %s" % (self.drive_flags, self.ramp.v_max, self.ramp.a_max, self.ramp.ang_v_max, self.ramp.ang_a_max)

class DriveForce(DriveTask):
    """
    Drive forward with a given force (translational) and torque (rotational)
    Only use this to drive against a wall or other fixed object!
    force unit: N
    """
    def __init__(self, force:float, torque:float):
        self.force = force
        self.torque = torque
    def _toLmcMessage(self):
        return "drive force %s %s" % (self.force, self.torque)

class DriveForceHoldAngleTask(DriveTask):
    """
    Drive forward with a given force (translational), holding the current robot orientation (angle)
    force unit: N
    """
    def __init__(self, force:float):
        self.force = force
    def _toLmcMessage(self):
        return "drive force_ha %s" % self.force

class DriveReleaseTask(DriveTask):
    """
    Release the wheels, so that the robot can roll freely
    """
    def _toLmcMessage(self):
        return "drive release"

class DriveEmergencyStopTask(DriveTask):
    """
    Immediately brake and stop the robot the hard way
    """
    def _toLmcMessage(self):
        return "drive estop"

class DriveSoftStopTask(DriveTask):
    """
    Immediately brake and stop the robot softly
    """
    def _toLmcMessage(self):
        return "drive softstop"

class DrivePwmTask(DriveTask):
    """
    Directly set the PWM duty cycles of the wheels
    left and right are the duty cycles as fraction (range 0.0 - 1.0)
    """
    def __init__(self, left:float, right:float):
        self.left = left
        self.right = right
    def _toLmcMessage(self):
        return "drive pwm %s %s" % (self.left, self.right)

class DriveSquareTask(DriveTask):
    """
    Drive a square
    Don't ask me why this is a dedicated drive task, as the same can be done with 4 DriveDist and 4 DriveAngle tasks.
    """
    def __init__(self, length:float, counterclockwise:bool, ramp:DriveRamp):
        super().__init__(ramp)
        self.length = length
        self.counterclockwise = counterclockwise
    def _toLmcMessage(self):
        return "drive pwm %s %d %s %s %s %s" % (self.length, 1 if self.counterclockwise else -1, self.ramp.v_max, self.ramp.a_max, self.ramp.ang_v_max, self.ramp.ang_a_max)

