"""
Purpose: The DeckManager will:
    + track purchased/available cards
    + support PlayerBot card purchases

Knows:
    + Total Available per type
    + Current Available per type
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

    def _IsCardAvailable(self,card):
        """Returns boolean flag of card availablity."""
        if card not in self._deck.keys():
            return False

        cnt = self._deck[card]
        return cnt>0

    def RequestCard(self,card):
        """Request a card from the deck. If available it is awarded, if not, then denied"""
        if not self._IsCardAvailable(card):
            return False

        self._deck[card] -=1
        return True

    def GetAvailableCards(self):
        result = []

        for key in self._deck.keys():
            if self._deck[key] > 0:
                result.add(key)

        return result
