import rclpy
import asyncio
from im_actions.action import Trigger
from rclpy.action import ActionClient


class Clients:
    def __init__(self, imam):
        self.imam = imam
        self.pickup_client = ActionClient(self.imam, Trigger, "IMA/PickUp")
        self.drop_client = ActionClient(self.imam, Trigger, "IMA/Drop")
        self.store_client = ActionClient(self.imam, Trigger, "IMA/Store")
        self.build_cake_client = ActionClient(self.imam, Trigger, "IMA/BuildCake")

    def feedback_callback(self, feedback):
        self.imam.get_logger().info(
            "Received feedback: {0}".format(feedback.feedback.feedback)
        )

    async def send_pickup_execute(self):
        goal_msg = Trigger.Goal()
        self.pickup_client.wait_for_server()

        goal_handle = await self.pickup_client.send_goal_async(
            goal_msg, feedback_callback=self.feedback_callback
        )

        res = await goal_handle.get_result_async()

        result = res.result
        status = res.status

        return result, status

    async def send_drop_execute(self):
        goal_msg = Trigger.Goal()
        self.drop_client.wait_for_server()

        goal_handle = await self.drop_client.send_goal_async(
            goal_msg, feedback_callback=self.feedback_callback
        )

        res = await goal_handle.get_result_async()

        result = res.result
        status = res.status

        return result, status

    async def send_store_execute(self):
        goal_msg = Trigger.Goal()
        self.store_client.wait_for_server()

        goal_handle = await self.store_client.send_goal_async(
            goal_msg, feedback_callback=self.feedback_callback
        )

        res = await goal_handle.get_result_async()

        result = res.result
        status = res.status

        return result, status

    async def send_build_cake_execute(self):
        goal_msg = Trigger.Goal()
        self.build_cake_client.wait_for_server()

        goal_handle = await self.build_cake_client.send_goal_async(
            goal_msg, feedback_callback=self.feedback_callback
        )

        res = await goal_handle.get_result_async()

        result = res.result
        status = res.status

        return result, status
