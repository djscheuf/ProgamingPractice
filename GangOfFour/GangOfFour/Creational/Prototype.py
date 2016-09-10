__author__ = 'DJS'
"""
Intent: Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

Python appears to not need prototyping as much. That or it is very abstracted, allowing for the very state of an object
to be replicated... Similar to the Borg based Singleton. Alternatively, you can use this in conjunction with an object
factory. For the purpose of this example, I shall assume pyototype to be an inherited class.
"""
import copy


class Prototype:
    _type = None
    _value = None

    def clone(self):
        pass

    def getType(self):
        return self._type

    def getValue(self):
        return self._value

class TypeOne(Prototype):
    def __init__(self,value):
        self._type = 'Type1'
        self._value = value

    def clone(self):
        return copy.copy(self) # This is important, as this is how a prototype is used!

class TypeTwo(Prototype):
    def __init__(self,value):
        self._type = 'Type2'
        self._value = value

    def clone(self):
        return copy.copy(self)

class Factory:
    _T1V1 = None
    _T1V2 = None
    _T2V1 = None
    _T2V2 = None

    @staticmethod
    def init():
        Factory._T1V1 = TypeOne("One")
        Factory._T1V2 = TypeOne(2)
        Factory._T2V1 = TypeTwo(1)
        Factory._T2V2 = TypeTwo("Two")

    @staticmethod
    def getT1V1():
        return Factory._T1V1.clone()

    @staticmethod
    def getT1V2():
        return Factory._T1V2.clone()

    @staticmethod
    def getT2V1():
        return Factory._T2V1.clone()

    @staticmethod
    def getT2V2():
        return Factory._T2V2.clone()




def demonstrate():
    factory = Factory()
    factory.init()

    inst = factory.getT1V1()
    print("%s : %s"%(inst.getType(),inst.getValue()))

    inst = factory.getT1V2()
    print("%s : %s"%(inst.getType(),inst.getValue()))

    inst = factory.getT2V1()
    print("%s : %s"%(inst.getType(),inst.getValue()))

    inst = factory.getT2V2()
    print("%s : %s"%(inst.getType(),inst.getValue()))

    assert inst is not factory._T2V2 # proof that it is a clone not the same as.

if __name__ == "__main__":
    demonstrate()