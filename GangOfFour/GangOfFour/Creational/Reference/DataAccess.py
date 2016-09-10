__author__ = 'D'

'''
Storage for some DataAccessor Classes. For now these are simply Mock Objects
'''

from random import SystemRandom
from datetime import datetime
from Creational import Singleton

@Singleton
class DataAccess:
    def __init__(self):
        localRand = SystemRandom()
        a = localRand.randint(1,45)
        b = localRand.randint(47,68)
        self._id = str(localRand.randint(a,b))+"_"+ datetime.strftime("%d/%m/%y")

    def getObject(self):
        print("Reading Storage...")
        print("Got Object!")
        return self._object

    def setObject(self, objectToStore):
        print("Checking Object...")
        print("Set Object.")
        self._object = objectToStore

def demonstrate():
    access = DataAccess.Instance()
    access2 = DataAccess.Instance()

    assert access is access2
    print( "Access is Access2")

    print(access._id)
    print(access2._id)

    input = "I am Groot"
    access.setObject(input)
    response = access2.getObject()
    assert response == input
    print( response )


if __name__ == '__main__':
    demonstrate()
