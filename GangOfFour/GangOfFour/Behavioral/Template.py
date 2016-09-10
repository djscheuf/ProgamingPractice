__author__ = 'D'
'''
Intent:
[Copied from GOF Site]

For this implementation, I will create a template for doing this and then that, and then the other thing.
I will then create two concrete subclasses. whose do this , that and the other thing will be different
The demonstration will use both, by simply calling the organized method

Reference:
http://www.aleax.it/Python/os03_template_dp.pdf -- a very good explanation imho
-- Template Method DP
    = Abstract base class has organizing method, and calls a hook method
    = concrete subclass implement hook method
    = Client code calls organizing method on concrete instance
'''

class TemplateBase:
    def Execute(self):
        self.doThis()
        self.doThat()
        self.doTheOtherThing()

class MutexAccess(TemplateBase):
    def __init__(self):
        self._Lock = False

    def doThis(self):
        print("Acquire Lock")
        self._Lock = True

    def doThat(self):
        print("Have Lock, do thing")
        #actual op here#
        print("Lock Status: %r"%self._Lock)
        print("Operation Complete")

    def doTheOtherThing(self):
        print("Release Lock")
        self._Lock = False

class DoTheDishes(TemplateBase):

    def doThis(self):
        print("Unload Dishwasher")
        print("Put away clean dishes")


    def doThat(self):
        print("Rinse Dishes in Sink")
        print("Load Dishwasher")

    def doTheOtherThing(self):
        print("Add Soap")
        print("Run Dishwasher")
        print("Walk away")

def demonstrate():
    templates = [ MutexAccess(), DoTheDishes()]

    for item in templates:
        item.Execute()
        print()

if __name__ == "__main__":
    demonstrate()
