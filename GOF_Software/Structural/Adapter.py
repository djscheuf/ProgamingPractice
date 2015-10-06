__author__ = 'D'
'''
Adapter Pattern:
Intent: Convert the interface of some class b into an interface a that some client class c understands.
The AdapterPattern lets classes with incompatible interfaces work together. This is sometimes called a wrapper
because an adapter class wraps the implementation of another class in the desired interface. This pattern makes
heavy use of delegation where the delegator is the adapter (or wrapper) and the delegate is the class being adapted.
[copied from GOF site]

For this implementation we will be following the example on the GOF site page for the Adapter pattern.
That is we will be adapting python list into a stack for our uses. This could be used as a
'''

#List already exists as a python data type.
#technically so does stack... but oh well.

class MyStack():
    def __init__(self):
        self._count = 0
        self._storage = []

    def push(self, input,verbose=False):
        if(verbose):
            print("Got: "+str(input))
            print("AddingItem")
            print("IncreasingSize")
        #checks on input here
        self._storage.append(input)
        self._count+=1

    def pop(self,verbose=False):
        removed = None
        empty = self.isEmpty()
        if( not empty ):
            removed = self._storage[self._count-1]

        if(verbose):
            print("Check if Empty")
            print("Remove Last Item")
            print("DecreaseCount")
            if(not empty):
                print("Return: "+str(removed))
            else:
                print("Nothing to return")

        if( not empty ):
            self._storage.pop()
            self._count-=1
            return removed
        else:
            return None

    def size(self):
        return self._count

    def isEmpty(self):
        return self._count == 0

    def clear(self):
        self._count = 0
        self._storage.clear()

def demonstrate():
    stack = MyStack()

    #Stack starts empty
    assert stack.isEmpty()

    #Add Item to stack and get it back
    input1 = "Item1"
    stack.push(input1,True)
    response = stack.pop(True)
    assert response == input1

    #clear stack empties stack and becomes empty
    stack.push(input1,True)
    stack.clear()
    assert stack.size() == 0
    assert stack.isEmpty()

    #pop when empty returns nothing
    response = stack.pop(True)
    assert response == None

    #adding two items to stack
    input2 = "Item2"
    stack.push(input1,True)
    stack.push(input2,True)
    assert stack.size() == 2

    #items coming off stack come in reverse order
    response1 = stack.pop()
    response2 = stack.pop()
    assert response1 == input2
    assert response2 == input1

if __name__ == '__main__':
    demonstrate()

