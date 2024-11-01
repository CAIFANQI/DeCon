from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    return result
assert intersperse(numbers=[1, 2, 3, 4], delimeter=0) == [1, 0, 2, 0, 3, 0, 4]
assert intersperse([1], 2) == [1]
assert intersperse([1], 0) == [1]
assert 	intersperse([1, 2, 3, 4, 5], 1) == [1, 1, 2, 1, 3, 1, 4, 1, 5]
