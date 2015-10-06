'''
Storage for Utility  Method which do not strictly belong to any class...
'''

from random import SystemRandom
def rollDice(diceSize):
    localRand = SystemRandom()
    return localRand.randint(1,diceSize)
