from im_actions.action import DriveEmergencyStop
from EB23_Enums import Actuator
from IMA_Interface import IMA
from time import sleep


class DriveEmergencyStopClass(IMA):
    def __init__(self) -> None:
        super().__init__()

    def registerIMA() -> dict:

        properties = {}
        properties["IMA"] = DriveEmergencyStopClass
        properties["action_type"] = DriveEmergencyStop
        properties["required_actuators"] = [Actuator.LMC]

        register = {}
        register["DriveEmergencyStop"] = properties

        return register

    def execute(self, imam: object, goal_handle, **kwargs) -> True:
        for i in range(10):
            imam.log_info(f"Emergency Stop {i}")
            sleep(0.5)
