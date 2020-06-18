import random
from collections import Counter

class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def roll_dice(dice_count):
        running_total = []
        for _ in range(dice_count):
            one_die = random.randint(1,6)
            running_total.append(one_die)
        # print(running_total)
        return tuple(running_total)


    @staticmethod
    def calculate_score(dice_set):
        ctr = Counter(dice_set)
        first_key_of_ctr = list(ctr.keys())[0]
        if len(ctr) >= 2:
            second_key_of_ctr = list(ctr.keys())[1]
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
        if len(ctr) == 3 and ctr[2] == 2:
            return 1500
        if len(ctr) == 1:
            if first_key_of_ctr == 1:
                return 4000 + leftovers
            else:
                return first_key_of_ctr * 400 + leftovers
        if len(ctr) == 2 and ctr[0] == 5:
            if first_key_of_ctr == 1:
                return 3000 + leftovers
            else:
                return first_key_of_ctr * 300 + leftovers
        if ctr[0] == 4:
            if first_key_of_ctr == 1:
                return 2000 + leftovers
            else:
                return first_key_of_ctr * 200 + leftovers
        if len(ctr) == 2 and ctr[0] == 3:
            if first_key_of_ctr == 1:
                return 1000 + (second_key_of_ctr * 100)
            elif second_key_of_ctr == 1:
                return 1000 + first_key_of_ctr * 100
            else:
                return (first_key_of_ctr * 100) + (second_key_of_ctr * 100)
        if ctr[0] == 3:
            if first_key_of_ctr == 1:
                return 1000 + leftovers
            else:
                return first_key_of_ctr * 100 + leftovers
        return 0


class Banker:
    pass


if __name__ == "__main__":
    # GameLogic.roll_dice(1)
    # GameLogic.calculate_score((2,2,2,2,2,2))
    # GameLogic.calculate_score(GameLogic.roll_dice(6))
    GameLogic.calculate_score((1,1,1,5,5,5))