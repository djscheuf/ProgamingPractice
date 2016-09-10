__author__ = 'D'
'''
This behavioral pattern is difficult to test rigorously because Python exhibits duck typing,
that is we cannot check the constructors or functions except by using them.
'''

from Behavioral.Strategy import *
import unittest

class Strategy_UnitTest(unittest.TestCase):

    def setUp(self):
        self._greatStrategy = GreatestFirstStrategy()
        self._leastStrategy = LeastFirstStrategy()
        self._data1 = 3,6,9,0,1,7,2,8,3
        self._data2 = 9,6,0,1,5,3,8,7,4

    def test_greatStrategyIsSortingStrategy(self):
        #Build-Operate-Check
        assert isinstance(self._greatStrategy,SortingStrategy)

    def test_leastStrategyIsSortingStrategy(self):
        #Build-Operate-Check
        assert isinstance(self._leastStrategy,SortingStrategy)

    def test_canCallEachStrategySameWay(self):
        #really this is just a test of duck typing...
        strategy = self._greatStrategy
        response = strategy.sort(self._data1)
        assert response == sorted(self._data1,reverse=True)

        strategy = self._leastStrategy
        response2 = strategy.sort(self._data2)
        assert response2 == sorted(self._data2)


if __name__ == '__main__':
    unittest.main()