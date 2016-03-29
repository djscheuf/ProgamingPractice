__author__ = 'DJS'

'''
Intent: Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
[Copied from GOF site]

THe general opinion to implement the observer pattern is two parts.
    1. The Observable object should manage the list of, and notifying of the observers
    2. THe Observer must provide an agreed upon interface to update itself.
'''

class Observable():
    def __init__(self):
        self.observers = []

    def register(self,nuObserver):
        if not nuObserver in self.observers:
            self.observers.append(nuObserver)

    def unregister(self,observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def unregister_all(self):
        if self.observers:
            del self.observers[:]

    def update_observers(self, *args,**kwargs):
        for observer in self.observers:
            observer.update(*args,**kwargs)

from abc import ABCMeta, abstractmethod
class Observer():
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self,*args, **kwargs):
        pass

class AmericanStockMarkets(Observer):
    def update(self,*args, **kwargs):
        print ("ASM received: {0}\n{1}".format(args,kwargs))

class EuropeanStockMarkets(Observer):
    def update(self,*args, **kwargs):
        print ("ESM received: {0}\n{1}".format(args,kwargs))

if __name__ == "__main__":
    observable = Observable()

    asm_Observer = AmericanStockMarkets()
    esm_Observer = EuropeanStockMarkets()

    observable.register(asm_Observer)
    observable.register(esm_Observer)

    observable.update_observers("Market Rally", something="Hello World")
