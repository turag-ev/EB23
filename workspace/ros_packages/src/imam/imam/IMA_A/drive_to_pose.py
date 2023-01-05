from im_actions.action import DriveToPose as DriveToPoseAction
from EB23_Enums import Actuator
from IMA_Interface import IMA
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

    def execute(self, imam: object, goal_handle, **kwargs) -> True:
        for i in range(10):
            imam.log_info(f"Drive to Pose {i}")
            sleep(0.5)
