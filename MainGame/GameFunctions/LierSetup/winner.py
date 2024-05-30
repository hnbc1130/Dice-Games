def winner(self):
        
        try:
            #put in own gamefunction file
            total = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
            for player in self.player:
                for roll in player.dice_rolls:
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
      
            for player in self.player:                   
                if player.bids == (0, 0): 
                        print(f"{player.player_name} skipped")                            
                else:   
                    face = player.bids[1]
                    how_many = player.bids[0]
                    if how_many <= total[face]:
                        player.wins += 1 
                        print(f"{player.player_name} you win")
                    else:
                        player.dice -= 1
                        print(f"{player.player_name} you lose")

        except:
            return