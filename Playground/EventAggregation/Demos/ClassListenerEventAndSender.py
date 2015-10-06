__author__ = 'DJS'

class ValueTransferEvent:
    def __init__(self,valueToPass):
        self.value = valueToPass

from EventAggregation.IEventAggregator import *

class ClassListener:
    def __init__(self,eventAggregator,initValue=-1):
        assert isinstance(eventAggregator,IEventAggregator)

        eventAggregator.Subscribe(EventTopic.ValueTransfer,self._eventListener)

        self.value = initValue
        self.name = "Listener"

    def _eventListener(self,event):
        assert isinstance(event,ValueTransferEvent)

        self.value = event.value
        self.printValue()

    def SetName(self,newName):
        self.name = newName

    def printValue(self):
        print(" Inside: ", self.name)
        print('Value Received: ', self.value)

class ClassSender:
    def __init__(self, eventAggregator):
        assert isinstance(eventAggregator,IEventAggregator)

        self.eventAgg = eventAggregator
        self.value = 5
        self.name = "Sender"

    def SetName(self,newName):
        self.name = newName

    def SetValue(self,newValue):
        self.value = newValue

    def SendValue(self):
        print(" Inside: ", self.name)
        self.eventAgg.Publish(EventTopic.ValueTransfer,ValueTransferEvent(self.value))
