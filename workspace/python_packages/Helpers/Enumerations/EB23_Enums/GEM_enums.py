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

@unique
class GameActionEnum(Enum):
    PICK_UP = 1
    STORE = 2
    REVOLVE = 3
    RETRIEVE = 4
    DROP = 5

