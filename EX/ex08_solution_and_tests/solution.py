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
    if five_kg_baskets == ordered_amount:
        return 0
    if ordered_amount == all_kg:
        return small_baskets
    if big_baskets == 0:
        if small_baskets > ordered_amount:
            return ordered_amount
    if all_kg != ordered_amount:
        return -1


print(fruit_order(3, 3, 15))
print(fruit_order(3, 1, 8))
print(fruit_order(10, 0, 9))
print(fruit_order(3, 15, 10))
