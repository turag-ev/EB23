from im_actions.action import Trigger
from EB23_Enums import Actuator
from IMA_Interface import IMA
from time import sleep
from rclpy.node import Node


class BuildCake(IMA):
    def __init__(self) -> None:
        super().__init__()

    def registerIMA() -> dict:

        properties = {}
        properties["IMA"] = BuildCake
        properties["action_type"] = Trigger
        properties["required_actuators"] = []

        register = {}
        register["BuildCake"] = properties

        return register

    def execute(self, imam: Node, goal_handle, **kwargs) -> True:
        for i in range(10):
            imam.log_info(f"Building Cake {i}")
            sleep(0.5)
