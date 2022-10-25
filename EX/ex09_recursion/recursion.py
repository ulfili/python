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
