import rclpy
from rclpy.node import Node
import asyncio
from asyncio import AbstractEventLoop

from .servers import Servers
from .clients import Clients
from .subscriber import MinimalSubscriber
from .publisher import PublisherIM
from .actuator_state import ActuatorState
from rclpy.executors import MultiThreadedExecutor
from EB23_Enums import Actuator


class IMAM(Node):
    def __init__(self, loop: AbstractEventLoop):
        super().__init__("imam")
        self.loop = loop
        self.servers = Servers(self)
        self.clis = Clients(self)
        self.publisher = PublisherIM(self)
        # self.sub = MinimalSubscriber(self)
        self.actuators = [Actuator.ABC]
        self.actuator_state = ActuatorState(self.actuators)


async def spinning(node: Node, executor):
    while rclpy.ok():
        rclpy.spin_once(node, timeout_sec=0.01, executor=executor)
        await asyncio.sleep(0.001)


async def run(
    loop: AbstractEventLoop,
    args=None,
):
    rclpy.init()

    imam = IMAM(loop)
    executor = MultiThreadedExecutor()

    spin_task = loop.create_task(spinning(imam, executor))

    minor1 = loop.create_task(imam.clis.send_pickup_execute())
    minor2 = loop.create_task(imam.clis.send_pickup_execute())

    wait_future = asyncio.wait([minor1, minor2])

    finished, unfinished = await wait_future

    for task in finished:
        imam.get_logger().info("result {} and status flag {}".format(*task.result()))


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop=loop))
