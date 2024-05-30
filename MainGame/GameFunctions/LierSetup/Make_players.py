import GameFunctions.LierSetup.dice_set as dice_set
#add make this a Data classes
class players():
    try:
        def __init__(self):
            self.player_name = input("Player Name\n")
            self.dice = 4 
            self.dice_rolls = dice_set.dice_set(self.dice) #returns a lists in a list, removed []
            self.can_guess = True
            self.bids = (0, 0)
            self.wins = 0
            #add computer players
    
    except:
        TimeoutError
        
