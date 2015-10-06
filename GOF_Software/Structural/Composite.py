__author__ = 'D'
'''
Intent: Compose objects into tree structures that represent whole-part hierarchies.
Composite lets clients treat individual objects and compositions of objects uniformly.
A leaf has the same interface as a node.
[copied from GOF site]

For this implementation, It would appear wisest to implement a tree structure, which houses a common interface for use.
As such the base item will be called a 'component' with subclasses of a Leaf and a tree. The Tree will include the
ability to append Leaves. Finally, the components may be iterated through to "display"
'''

class Component(object):

    def __init__(self, phrase):
        self.Phrase = phrase

    def __str__(self):
        return self.__class__.__name__+self.Phrase

    def display(self):
        print(self, "is Displayed.");

class Leaf(Component):pass

class Tree(Component):

    def __init__(self, phrase):
        self.Phrase = phrase
        self.LeafList = []

    def append(self,component):
        isinstance(component, Component)
        self.LeafList.append(component)

    def display(self):
        print(self,"Is Displayed with: ")
        for leaf in self.LeafList:
            leaf.display()

def demonstrate():
    leaf = Leaf("First Leaf")
    leaf02 = Leaf("Second Leaf")

    tree = Tree("First Tree")
    tree.append(leaf02)
    tree.append(Leaf("New Leaf"))

    components = []
    components.append(leaf)
    components.append(tree)

    for comp in components:
        comp.display()

if __name__ == '__main__':
    demonstrate()
