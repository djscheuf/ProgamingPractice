__author__ = 'DJS'

from EventAggregation.EventTopicEnum import *

class IEventAggregator:
    '''
    Interface provided for Segregation and possible alternative implementations.
    '''
    def Subscribe(self,topic,action): pass
    def Publish(self,topic,argContainer):pass
    # should have included an Unsub function

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
"""
Upon later review, I realized that there ought to be an UnSub function, or some
other way to remove the references kept in this class. Otherwise it is possible
that this link will result in an object not being Garbage-collected properly.

I realized this possibility after seeing similar problems in [redacted].
However, it is possible that Python does not encounter such problems, and as a
result does not need such a fix. More research is required.
"""
