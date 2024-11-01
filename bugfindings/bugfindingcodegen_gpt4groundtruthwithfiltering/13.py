

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return b
assert greatest_common_divisor(15, 15) == 15
assert greatest_common_divisor(1, 4) == 1
assert greatest_common_divisor(2, 4) == 2
assert greatest_common_divisor(2, 6) == 2
assert greatest_common_divisor(3, 10) == 1
assert greatest_common_divisor(10, 6) == 2
assert greatest_common_divisor(6, 10) == 2
assert greatest_common_divisor(25, 5) == 5
assert greatest_common_divisor(9, 15) == 3
assert greatest_common_divisor(10, 10) == 10
assert greatest_common_divisor(12, 16) == 4
assert greatest_common_divisor(10, 5) == 5
assert greatest_common_divisor(8, 2) == 2
assert greatest_common_divisor(1, 1) == 1
assert greatest_common_divisor(1, 0) == 1
assert greatest_common_divisor(10, 3) == 1
assert greatest_common_divisor(9, 6) == 3
assert 1 == greatest_common_divisor(1, 1)
