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
    def __init__(self, dice_roller=None):
        self.remaining_dice = 6
        self.current_round = 1
        self.banker = Banker()
        if dice_roller:
            self.dice_roller = dice_roller
        else:
            self.dice_roller = GameLogic.roll_dice

    def welcome(self):
        gameon = False
        while not gameon:
            print("Welcome to Game of Greed")
            start_game = input("Wanna play?").lower()
            if start_game == 'y':
                gameon = True
                print(f"Starting round {self.current_round}")
                self.player_roll()

            elif start_game == 'n':
                gameon = True
                print("OK. Maybe another time")
                sys.exit()

    @staticmethod
    # Also check that all dice are scoring dice
    def validation(dice_values, dice_to_shelf):
        dice_values_to_validate =  list(dice_values) #dice roll
        dice_to_shelf = list(dice_to_shelf) #user input

        for i in dice_to_shelf:
            if i in dice_values_to_validate:
                dice_values_to_validate.remove(i)
            else:
                print('Cheater!!! Or possibly made a typo...')
                return True

        ctr = Counter(dice_to_shelf)
        if len(ctr) == 6:
            return False
        if len(ctr) == 3 and list(ctr.most_common())[2][1] == 2:
            return False

        for i in list(ctr.most_common()):
            if i[0] == 2 or i[0] == 3 or i[0] == 4 or i[0] == 6:
                if i[1] < 3:
                    print('Cheater!!! Or possibly made a typo...')
                    return True

        return False


    def player_roll(self):
        print(f"Rolling {self.remaining_dice} dice...")

        dice_values = self.dice_roller(self.remaining_dice)
        points_to_bank = GameLogic.calculate_score(dice_values)
        
        if points_to_bank == 0:
            roll_display = ""
            for x in range(len(dice_values)):
                roll_display += str(dice_values[x]) + ","
            print(roll_display[:-1])
            print('Zilch!!! Round over')
            print(f'You banked 0 points in round {self.current_round}')
            print(f'Total score is {self.banker.bank_points} points')
            self.banker.clear_shelf()
            self.next_round()         

        cheat_check = True
        while cheat_check:
            roll_display = ""
            for x in range(len(dice_values)):
                roll_display += str(dice_values[x]) + ","
            print(roll_display[:-1])
            select_dice = input("Enter dice to keep (no spaces), or (q)uit: ")
            if select_dice == 'q':
                self.quit_game()
            dice_to_shelf = list(select_dice)
            dice_to_shelf = tuple(map(int, dice_to_shelf))
            cheat_check = Game.validation(dice_values, dice_to_shelf)


        points_to_bank = GameLogic.calculate_score(dice_to_shelf)
        self.banker.shelf(points_to_bank)
        self.remaining_dice -= len(dice_to_shelf)
        print(f'You have {self.banker.shelf_points} unbanked points and {self.remaining_dice} dice remaining')
        user_choice = input("(r)oll again, (b)ank your points or (q)uit ").lower()

        if user_choice == 'r':
            # this also handles hot dice according to the flow tests
            if self.remaining_dice == 0:
                self.remaining_dice = 6 
            self.player_roll()

        elif user_choice == 'b':
            print(f'You banked {self.banker.shelf_points} points in round {self.current_round}')
            self.banker.bank()
            print(f'Total score is {self.banker.bank_points} points')
            self.next_round()

        elif user_choice == 'q':
            self.quit_game()

    def next_round(self):
        self.remaining_dice = 6
        self.current_round += 1
        if self.current_round <= 20:
            print(f"Starting round {self.current_round}")
            self.player_roll()
        else:
            # print('Game over')
            print(f"Thanks for playing. You earned {self.banker.bank_points} points")

    def quit_game(self):
        print(f"Total score is {self.banker.bank_points} points")
        print(f"Thanks for playing. You earned {self.banker.bank_points} points")
        sys.exit()

    def play(self):
        self.welcome()


if __name__ == '__main__':
    new_game = Game()
    new_game.play()


