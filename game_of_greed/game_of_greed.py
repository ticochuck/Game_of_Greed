import random

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
        pass


class Banker:
    pass


if __name__ == "__main__":
    GameLogic.roll_dice(1)
