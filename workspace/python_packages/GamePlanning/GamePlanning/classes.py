from dataclasses import dataclass;
from typing import Optional
from enum import Enum
import enum

@dataclass
class Position:
    x: int
    y: int

@dataclass
class angle:
    angle: float


# color of the cake. might be unicolor brown, yellow, pink or might be the perfect recipe
class color(Enum):
    BROWN: int = 0
    YELLOW: int = 1
    PINK: int = 2

    BUILT: int = 3


# represents a stack of 3 cake layers
@dataclass
class Cake:
    color: color
    position: Position


class Team(Enum):
    GREEN = 0
    BLUE = 1


@dataclass
class Bot:
    # general attributes of a Bot
    position: Position
    angle: angle
    velocity: float

    team: Team

@dataclass
class FriendlyBot(Bot):
    enemy: bool = False

    storage: list[list[color]] = []
    revolver: int = 0

@dataclass
class property:
    able: bool = False

    known: bool  = False
    haveGuess: bool = False

@dataclass
class EnemyBot(Bot):
    enemy: bool = True

    # capability of picking up cakes
    # if it is None, it is unknown whether is can or not
    can_pickup: property = property()
    storage: list[color] = []
    dropped: list[color] = []


    # capability of pushing cakes
    # if it is None, it is unknown whether is can or not
    can_push: property = property()

    # capability of picking up cherries
    # if it is None, it is unknown whether is can or not
    can_cherries: property = property()
    cherry_Storage: int = 0

    def couldAffectCake(self) -> bool:
        return (
            not self.can_pickup.known or self.can_pickup.able or not self.can_push.known or self.can_push.able
        )

    # if can_pickup or can_push is None, it is unknown to us 
    # whether it can pickup the cake or nor, or whether it can push the cake or not
    def hasUnknowns(self) -> bool:
        return not self.can_cherries.known or not self.can_cake.known or not self.can_push.known





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

@dataclass
class State:
    gamestage: Gamestage = None
    strategy: Strategies = None
    step: int = 1


# state of the strategy
state: State = State()
