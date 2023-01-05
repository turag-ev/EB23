from im_actions.action import DriveRelease as DriveReleaseAction
from EB23_Enums import Actuator
from IMA_Interface import IMA
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

    def execute(self, imam: object, goal_handle, **kwargs) -> True:
        for i in range(10):
            imam.log_info(f"Drive Release {i}")
            sleep(0.5)
