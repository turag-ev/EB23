from time import sleep

from IMA_Interface import MajorAction


class MajorAction1(MajorAction):
    used_actuators = []

    def __init__(self) -> None:
        super().__init__()

    def prepare(self, imam: object, **kw_actuators):
        print("Starting preparation!")
        for _ in range(5):
            print("[INFO] Preparing...")
            sleep(1)
        print("Finished preparation")

    def execute(self, imam: object, **kw_actuators):
        print("Starting execution :)")
        for _ in range(5):
            print("[INFO] Executing...")
            sleep(1)
        print("Finished execution!")

    def postProcess(self, imam: object, **kw_actuators):
        print("Starting post processessing!")
        for _ in range(5):
            print("[INFO] Post Processing....")
            sleep(1)

        print("Finished post processing!")