"""
Purpose: The GameManager will:
    + Evaluate Victory Conditions
    + Manage Turn Actors
    + Recall current turn
    + Hold Deck Manager
    + Hold PlayerBots
    + Present Victory Turn
    + Present Victor
    + Award funds based on dice role
    + Roll dice for PlayerBots, based on current-state (may be refactored later)

Knows:
    + PlayerBots(injected)
    + DeckManager
    + Current Turn
    + Current Turn Actor
    + How many dice PlayerBot can roll ( based on Playerboo current state)
    + How to award funds based on PlayerBot current state ( i.e. card rules)
    + How to determine Victor
    + Victorious PlayerBot
    + Turn of Victory
"""
