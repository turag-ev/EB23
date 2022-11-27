import rclpy
from rclpy.node import Node
import asyncio
from asyncio import AbstractEventLoop

from .servers import Servers
from .clients import Clients
from .publisher import PublisherIM
from rclpy.executors import MultiThreadedExecutor


class IMAM(Node):
    def __init__(self, loop: AbstractEventLoop):
        super().__init__("imam")
        self.loop = loop
        self.servers = Servers(self)
        self.clis = Clients(self)
        self.publisher = PublisherIM(self)


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

    minor1 = loop.create_task(imam.clis.send_minor1_execute())
    minor2 = loop.create_task(imam.clis.send_minor1_execute())

    wait_future = asyncio.wait([minor1])

    finished, unfinished = await wait_future

    for task in finished:
        imam.get_logger().info("result {} and status flag {}".format(*task.result()))


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop=loop))
