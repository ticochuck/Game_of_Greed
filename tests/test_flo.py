import pytest
from tests.flo import Flo


def test_class():
    assert Flo


def test_wanna_play():
    Flo.test('tests/flow/wanna_play.txt')


def test_do_wanna_play_then_quit():
    Flo.test('tests/flow/do_wanna_play_then_quit.txt')


def test_quitter():
    Flo.test('tests/flow/quitter.txt')


def test_bank_first_for_two_rounds():
    Flo.test('tests/flow/bank_first_for_two_rounds.txt')


def test_bank_one_roll_then_quit():
    Flo.test('tests/flow/bank_one_roll_then_quit.txt')


def test_cheat_and_fix():
    Flo.test('tests/flow/cheat_and_fix.txt')


def test_hot_dice():
    Flo.test('tests/flow/hot_dice.txt')


def test_living_on_the_edge():
    Flo.test('tests/flow/living_on_the_edge.txt')


def test_zilch():
    Flo.test('tests/flow/zilch.txt')