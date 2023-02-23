"""EX04- Utilities? Lists? idk."""
__author__ = "730552002"


def all(listy: list, checker: int) -> bool:
    n = 0
    while n < len(listy):
        if listy[n] != checker:
            return False
        n += 1
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    n = 0
    greatest = input[n]
    while n < len(input):
        if input[n] > greatest:
            greatest = input[n]
        n += 1
    return greatest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False
    n = 0
    while n < len(list1):
        if list1[n] != list2[n]:
            return False
        n += 1
    return True