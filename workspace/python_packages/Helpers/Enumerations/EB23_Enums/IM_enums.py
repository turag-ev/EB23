from enum import Enum, auto, unique


@unique
class Actuator(Enum):
    ABC = auto()


@unique
class Action(Enum):
    TEST_PREPARE = auto()
    TEST_EXECUTE = auto()
    TEST_POSTPROCESS = auto()
