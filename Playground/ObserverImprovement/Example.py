__author__ = 'DJS'
_purpose__ = "Demonstrate Alternative Observer/Observable Behavior"
_Comments__ = """
Upon later review, this activity is fundamentally flawed, as it requires the
observale and the observer to be present in a single context. Worse still,
The observable basically must know about all observers.

finally, it has become apparent that this is simply trying to acheive what
has already been accomplished by the Event Aggregator system in other examples.
THe same desired effect ( notification and action upon a particular occurence of
something.) has been acheived, but with the additional anonimity ( via Pub/Sub behavior).

This system acheived the goal by introducing a series of intermediaries,
in the form of various event types, and the Event Aggregator, which acts
as a store of the associations between types and actions. 
"""

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
