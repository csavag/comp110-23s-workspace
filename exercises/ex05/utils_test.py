"""Tests for the utils.py file."""
__author__ = "730552002"

from exercises.ex05.utils import only_evens, concat, sub

def test_evens_and_odds() -> None:
    assert only_evens([1,2,3,4,5,6]) == [2,4,6]
def test_other_numbers_idk() -> None:
    assert only_evens([3,6,7,9,10,18]) == [6,10,18]
def test_empty() -> None:
    assert only_evens([]) == []

def test_two_lists() -> None:
    assert concat([1,2,3], [4,5,6]) == [1,2,3,4,5,6]
def test_more_lists() -> None:
    assert concat([8,6], [7,5,3,0,9]) ==[8,6,7,5,3,0,9]
def test_one_empty() -> None:
    assert concat([1,4], []) == [1,4]

def test_normal_usasgh() -> None:
    assert sub([1,2,3,4,5], 2, 4) == [3,4]
def test_wiuadfhklb() -> None:
    assert sub([3,4,5,99], 0, 2) == [3,4]
def test_abnormal() -> None:
    assert sub([], 0, 0) == []