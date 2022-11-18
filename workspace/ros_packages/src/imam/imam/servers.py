import rclpy
from im_actions.action import Test
from .IMA_A import MajorAction1
from rclpy.action import ActionServer


class Servers:
    def __init__(self, imam):
        self.imam = imam
        self._prepare_server = ActionServer(
            self.imam, Test, "test_prepare", self.prepareCallback
        )
        self._execute_server = ActionServer(
            self.imam, Test, "test_execute", self.executeCallback
        )
        self._post_process_server = ActionServer(
            self.imam, Test, "test_post_process", self.postProcessCallback
        )

    def prepareCallback(self, goal_handle):
        action = MajorAction1()

        used_actuators = action.getActuators()

        # Do we need the ActionClient itself? Or do we just need some information from it?
        # Maybe we can send client data as request params
        action.prepare(self.imam)

        self.imam.get_logger().info("Preparing...")

        goal_handle.succeed()

        result = Test.Result()

        result.sequence = [1, 2, 3, 5, 8]

        return result

    def executeCallback(self, goal_handle):
        action = MajorAction1()

        used_actuators = action.getActuators()

        action.execute(self.imam)

        self.imam.get_logger().info("Executing...")

        goal_handle.succeed()

        result = Test.Result()

        result.sequence = [5, 4, 3, 2, 1]

        return result

    def postProcessCallback(self, goal_handle):
        action = MajorAction1()

        used_actuators = action.getActuators()

        action.postProcess(self.imam)

        self.imam.get_logger().info("Post-processing...")

        goal_handle.succeed()

        result = Test.Result()

        result.sequence = [1, 2, 3, 4, 5]

        return result
