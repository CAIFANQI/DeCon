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
assert rolling_max([1, 2, 3, 4]) == [1, 2, 3, 4]
assert rolling_max([2, 3, 4, 5]) == [2, 3, 4, 5]
assert rolling_max([3, 4, 5]) == [3, 4, 5]
assert rolling_max([4, 5, 6]) == [4, 5, 6]
assert rolling_max([6, 7, 8]) == [6, 7, 8]
assert rolling_max([7, 8, 9]) == [7, 8, 9]
assert rolling_max([8, 9, 10]) == [8, 9, 10]
assert rolling_max([9, 10, 11]) == [9, 10, 11]
assert rolling_max([10, 11, 12]) == [10, 11, 12]
assert rolling_max([11, 12, 13]) == [11, 12, 13]
assert rolling_max([12, 13, 14]) == [12, 13, 14]
assert rolling_max([13, 14, 15]) == [13, 14, 15]
assert rolling_max([14, 15, 16]) == [14, 15, 16]
assert rolling_max([15, 16, 17]) == [15, 16, 17]
assert rolling_max([16, 17, 18]) == [16, 17, 18]
assert rolling_max([17, 18, 19]) == [17, 18, 19]
assert rolling_max([18, 19, 20]) == [18, 19, 20]
assert rolling_max([19, 20, 21]) == [19, 20, 21]
assert rolling_max([20, 21, 22]) == [20, 21, 22]
assert rolling_max([21, 22, 23]) == [21, 22, 23]
assert rolling_max([22, 23, 24]) == [22, 23, 24]
assert rolling_max([10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert rolling_max([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
assert rolling_max([]) == []
assert rolling_max([1, 2, 3]) == [1, 2, 3]
assert rolling_max([-2, -1, 0, 1, 2]) == [-2, -1, 0, 1, 2]
assert rolling_max([0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0]
assert rolling_max([1]) == [1]
assert rolling_max([0, 1, 2]) == [0, 1, 2]
assert rolling_max([-1]) == [-1]
assert rolling_max([5, 5, 5]) == [5, 5, 5]
assert rolling_max([7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7]
assert rolling_max([3, 5]) == [3, 5]
assert rolling_max([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]) == [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
assert rolling_max([3, 6, 8, 12, 13, 15, 16, 17, 18, 19]) == [3, 6, 8, 12, 13, 15, 16, 17, 18, 19]
assert rolling_max([1,2,3]) == [1,2,3]
assert rolling_max([5, 6, 7, 8, 9]) == [5, 6, 7, 8, 9]
assert rolling_max([10]) == [10]
assert rolling_max([3, 5, 5, 7]) == [3, 5, 5, 7]
assert rolling_max([4, 6, 8, 10]) == [4, 6, 8, 10]
assert rolling_max([3, 3, 5, 7]) == [3, 3, 5, 7]
assert rolling_max([-4, -2, -1, 0, 1, 2]) == [-4, -2, -1, 0, 1, 2]
