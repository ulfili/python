"""Solution and test."""


def lottery(a: int, b: int, c: int) -> int:
    """Return Lottery victory result 10, 5, 1, or 0 according to input values."""
    if a == b == c == 5:
        return 10
    if a == b == c != 5:
        return 5
    if a != b and a != c:
        return 1
    else:
        return 0


print(lottery(5, 1, 5))


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """Return number of small fruit baskets if it's possible to finish the order, otherwise return -1."""
    five_kg_baskets = big_baskets * 5
    one_kg_baskets = small_baskets * 1
    all_kg = five_kg_baskets + one_kg_baskets
    print(all_kg)
    if five_kg_baskets == ordered_amount:
        return 0
    if ordered_amount == all_kg:
        return small_baskets
    if big_baskets == 0:
        if small_baskets > ordered_amount:
            return ordered_amount
    if all_kg != ordered_amount:
        return -1


print(fruit_order(1, 5, 21))


def students_study(time: int, coffee_needed: bool) -> bool:
    """Return True if students study in given circumstances."""
    if 5 <= time <= 17:
        if coffee_needed is True:
            return True
        else:
            return False
    else:
        if coffee_needed is True:
            return False
        else:
            return True


print(students_study(17, False))
print(students_study(18, True))
print(students_study(19, False))
print(students_study(1, True))
