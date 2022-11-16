import rclpy
from rclpy.node import Node

from .servers import Servers
from .publisher import PublisherIM


class IMAM(Node):
    def __init__(self):
        super().__init__("imam")
        # self._prepare_client = ActionClient(self, Test, "test_prepare")
        # self._execute_client = ActionClient(self, Test, "test_execute")
        # self._post_process_client = ActionClient(self, Test, "test_post_process")
        self.servers = Servers(self)
        self.publisher = PublisherIM(self)


def main():
    rclpy.init(args=None)
    imam = IMAM()
    rclpy.spin(imam)


if __name__ == "__name__":
    main()
