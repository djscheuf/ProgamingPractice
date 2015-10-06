__author__ = 'D'
'''
Builder Pattern:
Intent: Separate the steps for constructing of a complex object from its final representation so that
(a) an object with strict properties
    (e.g. immutable, or say, maxTemperature >= minTemperature) can be configured in less strict steps,
(b) avoid hard-to-remember/understand chatty constructors with many arguments, and
(c) where possible allow the caller to reuse steps for creating similar instances.
'''
from Reference.CharacterClasses import *

class Character:
    def __init__(self,characterClass):
        self.Class = characterClass
        self.Name = None
        self.Level = None
        self.Equipment = None

    def view(self):
        name = self.Name
        level = str(self.Level)
        className = CharacterClass.getClassName(self.Class)
        hitDice = str(CharacterClass.getHitDice(self.Class))
        armorSkills = str(self.Class.getArmorSkills(self.Class))
        print(name + " is a " + level +" Level " + className)
        print("Their hit dice is: d"+hitDice +".")
        print("And They can use the following armor: "+ armorSkills+".\n")

class CharacterBuilder:

    def makeName(self, newName):
        raise

    def makeLevel(self, levelToSet):
        raise

class ClericFirstLevelBuilder(CharacterBuilder):
    def __init__(self):
        self.character = Character(ClericClass);

    def makeName(self, newName):
        self.character.Name = "Holy Man " + newName

    def makeLevel(self, levelToSet):
        self.character.Level = 1


class FighterFifthLevelBuilder(CharacterBuilder):
    def __init__(self):
        self.character = Character(FighterClass);

    def makeName(self, newName):
        self.character.Name = "Valorous " + newName

    def makeLevel(self, levelToSet):
        self.character.Level = 5

class CharacterManufacturer:
    def __init__(self):
        self.Builder = None

    def create(self, name, level):
        assert not self.Builder is None, "No defined Builder!"
        self.Builder.makeName(name)
        self.Builder.makeLevel(level)
        return self.Builder.character

def demonstrate():
    manufacturer = CharacterManufacturer()

    manufacturer.Builder = ClericFirstLevelBuilder()
    cleric = manufacturer.create("Relian",10)
    cleric.view()

    manufacturer.Builder = FighterFifthLevelBuilder()
    fighter = manufacturer.create("Kalyxta", 7)
    fighter.view()

if __name__ == "__main__":
    demonstrate()