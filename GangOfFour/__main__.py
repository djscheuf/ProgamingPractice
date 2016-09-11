"""
Author: DJS
Date:  10SEP2016
Purpose:
    This file allows GangOfFour to be an executable directory. And will enclose
    calls to the various Demonstration codes.
"""

#TODO: Implement calls to Demo code
from GangOfFour._StructuralDemo import StructuresDemo
from GangOfFour._CreationalDemo import CreationalDemo
from GangOfFour._BehavioralDemo import BehavioralDemo

def PrettyFormatPrint(name,func):
    print(">>Starting {0}...\n".format(name))
    func()
    print(">>Completed {0}...\n".format(name))

if __name__ == "__main__":
    bd = BehavioralDemo()
    PrettyFormatPrint("Behavioral Demo",bd.demonstrate)

    cd = CreationalDemo()
    PrettyFormatPrint("Creational Demo",cd.demonstrate)

    sd = StructuresDemo()
    PrettyFormatPrint("Structural Demo",sd.demonstrate)
