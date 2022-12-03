from im_actions.action import Trigger
from EB23_Enums import Actuator
from IMA_Interface import IMA
from time import sleep
import asyncio


class Drop(IMA):
    def __init__(self) -> None:
        super().__init__()

    def registerIMA() -> dict:

        properties = {}
        properties["IMA"] = Drop
        properties["action_type"] = Trigger
        properties["required_actuators"] = []

        register = {}
        register["Drop"] = properties

        return register

    def execute(self, imam: object, goal_handle, **kwargs) -> True:
        for i in range(10):
            imam.log_info(f"Dropping {i}")
            sleep(0.5)
