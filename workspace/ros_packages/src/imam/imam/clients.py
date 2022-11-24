import rclpy
import asyncio
from im_actions.action import Test
from rclpy.action import ActionClient


class Clients:
    def __init__(self, imam):
        self.imam = imam
        self.minor1_client = ActionClient(self.imam, Test, "minor1_execute")
        self.minor2_client = ActionClient(self.imam, Test, "minor2_execute")
        self.minor3_client = ActionClient(self.imam, Test, "minor3_execute")

    async def send_minor1_execute(self, order):
        goal_msg = Test.Goal()
        goal_msg.order = order
        self.minor1_client.wait_for_server()

        goal_handle = await self.minor1_client.send_goal_async(goal_msg)

        res = await goal_handle.get_result_async()

        result = res.result
        status = res.status

        return result

    async def send_minor2_execute(self, order):
        goal_msg = Test.Goal()
        goal_msg.order = order
        self.minor2_client.wait_for_server()

        goal_handle = await self.minor2_client.send_goal_async(goal_msg)

        res = await goal_handle.get_result_async()

        result = res.result
        status = res.status

        return result

    async def send_minor3_execute(self, order):
        goal_msg = Test.Goal()
        goal_msg.order = order
        self.minor3_client.wait_for_server()

        goal_handle = await self.minor3_client.send_goal_async(goal_msg)

        res = await goal_handle.get_result_async()

        result = res.result
        status = res.status

        return result
