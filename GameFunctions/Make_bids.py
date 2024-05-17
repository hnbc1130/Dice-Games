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