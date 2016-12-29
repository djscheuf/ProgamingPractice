from ..Bot import BotState
from .InitializedEngineContext import InitializedEngineContext


class DeclareAnEngine:
    # May need more context for the engine ( needs a win condition)
    def WhoseInitialStateIs(deck, money):
        """provides initialization context for an engine"""
        state = BotState()
        state.Deck = deck
        state.Money = money

        return InitializedEngineContext(state)
