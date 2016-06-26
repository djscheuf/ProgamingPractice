import unittest

from Infra.CardEnum import CardEnum
import Infra.PlayerStrategy as strat


class PlayerStrategyTest(unittest.TestCase):
    def setUp(self):
        self.cards = CardEnum
        self.factory = strat.StratFactory

    def teardown(self):
        pass

    def test_Constructor(self):
        #Arrange
        #Act
        pStrat = strat.PlayerStrategy()
        #Assert
        self.assertIsNotNone(pStrat)

    def test_ConstructorParamter(self):
        #Arrange
        endState = { self.cards.Ranch:3, self.cards.CheeseFactory:3}
        #Act
        pStrat = strat.PlayerStrategy(endState)
        #Assert
        ActualEndState = {self.cards.WheatField:1,self.cards.Bakery:1,self.cards.Ranch:3,self.cards.CheeseFactory:3,self.cards.TrainStation:1,self.cards.ShoppingMall:1,self.cards.AmusementPark:1,self.cards.RadioTower:1}
        self.assertEqual(ActualEndState,pStrat.EndState)


if __name__ == '__main__':
    unittest.main()
