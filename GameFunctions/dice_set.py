import GameFunctions.diceroller as diceroller

def dice_set(dice):
    player_roll = [0] * dice
    for roll in range(len(player_roll)):
        player_roll[roll] = diceroller .diceroller(6).roll()
    return player_roll