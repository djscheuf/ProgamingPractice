__author__ = 'DJS'
"""
Intent: Provide a surrogate or placeholder for another object to control access to it.

Truthfully speaking there are a few varieties of proxy, they include: LazyInstanciation, Remote,Protection, and 'Smart'
proxies. Lazy Instance hides object creation, Remote generally hides communication protocols, Protections provides data protection.
A Smart proxy might be used to improve an existing class. E.g. Class provides non-threadsafe functionality. So instead of re-writing the class,
a Smart proxy could be written to encapsulate the class and implement the necessary threadsafety requirements.
"""

class ExampleProxy():
    def __init__(self,subject):
        self._subject = subject

    def __getattr__(self,name):
        return getattr(self._subject,name)

class RGB():
    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue

    def Red(self):
        return self._red

    def Green(self):
        return self._green

    def Blue(self):
        return self._blue

class NoBlueProxy(ExampleProxy):
    def Blue(self):
        return 0


class SecurityProxy():
    def __init__(self,subject):
        self._subject = subject
        self._Username = ""

    def Login(self,UN):
        self._Username = UN

    def __getattr__(self, item):
        if self._Username is not "":
            if(self._Username == "DJS"):
                return getattr(self._subject,item)
            else:
                print("Access Denied: Lacking Permission")
        else:
            print("Access Denied:No User Logged In")

        return lambda: None # returns callable that does nothing...

def demonstrate():
    rgb = RGB(100,192,240)
    print(rgb.Red())

    proxy = ExampleProxy(rgb)
    print(proxy.Green())

    noBlue = NoBlueProxy(rgb)
    print(noBlue.Green())
    print(noBlue.Blue())

    secure = SecurityProxy(rgb)
    secure.Red()

    secure.Login("BJT")
    secure.Blue()

    secure.Login("DJS")
    val = secure.Green()
    print(val)

if __name__ == "__main__":
    demonstrate()
