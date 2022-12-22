"""EXAM."""
import re


def find_capital_letters(text: str) -> str:
    """Function that finds capital letters."""
    pattern = r"[A-Z]"
    capital_letters = ""
    for match in re.finditer(pattern, text):
        capital_letters += match.group()
    return capital_letters


#print(find_capital_letters("Tomato AppLE cat Dog HoMe"))


def close_far(a: int, b: int, c: int) -> bool:
    """Docstring."""
    if abs(a - b) <= 1 and abs(a - c) >= 2 and abs(b - c) >= 2:
        return True
    if abs(a - c) <= 1 and abs(a - b) >= 2 and abs(b - c) >= 2:
        return True
    return False


print(close_far(1, 2, 5))  # True
print(close_far(1, 2, 3))  # False
print(close_far(2, 3, 5))  # True
print(close_far(1, 1, 2))  # False
print(close_far(1, 3, 5))  # False



def get_names_from_results(results_string: str, min_result: int) -> list:
    """Given a string of names and scores, return a list of names where the score is higher than or equal to min_result."""
    new_string = results_string.replace(',', " ")
    splited_result = new_string.split()
    name = (splited_result[::2])
    print("names are : ", name)


"""
print(get_names_from_results("ago 123,peeter 11", 0)) # ["ago", "peeter"]
print(get_names_from_results("ago 123,peeter 11,33", 10)) # ["ago", "peeter"]  # 33 does not have the name
print(get_names_from_results("ago 123,peeter 11", 100)) # ["ago"]
print(get_names_from_results("ago 123,peeter 11,kitty11!! 33", 11)) # ["ago", "peeter",  "kitty11!!"]
print(get_names_from_results("ago 123,peeter 11,kusti riin 14", 12)) # ["ago", "kusti riin"]
"""
