"""A file named dictionary.py."""
__author__ = "730552002"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts."""
    i = 0
    return_dict: dict = {}
    while i < len(input_dict):
        if input_dict[list(input_dict)[i]] in list(return_dict):
            raise KeyError("Multiple keys with the same name. That's bad. Fool.")
        return_dict[input_dict[list(input_dict)[i]]] = list(input_dict)[i]
        i += 1
    return return_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Colors."""
    new_dict = {}
    for item in input_dict:
        if input_dict[item] in new_dict:
            new_dict[input_dict[item]] += 1
        else:
            new_dict[input_dict[item]] = 1
    highest = 0
    value = ""
    for each in new_dict:
        if new_dict[each] > highest:
            highest = new_dict[each]
            value = each
    return value


def count(input_list: list[str]) -> dict[str, int]:
    """Count bleck!"""
    return_dict = {}
    for item in input_list:
        if item in return_dict:
            return_dict[item] += 1
        else:
            return_dict[item] = 1
    highest = 0
    value = ""
    for item in return_dict:
        if return_dict[item] > highest:
            highest = return_dict[item]
            value = item
    return value