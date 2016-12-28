import unittest

from Infra.CardEnum import *
from Infra import DeckManager

class DeckManagerTests(unittest.TestCase):
    def setUp(self):
        self.DeckMgr = DeckManager.DeckManager()

    def tearDown(self):
        del self.DeckMgr

    def test_Constructor(self):
        #Arrange
        expectedDeck = DeckManager._defaultStartingDeck
        #Act
        deckMgr = DeckManager.DeckManager()
        #Assert
        self.assertIsNotNone(deckMgr)
        self.assertEqual(expectedDeck, deckMgr._deck)

    def test_RequestAvailableCard(self):
        #Arrange
        qCard = CardEnum.Ranch
        #Act
        result = self.DeckMgr.RequestCard(qCard)
        #Assert
        self.assertTrue(result)

    def test_RequestUnavailableCard(self):
        #Arrange
        qCard = CardEnum.TVStation

        for i in range(0,4): # request 4 TVStations, resulting in 0 left
            self.DeckMgr.RequestCard(qCard)

        #Act
        result = self.DeckMgr.RequestCard(qCard)
        #Assert
        self.assertFalse(result)

    def test_IsCardAvailableWithAvailableCard(self):
        #Arrange
        qCard = CardEnum.Ranch
        #Act
        result = self.DeckMgr.IsCardAvailable(qCard)
        #Assert
        self.assertTrue(result)

    def test_IsCardAvailableWithInvalidCard(self):
        #Arrange
        qCard = CardEnum.Undefined
        #Act
        result = self.DeckMgr.IsCardAvailable(qCard)
        #Assert
        self.assertFalse(result)

    def test_IsCardAvailableWithUnavailableCard(self):
        #Arrange
        qCard = CardEnum.TVStation

        for i in range(0,4): # request 4 TVStations, resulting in 0 left
            self.DeckMgr.RequestCard(qCard)

        #Act
        result = self.DeckMgr.IsCardAvailable(qCard)
        #Assert
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
