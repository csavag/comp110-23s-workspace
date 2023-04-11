from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read csv file and return as a list of dicts with header keys"""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table columb under a specific header"""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row)
    return result

def columnar(table: list[dict[str,str]]) -> dict[str,list[str]]:
    """Reformats data so that it's a dictionary with column headings"""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table
    first_row: dict[str,str] = table[0]
    for key in first_row:
        #for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result

def head(data: dict[str, list[str]], num: int) -> dict[str, list[str]]:
    return_dict = {}
    for column in data.keys():
        temp = []
        for i in range(num):
            temp.append(data[column][i])
        return_dict[column] = temp
    return return_dict

def select(data: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    return_dict = {}
    for item in names:
        return_dict[item] = data[item]
    return return_dict

def concat(dict1: dict[str, list[str]], dict2: dict[str, list[str]]) -> dict[str, list[str]]:
    return_dict = {}
    for key in dict1.keys():
        return_dict[key] = dict1[key]
    for key in dict2.keys():
        if key in return_dict.keys():
            return_dict[key] += dict2[key]
        else:
            return_dict[key] = dict2[key]
    return return_dict

def count(list1: list[str]) -> dict[str, int]:
    return_dict = {}
    for item in list1:
        if item in return_dict:
            return_dict[item] += 1
        else:
            return_dict[item] = 1
    return return_dict