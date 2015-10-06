__author__ = 'DJS'

from EventAggregation.EventTopicEnum import *

class IEventAggregator:
    '''
    Interface provided for Segregation and possible alternative implementations.
    '''
    def Subscribe(self,topic,action): pass
    def Publish(self,topic,argContainer):pass

from collections import defaultdict
class EventAggregator(IEventAggregator):
    def __init__(self):
        self.Listeners = defaultdict(list) # should be a topic : List{OfListeners} dictionary

    def Subscribe(self,topic,action):
        assert isinstance(topic,EventTopic) # minor event type protection
        assert callable(action)

        self.Listeners[topic].append(action)


    def Publish(self,topic,argContainer):
        assert isinstance(topic,EventTopic) # minor event type protection

        if topic in self.Listeners.keys():
            for each in self.Listeners[topic]:
                argCopy = argContainer # prevents listeners from modifying each other
                each(argCopy) # might consider threading these...

        # should not act if no listeners.