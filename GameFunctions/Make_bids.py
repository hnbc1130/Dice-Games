def make_Bids(self): 
    #add fix to looping issue that if you have bid already and the other players skips it doesn't ask you to bid again. 
    try:
    
        skip = 0
        while skip < self.player_num - 1:
            for player in self.player:
                print(player.player_name)                
                if player.can_guess == False:
                    print(f"{player.player_name} has skipped")
                else:
                    move = input("press g, to guess \npress s, to skip \n")
                if move != "s" and move != "g":
                    player.can_guess = False
                    skip += 1
                    print("your input is bad and you should feel bad")
                elif move == "s":
                    if skip == self.player_num - 1:
                        return
                    else:
                        skip += 1 
                        player.can_guess = False
                        player.bids = (0, 0)
                elif move == "g":  
                    #add variable for face and sides then plug those into bids, better UI       
                    dice_num = int(input("How many dice?\n")) 
                    face = int(input("What Face?\n"))                                  
                    player.bids = tuple((dice_num, face))     


    except:
        print("The Error")