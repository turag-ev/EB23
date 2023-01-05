import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from time import sleep

from .imam import IMAM


class Motor:
    def __init__(self, name, imam: Node) -> None:
        self.imam = imam
        self.name = name
        self.current_pos = 0
        self.goal_pos_pub = self.imam.create_publisher(String, f"{name}_goal_pos", 20)
        self.current_pos_sub = self.imam.create_subscription(
            String, f"{name}_current_pos", self.update_current_pos, 20
        )

    def update_current_pos(self, msg):
        self.current_pos = int(msg.data)

    def get_current_pos(self):
        return self.current_pos

    def set_goal_pos(self, goal_pos: str):
        msg = String()
        msg.data = goal_pos
        self.goal_pos_pub.publish(msg)


if __name__ == "__main__":
    motor1 = Motor("whoop", "sdsd")
    motor2 = Motor("doop", "sdsd")

    motor1.set_goal_pos("20")

    while motor1.get_current_pos() < 5:
        sleep(0.02)

    motor2.set_goal_pos("30")

    while motor2.get_current_pos() < 30:
        sleep(0.02)
