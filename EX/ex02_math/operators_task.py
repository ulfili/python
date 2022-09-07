"""Math operators."""
import math                                   # open math modul


def add(x: int, y: int):
    return x + y


print(add(1, 2))


def sub(x: int, y: int):
    return x - y


print(sub(1, 2))


def multiply(x: int, y: int):
    return x * y


print(multiply(1, 2))


def div(x: int, y: int):
    return x / y


print(div(1, 2))


def modulus(x: int, y: int):
    return x % y


print(modulus(1, 2))


def floor_div(x: int, y: int):
    return x // y


print(floor_div(1, 2))


def exponent(x: int, y: int):
    return math.pow(x, y)


print(math.pow(2, 3))


def first_greater_or_equal(x: int, y: int):
    return x >= y


print(first_greater_or_equal(4, 3))


def second_less_or_equal(x: int, y: int):
    return y <= x


print(second_less_or_equal(4, 3))


def x_is_y(x: int, y: int):
    return x == y


print(x_is_y(2, 2))


def x_is_not_y(x: int, y: int):
    return x != y


print(x_is_not_y(2,4))


def if_else(a: int, b: int, c: int, d: int):
    mult = a * b
    div = c / d
    if mult == div:
        return 0
    if mult > div:
        return mult
    return div


print(if_else(2, 2, 8, 2))
print(if_else(8, 4, 2, 1))
print(if_else(1,1,9,3))

