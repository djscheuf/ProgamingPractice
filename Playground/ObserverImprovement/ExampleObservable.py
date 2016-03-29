__author__ = 'DJS'
__purpose__= """In the GOF examplem,the observer relies on the observable to call a specified function. This seems to
    encourage the Observer to aggregate the updating behavior in a single function, or else use it as a router function.
    Neither seems to be a good way to execute it. So instead I am opting to try a method where in the observer also
    registers a function, that is called on it so that a particular observable calls a particular function in the given observer.
"""

class ExampleObservable():
    def __init__(self):
        self.functions = []

    def register(self,callback):
        if callback not in self.functions:
            self.functions.append(callback)

    def unregister(self,callback):
        if callback in self.functions:
            self.functions.remove(callback)

    def unregister_all(self):
        del self.functions[:]

    def update_observers(self):
        for fn in self.functions:
            fn()
