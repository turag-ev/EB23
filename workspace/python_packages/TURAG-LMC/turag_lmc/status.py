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


from enum import IntFlag
from .drive import Pose
import time


class LMCStatusFlags(IntFlag):
    """
    Flags for general LMC status
    READY: LMC is initialized and ready to accept drive commands
    DRIVING: LMC is currently executing a drive action
    ERROR: LMC has an unrecoverable error (typically a hardware failure)
    """

    READY = 1
    DRIVING = 2
    ERROR = 4

    def __str__(self):
        if self.value == 0:
            return "(none)"
        return "|".join(m.name for m in self.__class__ if m.value & self.value)


class TransRot:
    """
    Translational and rotational values
    Units Distance: mm + deg
    Units Velocity: m/s + rad/s
    Units Force   : N + Nm
    """

    def __init__(self, trans=0, rot=0) -> None:
        self.trans = trans
        self.rot = rot

    def fromString(self, string: str):
        spl = string.split(",")
        self.trans = float(spl[0])
        self.rot = float(spl[1])


class LeftRight:
    """
    Left and right values
    """

    def __init__(self, left=0, right=0) -> None:
        self.left = left
        self.right = right

    def fromString(self, string: str):
        spl = string.split(":")
        self.left = float(spl[0])
        self.right = float(spl[1])


class LMCStatus:
    """
        Class encapsulating the LMC's current status, as received by the LMC status messages

        Fields:

    LMC Status message from LMC
     stx
     <flags>
     <pose/mm/deg>
     <motor_distance_trans/mm>,<motor_distance_rot/deg>
     <odo_distance_trans/mm>,<odo_distance_rot/deg>
     <motor_velocity/mm/s>,<motor_velocity_rot/rad/s>
     <odo_velocity/mm/s>,<odo_velocity_rot/rad/s>
     <force/N>,<torque/Nm>
     <motor_current_left/mA>:<motor_current_right/mA>
     <motor_pwm_left>:<motor_pwm_right> (flat 0.0-1.0)

    //   FL Pose     DTmDR DToDR VTmVR VToVR FT FR CURR  PWM
    stx  %d %d,%d,%d %d,%f %d,%f %f,%f %f,%f %f,%f %d:%d %f:%f\n",
    """

    def __init__(self, message: list = None) -> None:
        self.time = time.monotonic()
        self.flags = LMCStatusFlags(0)
        self.pose = Pose()
        self.isExtended = False
        self.motor_distance = TransRot()
        self.odo_distance = TransRot()
        self.motor_velocity = TransRot()
        self.odo_velocity = TransRot()
        self.force = TransRot()
        self.motor_current = LeftRight()  # unit: A
        self.motor_pwm = LeftRight()  # unit: flat 0-1
        if message is not None:
            self.updateFromLmcMessage(message)

    def updateFromLmcMessage(self, message: list):
        self.time = time.monotonic()
        self.flags = LMCStatusFlags(int(message[0]))
        self.pose = Pose(lmcMessage=message[1])
        if len(message) > 2:
            self.isExtended = True
            self.motor_distance.fromString(message[2])
            self.odo_distance.fromString(message[3])
            self.motor_velocity.fromString(message[4])
            self.odo_velocity.fromString(message[5])
            self.force.fromString(message[6])
            self.motor_current.fromString(message[7])
            self.motor_pwm.fromString(message[8])
        else:
            self.isExtended = False

    def __str__(self):
        s = "LMC Status:\n"
        s += str(time.monotonic() - self.time) + " s ago"
        s += "\nFlags: " + str(self.flags)
        s += "\nPose:  " + str(self.pose)
        if self.isExtended:
            s += f"\nMotor Dist {self.motor_distance.trans: 6.0f} mm | {self.motor_distance.rot: 5.0f} °"
            s += f"\nOdo   Dist {self.odo_distance.trans: 6.0f} mm | {self.odo_distance.rot: 5.0f} °"
            s += f"\nMotor Vel  {self.motor_velocity.trans: 01.5f} m/s | {self.motor_velocity.rot: 01.4f} rad/s"
            s += f"\nOdo   Vel  {self.odo_velocity.trans: 01.5f} m/s | {self.odo_velocity.rot: 01.4f} rad/s"
            s += f"\nForce {self.force.trans: 2.4f} N  | Torque {self.force.rot: 2.4f} Nm"
            s += f"\nCurrent left {self.motor_current.left:01.5f} A  | right {self.motor_current.right:01.5f} A"
            s += f"\nPWM     left {self.motor_pwm.left:01.5f}    | right {self.motor_pwm.right:01.5f}"
        return s
