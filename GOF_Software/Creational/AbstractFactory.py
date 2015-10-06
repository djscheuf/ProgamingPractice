__author__ = 'D'
'''
Abstract Factory Pattern:
An AbstractFactory is a class that exists to create instances of another class. Described on page 87 of the
DesignPatternsBook. Typically, if you want to construct instances of a class, where the class is selected at run time,
you...
1. Create one AbstractFactory class for each existing class (or group of related classes) you wish to create.
2. Have a polymorphic "create instance" method on each AbstractFactory class, conforming to a common method signature,
    used to create instances of the corresponding class.
3. Store and pass around instances of the AbstractFactory class to control selection of the class to create.
[Copied from GOF Site]

For this implementation, we will assume the circumstance of a DnD application, specifically at PC creation time, or
basically any enemy based on a class. We will create a ClassFactory, which will instantiate the correct class based on
input parameters.
'''
from Reference.CharacterClasses import *

class CharacterClassFactory:
    # edition - representation of the Game Edition to Create Classes for
    def __init__(self,editionEnum):
        # differentiated init based on edition.
        self.edition = EditionEnum.FIFTH

    def getClassInfo(self,classType):
        if classType == ClassEnum.CLERIC:
            return ClericClass(self.edition)
        elif classType == ClassEnum.FIGHTER:
            return FighterClass(self.edition)
        elif classType == ClassEnum.WIZARD:
            return WizardClass(self.edition)
        else:
            return CharacterClass(self.edition)

def demonstrate():
    factory = CharacterClassFactory(EditionEnum.FIFTH)

    cleric = factory.getClassInfo(ClassEnum.CLERIC)
    assert isinstance(cleric,CharacterClass)
    fighter = factory.getClassInfo(ClassEnum.FIGHTER)
    assert fighter is not cleric
    wizard = factory.getClassInfo(ClassEnum.WIZARD)

    print("Wizard HD: " + str(wizard.getHitDice()))
    response =  fighter.getArmorSkills()
    print( "Fighter Armor Skills: ")
    for parts in response:
        print("\t"+parts)
    print("Clerics HP at a level 10, and ConMod 4: \n\t"+ str(cleric.getNewLevelHP(10,4)))

if __name__ == "__main__":
    demonstrate()