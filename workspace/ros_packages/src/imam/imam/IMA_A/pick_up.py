from im_actions.action import Trigger
from EB23_Enums import Actuator
from IMA_Interface import IMA


class PickUp(IMA):
    def __init__(self) -> None:
        super().__init__()

    def registerIMA() -> dict:

        properties = {}
        properties["IMA"] = PickUp
        properties["action_type"] = Trigger
        properties["required_actuators"] = [Actuator.ABC]

        register = {}
        register["PickUp"] = properties

        return register

    def execute(self, imam: object, goal_handle, **kwargs) -> bool:
        return True


if __name__ == "__main__":
    print(PickUp.registerIMA())
