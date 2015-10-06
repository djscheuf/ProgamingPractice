__author__ = 'D'

from Structural.Adapter import *
import unittest

class Adapter_UnitTest(unittest.TestCase):
    _input1 = "Item1"
    _input2 = "Item2"
    _input3 = "Item3"

    def setUp(self):
        self.stack = MyStack()

    def tearDown(self):
        self.stack.clear()

    def _addAnItemToStack(self):
        self.stack.push(self._input1)

    def _addSeveralItemsToStack(self):
        self.stack.push(self._input1)
        self.stack.push(self._input2)
        self.stack.push(self._input3)

    def test_newStackStartsEmpty(self):
        #B-O-C
        assert self.stack.size() == 0
        assert self.stack.isEmpty()

    def test_AddingItemToStackMakeItNotEmpty(self):
        #B-O
        self._addAnItemToStack()
        #C
        assert not self.stack.isEmpty()

    def test_popWhenEmptyReturnsNone(self):
        #B-O
        response = self.stack.pop()
        #c
        assert response is None

    def test_sizeReturnsNumberOfItemsInStackCorrectlyWithOneInput(self):
        #B-O
        self._addAnItemToStack()
        #C
        assert self.stack.size() == 1

    def test_sizeReturnsNumberOfItemsInStackCorrectlyWithSeveralInput(self):
        #B-O
        self._addSeveralItemsToStack()
        #C
        assert self.stack.size() == 3

    def test_stackReturnsInputsInReverseOrder(self):
        #B
        self._addSeveralItemsToStack()
        #O
        response1 = self.stack.pop()
        response2 = self.stack.pop()
        response3 = self.stack.pop()
        #C
        assert response1 == self._input3
        assert response2 == self._input2
        assert response3 == self._input1

    def test_clearRemovesAllEntriesInStack(self):
        #B
        self._addSeveralItemsToStack()
        #O
        self.stack.clear()
        #C
        assert self.stack.size() == 0
        assert self.stack.isEmpty()

if __name__ == '__main__':
    unittest.main()