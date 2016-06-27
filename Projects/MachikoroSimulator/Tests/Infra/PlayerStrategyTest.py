import unittest

from Infra.CardEnum import *
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

    def test_ConstructDiffState(self):
        #Arrange
        endstate = {self.cards.Ranch:1}
        pStrat = strat.PlayerStrategy(endstate)
        curState = {self.cards.WheatField:1,self.cards.Bakery:1}
        expected = {
            self.cards.Ranch:CardCosts[self.cards.Ranch],
            self.cards.TrainStation:CardCosts[self.cards.TrainStation],
            self.cards.ShoppingMall:CardCosts[self.cards.ShoppingMall],
            self.cards.AmusementPark:CardCosts[self.cards.AmusementPark],
            self.cards.RadioTower:CardCosts[self.cards.RadioTower]
            }
        #Act
        result = pStrat._createDiffState(curState)
        #Assert
        self.assertEqual(expected, result)

    def test_WhatToBuyNext(self):
        #Arrange
        endstate = {self.cards.Ranch:1}
        pStrat = strat.PlayerStrategy(endstate)
        curState = {self.cards.WheatField:1,self.cards.Bakery:1}
        #Act
        result = pStrat.GetNextPurchase(curState)
        #Assert
        self.assertEqual(self.cards.Ranch, result)



if __name__ == '__main__':
    unittest.main()
