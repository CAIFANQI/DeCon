

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k - 1):
            if k % i == 0:
                return False
        return True
    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(n):
            largest = max(largest, j)
    return largest
assert largest_prime_factor(4) == 2
assert 	largest_prime_factor(13195 * 2) == 29
assert 	largest_prime_factor(13195 * 3) == 29
assert 	largest_prime_factor(3) == 3
assert 	largest_prime_factor(7) == 7
assert 	largest_prime_factor(13) == 13
assert 	largest_prime_factor(17) == 17
assert 	largest_prime_factor(11) == 11
assert 	largest_prime_factor(2) == 2, "error"
assert 	largest_prime_factor(4) == 2, "error"
assert 	largest_prime_factor(11) == 11, "error"
assert 	largest_prime_factor(29) == 29, "error"
assert 	largest_prime_factor(37) == 37, "error"
assert 	largest_prime_factor(101) == 101, "error"
assert 	largest_prime_factor(110) == 11, "error"
