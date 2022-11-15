import rclpy
from EB23_Enums import Action
from im_actions.action import Test
from IMA_A import MajorAction1
from rclpy.action import ActionServer
from rclpy.node import Node


class Servers(Node):
    def __init__(self):
        super().__init__("servers")
        self._prepare_server = ActionServer(self, Test, "test_prepare", self.prepareCallback)
        self._execute_server = ActionServer(self, Test, "test_execute", self.executeCallback)
        self._post_process_server = ActionServer(self, Test, "test_post_process", self.postProcessCallback)

    def prepareCallback(self, goal_handle):
        action = MajorAction1()

        used_actuators = action.getActuators()

        # Do we need the ActionClient itself? Or do we just need some information from it?
        # Maybe we can send client data as request params
        # action.prepare(self._action_client)

        self.get_logger().info('Preparing...')

        goal_handle.succeed()

        result = Test.Result()

        result.sequence = [1, 2, 3, 5, 8]

        return result

    def executeCallback(self, goal_handle):
        action = MajorAction1()

        used_actuators = action.getActuators()

        # action.execute()

        self.get_logger().info('Executing...')

        goal_handle.succeed()

        result = Test.Result()

        result.sequence = [5, 4, 3, 2, 1]

        return result

    def postProcessCallback(self, goal_handle):
        action = MajorAction1()

        used_actuators = action.getActuators()

        # action.postProcess()

        self.get_logger().info('Post-processing...')

        goal_handle.succeed()

        result = Test.Result()

        result.sequence = [1, 2, 3, 4, 5]

        return result


if __name__ == "__main__":
    rclpy.init(args=None)

    servers = Servers()

    rclpy.spin(servers)