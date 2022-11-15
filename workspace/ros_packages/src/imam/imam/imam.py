from im_actions.action import Test
import rclpy
from rclpy.action import ActionServer, ActionClient
from rclpy.node import Node
from IMA_A import MajorAction1
from EB23_Enums import Action
from servers import Servers


class IMAM(Node):
    def __init__(self):
        super().__init__("imam")
        self._prepare_client = ActionClient(self, Test, "test_prepare")
        self._execute_client = ActionClient(self, Test, "test_execute")
        self._post_process_client = ActionClient(self, Test, "test_post_process")

    def callAction(action: Action, **kwargs):
        pass

    def callActionAsync(action: Action, **kwargs):
        pass


if __name__ == "__main__":
    rclpy.init(args=None)

    imam = IMAM()

    rclpy.spin(imam)
