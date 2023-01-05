from im_actions.action import DriveToPose as DriveToPoseAction
from EB23_Enums import Actuator
from IMA_Interface import IMA
from turag_lmc import DrivePoseTask, Pose, DR
from rclpy.node import Node
from time import sleep


class DriveToPose(IMA):
    def __init__(self) -> None:
        super().__init__()

    def registerIMA() -> dict:

        properties = {}
        properties["IMA"] = DriveToPose
        properties["action_type"] = DriveToPoseAction
        properties["required_actuators"] = [Actuator.LMC]

        register = {}
        register["DriveToPose"] = properties

        return register

    def execute(self, imam: Node, goal_handle, **kwargs) -> True:
        pose = Pose(
            goal_handle.request.pose.x,
            goal_handle.request.pose.y,
            goal_handle.request.pose.angle,
        )
        drive_task = DrivePoseTask(
            target=pose,
            drive_flags=goal_handle.request.drive_flag,
            ramp=DR.ramp_dict[goal_handle.request.ramp],
        )
        self.imam.lmc.issueDriveTask(drive_task)
        # TODO wait for task to finish
        return True
