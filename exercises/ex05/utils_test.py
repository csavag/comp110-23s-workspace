"""Tests for the utils.py file."""
__author__ = "730552002"

from exercises.ex05.utils import only_evens, concat, sub

def test_evens_and_odds() -> None:
    """asdf."""
    assert only_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_other_numbers_idk() -> None:
    """awrsf."""
    assert only_evens([3, 6, 7, 9, 10, 18]) == [6, 10, 18]


def test_empty() -> None:
    """spofihb."""
    assert only_evens([]) == []


def test_two_lists() -> None:
    """sporiuf."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_more_lists() -> None:
    """wpeoav."""
    assert concat([8, 6], [7, 5, 3, 0, 9]) ==[8, 6, 7, 5, 3, 0, 9]


def test_one_empty() -> None:
    """aodvl."""
    assert concat([1, 4], []) == [1, 4]


def test_normal_usasgh() -> None:
    """skbvfd."""
    assert sub([1, 2, 3, 4, 5], 2, 4) == [3, 4]


def test_again() -> None:
    """pc9qoah."""
    assert sub([55, 22, 17, 98103], 0, 4) == [55, 22, 17, 98103]


def test_wiuadfhklb() -> None:
    """;oqci;new."""
    assert sub([3, 4, 5, 99], 1, 2) == [4]