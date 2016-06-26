"""
Purpose: The PlayerStrategy represnets, the desired final state of Owned CardEnum.

"""
from .CardEnum import CardEnum

class PlayerStrategy():
    def __init__(self,desiredEndState=None):
        self.EndState = self._defaultEndState()

        if(desiredEndState != None):
            for key in desiredEndState.keys():
                self.EndState[key] = desiredEndState[key]

    def _defaultEndState(self):
        return {CardEnum.WheatField:1,CardEnum.Bakery:1,CardEnum.TrainStation:1,CardEnum.ShoppingMall:1,CardEnum.AmusementPark:1,CardEnum.RadioTower:1}


class PlayerStategyFactory():
    def __inint__(self):
        pass
        
    def CheeseFactoryStrategy(self):
        endState = {CardEnum.Ranch:3,CardEnum.CheeseFactory:3}
        return PlayerStrategy(endState)

    def FurnitureFactoryStrategy(self):
        endState = {CardEnum.Forest:3,CardEnum.FurnitureFactory:3}
        return PlayerStrategy(endState)

    def MyStrategy(self):
        endState = {CardEnum.Ranch:2, CardEnum.Bakery:2, CardEnum.FamilyRestaurant:2,CardEnum.CheeseFactory:2,CardEnum.Forest:2,CardEnum.FurnitureFactory:2}
        return PlayerStrategy(endState)

StratFactory = PlayerStategyFactory()
