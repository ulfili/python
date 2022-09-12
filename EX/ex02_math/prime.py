"""Prime number identifier."""


def is_prime_number(a: int) -> bool:          # find a prime number
    """
    Check if the number is a prime number.

    Prime number is a natural number which is only divisible by 1 and itself. 0 and 1 are not prime numbers.

    Conditions:
    1. If number is a prime number then return boolean True
    2. If number is not a prime number then return boolean False

    :param a: the number to check.
    :return: boolean True if number is a prime number or False if number is not a prime number.
    """
    print("number to test is:", a)
    if a == 0:
        return False                          # system says that 1 and 0 are not prime numbers
    if a == 1:
        return False
    if a == 2:                                # system says that 2 is a prime number
        print("2, 1 and 0 test")
        return True
    for i in range(2, a):
        print(f"{i} test ")
        if a % i == 0:                        # kui jagamisel ei tekki jääki siis arv ei ole algarv
            print(f"{a} div {i} positive, we return false")
            return False
    return True


print(is_prime_number(1))
print(is_prime_number(2))
print(is_prime_number(3))
print(is_prime_number(4))
print(is_prime_number(5))
print(is_prime_number(6))
print(is_prime_number(7))
print(is_prime_number(9))
print(is_prime_number(13))
print(is_prime_number(15))
print(is_prime_number(17))
