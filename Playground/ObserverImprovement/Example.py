__author__ = 'DJS'
_purpose__ = "Demonstrate Alternative Observer/Observable Behavior"

from ExampleObservable import *

from ExampleObserver import *

def execute():
    observable1 = ExampleObservable()
    observable2 = ExampleObservable()

    observer = ExampleObserver(observable1)
    observable2.register(observer.ChangeStr2)

    observer.printStr()

    observable1.update_observers()

    observer.printStr()

    observable2.update_observers()

    observer.printStr()

if __name__ == "__main__":
    execute()