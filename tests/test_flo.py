import pytest
from tests.flo import Flo


def test_class():
    assert Flo

@pytest.mark.skip
def test_wanna_play():
    Flo.test('tests/flow/wanna_play.txt')

@pytest.mark.skip
def test_do_wanna_play_then_quit():
    Flo.test('tests/flow/do_wanna_play_then_quit.txt')


