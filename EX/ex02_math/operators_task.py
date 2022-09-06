"""Math operators."""

def add(x: int, y: int) -> int:
    return x + y
def sub(x: int, y: int) -> int:
    return x - y
def multiply(x: int, y: int) -> int:
    return x * y
def div(x: int, y: int) -> int:
    return x / y
def modulus(x: int, y: int) -> int:
    return x % y
def floor_div(x: int, y: int) -> int:
    return x // y
def exponent(x: int, y: int) -> int:
    return math.pow(x, y)
def first_greater_or_equal(x: int, y: int) -> int:



if __name__ == '__main__':
    print(add(1, 2))
    print(sub(1, 2))
    print(multiply(1, 2))
    print(div(1, 2))
    print(modulus(1, 2))
    print(floor_div(1, 2))
    import math
    print(math.pow(2, 3))

