"""
Purpose: The DeckManager will:
    + track purchased/available cards
    + card prices?
    + support PlayerBot card purchases

Knows:
    + Total Available per type
    + Current Available per type
    + Card prices
"""

from .CardEnum import *

_defaultStartingDeck = {
    CardEnum.WheatField:6,
    CardEnum.Ranch:6,
    CardEnum.Bakery:6,
    CardEnum.Cafe:6,
    CardEnum.ConvenienceStore:6,
    CardEnum.Forest:6,
    CardEnum.TVStation:4,
    CardEnum.Stadium:4,
    CardEnum.BusinesCenter:4,
    CardEnum.CheeseFactory:6,
    CardEnum.FurnitureFactory:6,
    CardEnum.Mine:6,
    CardEnum.FamilyRestaurant:6,
    CardEnum.AppleOrchard:6,
    CardEnum.FruitAndVegetableStand:6
}

class DeckManager():
    def __init__(self):
        from copy import deepcopy
        self._deck = deepcopy(_defaultStartingDeck)

    def RequestCard(self, card):
        if not self.IsCardAvailable(card):
            return False

        self._deck[card] -=1
        return True

    def IsCardAvailable(self,card):
        if card not in self._deck.keys():
            return False

        cnt = self._deck[card]
        return cnt>0
