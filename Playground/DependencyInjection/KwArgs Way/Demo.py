__author__ = 'DJS'

from FeatureNamesEnum import *
from ComponentClasses import *

def demonstrate():
    features = {}
    #features["console"] = SimpleConsole()
    features[GlobalFeatureNames.Console] = BetterConsole(prefix='--->')
    features[GlobalFeatureNames.AppTitle] = "I'm sorry, Dave. I can't do that."
    #features["title"] = "Inversion of Control ...\n\n ... The Python Way"
    features[GlobalFeatureNames.CurrentUser] = GetCurrentUser()

    bar = Bar(**features)

    bar.PrintYourself()

if __name__ == '__main__':
    demonstrate()
