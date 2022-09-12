"""Prime number identifier."""


def is_prime_number(a: int) -> bool:          # find a prime number
    if a == 0:
        return False                          # system says that 1 and 0 are not prime numbers
    if a == 1:
        return False
    if a == 2:                                # system says that 2 is a prime number
        return True
    for i in range(2, a + 1):
        if a % i == 0:                        # kui jagamisel ei tekki jääki siis arv ei ole algarv
            return False
        if a % i != 0:
            return True                       # kui jagamisel tekkib jääk siis number on algarv


print(is_prime_number(17))
