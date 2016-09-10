__author__ = 'D'

from Behavioral.Visitor import *
import unittest
import random

class Flower(IVisitable):
    def pollinate(self,pollinator):
        print(self," pollinated by",pollinator)

    def eat(self, eater):
        print(self," was eaten by", eater)


class Chrysanthemum(Flower): pass
class Bluebonnet(Flower):pass
class BlackSalvia(Flower):pass
class TexasRose(Flower):pass

class Bug(IVisitor):pass
class Pollinator(Bug):
    def visit(self, flower):
        flower.pollinate(self)

class Predator(Bug):
    def visit(self, flower):
        flower.eat(self)

class Bee(Pollinator): pass
class Fly(Pollinator): pass
class Worm(Predator): pass

def flowerGen(n):
    flowers = Flower.__subclasses__()
    for i in range(n):
        yield random.choice(flowers)()


class Visitor_UnitTest(unittest.TestCase):

    def setUp(self):
        self.bee = Bee()
        self.fly = Fly()
        self.worm = Worm()

        self.flowerSet = flowerGen(10)

    def tearDown(self):pass

    def test_FlowersVisitableByAppropriateVisitor(self):
        for flower in self.flowerSet:
            flower.accept(self.bee)
            flower.accept(self.fly)
            flower.accept(self.worm)

if __name__ == '__main__':
    unittest.main()