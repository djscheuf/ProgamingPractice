__author__ = 'DJS'

'''
Component and Subclasses, used for the example
'''
from FeatureAssertions import *

class Component(object):
    "Symbolic base class for components"

class Bar(Component):

    def __init__(self, featureProvider):
        self.console = featureProvider.SafeRequest("Console",HasMethods('WriteLine'))
        self.title = featureProvider.SafeRequest("AppTitle",IsInstanceOf(str))
        self.user = featureProvider.SafeRequest("CurrentUser",IsInstanceOf(str))
        self.X = 0

    def PrintYourself(self):
        self.console.WriteLine('--Bar Instance--')
        self.console.WriteLine('Title: %s'% self.title)
        self.console.WriteLine('User: %s'%self.user)
        self.console.WriteLine('X: %d'% self.X)

class SimpleConsole(Component):
    def WriteLine(self,s):
        print(s)

class BetterConsole(Component):
    def __init__(self, prefix=''):
        self.prefix = prefix

    def WriteLine(self,s):
        lines = s.split('\n')
        for line in lines:
            if line:
                print(self.prefix,line)
            else:
                print()

def GetCurrentUser():
    import os
    return os.getenv('USERNAME') or 'Some User'

if __name__ == '__main__':
    print("Sector: Component Classes")


