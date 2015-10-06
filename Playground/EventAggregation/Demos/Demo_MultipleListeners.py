__author__ = 'DJS'

from EventAggregation.Demos.ClassListenerEventAndSender import *
from EventAggregation.IEventAggregator import *

def demonstrate():
    eventAgg = EventAggregator()

    firstListener = ClassListener(eventAgg)
    firstListener.SetName("First")

    anotherListener = ClassListener(eventAgg,3)
    anotherListener.SetName("Another")

    sender = ClassSender(eventAgg)

    print("Before Events")
    firstListener.printValue()
    anotherListener.printValue()

    print("Send Event")
    sender.SendValue()

    print("After Event")
    firstListener.printValue()
    anotherListener.printValue()

if __name__ == '__main__':
    demonstrate()