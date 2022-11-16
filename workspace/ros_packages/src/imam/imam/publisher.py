import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from time import sleep
from .imam import IMAM


class Publisher:

    message: str = ""

    def __init__(self, imam: IMAM):
        self._imam = imam

        self.action_publisher = self._imam.create_publisher(
            String, "executed_actions", 20
        )

        self.motor_state_publisher = self._imam.create_publisher(
            String, "motor_state", 20
        )
        timer_period = 0.5

        self.timer = self._imam.create_timer(timer_period, self.publishMotorState)
        self.motor_state_counter = 0

        self.robot_state_publisher = self._imam.create_publisher(
            String, "robot_state", 20
        )
        self.robot_state_counter = 0

    def publishAction(self):
        msg = String()
        msg.data = self.message
        self.action_publisher.publish(msg)

    def publishMotorState(self):
        msg = f"Motor Status {self.motor_state_counter}"
        msg.data = msg
        self.motor_state_publisher.publish(msg)
        self.motor_state_counter += 1

    def publishRobotState(self):
        msg = f"Robot State {self.robot_state_counter}"
        msg.data = msg
        self.robot_state_publisher.publish(msg)
        self.motor_state_counter += 1


def main():
    rclpy.init(args=None)
    imam = IMAM()
    pub = Publisher(imam)
    for i in range(100):
        pub.message = f"Action {i}"
        pub.publishAction()
        sleep(0.5)


if __name__ == "__main__":
    main()
