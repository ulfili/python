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
    if len(str(n)) < 4:
        return str(n)
    else:
        return add_commas(str(n)[:-3]) + ',' + str(n)[-3:]


print(add_commas(1245))
print(add_commas(103))


def sum_digits_recursive(number: int) -> int:
    """Return the sum of the digits in number."""
    if number <= 0:
        return number
    else:
        return int(number % 10) + sum_digits_recursive(number // 10)


print(sum_digits_recursive(10000))
print(sum_digits_recursive(123))


def pair_star_recursive(word: str) -> str:
    """Add star between identical adjacent chars."""
    if len(word) <= 1:
        return word
    first_char = word[0]
    rest_chars = word[1:]
    if first_char == rest_chars[0]:
        return first_char + "*" + pair_star_recursive(rest_chars)
    else:
        return first_char + pair_star_recursive(rest_chars)


print(pair_star_recursive("hello"))
print(pair_star_recursive("aaab"))
print(pair_star_recursive("***"))


def stonks(coins: float, rate: float, years: int) -> int:
    """Each year your crypto-investment grows."""
    new_coins = coins * (1 + (rate / 100.0))
    if years <= 1:
        return int(new_coins)
    else:
        return stonks(new_coins, rate, years - 1)


print(stonks(1000, 10, 10)) # 2593
print(stonks(100000, 12, 3)) # 140492


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
