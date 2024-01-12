import random

class diceroller:
    def __init__(self, sides):
        self.sides = sides
    
    def roll(self):
        min_value = 1 
        max_value = self.sides 
        roll = random.randint(min_value, max_value)
        return roll

class pig:
    def __init__(self):
        while True:
            print("Must input players to continue")
            players = input("Enter number of players: ")
            if players.isdigit(): 
                players = int(players)
                if 1 <= players <= 4:
                    break
                else: 
                    print("invalid inpput")
            else:
                print("enter number")

        print(players)

        winning_score = 50
        players_scores = [0 for _ in range((players))]

        print(players_scores)

        while max(players_scores) < winning_score: 
            for player in range(players):
                print(f"{player + 1} is rolling \n Total score {players_scores[player]}")
                current_score = 0 
                while max(players_scores) < winning_score:
                    take_roll = input("roll the dice (y)? ")
                    if take_roll.lower() != "y":
                        break
                    elif max(players_scores) < winning_score:
                        attempt = diceroller(6).roll()
                        print(f"rolled {attempt}")
                        if attempt == 1:
                            print("You Get Nothing")
                            current_score = 0
                            break 
                        elif attempt > 1 < 7: 
                            current_score += attempt
                            print(current_score)

                players_scores[player] += current_score
                print(f"Total Score: {players_scores[player]}")

        finals = max(players_scores)
        winner = players_scores.index(finals)
        print(f"winner is {winner + 1}")

pig()