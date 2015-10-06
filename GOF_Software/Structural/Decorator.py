__author__ = 'D'
'''
Intent: Attach additional responsibilities to an object dynamically.
Decorators provide a flexible alternative to subclassing for extending functionality.
[Copied from GOF site]

While I have already used this pattern in the Singleton realization, I shall try to use this pattern to realize
something separate. for this instance I will show a possible implementation of a critical section, using the method
decorator.
'''

#Note: The Critical Section is really just a dummy here. If you really wanted a critical section, you'd need
# someway to either lock all critical section, or have the critical sections keyed, and on different threads.
# Meaning the Decorator would need a static set of keys, locks.

class CriticalSectionDecorator:
    def __init__(self,decorated):
        self._decorated = decorated

    def __call__(self, *args, **kwargs):
        self._LockCriticalSection()
        self._decorated(*args)
        self._UnlockCriticalSection()

    def _LockCriticalSection(self):
        print("Locking Critical Section...")

    def _UnlockCriticalSection(self):
        print("Unlocking Critical Section...\n")

@CriticalSectionDecorator
def demoFoo(n):
    print("\tInside FOO with n =", n)

@CriticalSectionDecorator
def demoAltFoo(phrase):
    print("\tInside Alt Foo, with phrase: \"", phrase, "\"")

def demonstrate():
    demoFoo(5)
    demoAltFoo("Bar")
    demoFoo(3)

if __name__ == '__main__':
    demonstrate()