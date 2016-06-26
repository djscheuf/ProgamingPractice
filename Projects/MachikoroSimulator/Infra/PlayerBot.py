"""
Purpose: PlayerBot will:
    + utilize it's known end-state, and current-state to
        determine what action to take for the turn ( what cards to buy)
    + request desired cards from DeckManager (injected)
    + present its current state to GameManager for evaluation
    + recall and manage its funds, awarded by GameManager

Knows:
    + Current state
    + Desired End state
    + Current funds
    + How to choose next desired purchase ( may be refactored later)
"""
