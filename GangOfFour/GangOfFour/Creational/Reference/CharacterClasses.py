'''
Storage for DnD Character Classes, used by Abstract Factory
'''

from .ReferenceClasses import *
from .ReferenceFunctions import *

class CharacterClass:
    # edition - should dictate how to create class and its values.
    _hitDice = DiceEnum.D4
    _className = None
    def __init__(self,editionEnum):
        self.edition = editionEnum

    def getArmorSkills(self):
        return 'None','None'

    def getHitDice(self):
        return self._hitDice

    def getClassName(self):
        return self._className

    def getNewLevelHP(self, level, conMod):
        return 0

    def getHPAtLevelOne(self,conMod):
        return self._hitDice

class ClericClass(CharacterClass):
    _hitDice = DiceEnum.D8
    _className = "Cleric"

    def getArmorSkills(self):
        return "Light", "Medium", "Shields"

    def getNewLevelHP(self, level, conMod):
        if level == 1:
            return self.getHPAtLevelOne(conMod)
        return rollDice(self._hitDice)+conMod

    def getHPAtLevelOne(self, conMod):
        return self._hitDice +conMod

class FighterClass(CharacterClass):
    _hitDice = DiceEnum.D10
    _className = "Fighter"

    def getArmorSkills(self):
        return 'Light','Medium','Heavy','Shields'

    def getNewLevelHP(self, level, conMod):
        if level == 1:
            return self.getHPAtLevelOne(conMod)
        return rollDice(self._hitDice)+conMod

    def getHPAtLevelOne(self, conMod):
        return self._hitDice +conMod

class WizardClass(CharacterClass):
    _hitDice = DiceEnum.D6
    _className = "Wizard"

    def getArmorSkills(self):
        return 'None'

    def getNewLevelHP(self, level, conMod):
        if level == 1:
            return self.getHPAtLevelOne(conMod)
        return rollDice(self._hitDice)+conMod

    def getHPAtLevelOne(self, conMod):
        return self._hitDice +conMod
