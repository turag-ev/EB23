import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from time import sleep


class PublisherIM:

    message: str = ""

    def __init__(self, imam):
        self.imam = imam
        self.action_publisher = self.imam.create_publisher(
            String, "executed_actions", 20
        )

        self.motor_state_publisher = self.imam.create_publisher(
            String, "motor_state", 20
        )
        timer_period = 0.5

        self.timer = self.imam.create_timer(timer_period, self.publishMotorState)
        self.motor_state_counter = 0

        self.robot_state_publisher = self.imam.create_publisher(
            String, "robot_state", 20
        )

        self.timer = self.imam.create_timer(timer_period, self.publishRobotState)

        self.robot_state_counter = 0

    def publishAction(self, message):
        msg = String()
        msg.data = message
        self.action_publisher.publish(msg)

    def publishMotorState(self):
        msg = String()
        message = f"Motor State {self.motor_state_counter}"
        msg.data = message
        self.motor_state_publisher.publish(msg)
        self.motor_state_counter += 1

    def publishRobotState(self):
        msg = String()
        message = f"Robot State {self.robot_state_counter}"
        msg.data = message
        self.robot_state_publisher.publish(msg)
        self.robot_state_counter += 1


def main():
    rclpy.init(args=None)
    pub = PublisherIM()
    rclpy.spin(pub)
    for i in range(100):
        pub.message = f"Action {i}"
        pub.publishAction()
        sleep(0.5)
