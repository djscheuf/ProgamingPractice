__author__ = 'DJS'

import SimplePackage

def demonstrate():
    print("Demo for Import Simple Package")

    SimplePackage.a.bar()
    SimplePackage.b.foo()


if __name__ == '__main__':
    demonstrate()