import random

class diceroller:
    def __init__(self, sides):
        self.sides = sides
    
    def roll(self):
        min_value = 1 
        max_value = self.sides 
        roll = random.randint(min_value, max_value)
        return roll
    
class lier:
    def __init__(self, player_num):
        self.players = {}
        self.player_num = player_num 

    def game(self):
        lier.make_players(self)
        lier.make_Bids(self)
        lier.winner(self)
   
    def make_players(self):
        while len(self.players) < self.player_num:
            player_name = input("Player unique Name: ")
            player_roll = [0, 0, 0, 0]
            for roll in range(len(player_roll)):
                player_roll[roll] = diceroller(6).roll()
            self.players[f"{player_name}"] = player_roll 
        self.bids = self.players.copy()
        self.can_guess = self.players.copy()  
        for player in self.can_guess:
            self.can_guess[f"{player}"] = "y"  
        for player in self.bids:
            self.bids[f"{player}"] = (0, 0)

    def make_Bids(self): 
        try: 
            skip = 0
            while skip < self.player_num - 1:
                for player in self.can_guess:
                    print(player)
                    if self.can_guess[f"{player}"] == 'n':
                        print(f"{player} has skipped")
                    else:
                        move = input("press g, to guess \npress s, to skip \n")
                        if move != "s" and move != "g":
                            print("your input is bad and you should feel bad")
                        elif move == "s":
                            skip += 1 
                            self.can_guess[f"{player}"] = "n"
                            self.bids[player] = (0, 0)
                        elif move == "g":                                            
                            self.bids[player] = tuple(input("Guess(dice face):"))     

        except:
            print("The Error")

    def winner(self):
        
        try:
            #make an empty dict then loop through to the length of diceroller with each face being a key.
            #loop through each players rolls and add 1 to the coresponding key for each face. 
            #check the player bid, use first digit as key, then if bid is <= to the dict value, winner, else player_roll for that player - 1 (is that a set var that can be changed and saved as a state?)


            total = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
            for player in self.players.values():
                for roll in player:
                    if roll == 1:
                        total[roll] += 1
                    elif roll == 2:
                        total[roll] += 1
                    elif roll == 3:
                        total[roll] += 1
                    elif roll == 4:
                        total[roll] += 1
                    elif roll == 5:
                        total[roll] += 1
                    elif roll == 6:
                        total[roll] += 1
                    else:
                        return total
      
            for key, Value in self.bids.items():
                if Value == (0, 0): 
                        print(f"{key} skipped")                            
                    #print(f"{user.values()} skipped")
                else:   
                    face = int(Value[1])
                    how_many = int(Value[0])
                    if how_many <= total[face]:
                        print(f"{key} you win")
                    else:
                        print(f"{key} you lose")
        except:
            return

        #Make a dict where the key is each numbeber in player_num and the value is the total in player_roll
        #for player in self.players:
            #for roll in player:
                #if roll = 1 dict.value += 1 

lier(3).game()

