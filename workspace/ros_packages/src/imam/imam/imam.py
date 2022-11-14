from im_actions.action import Test
import rclpy
from rclpy.action import ActionServer, ActionClient
from rclpy.node import Node
from IMA_A import MajorAction1
from EB23_Enums import Action


class IMAM(Node):
    def __init__(self):
        super().__init__("imam")
        self._action_server = ActionServer(self, Test, "test_prepare", self.testPrepare)
        # self._action_server = ActionServer(self, Test, "test_execute", self.testExecute)
        # self._action_server = ActionServer(
        #    self, Test, "test_postProcess", self.testPostProcess
        # )
        self._action_client = ActionClient(self, Test, "test_execute")

    def testPrepare(self, goal_handle):
        action = MajorAction1()

        used_actuators = action.getActuators()

        action.prepare(self._action_client)

        goal_handle.succeed()

        result = Test.Result()

        result.sequence = [1, 2, 3, 5, 8]

        return result

    def testExecute(self):
        pass

    def callAction(action: Action, **kwargs):
        pass

    def callActionAsync(action: Action, **kwargs):
        pass


if __name__ == "__main__":
    rclpy.init(args=None)

    imam = IMAM()

    rclpy.spin(imam)
