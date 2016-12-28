from copy import deepcopy

class Engine():
    def __init__(self, initialPlayerState, deck):
        self._initPlayerState = initialPlayerState

        self._initialDeck = deepcopy(deck)
        self._currentDeck = deck

    def Reset(self):
        self._currentDeck = deepcopy(self._initialDeck)

    def WinConditionMet(self,players):
        """Evaluates all player states for one matching the win condition"""
        return True

    def GetWinner(self,players):
        """Returns first player who matches the win condition"""
        return players[0]
