from typing import Optional, Union
import enum

from classes import *
from gloabals import *
from utils import *
from actions import *


def strategy():
    match state.gamestage:
        case Gamestage.OPENING:
            opening()

        case Gamestage.MIDGAME:
            pass

        case Gamestage.ENDGAME:
            pass


        case Gamestage.FALLBACK:
            fallbackStrategy()


def nextstage():
    state.step = 1
    state.gamestage += 1


def determineOpening() -> Strategies:
    global state

    if state.strategy is not None:
        return state.strategy

    EnemyOnFour: EnemyBot = enemyOnSpawn(square=4)
    if (EnemyOnFour is None) or (not EnemyOnFour.couldAffectCake()):
        return Strategies.SHORT

    EnemyOnBase: EnemyBot = enemyOnSpawn(square=0)
    if (EnemyOnBase is None) or (not EnemyOnBase.couldAffectCake()):
        return Strategies.TOP

    # if is is unknown whether it can affect cake or not
    if EnemyOnFour.hasUnknowns() or EnemyOnBase.hasUnknowns():
        return Strategies.CAREFUL

    # if it is known, go long
    else:
        return Strategies.LONG


def opening():
    global state
    state.strategy = determineOpening()

    match state.strategy:

        case Strategies.TOP:
            openingTop()

        case Strategies.SHORT:
            openingShort()

        case Strategies.LONG:
            openingLong()

        case Strategies.CAREFUL:
            openingCareful()



def openingTop(): 
    global state

    match state.step:
      case 1: getCake(targetCake(ifgreen = BROWNCAKES[0],  ifblue = BROWNCAKES[2] )); nextstep()
      case 2: getCake(targetCake(ifgreen = YELLOWCAKES[0], ifblue = YELLOWCAKES[2])); nextstep()
      case 3: getCake(targetCake(ifgreen = PINKCAKES[0],   ifblue = PINKCAKES[2]  )); nextstep()
      case 4: submitCake(targetSquare(ifgreen = START_GREEN[0], ifblue = START_BLUE[0])); nextstep()

      case 5: nextstage()



def openingShort():
    global state

    match state.step:
      case 1: getCake(targetCake(ifgreen = BROWNCAKES[0],  ifblue = BROWNCAKES[2] )); nextstep()
      case 2: getCake(targetCake(ifgreen = YELLOWCAKES[2], ifblue = YELLOWCAKES[0])); nextstep()
      case 3: getCake(targetCake(ifgreen = PINKCAKES[2],   ifblue = PINKCAKES[0]  )); nextstep()
      case 4: submitCake(targetSquare(ifgreen = START_GREEN[0], ifblue = START_BLUE[0])); nextstep()

      case 5: nextstage()



def openingLong():
    global state

    match state.step:
      case 1: getCake(targetCake(ifgreen = YELLOWCAKES[0], ifblue = YELLOWCAKES[2])); nextstep()
      case 1: getCake(targetCake(ifgreen = BROWNCAKES[0],  ifblue = BROWNCAKES[2] )); nextstep()
      case 2: getCake(targetCake(ifgreen = BROWNCAKES[1],  ifblue = BROWNCAKES[3] )); nextstep()
      case 4: getCake(targetCake(ifgreen = PINKCAKES[1],   ifblue = PINKCAKES[3]  )); nextstep()
      case 5: getCake(targetCake(ifgreen = PINKCAKES[3],   ifblue = PINKCAKES[1]  )); nextstep() # maybe
      case 7: submitCake(targetSquare(ifgreen = START_GREEN[0], ifblue = START_BLUE[0])); nextstep()

      case 8: nextstage()


def openingCareful():
    pass


def fallbackStrategy():
    AVERAGE_VECOLITY: float = 0  # temp values. so it compiles
    timeleft: float = 100        # change them to actual implementation

    # get cake
    # move to closest droppoint
    # repeat

    closestCake, toBase = closestCakePlusBase(main_bot.position)
    distance: float = dist(main_bot.position, closestCake.position) + dist(closestCake.position, closestBase.position)
    
    if timeleft < distance + AVERAGE_VECOLITY:
        cancelActions()
        gotoBase(closestBase(main_bot.position))
    else:
        match state.step:
            case 1: getCake(closestCake);    nextstep()
            case 2: submitCake(closestBase); nextstep()
            case 3: resetStep();             nextstep()









def main():
    while True:
        update()
        strategy()


if __name__ == "__main__":
    main()
