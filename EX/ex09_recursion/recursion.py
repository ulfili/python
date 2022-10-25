"""If you're going to perform recursion, you need to use recursion."""


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


def add_commas(n: int):
    """Add comas into a number."""
    return "{:,}".format(n)


def sum_digits_recursive(number: int) -> int:
    """
    Return the sum of the digits in number.

    Given a non-negative int n, return the sum of its digits recursively (no loops).

    sum_digits_recursive(123) => 6
    sum_digits_recursive(1) => 1
    sum_digits_recursive(0) => 0
    sum_digits_recursive(999) => 27

    Hint: turn the number into string and take one digit at a time.

    :param number: non-negative number
    :return: sum of digits in the number
    """
    pass


def pair_star_recursive(s: str) -> str:
    """
    Add star between identical adjacent chars.

    Given a string, compute recursively a new string
    where identical chars that are adjacent in the original string
    are separated from each other by a "*".

    pair_star_recursive("abc") => "abc"
    pair_star_recursive("aa") => "a*a"
    pair_star_recursive("aaa") => "a*a*a"
    pair_star_recursive("") => ""

    :param s: input string
    :return: string with stars between identical chars.
    """
    pass


def stonks(coins: float, rate: float, years: int) -> int:
    """
    Each year your crypto-investment grows.

    Write a recursive function that calculates the net worth of coins after some years.
    Rate is in percents.
    Round the answer down to the nearest integer.

    stonks(1000, 10, 10) -> 2593
    stonks(100000, 12, 3) -> 140492

    :param coins: starting amount (0-10000)
    :param rate: rate percentage (0-100)
    :param years: number of years (0-50)
    :return: coins after years
    """
    pass


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
    pass