

def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return sum(range(n))
assert sum_to_n(1) == 1
assert sum_to_n(2) == 3
assert sum_to_n(3) == 6
assert sum_to_n(4) == 10
assert sum_to_n(5) == 15
assert sum_to_n(6) == 21
assert sum_to_n(7) == 28
assert sum_to_n(8) == 36
assert sum_to_n(9) == 45
assert sum_to_n(10) == 55
assert sum_to_n(11) == 66
assert sum_to_n(12) == 78
assert sum_to_n(13) == 91
assert sum_to_n(14) == 105
assert sum_to_n(15) == 120
assert sum_to_n(16) == 136
assert sum_to_n(17) == 153
assert sum_to_n(18) == 171
assert sum_to_n(19) == 190
assert sum_to_n(20) == 210
assert sum_to_n(100) == 5050
assert sum_to_n(1000) == 500500#
