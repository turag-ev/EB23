from im_actions.action import DriveSoftStop as DriveSoftStopAction
from EB23_Enums import Actuator
from IMA_Interface import IMA
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

    def execute(self, imam: object, goal_handle, **kwargs) -> True:
        for i in range(10):
            imam.log_info(f"Soft Stop {i}")
            sleep(0.5)
