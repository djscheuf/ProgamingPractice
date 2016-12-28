"""
Purpose: A Bot is the element which knows how ot use a strategy.
  It contains the state a given strategy acts upon, and provides the desicions to the game engine.

Has a strategy
Knows Bot's current state:
  - Bot's current deck ( separate from Game deck)
  - Bot's current money
Decides:
  - Roll 1 or 2
  - Purchase? (Boolean)
  - - Purchase what? (which card)
"""

class BotState():
    def __init__():
        self.Deck = {}
        self.Money = 0

class Bot():
    def __init__(self):
        self._state = None
        self._strategy = None

    def WithPlan(self, strategy):
        """Provides Bot with a Plan to follow"""
        self._strategy = strategy

    def InitialState(self, state):
        """Initialized Bot state at the beginning of a game."""
        self._state = state

    def CurrentState(self):
        """Returns the current state of the bot"""
        return self._state

    def HowManyToRoll(self):
        """Asks bot how many dice to roll"""
        return self._strategy.HowManyToRoll(self._state)

    def PurchaseCard(self, availableCards):
        """Returns card to purchase or NoCard if undesired."""
        return self._strategy.PurchaseCard(self._state,availableCards)
