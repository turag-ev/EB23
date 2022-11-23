import rclpy
from im_actions.action import Test
from rclpy.action import ActionClient


class Clients:
    def __init__(self, imam):
        self.imam = imam
        self.prepare_client = ActionClient(self.imam, Test, "test_prepare")
        self.execute_client = ActionClient(self.imam, Test, "test_execute")
        self.post_process_client = ActionClient(self.imam, Test, "test_post_process")

    def send_prepare_goal(self, order):
        goal_msg = Test.Goal()
        goal_msg.order = order

        self.prepare_client.wait_for_server()

        return self.prepare_client.send_goal_async(goal_msg)

    def send_execute_goal(self, order):
        goal_msg = Test.Goal()
        goal_msg.order = order

        self.execute_client.wait_for_server()

        return self.execute_client.send_goal_async(goal_msg)

    def send_post_process_goal(self, order):
        goal_msg = Test.Goal()
        goal_msg.order = order

        self.post_process_client.wait_for_server()

        return self.post_process_client.send_goal_async(goal_msg)
