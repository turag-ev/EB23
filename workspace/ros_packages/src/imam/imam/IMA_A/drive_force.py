from im_actions.action import DriveForce as DriveForceAction
from EB23_Enums import Actuator
from IMA_Interface import IMA
from turag_lmc import DriveForceTask as DF
from rclpy.node import Node
from time import sleep


class DriveForce(IMA):
    def __init__(self) -> None:
        super().__init__()

    def registerIMA() -> dict:

        properties = {}
        properties["IMA"] = DriveForce
        properties["action_type"] = DriveForceAction
        properties["required_actuators"] = [Actuator.LMC]

        register = {}
        register["DriveForce"] = properties

        return register

    def execute(self, imam: Node, goal_handle, **kwargs) -> True:
        drive_task = DF(
            force=goal_handle.request.force.force,
            torque=goal_handle.request.force.torque,
        )
        self.lmc.issueDriveTask(drive_task)
        # TODO wait for task to finish
        return True
