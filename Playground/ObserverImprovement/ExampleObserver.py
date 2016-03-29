__author__ = 'DJS'
__purpose__ = "Having implemented the Observer Pattern in small I think I can improve the available example."

class ExampleObserver():
    def __init__(self,observable):
        self.str = ""
        self.str2 = ""
        observable.register(self.UpdateStr)

    def UpdateStr(self):
        print("Updating String")
        self.str = "Hello World"
        print("Update complete")

    def ChangeStr2(self):
        print("Updating String2")
        self.str2 = "The End is Nigh"
        print("Update complete2")

    def printStr(self):
        print("String: "+self.str)
        print("String2: "+self.str2)


