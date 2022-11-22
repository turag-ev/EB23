from IMA_Interface import MinorAction
from time import sleep


class MinorAction2(MinorAction):
    used_actuators = []

    def __init__(self) -> None:
        super().__init__()

    def execute(self, imam: object, **kw_actuators):
        print("Starting execution of MinorAction2:)")
        for _ in range(5):
            print("[INFO] Executing MinorAction2...")
            sleep(1)
        print("Finished execution of MinorAction2!")
