import sys
from collections import Counter
from textwrap import dedent
try:
    from game_of_greed.game_logic import GameLogic
    from game_of_greed.banker import Banker
except:
    from game_logic import GameLogic
    from banker import Banker


class Game:
    def __init__(self):
        self.remaining_dice = 6
        self.current_round = 1


    def welcome(self):
        
        gameon = False
        while not gameon:
            print("Welcome to Game of Greed")
            start_game = input("Wanna play?").lower()
            if start_game == 'y':
                gameon = True
                self.player_roll()

            elif start_game == 'n':
                gameon = True
                print("OK. Maybe another time")
                sys.exit()

    @staticmethod
    def validation(dice_values, dice_to_shelf):
        dice_values_to_validate =  list(dice_values)
        dice_to_shelf = list(dice_to_shelf)
        
        for i in dice_to_shelf:
            if i in dice_values_to_validate:
                dice_values_to_validate.remove(i)
            else:
                print('Cheater!!! Or possibly made a typo...')
                return True
        
        return False
        

    def player_roll(self):
        print(f"Starting round {self.current_round}")
        print(f"Rolling {self.remaining_dice} dice...")
          
        dice_values = GameLogic.roll_dice(self.remaining_dice)
        
        points_to_bank = GameLogic.calculate_score(dice_values)
        
        if points_to_bank == 0:
            print('Zilch!!! Round over')
            print(f'You banked 0 points in round {self.current_round}')
            banker.clear_shelf()
            self.next_round()         
            
        cheat_check = True

        while cheat_check:
            print(dice_values)
            select_dice = input("Enter dice to keep (no spaces), or (q)uit: ")
            
            if select_dice == 'q':
                self.quit_game()

            dice_to_shelf = list(select_dice)

            # check to make sure these are all integers

            dice_to_shelf = tuple(map(int, dice_to_shelf))
            
            cheat_check = Game.validation(dice_values, dice_to_shelf)
          
        points_to_bank = GameLogic.calculate_score(dice_to_shelf)
        print(points_to_bank)
        
        
        banker.shelf(points_to_bank)
        
        self.remaining_dice -= len(dice_to_shelf)
        print(f'You have {banker.shelf_points} unbanked points and {self.remaining_dice} dice remaining')
        user_choice = input("(r)oll again, (b)ank your points or (q)uit ").lower()
        
        if user_choice == 'r':
            if self.remaining_dice == 0:
                self.remaining_dice = 6
            self.player_roll()
        
        elif user_choice == 'b':
            banker.bank()
            print('Your Banked Points: ', banker.bank_points)
            self.next_round()
        
        elif user_choice == 'q':
            self.quit_game()

    def next_round(self):
        self.remaining_dice = 6
        self.current_round += 1
        if self.current_round <= 20:
            self.player_roll()
        else:
            print('Game over')
            self.quit_game()

    def quit_game(self):
        print(f"Total score is {banker.bank_points} points")
        print(f"Thanks for playing. You earned {banker.bank_points} points")
        sys.exit()
    
    def play(self):
        self.welcome()
        self.player_roll()
    

        

if __name__ == '__main__':
    new_game = Game()
    banker = Banker()
    #new_game.welcome()
    new_game.play()
    #new_game.player_roll()
    
    
    