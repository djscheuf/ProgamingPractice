__author__ = 'DJS'

'''
A collection of common assertions on Feature Modules/Instances
'''

def NoAssertion(obj): return True

def IsInstanceOf(*classes):
   def test(obj): return isinstance(obj, classes)
   return test

def HasAttributes(*attr):
    def test(obj):
        for each in attr:
            if not hasattr(obj,each):return False
        return True
    return test

def HasMethods(*methods):
    def test(obj):
        for each in methods:
            try:
                attr = getattr(obj,each)
            except AttributeError:
                return False
            if not callable(attr): return False
        return True
    return test

if __name__ == '__main__':
    print("Sector: Feature Assertions")