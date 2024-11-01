

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in reversed(range(n)):
        if n - i == 0:
            return i
assert largest_divisor(25) == 5
assert largest_divisor(30) == 15
assert largest_divisor(49) == 7
assert largest_divisor(2) == 1
assert largest_divisor(3) == 1
assert largest_divisor(4) == 2
assert largest_divisor(5) == 1
assert largest_divisor(9) == 3
assert largest_divisor(14) == 7
