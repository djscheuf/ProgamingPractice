__author__ = 'DJS'

class FearEvent:
    def __init__(self,phrase):
        self.phrase = phrase

def FearListener(event):
    assert isinstance(event,FearEvent)

    print("Fear Listener")
    print("\tFear > ",event.phrase)

def AltFearListener(event):
    assert isinstance(event,FearEvent)

    print("Duke Atreides Fear Listener")
    print("""\tI must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration.
    I will face my fear. I will permit it to pass over me and through me.
    And when it has gone past I will turn the inner eye to see its path.
    Where the fear has gone there will be nothing. Only I will remain.""",
    "\n\t\tEven Fear of ",event.phrase)

class PanicEvent:
    def __init__(self,cause):
        self.cause = cause

def PanicListener(event):
    assert isinstance(event,PanicEvent)

    print("Panicking because: ",event.cause)

from EventAggregation.IEventAggregator import *
from EventAggregation.EventTopicEnum import *
def demonstrate():
    eventAgg = EventAggregator()

    print("Publish to Fear")
    eventAgg.Publish(EventTopic.Fear,FearEvent("Reason"))
    print("Nothing Happens\n")

    print("Subscribe to Fear")
    eventAgg.Subscribe(EventTopic.Fear,FearListener)

    print("Publish to Fear")
    eventAgg.Publish(EventTopic.Fear,FearEvent("Reason"))

    print("\nAfter Fear Event Raised\n")

    print("Add New Listener")
    eventAgg.Subscribe(EventTopic.Fear,AltFearListener)

    print("Publish to Fear")
    eventAgg.Publish(EventTopic.Fear,FearEvent("Reason"))

    print("\nAfter Multi-listener\n")

    print("Subscribe to Panic")
    eventAgg.Subscribe(EventTopic.Panic,PanicListener)

    print("Publish to Panic, and see no Fear")
    eventAgg.Publish(EventTopic.Panic,PanicEvent("Just Because..."))

    print("\n After Panic\n")

if __name__ == '__main__':
    demonstrate()
