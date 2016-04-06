__author__ = 'DJS'

'''
Improvement on Existing Demo: Usage of Python Enum as Feature Keys

This allows users of the system to share the global Feature provider and have
a uniform, and hopefully controller way to request their features. Further,
If the FeatureProvider is restricted to take only FeatureKey inputs, then
the users will be unable to ask for Features the the system is unaware of.

This will be a minor inconvinience during new development of features, but provides
a measure of safety for use of existing ones. (No spelling errors can be made).
'''

from enum import Enum

class FeatureKey(Enum):
    AppTitle = 1
    Console = 2
    User = 3

from ComponentClasses import *

class ImprovedBar(Bar):
    def __init__(self, featureProvider):
        self.console = featureProvider.SafeRequest(FeatureKey.Console,HasMethods('WriteLine'))
        self.title = featureProvider.SafeRequest(FeatureKey.AppTitle,IsInstanceOf(str))
        self.user = featureProvider.SafeRequest(FeatureKey.User,IsInstanceOf(str))
        self.X = 10

from FeatureProvider import *
def demonstrateImprovement():
    print("\n*** Safer IoC Demo ***")
    #GlobalFeatureProvider.Provide(FeatureKey.Console,SimpleConsole())
    GlobalFeatureProvider.Provide(FeatureKey.Console,BetterConsole(prefix='-->'))
    GlobalFeatureProvider.Provide(FeatureKey.User,GetCurrentUser)
    GlobalFeatureProvider.Provide(FeatureKey.AppTitle,"New and Improved Demo...")

    bar = ImprovedBar(GlobalFeatureProvider)

    bar.PrintYourself()

if __name__ == '__main__':
    demonstrateImprovement()
