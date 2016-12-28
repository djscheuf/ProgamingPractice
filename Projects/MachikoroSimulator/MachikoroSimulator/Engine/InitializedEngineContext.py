class InitializedEngineContext():
    def __init__(self,state):
        self._initState = state

    def ProvidingThisDeck(self,deck):
        """Returns an engine ready to run a game"""
        return Engine(self._initState,deck)
