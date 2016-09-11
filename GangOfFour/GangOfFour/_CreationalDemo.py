
from .Creational import *

class CreationalDemo():
    def demonstrate(self):
        self._prettyFormatPrintEncasing("AbstractFactory Pattern",AbstractFactory.demonstrate)
        self._prettyFormatPrintEncasing("Builder Pattern",Builder.demonstrate)
        self._prettyFormatPrintEncasing("FactoryMethod Pattern",FactoryMethod.demonstrate)
        self._prettyFormatPrintEncasing("Prototype Pattern",Prototype.demonstrate)
        self._prettyFormatPrintEncasing("Singleton Pattern",Singleton.demonstrate)

    def _prettyFormatPrintEncasing(self,name, func):
        print("***Starting {0}...***\n".format(name))
        func()
        print("\n***Completed {0}...***\n".format(name))

if __name__ == "__main__":
    cd = CreationalDemo()
    cd.demonstrate()
