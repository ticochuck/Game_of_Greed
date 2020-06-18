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


# @pytest.mark.skip
def test_return_six_dice():
    six = GameLogic.roll_dice(6)
    assert type(six) == tuple
    assert len(six) == 6


def test_return_one_thru_six():
    for _ in range(1000):
        actual = GameLogic.roll_dice(1)[0]
        assert 1 <= actual <= 6


