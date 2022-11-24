import rclpy
import asyncio
from im_actions.action import Test
from .IMA_A import MajorAction1, MinorAction1, MinorAction2, MinorAction3
from rclpy.action import ActionServer
from rclpy.callback_groups import ReentrantCallbackGroup
from time import sleep


class Servers:
    def __init__(self, imam):
        self.imam = imam
        self._prepare_server = ActionServer(
            self.imam,
            Test,
            "test_prepare",
            execute_callback=self.prepareCallback,
            callback_group=ReentrantCallbackGroup(),
        )
        self._execute_server = ActionServer(
            self.imam,
            Test,
            "test_execute",
            execute_callback=self.executeCallback,
            callback_group=ReentrantCallbackGroup(),
        )
        self._post_process_server = ActionServer(
            self.imam,
            Test,
            "test_post_process",
            execute_callback=self.postProcessCallback,
            callback_group=ReentrantCallbackGroup(),
        )
        self._minor1_server = ActionServer(
            self.imam,
            Test,
            "minor1_execute",
            execute_callback=self.minor1Callback,
            callback_group=ReentrantCallbackGroup(),
        )
        self._minor2_server = ActionServer(
            self.imam,
            Test,
            "minor2_execute",
            execute_callback=self.minor2Callback,
            callback_group=ReentrantCallbackGroup(),
        )
        self._minor3_server = ActionServer(
            self.imam,
            Test,
            "minor3_execute",
            execute_callback=self.minor3Callback,
            callback_group=ReentrantCallbackGroup(),
        )

    async def prepareCallback(self, goal_handle):

        self.imam.get_logger().info(
            "\n-------------------- \n Start Prepare Action \n--------------------"
        )

        action = MajorAction1()

        used_actuators = action.getActuators()

        # Do we need the ActionClient itself? Or do we just need some information from it?
        # Maybe we can send client data as request params
        await action.prepare(self.imam)

        self.imam.get_logger().info(
            "\n-------------------- \n End Prepare Action \n--------------------"
        )

        goal_handle.succeed()

        result = Test.Result()

        result.sequence = [1, 2, 3, 5, 8]

        return result

    async def executeCallback(self, goal_handle):
        self.imam.get_logger().info(
            "\n-------------------- \n Start Execute Action \n --------------------"
        )
        action = MajorAction1()

        used_actuators = action.getActuators()

        await asyncio.sleep(3)
        # sleep(3)

        # await action.execute(self.imam)

        self.imam.get_logger().info(
            "\n-------------------- \n End Execute Action \n--------------------"
        )

        goal_handle.succeed()

        result = Test.Result()

        result.sequence = [5, 4, 3, 2, 1]

        return result

    async def postProcessCallback(self, goal_handle):
        self.imam.get_logger().info(
            "\n-------------------- \n Start Post Process Action \n--------------------"
        )
        action = MajorAction1()

        used_actuators = action.getActuators()

        await asyncio.sleep(3)
        # sleep(3)

        # await action.postProcess(self.imam)

        self.imam.get_logger().info(
            "\n-------------------- \n End Post Process Action \n--------------------"
        )

        goal_handle.succeed()

        result = Test.Result()

        result.sequence = [1, 2, 3, 4, 5]

        return result

    async def minor1Callback(self, goal_handle):
        self.imam.get_logger().info(
            "\n-------------------- \n Start minor1 Action \n--------------------"
        )

        action = MinorAction1()

        sleep(3)

        # action.execute(self.imam)
        self.imam.get_logger().info(
            "\n-------------------- \n End minor1 Action \n--------------------"
        )
        goal_handle.succeed()
        result = Test.Result()

        result.sequence = [1, 2, 3, 4, 5]

        return result

    async def minor2Callback(self, goal_handle):
        self.imam.get_logger().info(
            "\n-------------------- \n Start minor2 Action \n--------------------"
        )
        action = MinorAction2()

        sleep(3)

        # action.execute(self.imam)
        self.imam.get_logger().info(
            "\n-------------------- \n End minor2 Action \n--------------------"
        )
        goal_handle.succeed()
        result = Test.Result()

        result.sequence = [1, 2, 3, 4, 5]

        return result

    async def minor3Callback(self, goal_handle):
        self.imam.get_logger().info(
            "\n------------------- \n Start minor3 Action \n--------------------"
        )
        action = MinorAction3()
        action.execute(self.imam)
        self.imam.get_logger().info(
            "\n-------------------- \n End minor3 Action \n--------------------"
        )
        goal_handle.succeed()
        result = Test.Result()

        result.sequence = [1, 2, 3, 4, 5]

        return result
