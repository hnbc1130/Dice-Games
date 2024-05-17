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