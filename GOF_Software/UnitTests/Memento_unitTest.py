__author__ = 'D'

import unittest
from Behavioral.Memento import *

class TestObject():
    def __init__(self):
        self.data = {"defaultKey":"defaultValue"}

    def __delitem__(self, key):
        del self.data[key]
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.data[key] = value


class Memento_unitTest(unittest.TestCase):
    def setUp(self):
        self.testObj = TestObject()
        self.testObj["Key1"] = "value1"
        self.testObj["Key2"] = "value2"

    def tearDown(self):pass

    def test_MementoRestoresObjectOnRestoreCallWithDeepCopy(self):
        #B
        restorePoint = Memento(self.testObj, True)

        self.testObj["Key1"] = "Value3"
        assert self.testObj["Key1"] is "Value3"

        #O
        restorePoint()

        #C
        assert self.testObj["Key1"] is "value1"