__author__ = 'D'
'''
Intent: Represent an operation to be performed on the elements of an object structure.
Visitor lets you define a new operation without changing the classes of the elements on which it operates.
[Copied from GOF Site]

For this implementation I will create two interfaces, IVisitable, and IVisitor. THe IVisitable will define an
accept method, which will call the Visit method defined by the IVisitor interface.
'''
class IVisitor:
    def visit(self, caller): pass
    def __str__(self):
        return self.__class__.__name__

class IVisitable:
    def accept(self, visitor):
        return visitor.visit(self)
    def __str__(self):
        return self.__class__.__name__

class DemoVisitor(IVisitor):
    def visit(self, caller):
        print(self, " was called by:", caller)

class DemoVisitable(IVisitable): pass

def demonstrate():
    visitable = DemoVisitable()
    visitor = DemoVisitor()

    visitable.accept(visitor)
    print("Demo-ed")

if __name__ == '__main__':
    demonstrate()
