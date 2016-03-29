__author__ = 'DJS'
"""
Intent: Provide an object which traverses some aggregate structure, abstracting away assumptions about the
implementation of that structure.

Obviously python has some native support for this, through the __iter__ function, as well as shown with the for x in y syntax.
"""

class notLinearData():
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __iter__(self):
        return IterableData(self.a,self.b,self.c)

    def PrintContent(self):
        print("Not Linear stuff: ")
        print(self.a)
        print(self.c)
        print(self.b)

class IterableData():
    def __init__(self,a,b,c):
        self.i = 0
        self.data = [c,b,a]

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.data):
            self.i += 1
            return self.data[self.i-1]
        else:
            raise StopIteration()

def demonstrate():
    noneLin = notLinearData(1 ,"Two", {"3": 3})
    noneLin.PrintContent()

    iterator = iter(noneLin)

    print("\nNow with the iterator: ")
    for item in iterator:
        print(item)

if __name__ == "__main__":
    demonstrate()