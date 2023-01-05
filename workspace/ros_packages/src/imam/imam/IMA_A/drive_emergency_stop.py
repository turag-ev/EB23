from im_actions.action import DriveEmergencyStop as DriveEmergencyStopAction
from EB23_Enums import Actuator
from IMA_Interface import IMA
from turag_lmc import DriveEmergencyStopTask
from rclpy.node import Node
from time import sleep


class DriveEmergencyStop(IMA):
    def __init__(self) -> None:
        super().__init__()

    def registerIMA() -> dict:

        properties = {}
        properties["IMA"] = DriveEmergencyStop
        properties["action_type"] = DriveEmergencyStopAction
        properties["required_actuators"] = [Actuator.LMC]

        register = {}
        register["DriveEmergencyStop"] = properties

        return register

    def execute(self, imam: Node, goal_handle, **kwargs) -> True:
        drive_task = DriveEmergencyStopTask()
        imam.lmc.issueDriveTask(drive_task)
        # TODO wait for task to finish
        return True
