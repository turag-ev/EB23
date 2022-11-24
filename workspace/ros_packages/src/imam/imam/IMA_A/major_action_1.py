from time import sleep
from IMA_Interface import MajorAction


class MajorAction1(MajorAction):
    used_actuators = []

    def __init__(self) -> None:
        super().__init__()

    async def prepare(self, imam: object, **kw_actuators):
        for _ in range(5):
            imam.get_logger().info("[INFO] Preparing...")
            sleep(1)

        future = imam.clis.send_minor1_execute(5)

        future2 = imam.clis.send_minor2_execute(5)

        await future2, future

        imam.publisher.publishAction("TEST")

    async def execute(self, imam: object, **kw_actuators):
        for _ in range(5):
            imam.get_logger().info("[INFO] Executing...")
            sleep(1)

    async def postProcess(self, imam: object, **kw_actuators):
        for _ in range(5):
            imam.get_logger().info("[INFO] Post Processing....")
            sleep(1)
