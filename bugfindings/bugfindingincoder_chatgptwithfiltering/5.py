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
assert intersperse([1,2,3,4,5], 7) == [1,7,2,7,3,7,4,7,5]
assert intersperse([], 5) == []
assert intersperse([4], 2) == [4]
assert intersperse([5], 1) == [5]
