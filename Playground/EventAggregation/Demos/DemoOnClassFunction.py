__author__ = 'DJS'

from EventAggregation.Demos.ClassListenerEventAndSender import *
from EventAggregation.IEventAggregator import *

def demonstrate():
    eventAgg = EventAggregator()

    listener = ClassListener(eventAgg)

    listener.printValue()

    eventAgg.Publish(EventTopic.ValueTransfer,ValueTransferEvent(10))

    listener.printValue()

if __name__ == '__main__':
    demonstrate()