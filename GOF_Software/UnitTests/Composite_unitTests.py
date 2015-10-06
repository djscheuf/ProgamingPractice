__author__ = 'D'

from Structural.Composite import *
import unittest

class Adapter_UnitTest(unittest.TestCase):
    _DefaultLeaf = Leaf("Default Leaf")
    _DefaultTree = Tree("Default Tree")

    def setUp(self):
        self.componentList = []
        self._DefaultLeaf = Leaf("Default Leaf")
        self._DefaultTree = Tree("Default Tree")

    def _populateComponentList(self):
        self.componentList.append(self._DefaultLeaf)
        self.componentList.append(self._DefaultTree)

    def tearDown(self): pass

    def test_BothTreeAndLeafCanDisplayOnIteration(self):
        print("\nSame Interface Test:")
        #B
        self._populateComponentList()
        # O-C
        for comp in self.componentList:
            comp.display()

    def test_TreeWithLeavesStillIterableWithComponent(self):
        print("\nTree Iterates through Leaves on Action Test:")
        #B
        self._DefaultTree.append(Leaf("New Leaf"))
        self._DefaultTree.append(Leaf("Experiemental Leaf"))
        self._populateComponentList()
        # O-C
        for comp in self.componentList:
            comp.display()

if __name__ == '__main__':
    unittest.main()