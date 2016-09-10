__author__ = 'DJS'
"""
Intent: Allow classes to defer object creation to a separately defined method.

It appears to be used to generate subtypes of a given class based on parameters given to the constructor. It occurs to
me that this factory method can also be used for other purposes, such as tracking of instances, or passing other
more consistently passed information, that could be initialized once, but used many times. However that makes it seem
more like an Abstract Factory that simply a factory method.
"""

class Fish:
    color = None
    count = 0

    @staticmethod
    def ConstructFish(fishColor ):
        if(fishColor == "red"):
            Fish.count+=1
            return RedFish(Fish.count)
        elif(fishColor == "blue"):
            Fish.count+=1
            return BlueFish(Fish.count)
        else:
            return None

class RedFish(Fish):
    color = "Red"
    def __init__(self,number):
        self.number = number


class BlueFish(Fish):
    color = "Blue"

    def __init__(self,number):
        self.number = number


def demonstrate():
    #1 Fish, 2 Fish
    redFish = Fish.ConstructFish("red")
    blueFish = Fish.ConstructFish("blue")

    print("Total Fish count: %s"%(Fish.count))
    print("%s(%s):#%s"%(redFish.color, redFish.__class__.__name__,redFish.number))
    print("%s(%s):#%s"%(blueFish.color, blueFish.__class__.__name__,blueFish.number))

if __name__ == "__main__":
    demonstrate()