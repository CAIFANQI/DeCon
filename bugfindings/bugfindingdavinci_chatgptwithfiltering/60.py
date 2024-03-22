

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
assert sum_to_n(10) == 55
assert sum_to_n(100) == 5050
assert 5050 == sum_to_n(100)
assert sum_to_n(3) == 6
assert sum_to_n(4) == 10
assert sum_to_n(5) == 15
assert sum_to_n(200) == 20100
assert sum_to_n(0) == 0
assert 0 == sum_to_n(0)
assert sum_to_n(1000) == 500500
assert sum_to_n(-1) == 0
assert 55 == sum_to_n(10)
assert sum_to_n(11) == 66
assert sum_to_n(13) == 91
