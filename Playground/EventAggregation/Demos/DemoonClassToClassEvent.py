__author__ = 'DJS'


from EventAggregation.Demos.ClassListenerEventAndSender import *
from EventAggregation.IEventAggregator import *

def demonstrate():
    eventAgg = EventAggregator()

    listener = ClassListener(eventAgg)
    sender = ClassSender(eventAgg)

    print("Before Events")
    listener.printValue()

    print("Send Event")
    sender.SendValue()

    print("After Event")
    listener.printValue()

if __name__ == '__main__':
    demonstrate()