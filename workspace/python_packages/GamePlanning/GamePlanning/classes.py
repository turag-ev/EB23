from typing import Optional
from enum import Enum
import enum


class position:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class angle:
    angle: float


# color of the cake. might be unicolor brown, yellow, pink or might be the perfect recipe
class color(Enum):
    BROWN: int = 0
    YELLOW: int = 1
    PINK: int = 2

    BUILT: int = 3


# represents a stack of 3 cake layers
class Cake:
    color: color
    position: position

    def __init__(self, color: color, position: position):
        self.color = color
        self.position = position


class team(Enum):
    GREEN = 0
    BLUE = 1



class Bot:
    # general attributes of a Bot
    position: position
    angle: angle
    velocity: float

    team: team


class FriendlyBot(Bot):
    enemy: bool = False

    storage: list[list[Cake]]
    revolver: int = 0


class EnemyBot(Bot):
    enemy: bool = True

    # capability of picking up cakes
    # if it is None, it is unknown whether is can or not
    can_pickup: Optional[bool]
    storage: list[color]

    # capability of pushing cakes
    # if it is None, it is unknown whether is can or not
    can_push: Optional[bool]

    # capability of picking up cherries
    # if it is None, it is unknown whether is can or not
    can_cherries: Optional[bool]
    cherry_Storage: int

    def couldAffectCake(self) -> bool:
        return (
            (self.can_pickup is None)
            or (self.can_pickup)
            or (self.can_push is None)
            or (self.can_push)
        )

    # if can_pickup or can_push is None, it is unknown to us 
    # whether it can pickup the cake or nor, or whether it can push the cake or not
    def hasUnknowns(self) -> bool:
        return (self.can_pickup is None) or (self.can_push is None)





class Gamestage(Enum):
    OPENING: int = 0
    MIDGAME: int = 1
    ENDGAME: int = 2

    FALLBACK: int = 3


class Strategies(Enum):
    NONE = enum.auto()

    # Opening 
    TOP = enum.auto()
    SHORT = enum.auto()
    LONG = enum.auto()
    CAREFUL = enum.auto()

    # Midgame

    # Endgame

    # Fallback
    FALLBACK = enum.auto()


class State:
    gamestage: Gamestage = None
    strategy: Strategies = None
    step: int = 1


# state of the strategy
state: State = State()
