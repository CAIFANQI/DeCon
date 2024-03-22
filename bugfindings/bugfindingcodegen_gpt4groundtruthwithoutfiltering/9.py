from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    running_max = None
    result = []

    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(numbers)

        result.append(running_max)

    return result
assert 	rolling_max([3, 2, 1]) == [3, 3, 3]
assert 	rolling_max([4, 3, 2, 1]) == [4, 4, 4, 4]
assert 	rolling_max([6, 5, 4, 3, 2, 1]) == [6, 6, 6, 6, 6, 6]
assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert rolling_max([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert rolling_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert rolling_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
assert rolling_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30]
assert rolling_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50]
assert rolling_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70]
assert 	rolling_max([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert rolling_max([1, 2, 3, 4]) == [1, 2, 3, 4]
assert rolling_max([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
assert rolling_max([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
assert rolling_max([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
assert rolling_max([1, 2, 3]) == [1, 2, 3]
assert 	rolling_max([1, 1, 1]) == [1, 1, 1]
assert 	rolling_max([1]) == [1]
assert 	rolling_max([]) == []
assert rolling_max([2, 4, 6, 8]) == [2, 4, 6, 8]
assert rolling_max([2, 3, 4, 6, 7]) == [2, 3, 4, 6, 7]
assert rolling_max([2, 3, 4, 6, 7, 7, 7, 7, 7]) == [2, 3, 4, 6, 7, 7, 7, 7, 7]
assert rolling_max([2, 3, 4, 6, 7, 7, 7, 8]) == [2, 3, 4, 6, 7, 7, 7, 8]
assert 	rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "wrong result"
assert 	rolling_max([2, 3, 4, 5, 6]) == [2, 3, 4, 5, 6], "wrong result"
assert 	rolling_max([7, 7, 7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7, 7, 7], "wrong result"
assert 	rolling_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "wrong result"
assert 	rolling_max([]) == [], "wrong result"
assert 	rolling_max([1]) == [1], "wrong result"
assert 	rolling_max([1, 2]) == [1, 2], "wrong result"
assert 	rolling_max([1, 2, 3]) == [1, 2, 3], "wrong result"
assert rolling_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
