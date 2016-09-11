__author__ = 'DJS'
"""
Intent: Use sharing to support large numbers of fine-grained objects efficiently

Python has several ways to implement flyweight pattern. THe one shown below appears to manage the instanctionation of
objects so that objects being created with the same parameters point to the same instance. This is done with some magic
relating to Pythons underpinnings. However the decorator does seem the most logical approach for this implementation.
"""

def flyweight(cls):
    instances = dict()
    return lambda *args, **kargs: instances.setdefault((args, tuple(kargs.items())),cls(*args, **kargs))

@flyweight
class Spam():
    def __init__(self,a,b):
        self.a = a
        self.b = b

@flyweight
class Eggs():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def demonstrate():
    # recall that these are separate calls to the class constructors.
    print("Asserting to two calls to constructor with same args, returns pointer to same instance.")
    assert Spam(1,2) is Spam(1,2)
    assert Eggs('a', 'b') is Eggs('a', 'b')
    print("Asserting to two calls to differentc classes with same args, does not return pointer to same instace")
    print("\t( as expected, but proves no black magic)")
    assert Spam(1,2) is not Eggs(1,2)

    #cannot subclass.

if __name__ == "__main__":
    demonstrate()
