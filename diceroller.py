import random

class diceroller:
    def __init__(self, sides):
        self.sides = sides
    
    def roll(self):
        min_value = 1 
        max_value = self.sides 
        roll = random.randint(min_value, max_value)

        return roll

