def make_Bids(self): 
    try:
    
        skip = 0
        while skip < self.player_num - 1:
            for player in self.player:
                print(player.player_name)                
                if player.can_guess == False or player.dice == 0 or skip == self.player_num - 1: 
                    if player.can_guess == False:
                        print(f"{player.player_name} has skipped")
                    else:
                        return self.player_num
                else:
                    move = input("press g, to guess \npress s, to skip \n")
                
                    if move != "s" and move != "g":
                        player.can_guess = False
                        skip += 1
                        print("your input is bad and you should feel bad")
                    elif move == "s":
                        if skip == self.player_num - 1:
                            return
                        skip += 1 
                        player.can_guess = False
                        player.bids = (0, 0)
                    elif move == "g":
                        print(player.dice_rolls)         
                        dice_num = int(input("How many dice?\n")) 
                        face = int(input("What Face?\n"))                                  
                        player.bids = tuple((dice_num, face))     


    except:
        print("The Error")