"""
Purpose: PlayerBot will:
    + utilize a strategy to determine what to card to buy, if any ( based on funds)
    + request desired cards from DeckManager (injected)
    + present its current state to GameManager for evaluation
    + recall and manage its funds, awarded by GameManager

Knows:
    + Current state
    + Desired End state
    + Current funds
    + How to choose next desired purchase ( may be refactored later)
"""
from .CardEnum import *


class PlayerBot():
    def __init__(self, strat):
        self._strat = strat
        self._funds = 0
        self._deck = None
        #default properties from basic game.
        self._properties = {
            CardEnum.WheatField:1,
            CardEnum.Bakery:1
            }

    def InjectDeck(self,deckMgr):
        self._strat.InjectDeck(deckMgr)

    def AwardFunds(self,increment):
        #increment expected to be positive
        self._funds += increment

    def TakeFunds(self,decrement):
        #reports success of decrement
        # decrement expected to be a positive number
        if(self._funds > decrement):
            self._funds -= decrement
            return True

        return False

    def GetNextPurchase(self):
        return self._strat.GetNextPurchase(self._properties)
