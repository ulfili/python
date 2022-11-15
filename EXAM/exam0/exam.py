"""EXAM."""
import re


def find_capital_letters(text: str) -> str:
    """Function that finds capital letters."""
    pattern = r"[A-Z]"
    capital_letters = ""
    for match in re.finditer(pattern, text):
        capital_letters += match.group()
    return capital_letters


print(find_capital_letters("Tomato AppLE cat Dog HoMe"))


def close_far(a: int, b: int, c: int) -> bool:
    """Docstring."""
    if a - b <= 1:
        return True
    if a - c <= 1:
        return True
    else:
        return False


print(close_far(3, 1, 1))
