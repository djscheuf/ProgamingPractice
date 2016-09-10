__author__ = 'D'

from Creational.Singleton import *
import unittest

class Singleton_UnitTest(unittest.TestCase):
    def setUp(self):
        self.DataAccess = DataAccess.Instance()

    def _getSecondAccess(self):
        return DataAccess.Instance()

    #def tearDown(self):
        #self.factory.dispose()

    def test_multipleGetsReturnSameInstance(self):
        #Build-Operate
        secondary = self._getSecondAccess()

        #Check
        assert secondary is self.DataAccess
        assert secondary._id == self.DataAccess._id

    def test_confirmSharedStateOfSingletonFromNewObjectToExisting(self):
        #Build
        secondary = self._getSecondAccess()

        #Operate
        inputString = "InputFromSecondary"
        secondary.setObject(inputString)

        response = self.DataAccess.getObject()

        #Check
        assert response == inputString

    def test_confirmSharedStateOfSingletonFromExistingObjectToNew(self):
        #Build
        secondary = self._getSecondAccess()

        #Operate
        inputString = "InputFromExisting"
        self.DataAccess.setObject(inputString)

        response = secondary.getObject()

        #Check
        assert response == inputString

    def test_newInstanceGetAllCurrentStateNotFreshState(self):
        #Build
        inputString = "InputBeforeSecondaryCreated"
        self.DataAccess.setObject(inputString)

        #Operate
        secondary = self._getSecondAccess()
        response = secondary.getObject()

        #Check
        assert response == inputString

    def test_cannotAccessSingletonOutsideInstanceFunction(self):
        #Build-Operate
        try:
            access = DataAccess()
        except TypeError:
            #Check
            pass

    def test_returnedInstanceIsOfDecoratedType(self):
        #Build-Operate-Check
        assert Singleton.__instancecheck__(DataAccess,self.DataAccess)

if __name__ == '__main__':
    unittest.main()