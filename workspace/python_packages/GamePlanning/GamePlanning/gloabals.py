from classes import *

# starting posiions of all the cakes
BROWNCAKES: list[Cake] = [
    Cake(color.BROWN, Position(725, 1875)),
    Cake(color.BROWN, Position(725, 1125)),
    Cake(color.BROWN, Position(1275, 1875)),
    Cake(color.BROWN, Position(1275, 1125)),
]

YELLOWCAKES: list[Cake] = [
    Cake(color.YELLOW, Position(225, 2225)),
    Cake(color.YELLOW, Position(225, 775)),
    Cake(color.YELLOW, Position(1725, 2225)),
    Cake(color.YELLOW, Position(1725, 775)),
]
    
PINKCAKES: list[Cake] = [
    Cake(color.PINK, Position(225, 2425)),
    Cake(color.PINK, Position(225, 575)),
    Cake(color.PINK, Position(1725, 2425)),
    Cake(color.PINK, Position(1725, 575)),
    ]


# Starting Positions
# The coordinates are of the center of the square
START_BLUE: list[Position] = [
    Position(1775, 2775),
    Position(1775, 1125),
    Position(1275, 225),
    Position(225, 225),
    Position(225, 1875)
]

START_GREEN: list[Position] = [
    Position(225, 2775),
    Position(225, 1125),
    Position(750, 225),
    Position(1775, 225),
    Position(1775, 1875)
]


# the color that we are on
our_team: Team = Team(0)

# the cakes currently on the field
cakes: list[Cake] = list()
# the cakes on the field last tick
old_cakes: list[Cake] = list()



# our two Bots
main_bot: FriendlyBot
sub_bot: FriendlyBot
# our bots on the last tick
old_main_bot: FriendlyBot
old_sub_bot: FriendlyBot


# the two Bots of the enemy
enemyA: EnemyBot
enemyB: EnemyBot
# the enemy Bots on the last tick
old_enemyA: EnemyBot
old_enemyB: EnemyBot



