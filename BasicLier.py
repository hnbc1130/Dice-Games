from GameFunctions.Make_players import make_players
from GameFunctions.Make_bids import make_Bids
from GameFunctions.winner import winner

class lier:
    def __init__(self, player_num):
        self.players = {}
        self.player_num = player_num 

    def game(self):
        make_players(self)
        make_Bids(self)
        winner(self)
   
lier(3).game()

