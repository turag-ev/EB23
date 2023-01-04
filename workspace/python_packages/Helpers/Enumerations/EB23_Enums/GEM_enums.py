from enum import Enum, auto, unique

class Robot(Enum):
    ROBOT_A = "robot_a"
    ROBOT_B = "robot_b"
    OPPONENT_1 = "opponent_1"
    OPPONENT_2 = "opponent_2"

class CakeLayer(Enum):
    BROWN = auto()
    YELLOW = auto()
    PINK = auto()
    CHERRIES = auto()