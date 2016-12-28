class Game():
    def __init__(self,players,engine):
        self._players = players

        self._playerCount = len(self._players)

        self._engine = engine
        self._initializeGame()

    def _initializeGame(self):
        initState = self._engine.InitialState

        for player in self.Players:
            player.InitialState(initState)

        self._currentPlayer = 0
        self._turn = 0

    def Run(self):

        gameFinished = False
        while not gameFinished:
            self._executeTurn()
            gameFinished = self._engine.WinConditionMet(self._players)

        self.Winner = self._engine.GetWinner(self._players)
        self.TotalTurns = self._turns

    def _executeTurn(self):
        pass


    def Reset(self):
        self._engine.Reset()
        self._initializeGame()
