"""If you're going to perform recursion, you need to use recursion."""
from math import floor


def loop_reverse(s: str) -> str:
    """Reverse a string."""
    reversed_string = ""
    for i in s:
        reversed_string = i + reversed_string
    return reversed_string


def recursive_reverse(s: str) -> str:
    """Reverse a string using recursion."""
    if len(s) == 0:
        return s
    else:
        return recursive_reverse(s[1:]) + s[0]


def loop_sum(n: int) -> int:
    """Sum of numbers using loop."""
    num = 0
    for i in range(1, n + 1):
        num = i + num
    return num


def recursive_sum(n: int) -> int:
    """Sum of numbers using recursion."""
    if n == 0:
        return n
    return n + recursive_sum(n - 1)


def countdown(n: int):
    """Make list of numbers from n to 0."""
    if n < 0:
        return []
    else:
        return [n] + countdown(n - 1)


def add_commas(n: str):
    """Add comas into a number."""
    if len(n) < 3:
        return n
    else:
        return add_commas(n[:-3]) + ',' + n[-3:]


print(add_commas("1245"))


def sum_digits_recursive(number: int) -> int:
    """Return the sum of the digits in number."""
    if number <= 0:
        return number
    else:
        return int(number % 10) + sum_digits_recursive(int(number / 10))


print("sum of digits is:")
print(sum_digits_recursive(10000))


def pair_star_recursive(word: str, number: int) -> str:
    """Add star between identical adjacent chars."""
    lenght = len(word)
    if number == lenght or number == lenght - 1:
        return word[number]
    if word[number] == word[number + 1]:
        return word[number] + "*" + pair_star_recursive(word, number + 1)
    else:
        return word[number] + pair_star_recursive(word, number + 1)


print(pair_star_recursive("hello", 0))


def stonks(coins: float, rate: float, years: int) -> int:
    """Each year your crypto-investment grows."""
    protsent = coins * (rate / 100)
    new_coins = coins + protsent
    if years <= 1:
        return floor(new_coins)
    else:
        return stonks(new_coins, rate, years - 1)


print(stonks(100000, 12, 3))
print(stonks(1000, 10, 10))


def quic_mafs(a: int, b: int) -> list:
    """
    Write a recursive function that applies the following operations.

    i) If a = 0 or b = 0, return [a,b]. Otherwise, go to step (ii);
    ii) If a >= 2*b, set a = a - 2*b, and repeat step (i). Otherwise, go to step (iii);
    iii) If b >= 2*a, set b = b - 2*a, and repeat step (i). Otherwise, return [a,b].

    quic_mafs(6, 19) -> [6, 7]
    quic_mafs(2, 1) -> [0, 1]
    quic_mafs(22, 5) -> [0, 1]
    quic_mafs(8796203,7556) -> [1019,1442]

    :param a: int
    :param b: int
    :return: result
    """
    # print("Function quack_mafs called, a is ", a, " b is ", b)
    if a == 0 or b == 0:
        return [a, b]
    if a >= 2 * b:
        a = a - 2 * b
        return quic_mafs(a, b)
    else:
        if b < 2 * a:
            return [a, b]
        b = b - 2 * a
        return quic_mafs(a, b)
