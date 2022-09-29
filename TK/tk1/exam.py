"""TK1."""


def format_time(min: int) -> str:
    """Given minutes as an int, return correctly formatted time in hours and minutes."""
    hour = min // 60
    minut = min % 60
    if min % 60 == 0:
        if min == 0:
            return str(min) + "min"
        return str(hour)+"h"
    if min % 60 != 0:
        if min < 60:
            return str(min) + "min"
        if min > 60:
            answ = min - minut
            answ_2 = answ // 60
            return str(answ_2) + "h " + str(minut) + "min"


print(format_time(0))


def caught_speeding(num: int, birthday: bool):
    """Return which category speeding ticket you would get."""
    if birthday:
        num = num + 5
    if num < 60:
        return 0
    if num > 80:
        return 2
    if num:
        for i in range(61, 81):
            return 1


print(caught_speeding(5, True))


def first_half(word: str):
    """Return the first half of an string."""
    if len(word) % 2 == 0:
        return word[:len(word)//2]


print(first_half("kiki"))
