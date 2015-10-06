__author__ = 'D'

from Creational.Builder import *
import unittest

class Builder_UnitTest(unittest.TestCase):
    def setUp(self):
        self.Manufacturer = CharacterManufacturer()
        self.Manufacturer.Builder = ClericFirstLevelBuilder()
        self.buildClass = self.Manufacturer.create("Empty",0)
    #def tearDown(self):
        #self.factory.dispose()

    def createClassAgain(self, name, level):
        self.buildClass = self.Manufacturer.create(name, level);

    def test_getConcreteBuilderClassName(self):
        response = self.buildClass.getClassName(self.buildClass)
        assert response == "Cleric", "Class was Not Cleric as Expected: " + response

    def test_getDifferentConcreteBuilderClassName(self):
        self.Manufacturer.Builder = FighterFifthLevelBuilder()
        buildClass = self.Manufacturer.create("Empty",0)
        response = buildClass.getClassName(buildClass)
        assert response == "Fighter", "Class was Not Fighter as Expected: " + response

    def test_getLevelControlledByBuilder(self):
        response = self.buildClass.Level
        assert response == 1, "Level was Not 1 as Expected: " + response

        self.Manufacturer.Builder = FighterFifthLevelBuilder()
        self.createClassAgain("Empty", 0)
        response = self.buildClass.level
        assert response == 5, "Level was Not 5 as Expected: " + response

    def test_getNameGivenAtCreateTime(self):
        response = self.buildClass.Name
        assert response == "Holy Man Empty", "Name was not Holy Man Empty as Expected: " + response

        self.Manufacturer.Builder = FighterFifthLevelBuilder()
        self.createClassAgain("NewName", 0)
        response = self.buildClass.Name
        assert response == "Valorous NewName", "name was Not Valorous NewName as Expected: " + response


if __name__ == '__main__':
    unittest.main()