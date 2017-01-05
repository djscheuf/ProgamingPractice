import unittest
from ...DeckManager import *
from ...Bot import *
from ...Engine.Engine import Engine
from ...Game.Game import Game
from ...Strategy import StrategyFactory

class GameTest(unittest.TestCase):
    def setUp(self):
        state = BotState()
        state.Deck = {CardEnum.WheatField: 1, CardEnum.Bakery: 1}
        state.Money = 3

        self._initPlayerState = state
        self.engine = Engine(self._initPlayerState)
        self.deck = DeckManager()

        self.basePlayers = [Bot(), Bot()]
        self.subject = Game(self.basePlayers,self.engine, self.deck)

    def _initState(self):
        state = BotState()
        state.Deck = {CardEnum.WheatField: 1, CardEnum.Bakery: 1}
        state.Money = 3

        return state

    def _goodState(self):
        state = self._initState()

        state.Deck[CardEnum.Ranch] = 3
        state.Deck[CardEnum.CheeseFactory] = 2
        state.Money = 10

        return state

    def _badState(self):
        state = self._initState()
        state.Money = 1

        return state

    def _createSmartPlayer(self):
        state = BotState()
        state.Deck = {CardEnum.WheatField: 1, CardEnum.Bakery: 1}
        state.Money = 3

        strat = StrategyFactory().CheeseFactoryStrategy()

        bot = Bot()
        bot.InitialState(state)
        bot.WithPlan(strat)

        return bot

    def tearDown(self):
        pass

    def test_Init(self):
        #Arrange
        #performed by Setup
        #Act
        game = Game(self.basePlayers, self.engine,self.deck)
        #Assert
        self.assertIsNotNone(game)
        self.assertEqual(game._currentDeck, self.deck)
        self.assertEqual(game._playerCount, 2)
        self.assertEqual(self.basePlayers[0].CurrentState(),self._initPlayerState)
        self.assertEqual(game._currentPlayer, 0)
        self.assertEqual(game._turn, 0)

    def test_Roll_1Die(self):
        #Arrange
        #performed by setup
        #Act
        roll = self.subject._roll(1)
        #Assert
        self.assertTrue(roll >= 1)
        self.assertTrue(roll <= 6)

    def test_Roll_2Dice(self):
        #Arrange
        #performed by setup
        #Act
        roll = self.subject._roll(2)
        #Assert
        self.assertTrue(roll >= 2)
        self.assertTrue(roll <= 12)

    def test_NextPlayerIndex(self):
        #Arrange
        #performed by setup
        #Act
        idx = self.subject._getNextPlayerIndex()
        #Assert
        self.assertEqual(1, idx)

    def test_NextPlayerIndex_LoopsOnLastPlayer(self):
        #Arrange
        self.subject._currentPlayer = 1 #since there are 2 players
        #Act
        idx = self.subject._getNextPlayerIndex()
        #Assert
        self.assertEqual(0, idx)

    def test_NextPlayerIndex_GivenIndex(self):
        #Arrange
        #Act
        idx = self.subject._getNextPlayerIndex(1) # should loop since last player
        #Assert
        self.assertEqual(0, idx)

    def test_TakeMoney_RollNotOnARed(self):
        #Arrange
        self.basePlayers[0].InitialState(self._goodState())
        self.basePlayers[1].InitialState(self._badState())

        # Hacky hacky hacky!
        self.subject._players = self.basePlayers
        #Act
        self.subject._TakeMoneyIfNecessary(2)

        #Assert
        #Confirms no money changed hands
        self.assertEqual(self.basePlayers[0].CurrentState().Money, 10)
        self.assertEqual(self.basePlayers[1].CurrentState().Money, 1)

    def test_TakeMoney_RollOnARedButNoReds(self):
        #Arrange
        self.basePlayers[0].InitialState(self._goodState())
        self.basePlayers[1].InitialState(self._badState())

        # Hacky hacky hacky!
        self.subject._players = self.basePlayers
        #Act
        self.subject._TakeMoneyIfNecessary(3) # a 3 would activate a cafe, if there was one.

        #Assert
        #Confirms no money changed hands
        self.assertEqual(self.basePlayers[0].CurrentState().Money, 10)
        self.assertEqual(self.basePlayers[1].CurrentState().Money, 1)

    def test_TakeMoney_RollOnARed(self):
        #Arrange
        self.basePlayers[0].InitialState(self._goodState())
        redState = self._badState()
        redState.Deck[CardEnum.Cafe] = 1
        self.basePlayers[1].InitialState(redState)

        # Hacky hacky hacky!
        self.subject._players = self.basePlayers
        #Act
        self.subject._TakeMoneyIfNecessary(3) # a 3 would activate a cafe, if there was one.

        #Assert
        #Confirms money changed hands
        self.assertEqual(self.basePlayers[0].CurrentState().Money, 9)
        self.assertEqual(self.basePlayers[1].CurrentState().Money, 2)

    def test_AwardMoney_RollABlue(self):
        # Arrange
        self.basePlayers[0].InitialState(self._goodState())
        self.basePlayers[1].InitialState(self._badState())

        # Hacky hacky hacky!
        self.subject._players = self.basePlayers
        # Act
        self.subject._AwardMoneyIfNecessary(1)

        # Assert
        # Confirms everyone gets something
        self.assertEqual(self.basePlayers[0].CurrentState().Money, 11)
        self.assertEqual(self.basePlayers[1].CurrentState().Money, 2)

    def test_AwardMoney_RollABlueAndAGreen(self):
        # Arrange
        good = self._goodState()
        good.Deck[CardEnum.Ranch] = 1
        self.basePlayers[0].InitialState(good)
        bad = self._badState()
        bad.Deck[CardEnum.Ranch] = 1
        self.basePlayers[1].InitialState(bad)

        # Hacky hacky hacky!
        self.subject._players = self.basePlayers
        # Act
        self.subject._AwardMoneyIfNecessary(2) # a 2 hits both ranch and bakery

        # Assert
        # Confirms everyone gets something, but Current gets more
        self.assertEqual(self.basePlayers[0].CurrentState().Money, 12)
        self.assertEqual(self.basePlayers[1].CurrentState().Money, 2)

    def test_AwardMoney_RollEmpty(self):
        # Arrange
        self.basePlayers[0].InitialState(self._goodState())
        self.basePlayers[1].InitialState(self._badState())

        # Hacky hacky hacky!
        self.subject._players = self.basePlayers
        # Act
        self.subject._AwardMoneyIfNecessary(6)

        # Assert
        # Confirms nobody gets anything
        self.assertEqual(self.basePlayers[0].CurrentState().Money, 10)
        self.assertEqual(self.basePlayers[1].CurrentState().Money, 1)

    def test_ExecTurn_IncrementsNextPLayerButNotTurnIfNotLastPlayer(self):
        #Arrange
        players = [self._createSmartPlayer(), self._createSmartPlayer()]
        self.subject._players = players
        self.subject._initializeGame()

        #Act
        self.subject._executeTurn()

        # Assert
        self.assertEqual(self.subject._turn, 0)
        self.assertEqual(self.subject._currentPlayer, 1)

    def test_ExecTurn_IncrementsNextPLayerAndTurnIfLastPlayer(self):
        #Arrange
        players = [self._createSmartPlayer(), self._createSmartPlayer()]
        self.subject._players = players
        self.subject._initializeGame()

        self.subject._currentPlayer = 1

        #Act
        self.subject._executeTurn()

        # Assert
        self.assertEqual(self.subject._turn, 1)
        self.assertEqual(self.subject._currentPlayer, 0)
