import rclpy
from rclpy.node import Node


class GEM(Node):
    def __init__(self):
        super.__init__("gem")


def main():
    rclpy.init(args=None)
    gem = GEM()
    rclpy.spin(gem)


if __name__ == "__main__":
    main()
