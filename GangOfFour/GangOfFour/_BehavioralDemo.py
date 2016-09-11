from .Behavioral import *

class BehavioralDemo():
    def demonstrate(self):
        self._prettyFormatPrintEncasing("Chain of Responsibility Pattern",ChainOfResponsibility.demonstrate)
        self._prettyFormatPrintEncasing("Command Pattern",Command.demonstrate)
        self._prettyFormatPrintEncasing("Interpreter Pattern",Interpreter.demonstrate)
        self._prettyFormatPrintEncasing("Iterator Pattern",Iterator.demonstrate)
        self._prettyFormatPrintEncasing("Mediator Pattern",Mediator.demonstrate)
        self._prettyFormatPrintEncasing("Memento Pattern",Memento.demonstrate)
        self._prettyFormatPrintEncasing("Observer Pattern",Observer.demonstrate)
        self._prettyFormatPrintEncasing("Strategy Pattern",Strategy.demonstrate)
        self._prettyFormatPrintEncasing("Template Pattern",Template.demonstrate)
        self._prettyFormatPrintEncasing("Visitor Pattern",Visitor.demonstrate)

    def _prettyFormatPrintEncasing(self,name, func):
        print("***Starting {0}...***\n".format(name))
        func()
        print("\n***Completed {0}...***\n".format(name))

if __name__ == "__main__":
    bd = BehavioralDemo()
    bd.demonstrate()
