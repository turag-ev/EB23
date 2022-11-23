from enum import Enum, auto, unique


@unique
class OrderType(Enum):
    """
    Order type for movement motor.
    """

    FORWARD = auto()
    BACKWARD = auto()
    DIAGONAL_FORWARD = auto()
    TURN = auto()
    STAND = auto()
