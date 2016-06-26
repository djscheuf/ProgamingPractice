"""
Purpose: The SimulationConductor will:
    + Organize the games
    + Construct the PlayerBots
    + Execute desired number of games
    + Collect the Results
    + Compute Statistics
    + Present Stats upon completion

Knows:
    + PlayerBot Strategies (injected)
    + Knows Simulation History ( collected results)
    + Knows Desired Game Count ( injected)
    + Know current game Count
"""

class SimulationConductor():
    def __init__(self):
        self._finalGameCount = 0

    def SetGameCount(self,gameCnt):
        self._finalGameCount = gameCnt
