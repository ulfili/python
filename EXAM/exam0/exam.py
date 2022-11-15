"""EXAM."""
import re


def find_capital_letters(text: str) -> list:
    pattern = r"[A-Z]"
    my_list = []
    for match in re.finditer(pattern, text):
        found_letters = match.group()
        my_list.append(found_letters)
    return my_list


print(find_capital_letters("Tomato AppLE cat Dog HoMe"))
