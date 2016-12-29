from copy import deepcopy
from ..CardEnum import CardEnum

RequiredImprovements = [CardEnum.TrainStation, CardEnum.ShoppingMall, CardEnum.AmusementPark, CardEnum.RadioTower]

Blues = {CardEnum.AppleOrchard, CardEnum.Forest,
         CardEnum.Mine, CardEnum.WheatField,
         CardEnum.Ranch}

Greens = {CardEnum.Bakery, CardEnum.ConvenienceStore,
          CardEnum.CheeseFactory, CardEnum.FurnitureFactory,
          CardEnum.FruitAndVegetableStand}

Factories = {CardEnum.CheeseFactory, CardEnum.FurnitureFactory,
             CardEnum.FruitAndVegetableStand}

Reds = {CardEnum.Cafe, CardEnum.FamilyRestaurant}

Activations = {1: [CardEnum.WheatField], 2: [CardEnum.Ranch, CardEnum.Bakery], 3: [CardEnum.Cafe],
               4: [CardEnum.ConvenienceStore], 5: [CardEnum.Forest], 6: [],
               7: [CardEnum.CheeseFactory], 8: [CardEnum.FurnitureFactory], 9: [CardEnum.Mine],
               10: [CardEnum.AppleOrchard, CardEnum.FamilyRestaurant], 11: [CardEnum.FruitAndVegetableStand], 12: [CardEnum.FruitAndVegetableStand]}

SimpleValues = {CardEnum.WheatField: 1, CardEnum.Bakery: 1,
                CardEnum.Ranch: 1, CardEnum.ConvenienceStore: 3,
                CardEnum.Forest: 1, CardEnum.Mine: 5,
                CardEnum.AppleOrchard: 3}

FactoryMultiplierCards = {CardEnum.CheeseFactory: [CardEnum.Ranch],
                          CardEnum.FurnitureFactory: [CardEnum.Forest, CardEnum.Mine],
                          CardEnum.FruitAndVegetableStand: [CardEnum.WheatField, CardEnum.AppleOrchard]
                          }

class Engine:
    def __init__(self, initialPlayerState, deck):
        self._initPlayerState = initialPlayerState

        self._initialDeck = deepcopy(deck)
        self._currentDeck = deck

    def Reset(self):
        self._currentDeck = deepcopy(self._initialDeck)

    def WinConditionMet(self, players):
        """Evaluates all player states for one matching the win condition"""
        for player in players:
            state = player.CurrentState
            if all(k in state for k in RequiredImprovements):
                return True

        return False

    def GetWinner(self, players):
        """Returns first player who matches the win condition or None"""
        for player in players:
            state = player.CurrentState
            if all(k in state for k in RequiredImprovements):
                return player

        return None

    def EarnsMoney(self, state, roll, playersTurn):
        """Returns the amount earned by player, depending on whether it is their turn or not."""
        result = 0

        if playersTurn:
            result += self._EarnedWithGreens(state, roll)

        result += self._EarnedWithBlues(state, roll)

        return result

    def _EarnedWithGreens(self, state, roll):
        """Returns value earned by green cards"""
        # Technically this is a special case, but I might be able to re-use some of the logic for red and blue...
        #   just need to figure out the factories part.
        result = 0
        activated = Activations[roll]
        for card in activated:
            if card in Greens:
                if card not in Factories:
                    result += self._SimpleValueCalculation(state, card)
                else:
                    result += self._FactoryValueCalculation(state, card)
        return result

    def _SimpleValueCalculation(self, state, card):
        """Returns value earned from simple value cards"""
        multiplier = SimpleValues[card]
        count = state[card]
        return multiplier*count

    def _FactoryValueCalculations(self, state, factoryCard):
        """Returns value earned from Factorys and their multipliers"""
        multiplier = 0
        for card in FactoryMultiplierCards[factoryCard]:
            multiplier += state[card]

        count = state[factoryCard]
        return multiplier*count

    def _EarnsWithBlues(self, state, roll):
        """Returns value earned by blue cards"""
        # I recognize that this is technically a repeat of the reds, but with a different filter. May try to extract later.
        result = 0
        activated = Activations[roll]
        for card in activated:
            if card in Blues:
                result += self._SimpleValueCalculation(state, card)

        return result

    def StealsMoney(self, state, roll):
        """Returns money the player steals, since it is not their turn"""
        return self._EarnedWithReds(state, roll)

    def _EarnsWithReds(self, state, roll):
        """Returns value pseudo-earned by red cards"""
        # I recognize that this is technically a repeat of the blues, but with a different filter. May try to extract later.
        result = 0
        activated = Activations[roll]
        for card in activated:
            if card in Reds:
                result += self._SimpleValueCalculation(state, card)

        return result
