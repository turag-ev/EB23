import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from time import sleep


class ActionPublisher(Node):

    message: str = ""

    def __init__(self):
        super().__init__("action_publisher")
        self.publisher_ = self.create_publisher(String, "executed_actions", 20)
        # timer_period = 0.5
        # self.timer = self.create_timer(timer_period, self.publishMessage)
        # self.counter = 0

    def publishMessage(self):
        msg = String()
        msg.data = self.message
        self.publisher_.publish(msg)


def main():
    rclpy.init(args=None)
    pub = ActionPublisher()
    for i in range(100):
        pub.message = f"Action {i}"
        pub.publishMessage()
        sleep(0.5)


if __name__ == "__main__":
    main()
