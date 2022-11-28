import rclpy
from std_msgs.msg import String


class MinimalSubscriber:
    def __init__(self, imam):
        self.imam = imam
        self.paramter = 1
        self.subscription = self.imam.create_subscription(
            String,
            "robot_state",
            lambda msg: self.listener_callback(msg, self.paramter),
            10,
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg, parameter):
        self.imam.get_logger().info('I heard: "%s"' % msg.data)
        self.imam.get_logger().info(str(parameter))
