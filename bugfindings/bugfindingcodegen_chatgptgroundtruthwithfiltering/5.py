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
assert intersperse([], 3) == []
assert intersperse([], 5) == []
assert intersperse([], 100) == []
assert intersperse(numbers=[], delimeter=3) == []
assert intersperse(numbers=[1, 2, 3, 4], delimeter=0) == [1, 0, 2, 0, 3, 0, 4]
assert intersperse([], 0) == []
assert intersperse([1], 2) == [1]
assert intersperse([1], 0) == [1]
