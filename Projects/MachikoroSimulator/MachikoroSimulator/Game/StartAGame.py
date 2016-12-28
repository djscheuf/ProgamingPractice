from PlayerContext import PlayerContext

class StartAGame():
    def With(firstBot, secondBot):
        return PlayerContext(firstBot,secondBot)
