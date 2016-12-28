import unittest

from Infra.CardEnum import *
from Infra.PlayerStrategy import *
import Infra.DeckManager as Deck
import Infra.PlayerBot as Bot

class PlayerBotTests(unittest.TestCase):
    def setUp(self):
        self._testStrat = StratFactory.CheeseFactoryStrategy()
        self._bot = Bot.PlayerBot(self._testStrat)
        self._deckMgr = Deck.DeckManager()

    def tearDown(self):
        del self._bot
        del self._deckMgr

    def test_Constructor(self):
        #Arrange
        expectedStrat = StratFactory.CheeseFactoryStrategy()
        expectedProperties = { CardEnum.WheatField:1, CardEnum.Bakery:1}
        expectedFunds =0
        #Act
        bot = Bot.PlayerBot(expectedStrat)
        #Assert
        self.assertIsNotNone(bot)
        self.assertIsNotNone(bot._strat)
        # equivalent to stating the strategies are the same \/
        self.assertEqual(expectedStrat.EndState, bot._strat.EndState)
        self.assertEqual(expectedFunds,bot._funds)
        self.assertEqual(expectedProperties,bot._properties)

    def test_InjectDeck(self):
        #Arrange
        expectedDeck = Deck.DeckManager()

        #Act
        self._bot.InjectDeck(expectedDeck)

        #Assert
        self.assertEqual(self._bot._strat.Deck,expectedDeck)

    def test_AwardFunds(self):
        #Arrange
        defaultfunds = 0
        expectedIncrease = 5
        #Act
        self._bot.AwardFunds(expectedIncrease)
        #Assert
        self.assertEqual(defaultfunds+expectedIncrease,self._bot._funds)

    def test_TakeFunds(self):
        #Arrange
        increase = 5
        cost = 3
        self._bot.AwardFunds(increase)

        #Act
        result = self._bot.TakeFunds(cost)

        #Assert
        self.assertTrue(result)
        self.assertEqual(increase-cost,self._bot._funds)

    def test_GetNextDesiredCardWithCardsAvailable(self):
        #Arrange
        strat = StratFactory.DefaultStrategy()
        strat.EndState[CardEnum.TVStation] = 1

        bot = Bot.PlayerBot(strat)
        bot.InjectDeck(self._deckMgr)

        #Act
        result = bot.GetNextPurchase()

        #Assert
        self.assertEqual(CardEnum.TVStation,result)
        self.assertEqual(4,self._deckMgr._deck[CardEnum.TVStation])

    def test_GetNextDesiredCardWithoutCardsAvailable(self):
        #Arrange
        strat = StratFactory.DefaultStrategy()
        strat.EndState[CardEnum.TVStation] = 1

        for i in range(0,4):
            self._deckMgr.RequestCard(CardEnum.TVStation)

        bot = Bot.PlayerBot(strat)
        bot.InjectDeck(self._deckMgr)

        #Act
        result = bot.GetNextPurchase()

        #Assert
        self.assertEqual(CardEnum.Undefined,result)


if __name__ == '__main__':
    unittest.main()
