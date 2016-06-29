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
#from .CardEnum import *


class PlayerBot():
    def __init__(self, strat):
        self._strat = strat
        self._funds = 0

    def InjectDeck(self,deckMgr):
        self._deck = deckMgr
