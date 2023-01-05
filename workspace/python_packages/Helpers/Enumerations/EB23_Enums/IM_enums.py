from enum import Enum, auto, unique


@unique
class Actuator(Enum):
    LMC = auto()
    ABC = auto()
    MOTOR1 = auto()
    MOTOR2 = auto()
    MOTOR3 = auto()
    MOTOR4 = auto()
    MOTOR5 = auto()


@unique
class Action(Enum):
    TEST_PREPARE = auto()
    TEST_EXECUTE = auto()
    TEST_POSTPROCESS = auto()


@unique
class State(Enum):
    OCCUPIED = auto()
    FREE = auto()
