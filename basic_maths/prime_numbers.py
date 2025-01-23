"""The number which has two factors one and itself known as prime numbers. This also tells that "1" is not a prime number."""

def check_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(check_prime(91))  # Output: False
