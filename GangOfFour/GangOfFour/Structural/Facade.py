__author__ = 'DJS'

"""
Intent: Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that
makes the subsystem easier to use. This can be used to simplify a number of complicated object interactions into a
single interface.

Generally Speaking this should be a simple implementation. The trick is in accomplishing a meaningful example.
For the moment, let us reduce this to a very simple solutions, where there is a family of objects that are
 interrelated, but used in generally a fixed manner.

"""

class A:
    def __init__(self,text):
        self.Text = text

    def GetText(self):
        return self.Text

class B:
    def __init__(self,welcome,textHolder):
        self.Welcome = welcome
        self.Text = textHolder

    def Greet(self):
        return self.Welcome + self.Text.GetText()

class C:
    def __init__(self,Password):
        self.reqPasssword = Password

    def AttemptLogin(self,attempt):
        return self.reqPasssword == attempt

class D:
    def __init__(self,username):
        self.User = username

    def LoginAs(self,user):
        return self.User == user

class Facade:
    def __init__(self,user,password,welcomeMsg):
        self.A = A(user)
        self.B = B(welcomeMsg,self.A)
        self.C = C(password)
        self.D = D(user)

    def AttemptLogin(self,user,password):
        if(self.D.LoginAs(user) and self.C.AttemptLogin(password)):
            print(self.B.Greet())
        else:
            print("Unable to log-in as: "+user+" With password: "+password)

def demonstrate():
    facade = Facade("DJS","exNihilo","Welcome to the Facade: ")

    facade.AttemptLogin("XYZ","ABC")
    facade.AttemptLogin("DJS","exNihilo")

if __name__ == "__main__":
    demonstrate()
