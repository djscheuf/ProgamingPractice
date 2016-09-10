__author__ = 'D'

'''
Intent: Without violating encapsulation, capture and externalize an object's internal state so that the object
can be restored to this state later.
[Copied from GOF site]

In python the most common usage is the Memento closure, allowing a roll back of a transactional behavior.
to that end I will be implementing a Memento class, a Transaction and a Transactional classes to support some
'roll-back-able' actions in a testing class.
'''

import copy

def Memento(obj, deep=False):
    state = (copy.copy, copy.deepcopy)[bool(deep)](obj.__dict__)
        # essentially a python binary statement ()?x:y, but with methods
    def Restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)
    return Restore

class Transaction:
    '''
    Transactional Gard. (Really just syntactic sugar around memento closure.
    '''
    deep = False
    def __init__(self, *targets):
        self.targets = targets
        self.Commit()

    def Commit(self):
        self.states = [Memento(target,self.deep) for target in self.targets]
        # that is self.states = array of Mementos for each target in targets

    def Rollback(self):
        for state in self.states:
            state() # restores the state using the Memento call

class transactional(object):
    '''
    Method decorator to add transactional behavior to a method
    '''

    def __init__(self, method):
        self.method = method

    def __get__(self, obj, T):
        def transaction(*args,**kwargs):
            state = Memento(obj)
            try:
                return self.method(obj,*args,**kwargs)
            except:
                state()
                raise
        return transaction


'''
Entering Demonstration Code
'''

class NumObj(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<%s:%r>' %(self.__class__.__name__,self.value)

    def Increment(self):
        self.value += 1

    @transactional
    def DoStuff(self):
        self.value = '1111' # <- invalid value for Increment
        self.Increment() # <- will fail and roll back

def TransactionDemo(n):
    t = Transaction(n)
    print("-- begin transaction 1")
    try:
        for i in range(3):
            n.Increment()
            print("Change: ",n)
        t.Commit()
        print("-- committed")

        print("-- begin transaction 2")
        for i in range(3):
            n.Increment()
            print("Change: ",n)

        n.Value += 'x'  # invalid value
        print("Change: ",n)

    except:
        t.Rollback()
        print('-- rolled back')

    print("Final:",n)
    return n

def TransactionalDemo(n):
    print('-- now doing stuff ...')

    try:
        n.DoStuff()
    except:
        print("-- doing stuff failed...")
        import traceback
        traceback.print_exc(0)
        pass

    print(n)

def demonstrate():
    n = NumObj(-1)
    print(n)

    n = TransactionDemo(n)

    TransactionalDemo(n)

if __name__ == '__main__':
    demonstrate()