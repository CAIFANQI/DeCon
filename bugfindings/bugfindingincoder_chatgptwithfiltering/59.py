

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
assert largest_prime_factor(12) == 3
assert largest_prime_factor(2) == 2
assert largest_prime_factor(3) == 3
assert largest_prime_factor(5) == 5
assert largest_prime_factor(6) == 3
assert largest_prime_factor(11) == 11
assert largest_prime_factor(13) == 13
assert largest_prime_factor(17) == 17
assert largest_prime_factor(7) == 7
assert largest_prime_factor(9) == 3
assert largest_prime_factor(18) == 3
assert largest_prime_factor(23) == 23
assert largest_prime_factor(24) == 3
assert largest_prime_factor(29) == 29
assert largest_prime_factor(31) == 31
assert largest_prime_factor(8) == 2
assert largest_prime_factor(32) == 2
assert largest_prime_factor(48) == 3
assert largest_prime_factor(21) == 7
assert largest_prime_factor(200) == 5
assert largest_prime_factor(250) == 5
assert largest_prime_factor(3) == 3 # 3 is a prime factor
assert largest_prime_factor(4) == 2 # 4 is a prime factor
assert largest_prime_factor(5) == 5 # 5 is not a prime factor
assert largest_prime_factor(20) == 5 # 20 is a prime factor
assert largest_prime_factor(16) == 2
assert largest_prime_factor(25) == 5
assert largest_prime_factor(4) == 2
assert largest_prime_factor(10) == 5
assert largest_prime_factor(50) == 5
assert largest_prime_factor(20) == 5
assert largest_prime_factor(15) == 5
assert largest_prime_factor(36) == 3
assert largest_prime_factor(99) == 11
assert largest_prime_factor(28) == 7
assert largest_prime_factor(19) == 19
assert largest_prime_factor(54) == 3
assert largest_prime_factor(100) == 5
assert largest_prime_factor(1000) == 5
assert largest_prime_factor(14) == 7
assert largest_prime_factor(3) == 3 
assert largest_prime_factor(9) == 3 
assert largest_prime_factor(49) == 7 
assert largest_prime_factor(27) == 3
assert largest_prime_factor(105) == 7
assert largest_prime_factor(64) == 2
assert largest_prime_factor(700) == 7
assert largest_prime_factor(500) == 5
assert largest_prime_factor(101) == 101
assert largest_prime_factor(49) == 7
assert largest_prime_factor(729) == 3
