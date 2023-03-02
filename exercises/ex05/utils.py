"""Utility functions or something."""
__author__ = "730552002"


def only_evens(inp: list[int]) -> list[int]:
    """Returns only the even numbers in a list."""
    return_list: list[int] = []
    n: int = 0
    while n < len(inp):
        if inp[n] % 2 == 0:
            return_list.append(inp[n])
        n += 1
    return return_list


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Returns a new list containing lists 1 and 2."""
    return_list: list[int] = []
    n: int = 0
    while n < len(list1):
        return_list.append(list1[n])
        n += 1
    n = 0
    while n < len(list2):
        return_list.append(list2[n])
        n += 1
    return return_list


def sub(list1: list[int], idx1: int, idx2: int) -> list[int]:
    """Returns a list of the provided list ranging from the two provided indices."""
    return_list: list[int] = []
    n: int = idx1
    while n < idx2:
        return_list.append(list1[n])
        n += 1
    return return_list