"""TK1."""


def format_time(min: int) -> str:
    hour = min // 60
    minut = min % 60
    if min % 60 == 0:
        return hour
    if min % 60 != 0:
        if min < 60:
            return min
        if min > 60:
            answ = min - minut
            answ_2 = answ // 60
            return answ_2, minut


print(format_time(125))


def caught_speeding(num: int, birthday: bool):
    if birthday is True:
        num = num * 5
    if num < 60:
        return 0
    if num > 80:
        return 2
    if num:
        for i in range(61, 81):
            return 1


print(caught_speeding(5, True))
