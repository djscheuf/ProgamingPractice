"""
Purpose: The PlayerStrategy represnets, the desired final state of Owned CardEnum.

+ utilize it's known end-state, and a given current-state to
    determine what action to take for the turn ( what cards to buy)
"""
from .CardEnum import *

_defaultEndState = {
    CardEnum.WheatField:1,
    CardEnum.Bakery:1,
    CardEnum.TrainStation:1,
    CardEnum.ShoppingMall:1,
    CardEnum.AmusementPark:1,
    CardEnum.RadioTower:1
}

class PlayerStrategy():
    def __init__(self,desiredEndState=None):
        from copy import deepcopy
        self.EndState = deepcopy(_defaultEndState)
        self.Deck = None

        if(desiredEndState != None):
            for key in desiredEndState.keys():
                self.EndState[key] = desiredEndState[key]

    def InjectDeck(self,deckManager):
        self.Deck = deckManager

    def GetNextPurchase(self,curState):
        #get diffState
        diffState = self._createDiffState(curState)

        available = False
        while( not available):
            #get Cheapest next desired Card
            nextGet = self._findCheapestNextDesired(diffState)

            if(nextGet == CardEnum.Undefined):
                nextGet = CardEnum.Undefined
                available = True
                break

            diffState[nextGet] = None # removes next cheapest from possibles, prevents inf loop

            available = self._QueryCardAvailabile(nextGet)

        return nextGet

    def _createDiffState(self,curState):
        diffState = {}
        for key in self.EndState.keys():
            curCnt = 0
            try:
                curCnt = curState[key]
            except KeyError:
                pass

            diff = self.EndState[key] - curCnt
            if(diff > 0):
                diffState[key] = CardCosts[key]

        return diffState

    def _findCheapestNextDesired(self,diffState):
        # search for min within in Dict
        # may optimize later

        nextCard = CardEnum.Undefined
        minCost = 1e6 # Arbitrarily Large Number

        for key in diffState.keys():
            if(diffState[key] is not None):
                if(diffState[key] < minCost):
                    nextCard = key
                    minCost = diffState[key]

        return nextCard

        #[OTMZ] - tagged for optimization

    def _QueryCardAvailabile(self, nextGet):
        if(self.Deck is not None):
            available = self.Deck.IsCardAvailable(nextGet)
        else:
            available = True

        return available

class PlayerStategyFactory():
    def __inint__(self):
        pass

    def DefaultStrategy(self):
        endState = {}
        return PlayerStrategy(endState)

    def CheeseFactoryStrategy(self):
        endState = {CardEnum.Ranch:3,CardEnum.CheeseFactory:3}
        return PlayerStrategy(endState)

    def FurnitureFactoryStrategy(self):
        endState = {CardEnum.Forest:3,CardEnum.FurnitureFactory:3}
        return PlayerStrategy(endState)

    def MyStrategy(self):
        endState = {CardEnum.Ranch:2, CardEnum.Bakery:2, CardEnum.FamilyRestaurant:2,CardEnum.CheeseFactory:2,CardEnum.Forest:2,CardEnum.FurnitureFactory:2}
        return PlayerStrategy(endState)

StratFactory = PlayerStategyFactory()
