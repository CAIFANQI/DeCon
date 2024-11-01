from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    sum_value = 0
    prod_value = 0

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value
assert sum_product([1, 2, 3]) == (6, 6)
assert sum_product([-1, -2, -3]) == (-6, -6)
assert sum_product([]) == (0, 1)
assert sum_product([5]) == (5, 5)
assert sum_product([0, 0, 0]) == (0, 0)
assert sum_product([1, 2, 3, 4]) == (10, 24)
assert sum_product([0, 1, 2, 3, 4]) == (10, 0)
assert sum_product([-1, 0, 1]) == (0, 0)
assert sum_product([-1, -2, -3, -4, -5]) == (-15, -120)
assert sum_product([0, 1, 2, 3, 4, 5]) == (15, 0)
assert sum_product([1, 2, 3, 4, 5]) == (15, 120), "Test case 2 failed"
assert sum_product([-1, -2, -3, -4, -5]) == (-15, -120), "Test case 3 failed"
assert sum_product([0, 1, 2, 3, 4, 5]) == (15, 0), "Test case 4 failed"
assert sum_product([2, 3, 4]) == (9, 24), "Test case 5 failed"
assert sum_product([1, 2, 3, 4, 5]) == (15, 120)
assert sum_product([1, 2, 3, 0, 4, 5]) == (15, 0)
assert sum_product([1]) == (1, 1)
assert sum_product([-1]) == (-1, -1)
assert sum_product([0]) == (0, 0)
assert sum_product([-1, -2, -3, -4]) == (-10, 24)
assert sum_product([4, 5, 6]) == (15, 120)
assert sum_product([10, 20, 30]) == (60, 6000)
assert sum_product([-1, -2, -3]) == (-6, -6), 'Test Case 2 Failed'
assert sum_product([0, 1, 2, 3]) == (6, 0), 'Test Case 3 Failed'
assert sum_product([]) == (0, 1), 'Test Case 4 Failed'
assert sum_product([0, 1, 2, 3]) == (6, 0)
assert sum_product([1, 2, 3, 0, 4]) == (10, 0)
assert sum_product([-1, -2, -3, 0, -4]) == (-10, 0)
assert sum_product([-1, -2, -3]) == (-6, -6), "Test case 2 failed"
assert sum_product([0, 1, 2]) == (3, 0), "Test case 3 failed"
assert sum_product([]) == (0, 1), "Test case 4 failed"
assert sum_product([7]) == (7, 7)
assert sum_product([2, 3, 4, 5]) == (14, 120)
assert sum_product([4, 5, 6]) == (15, 120), "Test case 2 failed"
assert sum_product([]) == (0, 1), "Test case 3 failed"
assert sum_product([0, 1, 2]) == (3, 0)
assert sum_product([0, 1, 2, 3, 4]) == (10, 0), 'Test Case 3 Failed'
assert sum_product([-1, 0, 1]) == (0, 0), 'Test Case 5 Failed'
assert sum_product([4, 5, 6]) == (15, 120), 'Test Case 2 Failed'
assert sum_product([]) == (0, 1), 'Test Case 3 Failed'
assert sum_product([-1, -2, -3]) == (-6, -6), 'Test Case 4 Failed'
assert sum_product([0, 1, 2, 3]) == (6, 0), 'Test Case 5 Failed'
assert sum_product([-1, 2, -3]) == (-2, 6)
assert sum_product([2, 4, 6]) == (12, 48)
assert sum_product([2, 2, 2, 2, 2]) == (10, 32)
assert sum_product([2, 2, 2, 2]) == (8, 16)
assert sum_product([0, 0, 0, 0]) == (0, 0)
assert sum_product([-1, -2, 0, 3]) == (0, 0)
assert sum_product([2]) == (2, 2)
assert sum_product([-2]) == (-2, -2)
assert sum_product([2, 4, 6, 8]) == (20, 384)
assert sum_product([2]) == (2, 2), "Test case 5 failed"
assert sum_product([1, 2, 3, 0]) == (6, 0)
assert sum_product([1, 2, 3, -4]) == (2, -24)
assert sum_product([-1, 0, 1, 2, 3, 4]) == (9, 0)
assert sum_product([1, -2, 3, -4]) == (-2, 24)
assert sum_product([-1, 2, -3, 4]) == (2, 24)
assert sum_product([1, 2, 3, 4]) == (10, 24), 'Test Case 2 Failed'
assert sum_product([0, 1, 2, 3, 4]) == (10, 0), 'Test Case 4 Failed'
assert sum_product([1, 2, 3, 0, 4]) == (10, 0), 'Test Case 5 Failed'
assert sum_product([2, 3, 5, 7, 11]) == (28, 2310)
