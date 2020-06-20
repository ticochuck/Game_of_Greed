from game_logic import GameLogic
from banker import Banker


class GamePlay:
    def __init__(self):
        self.remaining_dice = 6

    # def welcome():
        #print('Hi, welcome to the game')
        #input('would you like to play? Y/N')
        # if Y
        # player.roll(6)
        # if N
        # bye
    
    def player_roll(self):
        dice_values = GameLogic.roll_dice(self.remaining_dice)
        print(dice_values)
        #select_dice = input('Would you like to keep a dice Y/N? Please enter the numbers separated by spaces \n')
        
        select_dice = input('Which dice would you like to keep? Please enter the numbers separated by spaces \n')
        dice_to_shelf = select_dice.split()
        dice_to_shelf = tuple(map(int, dice_to_shelf))
        print(dice_to_shelf)
        
        points_to_bank = GameLogic.calculate_score(dice_to_shelf)
        print(points_to_bank)

        # roll_again, bank, quit
        self.remaining_dice -= len(dice_to_shelf)
        user_choice = input("Would you like to Roll again ('R') or Bank your Points ('B') or Quit ('Q')? \n ").lower()
        
        
        # if user_choice == 'r':
        #     pass
        # elif user_choice == 'b':
            
            #we need the score

        # call roll_dice with dice left



    def play_game(self):
        pass
        #test = GameLogic.calculate_score((1,1,1,1,1))
        #print(test)

if __name__ == '__main__':
    new_game = GamePlay()
    new_game.play_game()
    new_game.player_roll()
    
    
    