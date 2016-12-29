import random
from ..CardEnum import *

class Game():
    def __init__(self, players, engine):
        self._players = players

        self._playerCount = len(self._players)

        self._engine = engine
        self._initializeGame()

    def _initializeGame(self):
        random.seed()
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
        player = self._players[self._currentPlayer]

        # Ask current player for roll.
        dicecnt = player.HowManyToRoll()
        # roll
        rollnum = self._roll(dicecnt)

        # use engine to determine earning.
        #  - Steal first
        self._TakeMoneyIfNecessary(rollnum)

        # - Then Earn
        self._AwardMoneyIfNecessary(rollnum)

        # ask current player for purchase
        card = player.PurchaseCard(self._engine.GetAvailableCards())

        # make purchase
        if card is not CardEnum.NoCard:
            if player.Deduct(CardCosts[card]):
                player.AwardCard(card)

        # increment current player (increment turn if back to first player)
        self._currentPlayer = self._getNextPlayerIndex()
        if self._currentPlayer == 0:
            self._turn += 1

    def _roll(self, dice):
        """Rolls the designated number of 6 sided dice. Returns sum of dice."""
        result = 0
        i = 0
        while i < dice:
            result += random.randint(1, 6)
            i += 1
        return result

    def _TakeMoneyIfNecessary(self,rollnum):
        """Iterates thru all other players to determine if money is owed by rolling player."""
        currentPlayer = self._players[self._currentPlayer]
        nextIdx = self._getNextPlayerIndex()
        canContinue= True

        while canContinue:
            # - Determine Cards activated on other players
            nextPlayer = self._players[nextIdx]
            owed = self._engine.StealsMoney(nextPlayer.state, rollnum)

            # - Attempt to aware going around to next
            available = currentPlayer.Deduct(owed)
            if available is None:
                canContinue = False
                break
            else:
                nextPlayer.Award(available)
                if owed != available:
                    canContinue = False
                    break

            nextIdx = self._getNextPlayerIndex(nextIdx)
            if nextIdx == self._currentPlayer:
                canContinue = False

    def _getNextPlayerIndex(self):
        return (self._currentPlayer + 1) % self._playerCount

    def _AwardMoneyIfNecessary(self, rollnum):
        """Iterates thru all players and awards money from bank as applicable."""
        # Iterate thru other players first
        nextIdx = self._getNextPlayerIndex(self._currentPlayer)
        while nextIdx != self._currentPlayer:
            player = self._players[next]
            earned = self._enging.EarnsMoney(player.CurrentState, rollnum, False)
            # False because it is not the players turn
            player.Award(earned)
            nextIdx = self._getNextPlayerIndex(next)

        # Award money to current player
        player = self._players[self._currentPlayer]
        earned = self._engine.EarnsMoney(player.state, rollnum, True)
        player.Award(earned)

    def Reset(self):
        self._engine.Reset()
        self._initializeGame()
