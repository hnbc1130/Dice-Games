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

    def game(self):
        
        #Make a dict where the key is each numbeber in player_num and the value is the total in player_roll
        #for player in self.players:
            #for roll in player:
                #if roll = 1 dict.value += 1 
         
        try: 
            #loop through players, check if can_guess is y, if so allow them to bid, if n then they cannot guess , if they skip their bid is set to 0 aaa
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
            
            print(self.can_guess, self.bids)  

        except:
            print("The Error")
        
lier(3).game()

            #loop through players and ask if they would like to guess the total number of a specific die,
            #must be a greater total than previous guess, i.e, 4 2's is 8 but 3 3's is 9   
            
            
#bids = self.players.copy()
#            can_guess = self.players.copy()     
#            for player in can_guess:
#                can_guess[f"{player}"] = "y"
#            skip = 0
#            while skip < self.player_num :
#                for player in self.players:
#                    print(player)
#                    move = input("press g, to guess \n press s, to skip \n")
#                    if move != "s" or "g":
#                        print("your input is bad and you should feel bad")
#                    elif move.lower() == "s":
#                            skip += 1 
#                            can_guess[f"{player}"] = "n"
#                    elif move.lower() == "g":                    
#                            bids.fromkeys(player) == tuple(input("Guess:"))

#alier(2).game()

#have each player make guesses for total of all the dice combined (later try to make liers dice rules   ) 
