__author__ = 'D'
'''
Intent: Define an object that encapsulates how a set of objects interact.
    Mediator promotes loose coupling by keeping objects from referring to each
    other explicitly, and it lets you vary their interaction independently.
[Copied from GOF Site]

For this implementation, I will create a series of classes whose state changes based
    on another objects change. These changes will be handled by the mediator.

Reference:
http://entitycrisis.blogspot.com/2007/07/mediator-pattern-in-python.html
'''

class Mediator:
    def __init__(self):
        self._hanlderGroups = {}
        
    def signal(self,signal_name,*args,**kw):
        print("Message:"+signal_name)
        for handler in self._hanlderGroups.get(signal_name,[]):
            handler(*args,**kw)
            
    def connect(self,signal_name,receiver):
        handlers = self._hanlderGroups.setdefault(signal_name,[])
        handlers.append(receiver)

    def disconnect(self,signal_name,receiver):
        self._hanlderGroups[signal_name].remove(receiver)

    '''Note: This is very similar to the event aggregator
        However in this case the 'events' are merely signals tied or untied at a higher level than
        the one receiving the signals will know, although this could be used in a PubSub fashion.'''

class Lockable:
    def __init__(self):
        self._Locked = False

    def IsLocked(self):
        return self._Locked

    def Lock(self):
        self._Locked = True

    def Unlock(self):
        self._Locked = False

class LockableTextBox(Lockable):
    def __init__(self):
        Lockable.__init__(self)
        self._text = ""

    def SetText(self,text):
        if not self.IsLocked():
            self._text = text
            return True
        return False

    def GetText(self):
        temp = '[Locked]' if self.IsLocked() else '[Unlocked]'
        temp +=self._text
        return temp

class LockingToggle():
    def __init__(self,mediator):
        self._Locked = False
        self._mediator = mediator

    def IsLocked(self):
        return self._Locked

    def Lock(self):
        self._Locked = True
        self._mediator.signal("UI_Locking")

    def Unlock(self):
        self._Locked = False
        self._mediator.signal("UI_Unlocking")


def demonstrate():
    theMediator = Mediator()
    theToggle = LockingToggle(theMediator)
    theTextBox = LockableTextBox()

    theMediator.connect("UI_Locking",theTextBox.Lock)
    theMediator.connect("UI_Unlocking",theTextBox.Unlock)

    print("Initial setup Complete")
    print("Toggle State: %r"%theToggle.IsLocked())
    print("The TextBox Lock State: %r"%theTextBox.IsLocked())

    print("\nSetting Text: things")
    flag = theTextBox.SetText("things")
    if flag:
        print("Operation Successful")
    else:
        print("Operation Failed!!!")
    print("Text: "+theTextBox.GetText())

    print("\nLocking\n")
    theToggle.Lock()
    print("\tshould have seen Mediators message received")
    print("Text Box Lock should be on: %r"%theTextBox.IsLocked())

    print("\nSetting Text: stuff")
    flag = theTextBox.SetText("stuff")
    if flag:
        print("Operation Successful")
    else:
        print("Operation Failed!!!")
    print("Text: "+theTextBox.GetText())

if __name__ == "__main__":
    demonstrate()