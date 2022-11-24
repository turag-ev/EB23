from IMA_Interface import MinorAction
from time import sleep


class MinorAction1(MinorAction):
    used_actuators = []

    def __init__(self) -> None:
        super().__init__()

    def execute(self, imam: object, **kw_actuators):
        for _ in range(5):
            print("[INFO] Executing MinorAction1...")
            sleep(1)
