"""EXAM."""
import re


def find_capital_letters(text: str) -> str:
    pattern = r"[A-Z]"
    capital_letters = ""
    for match in re.finditer(pattern, text):
        capital_letters += match.group()
    return capital_letters


print(find_capital_letters("Tomato AppLE cat Dog HoMe"))
