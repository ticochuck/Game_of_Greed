import sys
from textwrap import dedent
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class Game:
    def __init__(self, roll_dice = None):
        self.remaining_dice = 6
        self.current_round = 1


    def welcome(self):
        print('Hi, welcome to the game')
        start_game = input('Would you like to play? Y/N').lower()
        if start_game == 'y':
            self.player_roll()
        else:
            print('Ok, maybe next time')
            sys.exit()


    def player_roll(self):
        print(dedent(f"""
            Round:  {self.current_round}
            Bank Points: {banker.bank_points}
            Points in Shelf: {banker.shelf_points}
        """))

        dice_values = GameLogic.roll_dice(self.remaining_dice)
        print('Your roll ', dice_values)

        select_dice = input('Please enter the dice you want to keep separated by spaces or (q)uit')
        dice_to_shelf = select_dice.split()
        dice_to_shelf = tuple(map(int, dice_to_shelf))
        
        points_to_bank = GameLogic.calculate_score(dice_to_shelf)
        banker.shelf(points_to_bank)
        
        self.remaining_dice -= len(dice_to_shelf)
        user_choice = input("Would you like to Roll again ('R') or Bank your Points ('B') or Quit ('Q')?").lower()
        
        if user_choice == 'r':
            self.player_roll()
        
        elif user_choice == 'b':
            banker.bank()
            print('Your Banked Points: ', banker.bank_points)
            self.remaining_dice = 6
            self.current_round += 1
            self.player_roll()

    
    def play(self):
        self.welcome()
        self.player_roll()
        

if __name__ == '__main__':
    new_game = Game()
    banker = Banker()
    #new_game.welcome()
    new_game.play_game()
    #new_game.player_roll()
    
    
    