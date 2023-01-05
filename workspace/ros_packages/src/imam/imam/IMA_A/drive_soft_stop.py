from im_actions.action import DriveSoftStop as DriveSoftStopAction
from EB23_Enums import Actuator
from IMA_Interface import IMA
from turag_lmc import DriveSoftStopTask
from rclpy.node import Node
from time import sleep


class DriveSoftStop(IMA):
    def __init__(self) -> None:
        super().__init__()

    def registerIMA() -> dict:

        properties = {}
        properties["IMA"] = DriveSoftStop
        properties["action_type"] = DriveSoftStopAction
        properties["required_actuators"] = [Actuator.LMC]

        register = {}
        register["DriveSoftStop"] = properties

        return register

    def execute(self, imam: Node, goal_handle, **kwargs) -> True:
        drive_task = DriveSoftStopTask()
        imam.lmc.issueDriveTask(drive_task)
        # TODO wait for task to finish
        return True
