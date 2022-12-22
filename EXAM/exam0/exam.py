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
    if a == b == c:    # 1 1 1
        return False
    if b == a + 1:     # 1 2 3
        if c == b + 1:
            return False
    if b == c + 1:     # 1 1 0
        if a == b:
            return False
    if b == a + 1:     # 0 1 1
        if c == b:
            return False
    if c == a + 1:     # 1 0 1
        if b == c:
            return False

    else:
        return True


print(close_far(1, 2, 10))  # => True
print(close_far(1, 2, 3))   # => False
print(close_far(4, 1, 3))   # => True


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
