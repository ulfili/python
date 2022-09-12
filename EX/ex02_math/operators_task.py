"""Math operators."""
import math                                                           # open math modul


def add(x: int, y: int):                                              # + action
    """Add x to y."""
    return x + y


def sub(x: int, y: int):                                              # - action
    """Subtract y from x."""
    return x - y


def multiply(x: int, y: int):              # * action
    """Multiply x by y."""
    return x * y


def div(x: int, y: int):                                              # / action
    """Divide x by y."""
    return x / y


def modulus(x: int, y: int):                                          # % action
    """Divide x by y and return remainder. Use an arithmetic operator."""
    return x % y


def floor_div(x: int, y: int):                                        # // action
    """Divide x by y and floor the value. Use an arithmetic operator."""
    return x // y


def exponent(x: int, y: int):                                         # exponent
    """Calculate x raised to the power of y."""
    return math.pow(x, y)


def first_greater_or_equal(x: int, y: int):                           # x is bigger or same as y
    """If x is greater or equal than y then return True. If not then return False."""
    return x >= y


def second_less_or_equal(x: int, y: int):                             # x is bigger or same as y
    """If y is less or equal than x then return True. If not then return False."""
    return y <= x


def x_is_y(x: int, y: int):                                           # x and y are the same
    """If x value is the same as y value then return True. If not then return False."""
    return x == y


def x_is_not_y(x: int, y: int):                                       # x is not y
    """If x value is not the same as y value then return True. If not then return False."""
    return x != y


def if_else(a: int, b: int, c: int, d: int):                          # if multiplied a and b is same as divided c and d then return 0
    """
    Create a program that has 4 numeric parameters.

    Multiply parameters 1-2 (multiply a by b) by each other and divide parameters 3-4 (divide c by d) by each other.
    Next check and return the greater value. If both values are the same then return 0 (number zero).
    """
    mult = a * b                                                      # or return bigger result
    div = c / d
    if mult == div:
        return 0
    if mult > div:
        return mult
    return div


def surface(a: int, b: int):                                          # find rectangle area
    """Add the missing parameters to calculate the surface of a rectangle. Calculate and return the value of the surface."""
    return a * b


def volume(aa: int, bb: int, cc: int):                                # find cuboid volume
    """Add the missing parameters to calculate the volume of a cubiod. Calculate and return the value of the volume."""
    return aa * bb * cc


def clock(day: int, hour: int, minut: int, sec: int) -> float:        # return the total amount of minutes
    """k."""
    day = day * 1440
    hour = hour * 60
    minut = minut
    sec = sec / 60
    return day + hour + minut + sec


def calculate(act: int, num_1: int, num_2: int):                      # calculate function
    """l."""
    if act == 0:
        return num_1 + num_2
    if act == 1:
        return num_1 - num_2
    if act == 2:
        return num_1 * num_2
    if act == 3:
        return num_1 / num_2


print(add(1, 2))
print(sub(1, 2))
print(multiply(1, 2))
print(div(1, 2))
print(modulus(1, 2))
print(floor_div(1, 2))
print(math.pow(2, 3))
print(first_greater_or_equal(4, 3))
print(second_less_or_equal(4, 3))
print(x_is_y(2, 2))
print(x_is_not_y(2, 4))
print(if_else(2, 2, 8, 2))
print(if_else(8, 4, 2, 1))
print(if_else(1, 1, 9, 3))
print(surface(2, 3))
print(volume(1, 2, 3))
print(clock(1, 1, 1, 60))
print(calculate(1, 5, 2))
