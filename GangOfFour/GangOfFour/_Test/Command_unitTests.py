__author__ = 'D'

import unittest

class Command:
    def __init__(self,func):
        self.f = func

    def __call__(self, *args, **kwargs):
        return self.f()

    def __str__(self):
        return self.f.__name__+"Command"

def greet(who):
    return "Hello "+ who + "!"

def sum(a,b):
    return a+b

class Command_unitTest(unittest.TestCase):

    def setUp(self):
        self._greetCommand = Command(lambda: greet("World"))
        self._sumCommand = Command(lambda: sum(2,3))

    def tearDown(self):pass

    def test_GreetCommandCallable(self):
        result = self._greetCommand()

        assert "Hello World" in result

    def test_CommandCanTakeAnyLambda(self):
        result = self._sumCommand()

        assert result is 5
