from GameFunctions.Make_players import players
from GameFunctions.Make_bids import make_Bids
from GameFunctions.winner import winner

class lier:
    def __init__(self, player_num):
        self.player_num = player_num 
        self.player = []


    def game(self):
        for player in range(self.player_num):
            player = players()
            self.player.append(player)

        make_Bids(self)
        winner(self)
        print("continue")

#make a game file that just calls lier and allows the user to input number of players up to 4    
#lier(3).game()

