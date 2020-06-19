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

# ones - rolls with various number of 1s should return correct score

# twos - rolls with various number of 2s should return correct score

# threes - rolls with various number of 3s should return correct score

# fours - rolls with various number of 4s should return correct score

# fives - rolls with various number of 5s should return correct score

# sixes - rolls with various number of 6s should return correct score

# straight - 1,2,3,4,5,6 should return correct score

# three_pairs - 3 pairs should return correct score

# two_trios - 2 sets of 3 should return correct score

# leftover_ones - 1s not used in set of 3 (or greater) should return correct score

# leftover_fives - 5s not used in set of 3 (or greater) should return correct score


# Testing - Banker
# shelf should properly track unbanked points

# bank should properly add unbanked points to total and return the deposited amount

# clear_shelf
# should remove any unbanked points, resetting to zero.
# should not affect previously banked points

