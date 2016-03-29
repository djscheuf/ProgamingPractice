__author__ = 'DJS'
_purpose__ =""" Serve as Hard-coded list of port numbers to be used by a given instance of a service.
                Assume 1 service per type. """

from Infrastructure.ServiceTypeEnum import *


class PortNumberGenerator():
    basePort=5001
    numSet = {
        {ServiceType.Directory,basePort},
        {ServiceType.Database,basePort+1},
        {ServiceType.Security,basePort+2},
        {ServiceType.UserInterface,basePort+3},
        {ServiceType.Undefined,-1}
              }

    def GetPort(self,type):
        return numSet[type]
