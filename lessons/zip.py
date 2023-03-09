def zip(keys: list[str], values: list[int]) -> dict[str,int]:
    return_dict = {}
    if len(keys) != len(values):
        return return_dict
    for i in range(len(keys)):
        return_dict[keys[i]] = values[i]
    return return_dict