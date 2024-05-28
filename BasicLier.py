from GameFunctions.LierSetup.Make_players import players
from GameFunctions.LierSetup.Make_bids import make_Bids
from GameFunctions.LierSetup.winner import winner
import GameFunctions.LierSetup.dice_set as dice_set

class lier:
    def __init__(self, player_num):
        self.player_num = player_num 
        self.player = []
        for player in range(self.player_num):
            player = players()
            self.player.append(player)

    def game(self):
        
        try: 
            while True:
                make_Bids(self)
                winner(self)
                for player in self.player:
                    if player.wins == 4:
                        print(f"{player.name} has won")
                        return False 
                    else:
                        player.dice_rolls = dice_set.dice_set(player.dice) 
                        player.can_guess = True
                        player.bids = (0, 0)
                        continue

                
                #reset players back to default cleanup function?   

        except:
            EnvironmentError