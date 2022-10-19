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


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """Return number of small fruit baskets if it's possible to finish the order, otherwise return -1."""
    five_kg = 5
    five_kg_baskets = ordered_amount // five_kg
    all_kg = (five_kg_baskets * 5) + (small_baskets * 1)
    print("5 kg: ", five_kg_baskets)
    if five_kg_baskets <= big_baskets:
        if all_kg == ordered_amount:
            return small_baskets
    if all_kg == ordered_amount:
        return small_baskets
    else:
        return -1


print(fruit_order(1, 5, 21))
print(fruit_order(4, 1, 9))
print(fruit_order(2, 2, 13))


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
