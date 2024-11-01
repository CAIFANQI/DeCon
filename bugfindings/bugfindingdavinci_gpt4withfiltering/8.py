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
assert sum_product([1, 2, 3, 4, 5, 6]) == (21, 720)
assert sum_product([0, 1, 2, 3, 4, 5]) == (15, 0)
assert sum_product([]) == (0, 1)
assert sum_product([99]) == (99, 99)
assert sum_product([0, 0, 0, 0, 0]) == (0, 0)
assert sum_product([1, 2, 3, 4, 5, 6, 0]) == (21, 0)
assert sum_product([1, 2, 3, 4, 5, -6]) == (9, -720)
assert sum_product([5, 6, 7, 8, 9, 10]) == (45, 151200)
assert sum_product([0]) == (0, 0)
assert sum_product([1, -1, 1, -1]) == (0, 1)
assert sum_product([1, 2, 3]) == (6, 6)
assert sum_product([1, 2, 3, 4]) == (10, 24)
assert sum_product([-1, -2, -3, -4, -5, -6]) == (-21, 720)
assert sum_product([2, 3, 5, -1]) == (9, -30)
assert sum_product([0, 2, 3]) == (5, 0)
assert sum_product([-1, -2, -3]) == (-6, -6)
assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (55, 3628800)
assert sum_product([1, 2, 0]) == (3, 0)
assert sum_product([10, 3, 7, 0]) == (20, 0)
assert sum_product([0, 2, 3, 5, 7, 11]) == (28, 0)
assert sum_product([0, -1, 1]) == (0, 0)
assert sum_product([3]) == (3, 3)
assert sum_product([-1, -1, -1]) == (-3, -1)
assert sum_product([5, 5, 0, 10]) == (20, 0)
assert sum_product([13]) == (13, 13)
assert sum_product([1, 2, 3, 0]) == (6, 0)
assert sum_product([0, 0, 0, 0]) == (0, 0)
assert sum_product([1, 2]) == (3, 2)
assert sum_product([0, 1, 0]) == (1, 0)
assert sum_product([1, 3, 5, 7, 9]) == (25, 945)
assert sum_product([5, 3, 2, 6]) == (16, 180)
assert sum_product([2, 2, 2, 2, 2, 2]) == (12, 64)
assert sum_product([1, 2, 3, -2]) == (4, -12)
assert sum_product([2, 3, 4, -1]) == (8, -24)
assert sum_product([1, -1]) == (0, -1)
assert sum_product([5, 6, 7]) == (18, 210)
assert sum_product([10]) == (10, 10)
assert sum_product([100]) == (100, 100)
assert sum_product([1, 1, 1, 1, 1, 1]) == (6, 1)
assert sum_product([4, 5, 5]) == (14, 100)
assert sum_product([5]) == (5, 5)
assert sum_product([0, 1, -1, 100]) == (100, 0)
assert sum_product([0, 1, -1]) == (0, 0)
assert sum_product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (55, 0)
assert sum_product([0, 0, 0]) == (0, 0)
assert sum_product([-1, -2, -3, -4]) == (-10, 24)
assert sum_product([1, 0, 1, 0, 1, 0]) == (3, 0)
assert sum_product([1, 2, 3, 4, 5]) == (15, 120)
assert sum_product([2, 2, -1]) == (3, -4), "Sum and product of [-1, 2, 2] should be (3, -4)"
assert sum_product([1, 2, 3, 4, 5, 6]) == (21, 720), "Sum and product of [1, 2, 3, 4, 5, 6] should be (21, 720)"
assert sum_product([-1, 2, 3]) == (4, -6)
assert sum_product([1, 1, 1, 1, 1]) == (5, 1)
assert sum_product([3, 5, 7]) == (15, 105)
assert sum_product([-1, -2, -3, 0]) == (-6, 0)
assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == (210, 2432902008176640000)
assert sum_product([-99]) == (-99, -99)
assert sum_product([-99, 0, 99]) == (0, 0)
assert sum_product([0, 1, 2, 3]) == (6, 0)
assert sum_product([0, 0, 0, 0, 0, 0]) == (0, 0)
assert sum_product([1]) == (1, 1)
assert sum_product([1, 0, 3]) == (4, 0)
assert sum_product([0, 1, -1, 0]) == (0, 0)
assert sum_product([0, 1, 2, 3, 4]) == (10, 0)
assert sum_product([1, 5, 7]) == (13, 35)
assert sum_product([-3, 0, 3]) == (0, 0)
assert sum_product([3, 2, 5]) == (10, 30)
