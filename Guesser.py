import random

class diceroller:
    def __init__(self, sides):
        self.sides = sides
    
    def roll(self):
        min_value = 1 
        max_value = self.sides 
        roll = random.randint(min_value, max_value)
        return roll
    
class Guesser:
    def __init__(self, player_num):
        self.players = {}
        while len(self.players) < player_num:
            player_name = input("Player unique Name: ")
            player_roll = [0, 0, 0, 0]
            for roll in range(len(player_roll)):
                player_roll[roll] = diceroller(6).roll()
            self.players[f"{player_name}"] = player_roll
        #print(self.players)
        self.total = 0
        for i in self.players.values(): 
            self.total += sum(i)     
        #print(self.total)
        
    def game(self):
        self.guesses = self.players.copy()
        for player in self.guesses:
            print(player, sum(self.players.get(player)))
            self.guesses[f"{player}"] = int(input("Guess the total number: "))       
        differences = self.guesses.copy()
        outcome = self.players.copy()
        #print(differences)
        for player in outcome.keys():
            how_close = self.total - differences.get(player)
            outcome[f"{player}"] = how_close 
        #print(outcome)
        winner = min(outcome.values())
        for key, Value in outcome.items():
            if Value == winner:
                print(f"The winner is {key}")

Guesser(2).game()

#have each player make guesses for total of all the dice combined (later try to make liers dice rules   ) 
