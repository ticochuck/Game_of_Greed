import pytest

from game_of_greed import __version__
from game_of_greed.game_of_greed import (
    GameLogic,
    Banker,
)


def test_version():
    assert __version__ == '0.1.0'


def test_gamelogic_exists():
    assert GameLogic


def test_banker_exists():
    assert Banker


def test_roll_dice_exists():
    assert GameLogic.roll_dice


def test_calc_score_exists():
    assert GameLogic.calculate_score


# Testing - Roll Dice
# When rolling 1 to 6 dice ensure a sequence of correct length is returned
# @pytest.mark.skip
def test_return_six_dice():
    six = GameLogic.roll_dice(6)
    assert type(six) == tuple
    assert len(six) == 6


# Each item in sequence is an integer with value between 1 and 6
def test_return_one_thru_six():
    for _ in range(1000):
        actual = GameLogic.roll_dice(1)[0]
        assert 1 <= actual <= 6


# Testing - Calculate Score

# zilch - non scoring roll should return 0
#@pytest.mark.skip
def test_calc_zilch():
    assert GameLogic.calculate_score((2,2,3,3,4,6)) == 0


# ones - rolls with various number of 1s should return correct score
def test_calc_six_ones():
    assert GameLogic.calculate_score((1,1,1,1,1,1)) == 4000


def test_calc_five_ones():
    assert GameLogic.calculate_score((2,1,1,1,1,1)) == 3000


def test_calc_four_ones():
    assert GameLogic.calculate_score((1,1,1,1,2,2)) == 2000


def test_calc_three_ones():
    assert GameLogic.calculate_score((1,1,1,3,2,2)) == 1000


def test_calc_two_ones():
    assert GameLogic.calculate_score((1,1,3,2,4,4)) == 200


def test_calc_one_ones():
    assert GameLogic.calculate_score((1,2,2,3,3,4)) == 100


# twos - rolls with various number of 2s should return correct score

def test_calc_six_twos():
    assert GameLogic.calculate_score((2,2,2,2,2,2)) == 800


def test_calc_five_twos():
    assert GameLogic.calculate_score((3,2,2,2,2,2)) == 600


def test_calc_four_twos():
    assert GameLogic.calculate_score((3,3,2,2,2,2)) == 400


def test_calc_three_twos():
    assert GameLogic.calculate_score((3,3,4,2,2,2)) == 200


def test_calc_two_twos():
    assert GameLogic.calculate_score((2,2,1,5,4,6)) == 150


def test_calc_one_twos():
    assert GameLogic.calculate_score((1,2,6,3,3,4)) == 100

# threes - rolls with various number of 3s should return correct score

def test_calc_six_threes():
    assert GameLogic.calculate_score((3,3,3,3,3,3)) == 1200


def test_calc_five_threes():
    assert GameLogic.calculate_score((3,3,4,3,3,3)) == 900


def test_calc_four_threes():
    assert GameLogic.calculate_score((4,3,3,3,2,3)) == 600


def test_calc_three_threes():
    assert GameLogic.calculate_score((6,4,2,3,3,3)) == 300


def test_calc_two_threes():
    assert GameLogic.calculate_score((5,1,4,4,3,3)) == 150


def test_calc_one_threes():
    assert GameLogic.calculate_score((3,1,4,2,4,2)) == 100

# fours - rolls with various number of 4s should return correct score

def test_calc_six_fours():
    assert GameLogic.calculate_score((4,4,4,4,4,4)) == 1600


def test_calc_five_fours():
    assert GameLogic.calculate_score((3,4,4,4,4,4)) == 1200


def test_calc_four_fours():
    assert GameLogic.calculate_score((4,4,4,4,2,3)) == 800


def test_calc_three_fours():
    assert GameLogic.calculate_score((4,4,2,6,4,3)) == 400


def test_calc_two_fours():
    assert GameLogic.calculate_score((5,1,4,4,3,3)) == 150


def test_calc_one_fours():
    assert GameLogic.calculate_score((3,1,4,2,6,2)) == 100


# fives - rolls with various number of 5s should return correct score

def test_calc_six_fives():
    assert GameLogic.calculate_score((5,5,5,5,5,5)) == 2000


def test_calc_five_fives():
    assert GameLogic.calculate_score((5,5,5,5,5,4)) == 1500


def test_calc_four_fives():
    assert GameLogic.calculate_score((5,5,5,5,2,4)) == 1000


def test_calc_three_fives():
    assert GameLogic.calculate_score((5,5,5,6,4,2)) == 500
    assert GameLogic.calculate_score((5,5,5,6,4,1)) == 600


def test_calc_two_fives():
    assert GameLogic.calculate_score((5,6,5,4,3,3)) == 100


def test_calc_one_fives():
    assert GameLogic.calculate_score((3,4,5,2,6,2)) == 50


# sixes - rolls with various number of 6s should return correct score

def test_calc_six_sixes():
    assert GameLogic.calculate_score((6,6,6,6,6,6)) == 2400


def test_calc_five_sixes():
    assert GameLogic.calculate_score((6,6,6,6,6,4)) == 1800


def test_calc_four_sixes():
    assert GameLogic.calculate_score((6,6,6,6,4,4)) == 1200


def test_calc_three_sixes():
    assert GameLogic.calculate_score((6,6,6,2,3,4)) == 600


def test_calc_two_sixes():
    assert GameLogic.calculate_score((6,6,1,4,3,2)) == 100


def test_calc_one_sixes():
    assert GameLogic.calculate_score((3,4,5,2,6,2)) == 50


# straight - 1,2,3,4,5,6 should return correct score

def test_straight():
    assert GameLogic.calculate_score((2,4,1,3,5,6)) == 1500


# three_pairs - 3 pairs should return correct score

def test_three_pair():
    assert GameLogic.calculate_score((3,6,3,4,6,4)) == 1500


def test_three_pair_second():
    assert GameLogic.calculate_score((1,1,5,5,6,6)) == 1500


# two_trios - 2 sets of 3 should return correct score

def test_two_triplets():
    assert GameLogic.calculate_score((3,1,3,1,3,1)) == 1300
    assert GameLogic.calculate_score((5,5,5,1,1,1)) == 1500
    assert GameLogic.calculate_score((2,2,2,4,4,4)) == 600
    assert GameLogic.calculate_score((6,6,6,5,5,5)) == 1100
    assert GameLogic.calculate_score((3,2,2,3,2,3)) == 500


# Testing - Banker
# shelf should properly track unbanked points

def test_shelf_return():
    test_banker = Banker()
    test_banker.shelf(1000)
    test_points = test_banker.shelf_points
    assert test_points == 1000

# bank should properly add unbanked points to total and return the deposited amount

def test_bank():
    test_banker = Banker()
    test_banker.shelf(1000)
    test_banker.bank()
    assert test_banker.bank_points == 1000
    assert test_banker.shelf_points == 0

# clear_shelf

def test_clear_shelf_and_keep_bank():
    test_banker = Banker()
    test_banker.shelf(1000)
    test_banker.bank()
    test_banker.clear_shelf()
    assert test_banker.shelf_points == 0
    assert test_banker.bank_points == 1000

# combined methods tests

def test_add_to_shelf():
    test_banker = Banker()
    test_banker.shelf(1000)
    test_banker.shelf(400)
    test_points = test_banker.shelf_points
    assert test_points == 1400


# should remove any unbanked points, resetting to zero.
# should not affect previously banked points


