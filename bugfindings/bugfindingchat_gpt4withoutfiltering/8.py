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
assert sum_product([]) == (0, 1)
assert sum_product([]) == (0, 1), 'Test Case 4 Failed'
assert sum_product([]) == (0, 1), "Test case 4 failed"
assert sum_product([]) == (0, 1), "Test case 3 failed"
assert sum_product([]) == (0, 1), 'Test Case 3 Failed'
