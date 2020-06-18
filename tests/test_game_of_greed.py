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


