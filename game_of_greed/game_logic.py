import random
from collections import Counter

# Define a GameLogic class.
class GameLogic:
    def __init__(self):
        pass

# Handle rolling dice
# Add roll_dice static method to GameLogic class.
# The input to roll_dice is an integer between 1 and 6.
# The output of roll_dice is a tuple with random values between 1 and 6.
# The length of tuple must match the argument given to roll_dice method.
    @staticmethod
    def roll_dice(dice_count):
        running_total = []
        for _ in range(dice_count):
            one_die = random.randint(1,6)
            running_total.append(one_die)
        # print(running_total)
        return tuple(running_total)


    @staticmethod
    def get_scorers(dice_values):
        scorers = []
        return_scorers = []
        ctr = Counter(dice_values)
        if len(ctr) == 6:
            scorers = list(dice_values)
            return scorers
        if len(ctr) == 3 and list(ctr.most_common())[2][1] == 2:
            scorers = list(dice_values)
            return scorers
        for i in list(ctr.most_common()):
            if i[0] == 1 or i[0] == 5:
                scorers.append(i)
            if i[0] == 2 or i[0] == 3 or i[0] == 4 or i[0] == 6:
                if i[1] >= 3:
                    scorers.append(i)
        for i in scorers:
            for j in range(i[1]):
                return_scorers.append(i[0])
        return return_scorers

# Handle calculating score for dice roll
# Add calculate_score static method to GameLogic class.
# The input to calculate_score is a tuple of integers that represent a dice roll.
# The output from calculate_score is an integer representing the roll's score according to rules of game.
    @staticmethod
    def calculate_score(dice_set):
        ctr = Counter(dice_set)
        first_key_of_ctr = int(list(ctr.most_common())[0][0])
        if len(ctr) >= 2:
            second_key_of_ctr = list(ctr.most_common())[1][0]
            second_value_of_ctr = list(ctr.most_common())[1][1]
        first_value_of_ctr = list(ctr.most_common())[0][1]
        ones_score = 0
        fives_score = 0
        for x in ctr.keys():
            if x == 1 and ctr.get(x) <= 2:
                ones_score = ctr.get(x) * 100
            if x == 5 and ctr.get(x) <= 2:
                fives_score = ctr.get(x) * 50
        leftovers = ones_score + fives_score
        if len(ctr) == 6:
            return 1500
        if len(ctr) == 3 and list(ctr.most_common())[2][1] == 2:
            return 1500
        if first_value_of_ctr == 6:
            if first_key_of_ctr == 1:
                return 4000 + leftovers
            else:
                return first_key_of_ctr * 400 + leftovers
        if first_value_of_ctr == 5:
            if first_key_of_ctr == 1:
                return 3000 + leftovers
            else:
                return first_key_of_ctr * 300 + leftovers
        if first_value_of_ctr == 4:
            if first_key_of_ctr == 1:
                return 2000 + leftovers
            else:
                return first_key_of_ctr * 200 + leftovers
        if len(ctr) == 2 and second_value_of_ctr == 3:
            if first_key_of_ctr == 1:
                return 1000 + (second_key_of_ctr * 100)
            elif second_key_of_ctr == 1:
                return 1000 + first_key_of_ctr * 100
            else:
                return (first_key_of_ctr * 100) + (second_key_of_ctr * 100)
        if first_value_of_ctr == 3:
            if first_key_of_ctr == 1:
                return 1000 + leftovers
            else:
                return (first_key_of_ctr * 100) + leftovers
        return leftovers




# if __name__ == "__main__":
    # GameLogic.roll_dice(1)
    # GameLogic.calculate_score((2,2,2,2,2,2))
    # GameLogic.calculate_score(GameLogic.roll_dice(6))
    # GameLogic.calculate_score((1,1,1,5,5,5))
    