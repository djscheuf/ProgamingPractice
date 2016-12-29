from .Game import Game


class PlayerContext():
    maxPlayers = 4

    def __init__(self, firstPlayer, secondPlayer):
        self._players = []
        self._player.add(firstPlayer)
        self._players.add(secondPlayer)
        self._count = 2

    def And(self, player):
        if self._count >= PlayerContext.maxPlayers:
            raise Exception("Too many players added.")

        self._players.add(player)
        self._count += 1

    def Using(self, engine):
        return Game(self._players, engine)
