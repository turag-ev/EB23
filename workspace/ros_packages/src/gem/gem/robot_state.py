import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Bool
import math

from EB23_Enums import Robot, CakeLayer


class RobotState:
    def __init__(self, gem: Node, robot: Robot):
        self.gem = gem
        self.name = robot.value

        self.position: tuple(float, float) = (0, 0)

        self.oppo_1_pos: tuple(float, float) = (0, 0)
        self.oppo_2_pos: tuple(float, float) = (0, 0)

        self.shortest_oppo_dist: float = 0
        self.collision_danger = False

        self.stored_cakes: dict = {CakeLayer.BROWN: 0, CakeLayer.YELLOW: 0, CakeLayer.PINK: 0, CakeLayer.CHERRIES: 10}

        self.shortest_dist_timer = self.gem.create_timer(
            timer=0.1, callback=self.update_shortest_dist
        )

        self.own_pos_sub = self.gem.create_subscription(
            msg_type=String,
            topic=f"localization/{self.name}/position",
            callback=self.update_position,
        )
        self.oppo_1_pos_sub = self.gem.create_subscription(
            msg_type=String,
            topic=f"localization/{Robot.OPPONENT_1.value}/position",
            callback=self.update_oppo_1_pos,
        )
        self.oppo_2_pos_sub = self.gem.create_subscription(
            msg_type=String,
            topic=f"localization/{Robot.OPPONENT_2.value}/position",
            callback=self.update_oppo_2_pos,
        )
        self.collision_danger_sub = self.gem.create_subscription(
            msg_type=Bool,
            topic=f"localization/collision_danger",
            callback=self.update_collision_danger,
        )

        self.stored_cakes_pub = self.gem.create_subscription(msg_type=String, topic=f"IM/{robot.name}/stored_cakes", callback=self.update_stored_cakes)
        

    def update_position(self, msg):
        data = msg.data

        x = data.x
        y = data.y

        self.position = (x, y)

    def update_oppo_1_pos(self, msg):
        data = msg.data

        x = data.x
        y = data.y

        self.oppo_1_pos = (x, y)

    def update_oppo_2_pos(self, msg):
        data = msg.data

        x = data.x
        y = data.y

        self.oppo_2_pos = (x, y)

    def update_collision_danger(self, msg):
        self.collision_danger = msg.data

    def update_stored_cakes(self, msg):
        data = msg.data

        self.stored_cakes[CakeLayer.BROWN] = data.browns
        self.stored_cakes[CakeLayer.YELLOW] = data.yellows
        self.stored_cakes[CakeLayer.PINK] = data.pinks
        self.stored_cakes[CakeLayer.CHERRIES] = data.cherries

        
    def update_shortest_dist(self):
        distance_oppo_1 = math.dist(self.position, self.oppo_1_pos)
        distance_oppo_2 = math.dist(self.position, self.oppo_2_pos)

        if distance_oppo_1 >= distance_oppo_2:
            self.shortest_oppo_dist = distance_oppo_1
        else:
            self.shortest_oppo_dist = distance_oppo_2
    
    def get_position(self): return self.position

    def get_shortest_oppo_dis(self): return self.shortest_oppo_dist

    def get_collition_danger(self): return self.collision_danger
    
    def get_stored_cakes(self): return self.stored_cakes


