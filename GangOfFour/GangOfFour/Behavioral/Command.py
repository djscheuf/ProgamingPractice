__author__ = 'D'
'''
Intent: Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.
[Copied from GOF Site]

For this implementation, I will observe the simplest implementation through Python. However the following link also
indicates alternative and in a sense better use cases for Commands. Specifically when one wishes to be able to undo them
'''

def greet(who):
    print("Hello %s!" % who)

greetWorldCommand = lambda: greet("World")
greetUserCommand = lambda: greet("User")

def demonstrate():
    greetWorldCommand()
    greetUserCommand()

if __name__ == '__main__':
    demonstrate()

'''
Notes from  Link:
    http://stackoverflow.com/questions/1494442/general-command-pattern-and-command-dispatch-pattern-in-python
The command pattern as an object oriented design pattern makes more sense if your commands need to be able to do
 more than just be invoked. Common usecase is when you need to be able to undo/redo your actions. Then a command class
 is a good way to couple the forward and backwards actions together. For example:

---
class MoveFileCommand(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        os.rename(self.src, self.dest)
    def undo(self):
        os.rename(self.dest, self.src)

undo_stack = []
undo_stack.append(MoveFileCommand('foo.txt', 'bar.txt'))
undo_stack.append(MoveFileCommand('bar.txt', 'baz.txt'))
# foo.txt is now renamed to baz.txt
undo_stack.pop().undo() # Now it's bar.txt
undo_stack.pop().undo() # and back to foo.txt
---
'''