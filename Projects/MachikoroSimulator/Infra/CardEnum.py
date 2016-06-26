"""
Purpose: The CardEnum represents the available cards for player strategies, and the Deck Manager.
"""

from enum import IntEnum

class CardEnum(IntEnum):
    Undefined = -1
    WheatField = 0
    Ranch = 2
    Bakery = 3
    Cafe = 4
    ConvenienceStore = 5
    Forest = 6
    TVStation = 7 # Not presently supported
    Stadium = 8 # Not presently supported
    BusinesCenter = 9 # Not presently supported
    CheeseFactory = 10
    FurnitureFactory = 11
    Mine = 12
    FamilyRestaurant = 13
    AppleOrchard = 14
    FruitAndVegetableStand = 15

    TrainStation=91
    ShoppingMall=92
    AmusementPark=93
    RadioTower=94
