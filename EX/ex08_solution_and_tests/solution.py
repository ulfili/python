"""Solution and test."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """Return True if students study in given circumstances."""
    if 18 <= time <= 24:
        return True
    if 5 <= time <= 17:
        return coffee_needed
    else:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """Return Lottery victory result 10, 5, 1, or 0 according to input values."""
    if a == b == c == 5:
        return 10
    if a == b == c != 5:
        return 5
    if b == c != a:
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
        if five_kg_baskets * 5 == ordered_amount:
            return 0
        else:
            return -1
    if all_kg == ordered_amount:
        return small_baskets
    if big_baskets == 0:
        if small_baskets >= ordered_amount:
            return ordered_amount
        else:
            return -1
    else:
        return -1
