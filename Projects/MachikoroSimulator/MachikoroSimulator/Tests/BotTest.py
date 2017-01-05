import unittest
from ..Bot import *
from ..Strategy import StrategyFactory
from ..CardEnum import CardEnum

class BotTest(unittest.TestCase):
    def setUp(self):
        self.subject = Bot()

        self.FullBot = Bot()
        state = BotState()
        state.Deck[CardEnum.WheatField] = 1
        state.Deck[CardEnum.Bakery] = 1
        state.Money = 3

        self.FullBot.InitialState(state)
        self.FullBot.WithPlan(StrategyFactory().CheeseFactoryStrategy())

    def tearDown(self):
        pass

    def test_Init(self):
        #Arrange
        #Act
        bot = Bot()

        #Assert
        self.assertIsNone(bot._state)
        self.assertIsNone(bot._strategy)

    def test_WithPlan(self):
        #Arrange
        strat = StrategyFactory().DefaultStrategy()
        #Act
        self.subject.WithPlan(strat)
        #assert
        self.assertEqual(strat, self.subject._strategy)

    def test_InitialState(self):
        #Arrange
        state = BotState()
        state.Deck[CardEnum.WheatField] = 1
        state.Money = 1

        #Act
        self.subject.InitialState(state)

        #Assert
        self.assertEqual(self.subject._state, state)

    def test_CurrentState(self):
        # Arrange
        state = BotState()
        state.Deck[CardEnum.WheatField] = 1
        state.Money = 1

        self.subject.InitialState(state)

        #Act
        currState = self.subject.CurrentState()

        #Assert
        self.assertEqual(state, currState)

    def test_Deduct_RemovesAmount(self):
        #Arrange

        #Act
        result = self.FullBot.Deduct(2)

        #Assert
        state = self.FullBot.CurrentState()
        self.assertEqual(state.Money,1)
        self.assertEqual(result, 2)

    def test_Deduct_RemovesMaximumAmountIfNotEnough(self):
        # Arrange

        # Act
        result = self.FullBot.Deduct(4)

        # Assert
        state = self.FullBot.CurrentState()
        self.assertEqual(state.Money, 0)
        self.assertEqual(result, 3)

    def test_Deduct_NegativeAmountRaisesException(self):
        #Arrange
        unreachableFlag = True
        #Act
        try:
            self.FullBot.Deduct(-1)
            unreachableFlag = False
        except Exception:
            pass
        #Assert
        self.assertTrue(unreachableFlag)

    def test_Award_GivesAmount(self):
        #Arrange
        #Act
        self.FullBot.Award(1)
        #Assert
        self.assertEqual(self.FullBot.CurrentState().Money, 4)

    def test_Award_NegativeAmountThrowsException(self):
        # Arrange
        unreachableFlag = True
        # Act
        try:
            self.FullBot.Award(-1)
            unreachableFlag = False
        except Exception:
            pass
        # Assert
        self.assertTrue(unreachableFlag)

    def test_AwardCard_AddsNewCardToPlayerDeck(self):
        #Arrange
        card = CardEnum.Forest
        #Act
        self.FullBot.AwardCard(card)
        #Assert
        state = self.FullBot.CurrentState()
        self.assertTrue(card in state.Deck.keys())
        self.assertEqual(state.Deck[card], 1)

    def test_AwardCard_IncrementsCountOfExistingCards(self):
        #Arrange
        card = CardEnum.Bakery
        #Act
        self.FullBot.AwardCard(card)
        #Assert
        state = self.FullBot.CurrentState()
        self.assertEqual(state.Deck[card], 2)