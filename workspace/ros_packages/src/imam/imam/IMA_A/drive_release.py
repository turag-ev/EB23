from im_actions.action import DriveRelease as DriveReleaseAction
from EB23_Enums import Actuator
from IMA_Interface import IMA
from turag_lmc import DriveReleaseTask, DR
from rclpy.node import Node
from time import sleep


class DriveRelease(IMA):
    def __init__(self) -> None:
        super().__init__()

    def registerIMA() -> dict:

        properties = {}
        properties["IMA"] = DriveRelease
        properties["action_type"] = DriveReleaseAction
        properties["required_actuators"] = [Actuator.LMC]

        register = {}
        register["DriveRelease"] = properties

        return register

    def execute(self, imam: Node, goal_handle, **kwargs) -> True:
        drive_task = DriveReleaseTask(DR.ramp_dict[goal_handle.request.ramp])
        imam.lmc.issueDriveTask(drive_task)
        # TODO wait for task to finish
        return True
