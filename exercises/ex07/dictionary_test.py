"""Tests for the file named dictionary.py."""
__author__ = "730552002"


from exercises.ex07.dictionary import invert, favorite_color, count


def test_edge() -> None:
    """Edge case for invert."""
    assert invert({}) == {}


def test_norm() -> None:
    """Use case for invert."""
    assert invert({1:2, "a": 3}) == {2: 1, 3: "a"}


def test_again() -> None:
    """asdfasdf."""
    assert invert({"a": "b", 1: 2}) == {"b": "a", 2: 1}


def test_fav() -> None:
    """Whee."""
    assert favorite_color({"dan": "hat","0112": "red-tailed hawk","hemeny": "hat"}) == "hat"


def test_favnorm() -> None:
    """aiohv."""
    assert favorite_color({"Sheryl": "blue", "Waltuh": "blue","Wade": "red","Minerva": "red"}) == "blue"


def test_favthree() -> None:
    """s;odfgba;wfnd/."""
    assert favorite_color({"Hehehe": "chaiiro"}) == "chaiiro"


def test_count() -> None:
    """Counttest."""
    assert count([]) == {}


def test_wank() -> None:
    """laksdfh."""
    assert count(["apple", 34, "apple"]) == {"apple": 2, 34: 1}


def test_agained() -> None:
    """Last!"""
    assert count(["pop", "pop", "pop", "muzik"]) == {"pop": 3,"muzik": 1}