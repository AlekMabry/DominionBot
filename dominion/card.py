from enum import Enum

class CardType(Enum):
    TREASURE = 0
    ACTION = 1
    VICTORY = 2

class Card:
    def __init__(self, name, cost, type, canBuy, isValid, play):
        self.name = name
        self.cost = cost
        self.type = type
        self.isValid = isValid      # Returns whether card can be played
        self.play = play            # Runs if card is played

def Copper_isValid(player):
    return True

def Copper_play(player):
    player.coins += 1

def Silver_isValid(player):
    return True

def Silver_play(player):
    player.coins += 2
    # Increase player coins that turn by 1

def Gold_isValid(player):
    return True

def Gold_play(player):
    player.coins += 3


Deck = [
    Card("Copper", 0, CardType.TREASURE, Copper_isValid, Copper_play),
    Card("Silver", 3, CardType.TREASURE, Silver_isValid, Silver_play),
    Card("Gold", 6, CardType.TREASURE, Gold_isValid, Gold_play),
]