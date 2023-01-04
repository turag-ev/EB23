from typing import Optional, Union
import math


from classes import *
from gloabals import *
from actions import *
from config import *


# calculates the distance between two points
def dist(p1: Position, p2: Position) -> float:
    return math.sqrt(p1.x * p1.x + p2.y * p2.y)

# returns normalized vector
def normalize(vector: Position) -> Position:
    dist: float = dist(vector, Position(0, 0))
    return Position((vector.x / dist), (vector.y / dist))

#returns dot product of 2 vectors
def dotproduct(v1: Position, v2: Position) -> float:
    return v1.x * v2.x  +  v1.y * v2.y


# gets the closest cake from cakeliste to a given position
def closestCake(position: Position) -> Cake:
    if len(cakes) == 0:
        return None

    min: float = 1000000
    clostest: Cake
    
    for cake in cakes:
        distance = dist(position, cake.position)
        if distance < min:
            min = distance
            clostest = cake

    return clostest



def closestBot(position: Position) -> Bot:

    bots: list[Bot] = [main_bot, sub_bot, enemyA, enemyB]

    min: float = 1000000
    clostest: Bot
    
    for bot in bots:
        distance = dist(position, bot.position)
        if distance < min:
            min = distance
            clostest = bot

    return clostest


def closestBase(position: Position) -> Position:

    bases: list[Position]

    if our_team == Team.BLUE:
        bases = START_BLUE
    if our_team == Team.GREEN:
        bases = START_GREEN


    min: float = 1000000
    clostest: Position
    
    for base in bases:
        distance = dist(position, base.position)
        if distance < min:
            min = distance
            clostest = base

    return clostest

def closestSquare(position: Position) -> Position:

    bases: list[Position] = START_BLUE + START_GREEN

    min: float = 1000000
    clostest: Position
    
    for base in bases:
        distance = dist(position, base.position)
        if distance < min:
            min = distance
            clostest = base

    return clostest

def closestCakePlusBase(position: Position) -> tuple[Cake, Position]:
    minDist: float = 10000000
    minCake: Cake
    minBase: Position

    for cake in cakes:
        if not isCakeInBase(cake):
            distToCake: float = dist(main_bot.position, cake.position)

            square: Position = closestBase(cake.position)
            distToBase: float = dist(cake.position, cake.position)

            distTotal = distToCake + distToBase
            if (distTotal < minDist):
                minDist = distTotal
                minCake = cake
                minBase = square

    return (minCake, minBase)


def isCakeInBase(cake: Cake):
    POSITION_THRESHHOLD: float = 50.0

    base: Position = closestBase(cake.position)
    distance: float = dist(base, cake.position)

    if (distance < POSITION_THRESHHOLD):
        return True
    else:
        return False



# gets the index of the enemies starting position
# the index is easier to work with for the first gameplanning decisions
def determineSpawn(enemy: EnemyBot) -> int:
    pos = position(enemy.position.x, enemy.position.y)

    starting_positions: list[position] 

    if enemy.team == color.BLUE:
        starting_positions = START_BLUE

    elif enemy.team == color.GREEN:
        starting_positions = START_GREEN

    min: float = 1000000
    index: int = 0


    for i, position in enumerate(starting_positions):
        dist1 = dist(position, pos)
        if dist1 < min:
            min = dist
            index = i


    return index

# reurns the enemy that is on target starting square
# if there is one, if not it returns None
def enemyOnSpawn(square: int) -> Optional[Bot]:
    spawnA = determineSpawn(enemyA)
    spawnB = determineSpawn(enemyB)

    if spawnA == square:
        return enemyA

    if spawnB == square:
        return enemyB

    return None



# find the cake with the closes real position to the targeted cake
# the targeted cake depend on the color of our teams
def targetCake(ifgreen: Cake, ifblue: Cake) -> Cake:
    if our_team == Team.GREEN:
        return closestCake(ifgreen)
    if our_team == Team.BLUE:
        return closestCake(ifblue)


# glorified if statement. 
def targetSquare(ifgreen: Position, ifblue: Position) -> Position:
    if our_team == Team.GREEN:
        return ifgreen
    if our_team == Team.BLUE:
        return ifblue


def resetStep():
    state.step = 0

# returns a list of Cakes that are potentially targeted by our opponents
def enemytargets() -> list[Cake]:
    pass

def canMakePerfect(cakes: list[Cake]):

    colorPresent = [False, False, False]
    for cake in cakes:
        color[int(cake.color)] = True

    return all(colorPresent)




# takes the cakes the sensors gave us this tick, 
# compares them with the cake the sensors gave us last tick
# pairs cakes likely to be the same together. None if no cake is corresponding
# returns the list of pairs
def pairCurrentAndPastCakes() -> list[tuple[Optional[Cake], Optional[Cake]]]:
    corresponding: list[tuple[Optional[Cake], Optional[Cake]]] = list()


    for old_cake in old_cakes:
        closest: Cake = closestCake(old_cake)

        dontadd: bool = False
        for pair in corresponding:
            if pair[1] == closest:
                if dist(old_cake.position, closest) > dist(pair[0], pair[1]):
                    dontadd = True
                    break
                else:
                    corresponding.remove(pair)
                    break
        
        if dontadd == True:
            corresponding.append((old_cake, None))
        else:
            corresponding.append((old_cake, closest))


    for cake in cakes:
        exists: bool = False
        for pair in corresponding:
            if cake == pair[1]:
                exists = True

        if exists == False:
            corresponding.append((None, cake))

    return corresponding



def updateKnowledgeOnEnemy():
    POSITION_THRESHHOLD: float = 50.0
    ANGLE_THRESHHOLD: float = 0.5

    corresponding = pairCurrentAndPastCakes()
    for old, new_cake in corresponding:

        # cake disappeared, a Bot must have picked it up
        if new_cake is None:
            bot: EnemyBot = closestBot(old.position)
            if bot.enemy and dist(old.position, bot.position) < POSITION_THRESHHOLD:
                bot.can_pickup.haveGuess = True
                bot.can_pickup.able = True
                bot.storage += old.color

        # new cake appeared, a Bot must have dropped it
        if old is None and new_cake is not None:
            bot: EnemyBot = closestBot(new_cake.position)
            if bot.enemy and dist(old.position, bot.position) < POSITION_THRESHHOLD:
                if old.color == color.PINK:
                    bot.dropped += old
                    if mightPerfCount == 3:
                        bot.storage.remove(color.PINK)
                        bot.storage.remove(color.YELLOW)
                        bot.storage.remove(color.BROWN)

                        # add cakes to be perfect recepe 

                        bot.dropped.clear()
                else:
                    if bot.dropped.count() != 0:
                        for _ in range(bot.dropped.count()):
                             bot.storage.remove(color.PINK)
                    else:
                        bot.storage.remove(old.color)
                    


        
        # the cake might have stayed static or was pushed
        if (new_cake is not None) and (old is not None):
            cake_dx: float = old.position.x - new_cake.position.x
            cake_dy: float = old.position.y - new_cake.position.y

            cake_velocity_vector = Position(cake_dx, cake_dy)
            cake_velocity_vector = normalize(cake_velocity_vector)


            for old_bot, new_bot in [(old_enemyA, enemyA), (old_enemyB, enemyB)]:

                # if the bot is within a close distance of the cake
                if dist(new_cake.position, new_bot.position) < POSITION_THRESHHOLD:
                    # if the Bot is in the same line as the cake is pushed
                    cake_bot_vector = Position(new_cake.position.x - new_bot.position.x, new_cake.position.y - new_bot.position.y)
                    if math.acos(dotproduct(cake_bot_vector, cake_velocity_vector)) < ANGLE_THRESHHOLD:
                        bot_dx: float = old_bot.position.x - new_bot.position.x
                        bot_dy: float = old_bot.position.y - new_bot.position.y

                        bot_velocity_vector = Position(bot_dx, bot_dy)
                        bot_velocity_vector = normalize(bot_velocity_vector)

                        # if the cake is pushed in the same direction as the bot is moving
                        if math.acos(dotproduct(cake_velocity_vector, bot_velocity_vector)) < ANGLE_THRESHHOLD:
                            new_bot.can_push_unknown = False
                            new_bot.can_push = True

# add strategic layer: 
# if the best / most reasonable move was to move to a cake, 
# but it didnt, that most likley was because it is uncabable to

# make the above function have priority over that strategic function
# could just be bad planning










                





    
    

