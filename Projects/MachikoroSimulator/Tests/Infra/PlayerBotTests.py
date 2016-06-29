import unittest

from Infra.CardEnum import *
from Infra.PlayerStrategy import *
import Infra.PlayerBot as Bot

class PlayerBotTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Constructor(self):
        #Arrange
        expectedStrat = StratFactory.CheeseFactoryStrategy()
        expectedFunds =0
        #Act
        bot = Bot.PlayerBot(expectedStrat)
        #Assert
        self.assertIsNotNone(bot)
        self.assertIsNotNone(bot._strat)
        # equivalent to stating the strategies are the same \/
        self.assertEqual(expectedStrat.EndState, bot._strat.EndState)
        self.assertEqual(expectedFunds,bot._funds)

    def test_InjectDeck(self):
        #Arrange
        #Act
        #Assert

if __name__ == '__main__':
    unittest.main()
