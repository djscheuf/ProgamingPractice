"""
Purpose: The Strategy represents, the desired final state of Owned cards.

+ utilize it's known end-state, and a given current-state to
    determine what action to take for the turn ( what cards to buy)
"""

from .CardEnum import *

_defaultEndState = {
    CardEnum.WheatField: 1,
    CardEnum.Bakery: 1,
    CardEnum.TrainStation: 1,
    CardEnum.ShoppingMall: 1,
    CardEnum.AmusementPark: 1,
    CardEnum.RadioTower: 1
}


class Strategy:
    def __init__(self, desiredEndState = None):
        from copy import deepcopy
        self.EndState = deepcopy(_defaultEndState)

        if desiredEndState is not None:
            for key in desiredEndState.keys():
                self.EndState[key] = desiredEndState[key]

    def HowManyToRoll(self, state):
        """Returns how many dice to roll. If have train station always roll 2"""
        if CardEnum.TrainStation in state.Deck.keys() and state.Deck[CardEnum.TrainStation] > 0:
            return 2

        return 1

    def PurchaseCard(self, state, availableCards):
        """Returns card to purchase, or NoCard"""
        #get diffState
        diffState = self._createDiffState(state)

        available = False
        while not available:
            #get Cheapest next desired Card
            nextGet = self._findCheapestNextDesired(diffState)

            if nextGet == CardEnum.NoCard:
                nextGet = CardEnum.NoCard
                available = True
                break

            diffState[nextGet] = None
            # removes next cheapest from possibles, prevents inf loop

            if nextGet in availableCards:
                available = True

        return nextGet

    def _createDiffState(self, curState):
        """Determines difference between current and desired states"""
        diffState = {}
        for key in list(self.EndState.keys()):
            curCnt = 0
            try:
                curCnt = curState.Deck[key]
            except KeyError:
                pass

            diff = self.EndState[key] - curCnt
            if diff > 0:
                diffState[key] = CardCosts[key]

        return diffState

    def _findCheapestNextDesired(self, diffState):
        """Finds the next cheapest card that is desirable to purchase"""
        # search for min within in Dict
        # may optimize later

        nextCard = CardEnum.NoCard
        minCost = 1e6  # Arbitrarily Large Number

        for key in list(diffState.keys()):
            if diffState[key] is not None:
                if diffState[key] < minCost:
                    nextCard = key
                    minCost = diffState[key]

        return nextCard


class StrategyFactory:
    def __init__(self):
        pass

    def DefaultStrategy(self):
        endState = {}
        return Strategy(endState)

    def CheeseFactoryStrategy(self):
        endState = {CardEnum.Ranch: 3, CardEnum.CheeseFactory: 3}
        return Strategy(endState)

    def FurnitureFactoryStrategy(self):
        endState = {CardEnum.Forest: 3, CardEnum.FurnitureFactory: 3}
        return Strategy(endState)

    def MyStrategy(self):
        endState = {CardEnum.Ranch: 2, CardEnum.Bakery: 2,
                    CardEnum.ConvenienceStore: 2, CardEnum.Mine: 2,
                    CardEnum.CheeseFactory: 2, CardEnum.Forest: 2,
                    CardEnum.FurnitureFactory: 2}
        return Strategy(endState)
