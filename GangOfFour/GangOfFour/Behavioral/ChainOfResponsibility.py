__author__ = 'D'
'''
Intent: Avoid coupling the sender of a request to its receiver by giving more than one object a
chance to handle the request. Chain the receiving objects and pass the request along the chain until an object
handles it. There is a potentially variable number of "handler" objects and a stream of requests that must be
handled. Need to efficiently process the requests without hard-wiring handler relationships and precedence,
or request-to-handler mappings.

For this implementation I will be following the example from wikipedia, which appears the most sensible.
Oddly it is also a good example of dependency injection.
'''

class Car:
    '''
    Object to be Handled
    '''
    def __init__(self):
        self.name = None
        self.km = 11100
        self.fuel = 5
        self.oil = 5

'''
Handler functions
'''
def handle_fuel(car):
    if car.fuel <10:
        print("Adding fuel...")
        car.fuel = 100

def handle_km(car):
    if car.km > 10000:
        print("made a car test")
        car.km = 0

def handle_oil(car):
    if car.oil < 10:
        print("added oil")
        car.oil = 100

'''
Chain of responsibility Manager
'''
class Garage:
    def __init__(self):
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def handle_car(self, car):
        for handler in self.handlers:
            handler(car)

def demonstrate():
    handlers = [handle_fuel, handle_km] #,handle_oil]
    garage = Garage()

    for handle in handlers:
       garage.add_handler(handle)

    garage.handle_car(Car())

if __name__ == '__main__':
    demonstrate()
