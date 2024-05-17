import GameFunctions.diceroller as diceroller

def make_players(self):
    while len(self.players) < self.player_num:
        player_name = input("Player unique Name: ")
        player_roll = [0, 0, 0, 0]
        for roll in range(len(player_roll)):
            player_roll[roll] = diceroller.diceroller(6).roll()
        self.players[f"{player_name}"] = player_roll 
    self.bids = self.players.copy()
    self.can_guess = self.players.copy()  
    for player in self.can_guess:
        self.can_guess[f"{player}"] = "y"  
    for player in self.bids:
        self.bids[f"{player}"] = (0, 0)

