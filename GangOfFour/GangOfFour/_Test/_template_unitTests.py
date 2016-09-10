__author__ = 'D'

from something import *
import unittest

class ClassName_UnitTest(unittest.TestCase):
    #reused value for testing?

    def setUp(self):
        #setup for each test

    def tearDown(self):
        #teardown for each test

    #helper functions for tests?

    def test_something(self):
        #Build-Operate-Check

if __name__ == '__main__':
    unittest.main()