from im_actions.action import Trigger
from EB23_Enums import Actuator
from IMA_Interface import IMA
from time import sleep
import asyncio


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
        for i in range(5):
            imam.log_info(f"Picking Up {i}")
            sleep(0.5)

        print("sending motor control 1")
        feedback = 0
        while True:
            if feedback == 10:
                break
            else:
                sleep(0.5)
                feedback += 1
        print("sending motor control 2")
        while True:
            if feedback == 18:
                break
            else:
                sleep(0.5)
                feedback += 1

        return True

        # sub_task1 = imam.loop.create_task(imam.clis.send_store_execute())
        # sub_task2 = imam.loop.create_task(imam.clis.send_drop_execute())
        # future_1 = asyncio.wait([sub_task1, sub_task2])
        # await future_1

        # sub_task3 = imam.loop.create_task(imam.clis.send_build_cake_execute())
        # future_2 = asyncio.wait([sub_task3])
        # await future_2

        imam.clis.send_store_execute()

        imam.clis.send_build_cake_execute()
