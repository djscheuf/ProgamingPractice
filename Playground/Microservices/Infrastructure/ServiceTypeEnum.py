__author__ = 'DJS'
__purpose__ =""" Serve as codified list of Service Types for DirectoryService requests. """

from enum import IntEnum

class ServiceType(IntEnum):
    Directory=0
    Database=1
    Security=2
    UserInterface=3
    Undefined=-1
