from im_actions.action import DriveEmergencyStop as DriveEmergencyStopAction
from EB23_Enums import Actuator
from IMA_Interface import IMA
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

    def execute(self, imam: object, goal_handle, **kwargs) -> True:
        for i in range(10):
            imam.log_info(f"Emergency Stop {i}")
            sleep(0.5)
