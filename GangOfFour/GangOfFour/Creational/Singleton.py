__author__ = 'D'
'''
Singleton Pattern:
If a system only needs one instance of a class, and that instance needs to be accessible in
many different parts of a system, you control both instantiation and access by making that class a singleton.
[Copied from GOF site]

For this implementation we will be creating the singleton as a decorator on a data-access class,
as this is one of the key examples where a singleton would be preferable.
'''

class Singleton:
    '''
    Please note that this design is not inherently my own, but rather is based on :
    http://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons-in-python
    the post which discusses an actual singleton class as a decorator.

    The discussion also indicates that making something a singleton in python would be better done
    by making it a module. alternatively we could use the Borg pattern, which is also a python specific pattern.
    Borg Pattern: http://code.activestate.com/recipes/66531/

    For this exercise I have chosen the option I best understood.
    -DJS 20FEB2015
    '''

    def __init__(self,decorated):
        self._decorated = decorated

    def Instance(self):
        '''
        This is the workhorse function. Where instantiation and organized returns occur. It will follow
        the LazyInstantiation idiom and simply returns the created instance of the decorated object.

        Naturally it will call the decorated objects __init__ function when creating for the first time.
        '''
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        '''
            This is function is a python standard for objects. Here we block access to the decorated object
            in any manner except Instance. (however I am not certain of the circumstances where this function is
            invoked.
        '''
        raise TypeError('Singletons must be accessed through \'Instance()\'.')

    def __instancecheck__(self,inst):
        return isinstance(inst,self._decorated)



from random import SystemRandom
from datetime import datetime
@Singleton
class DataAccess:
    def __init__(self):
        localRand = SystemRandom()
        a = localRand.randint(1,45)
        b = localRand.randint(47,68)
        self._id = str(localRand.randint(a,b))+"_20FEB2015"

    def getObject(self, verbose=False):
        if( verbose):
            print("Reading Storage...")
            print("Got Object!")
        return self._object

    def setObject(self, objectToStore,verbose=False):
        if( verbose):
            print("Checking Object...")
            print("Set Object.")
        self._object = objectToStore

def demonstrate():

    #access = DataAccess()

    access = DataAccess.Instance()
    access2 = DataAccess.Instance()

    assert access is access2
    print( "Access is Access2")

    print(access._id)
    print(access2._id)

    input = "I am Groot"
    access.setObject(input,True)
    response = access2.getObject(True)
    assert response == input
    print( response )


if __name__ == '__main__':
    demonstrate()