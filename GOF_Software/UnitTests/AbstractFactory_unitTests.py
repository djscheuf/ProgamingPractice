__author__ = 'D'

from Creational.AbstractFactory import *
import unittest

class AbstractFactory_UnitTest(unittest.TestCase):
    def setUp(self):
        self.factory = CharacterClassFactory(EditionEnum.UNDEFINED)

    #def tearDown(self):
        #self.factory.dispose()

    def test_getFactoryDefaultEdition(self):
        response = self.factory.edition
        assert response == EditionEnum.FIFTH

    def test_getClericClassInfo(self):
        response = self.factory.getClassInfo(ClassEnum.CLERIC)
        assert type(response) is ClericClass
        # test Cleric class stuff elsewhere?

    def test_getWizardClassInfo(self):
        response = self.factory.getClassInfo(ClassEnum.WIZARD)
        assert type(response) is WizardClass
        # test Wizard class stuff elsewhere?

    def test_getFighterClassInfo(self):
        response = self.factory.getClassInfo(ClassEnum.FIGHTER)
        assert type(response) is FighterClass
        # test Fighter class stuff elsewhere?

    def test_getGivenClassHasSameEditionAsFactory(self):
        factoryEdition = self.factory.edition
        producedClass = self.factory.getClassInfo(ClassEnum.CLERIC)
        assert producedClass.edition == factoryEdition

    def test_getDefaultClass(self):
        response = self.factory.getClassInfo(ClassEnum.UNDEFINED)
        assert isinstance(response,CharacterClass)
        #exhaustive testing...
        assert type(response) is not ClericClass
        assert type(response) is not FighterClass
        assert type(response) is not WizardClass

if __name__ == '__main__':
    unittest.main()