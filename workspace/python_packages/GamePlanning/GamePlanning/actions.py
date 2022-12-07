from classes import *
from gloabals import *
import GameStrategy


# file for handeling all ros interactions
# a level of abstraction above ros actions and one level below gameplanning


# updated all global variables 
# when overwriting main_bot, sub_sub, enemyA, enemyB make sure to safe the old value into old_ ... 
def update():
    pass






# the following functions starts action if is was not started
# if it was, it does nothing 
# after that action is done, it sets a is done flag



# moves to the position of the cake
# picks it up
# stores it in a revolver chamber
def getCake(cake: Cake):
    pass

# moves to the position of the cake
# builds a cake on the way
# places it down
# builds the rest
# places the rest down
def submitCake(square: position):
    pass


# if one of the above methods is done, increaments state.step by one
def nextstep():
    pass