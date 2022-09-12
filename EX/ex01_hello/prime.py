"""Prime number identifier."""

def is_prime_number(k: int) -> bool:     # find prime nuber
    for i in range(2, k + 1):
        if k % i == 0:
            return False
        if k % i >= 0:
            return True


print(is_prime_number(5))
