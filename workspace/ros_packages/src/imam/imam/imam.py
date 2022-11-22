import rclpy
from rclpy.node import Node

from .servers import Servers
from .clients import Clients
from .publisher import PublisherIM


class IMAM(Node):
    def __init__(self):
        super().__init__("imam")
        self.servers = Servers(self)
        self.clis = Clients(self)
        self.publisher = PublisherIM(self)


def main():
    rclpy.init(args=None)
    imam = IMAM()
    rclpy.spin(imam)


if __name__ == "__name__":
    main()
