from .Structural import *

class StructuresDemo():
    def demonstrate(self):
        self._prettyFormatPrintEncasing("Adapter Pattern",Adapter.demonstrate)
        self._prettyFormatPrintEncasing("Bridge Pattern",Bridge.demonstrate)
        self._prettyFormatPrintEncasing("Composite Pattern",Composite.demonstrate)
        self._prettyFormatPrintEncasing("Decorator Pattern",Decorator.demonstrate)
        self._prettyFormatPrintEncasing("Facade Pattern",Facade.demonstrate)
        self._prettyFormatPrintEncasing("Flyweight Pattern",Flyweight.demonstrate)
        self._prettyFormatPrintEncasing("Proxy Pattern",Proxy.demonstrate)

    def _prettyFormatPrintEncasing(self,name, func):
        print("***Starting {0}...***\n".format(name))
        func()
        print("\n***Completed {0}...***\n".format(name))

if __name__ == "__main__":
    sd = StructuresDemo()
    sd.demonstrate()
