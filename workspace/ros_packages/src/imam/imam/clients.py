import rclpy
import asyncio
from im_actions.action import Trigger
from rclpy.action import ActionClient


class Clients:
    def __init__(self, imam):
        self.imam = imam
        self.pickup_client = ActionClient(self.imam, Trigger, "IMA/PickUp")

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

    async def send_minor1_execute(self):
        goal_msg = Trigger.Goal()
        self.minor1_client.wait_for_server()

        goal_handle = await self.minor1_client.send_goal_async(
            goal_msg, feedback_callback=self.feedback_callback
        )

        res = await goal_handle.get_result_async()

        result = res.result
        status = res.status

        return result, status

    async def send_minor2_execute(self):
        goal_msg = Trigger.Goal()
        self.minor2_client.wait_for_server()

        goal_handle = await self.minor2_client.send_goal_async(
            goal_msg, feedback_callback=self.feedback_callback
        )

        res = await goal_handle.get_result_async()

        result = res.result
        status = res.status

        return result, status

    async def send_minor3_execute(self):
        goal_msg = Trigger.Goal()
        self.minor3_client.wait_for_server()

        goal_handle = await self.minor3_client.send_goal_async(
            goal_msg, feedback_callback=self.feedback_callback
        )

        res = await goal_handle.get_result_async()

        result = res.result
        status = res.status

        return result, status
