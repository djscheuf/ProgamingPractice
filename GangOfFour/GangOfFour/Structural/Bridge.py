__author__ = 'DJS'
"""
Intent: The BridgePattern decouples an abstraction from its implementation so that the two can vary independently.
This is unlike the intent of the AdapterPattern, which exists only to adapt the interface of one class to another.

To rephrase this the bridge is responsible for routing the calls to through the agreed upon structure, but who does the calling
 and what functionality that is the two should be independent, and not really known until instrancation time?
"""

class Interface():
    def FunctionToCall(self):
        raise NotImplemented()

class Bridge(Interface):
    def __init__(self):
        self._implementation = None

    def _executeFunctionCall(self):
        if self._implementation is not None:
            self._implementation.FunctionToCall()

class UseCase1(Bridge):
    def __init__(self, implementation):
        self._implementation = implementation

    def FunctionToCall(self):
        print("Use Case = 1")
        self._executeFunctionCall()
        print("End Use Case 1")

class UseCase2(Bridge):
    def __init__(self, implementaiton):
        self._implementation = implementaiton

    def FunctionToCall(self):
        print("This is a different use case")
        print("With different actions prior to function call since this is:")
        self._executeFunctionCall()
        print("And we like:")
        self._executeFunctionCall()
        print("All is right with the world")

class Impl1(Interface):
    def FunctionToCall(self):
        print("Windows")

class Impl2(Interface):
    def FunctionToCall(self):
        print("Linux")


def demonstrate():
    linux = Impl2()
    win = Impl1()

    us1Win = UseCase1(win)
    us1Lin = UseCase1(linux)

    us2Lin = UseCase2(linux)
    us2Win = UseCase2(win)

    us1Win.FunctionToCall()
    us2Lin.FunctionToCall()

    us2Win.FunctionToCall()
    us1Lin.FunctionToCall()

if __name__ == "__main__":
    demonstrate()
