from im_actions.action import DriveForce as DriveForceAction
from EB23_Enums import Actuator
from IMA_Interface import IMA
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

    def execute(self, imam: object, goal_handle, **kwargs) -> True:
        for i in range(10):
            imam.log_info(f"Drive Force {i}")
            sleep(0.5)
