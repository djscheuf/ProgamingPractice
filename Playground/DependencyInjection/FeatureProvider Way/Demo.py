__author__ = 'DJS'

from FeatureProvider import *
from ComponentClasses import *

def demonstrateSystem():
    print("\n**IoC Demo - Feature Provider Way **")
    #GlobalFeatureProvider.Provide("AppTitle",'Inversion of Control ...\n\n ... The Python Way')
    GlobalFeatureProvider.Provide("AppTitle","I'm sorry, Dave. I can't do that.")
    GlobalFeatureProvider.Provide("CurrentUser",GetCurrentUser)
    GlobalFeatureProvider.Provide("Console",BetterConsole(prefix='--->')) # <-- Singleton Manner
    #GlobalFeatureProvider.Provide("Console",SimpleConsole())

    bar = Bar(GlobalFeatureProvider)
    bar.PrintYourself()

if __name__ == '__main__':
    demonstrateSystem()
