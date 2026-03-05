import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess, get_range_for_difficulty


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_guess_one_above_secret():
    outcome, _ = check_guess(6, 5)
    assert outcome == "Too High"


def test_guess_one_below_secret():
    outcome, _ = check_guess(4, 5)
    assert outcome == "Too Low"


def test_boundary_low():
    outcome, _ = check_guess(1, 1)
    assert outcome == "Win"


def test_boundary_high():
    outcome, _ = check_guess(100, 100)
    assert outcome == "Win"


# When app passes secret as a string (even-attempt branch in app.py)
def test_str_secret_win():
    outcome, _ = check_guess(42, "42")
    assert outcome == "Win"


def test_str_secret_too_high():
    outcome, message = check_guess(80, "50")
    assert outcome == "Too High"
    assert "LOWER" in message


def test_str_secret_too_low():
    outcome, message = check_guess(10, "50")
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20


def test_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50


def test_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100


def test_range_unknown_fallback():
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 50
