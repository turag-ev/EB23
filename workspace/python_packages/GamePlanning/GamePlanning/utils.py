from typing import Optional, Union
import math


from classes import *
from gloabals import *
from actions import *
from config import *


# calculates the distance between two points
def dist(p1: position, p2: position) -> float:
    return math.sqrt(p1.x * p1.x + p2.y * p2.y)

# returns normalized vector
def normalize(vector: position) -> position:
    dist: float = dist(vector, position(0, 0))
    return position((vector.x / dist), (vector.y / dist))

#returns dot product of 2 vectors
def dotproduct(v1: position, v2: position) -> float:
    return v1.x * v2.x  +  v1.y * v2.y


# gets the closest cake from cakeliste to a given position
def closestCake(position: position) -> Cake:
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



def closestBot(position: position) -> tuple[float, Bot]:

    bots: list[Bot] = [main_bot, sub_bot, enemyA, enemyB]

    min: float = 1000000
    clostest: Bot
    
    for bot in bots:
        distance = dist(position, bot.position)
        if distance < min:
            min = distance
            clostest = bot

    return clostest





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
    if our_team == team.GREEN:
        return closestCake(ifgreen)
    if our_team == team.BLUE:
        return closestCake(ifblue)


# glorified if statement. 
def targetSquare(ifgreen: position, ifblue: position) -> position:
    if our_team == team.GREEN:
        return ifgreen
    if our_team == team.BLUE:
        return ifblue




# returns a list of Cakes that are potentially targeted by our opponents
def enemytargets() -> list[Cake]:
    pass





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



def determineEnemyAtributes():
    POSITION_THRESHHOLD: float = 50.0
    ANGLE_THRESHHOLD: float = 0.5

    corresponding = pairCurrentAndPastCakes()
    for old, new_cake in corresponding:

        # cake disappeared, a Bot must have picked it up
        if new_cake is None:
            bot: EnemyBot = closestBot(old.position)
            if bot.enemy and dist(old.position, bot.position) < POSITION_THRESHHOLD:
                bot.can_cake_unknown = False
                bot.can_cakes = True
        
        # the cake might have stayed static or was pushed
        if (new_cake is not None) and (old is not None):
            cake_dx: float = old.position.x - new_cake.position.x
            cake_dy: float = old.position.y - new_cake.position.y

            cake_velocity_vector = position(cake_dx, cake_dy)
            cake_velocity_vector = normalize(cake_velocity_vector)


            for old_bot, new_bot in [(old_enemyA, enemyA), (old_enemyB, enemyB)]:

                # if the bot is within a close distance of the cake
                if dist(new_cake.position, new_bot.position) < POSITION_THRESHHOLD:
                    # if the Bot is in the same line as the cake is pushed
                    cake_bot_vector = position(new_cake.position.x - new_bot.position.x, new_cake.position.y - new_bot.position.y)
                    if math.acos(dotproduct(cake_bot_vector, cake_velocity_vector)) < ANGLE_THRESHHOLD:
                        bot_dx: float = old_bot.position.x - new_bot.position.x
                        bot_dy: float = old_bot.position.y - new_bot.position.y

                        bot_velocity_vector = position(bot_dx, bot_dy)
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










                





    
    

