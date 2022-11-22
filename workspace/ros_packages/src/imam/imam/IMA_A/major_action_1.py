from time import sleep

from IMA_Interface import MajorAction


class MajorAction1(MajorAction):
    used_actuators = []

    def __init__(self) -> None:
        super().__init__()

    def prepare(self, imam: object, **kw_actuators):
        imam.get_logger().info("Starting preparation!")
        for _ in range(5):
            imam.get_logger().info("[INFO] Preparing...")
            sleep(1)
        imam.get_logger().info("Finished preparation")

        imam.publisher.publishAction("TEST")

    def execute(self, imam: object, **kw_actuators):
        imam.get_logger().info("Starting execution :)")
        for _ in range(5):
            imam.get_logger().info("[INFO] Executing...")
            sleep(1)
        imam.get_logger().info("Finished execution!")

    def postProcess(self, imam: object, **kw_actuators):
        imam.get_logger().info("Starting post processessing!")
        for _ in range(5):
            imam.get_logger().info("[INFO] Post Processing....")
            sleep(1)

        imam.get_logger().info("Finished post processing!")
