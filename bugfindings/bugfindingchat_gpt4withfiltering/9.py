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
assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]
assert rolling_max([1, 2, 3, 2, 1]) == [1, 2, 3, 3, 3]
assert rolling_max([3, 2, 1, 2, 3]) == [3, 3, 3, 3, 3]
assert rolling_max([1, 2, 3, 2, 3]) == [1, 2, 3, 3, 3]
assert rolling_max([3, 2, 3, 2, 1]) == [3, 3, 3, 3, 3]
assert rolling_max([1, 3, 2, 4, 5]) == [1, 3, 3, 4, 5]
assert rolling_max([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
assert rolling_max([1, 3, 2, 4, 5, 3, 2, 1]) == [1, 3, 3, 4, 5, 5, 5, 5]
assert rolling_max([10, 5, 20, 15, 25]) == [10, 10, 20, 20, 25]
assert rolling_max([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 9, 9, 9, 9, 9, 9, 9, 9]
assert rolling_max([1]) == [1]
assert rolling_max([]) == []
assert rolling_max([1, 3, 2, 4, 6, 5, 7, 9, 8, 10]) == [1, 3, 3, 4, 6, 6, 7, 9, 9, 10]
assert rolling_max([10, 8, 9, 7, 5, 6, 4, 2, 3, 1]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
assert rolling_max([2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2]
assert rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]
assert rolling_max([1, 2, 3, 4, 3, 2, 1]) == [1, 2, 3, 4, 4, 4, 4]
assert rolling_max([1, 2, 3, 2, 1, 2, 3, 4, 5]) == [1, 2, 3, 3, 3, 3, 3, 4, 5]
assert rolling_max([1, 2, 3, 1, 2, 3]) == [1, 2, 3, 3, 3, 3]
assert rolling_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert rolling_max([5, 4, 3, 5, 2]) == [5, 5, 5, 5, 5]
assert rolling_max([4, 3, 2, 1]) == [4, 4, 4, 4]
assert rolling_max([1, 3, 2, 4]) == [1, 3, 3, 4]
assert rolling_max([3, 2, 4, 1]) == [3, 3, 4, 4]
assert rolling_max([1, 1, 1, 1]) == [1, 1, 1, 1]
assert rolling_max([1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == [1, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4]
assert rolling_max([4, 3, 2, 1, 2, 3, 4]) == [4, 4, 4, 4, 4, 4, 4]
assert rolling_max([5, 4, 2, 3, 1]) == [5, 5, 5, 5, 5]
assert rolling_max([1, 2, 3, 4, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 5, 5, 5, 5]
assert rolling_max([5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
assert rolling_max([1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5]
assert rolling_max([1, 2, 3, 2, 3, 4, 5]) == [1, 2, 3, 3, 3, 4, 5]
assert rolling_max([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == [3, 3, 4, 4, 5, 9, 9, 9, 9, 9, 9, 9, 9, 9]
assert rolling_max([1, 3, 2, 4, 5, 7, 6, 8, 9, 10]) == [1, 3, 3, 4, 5, 7, 7, 8, 9, 10]
assert rolling_max([5, 4, 3, 4, 5]) == [5, 5, 5, 5, 5]
assert rolling_max([10, 5, 7, 8, 3, 9]) == [10, 10, 10, 10, 10, 10]
assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test case 2 failed"
assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5], "Test case 3 failed"
assert rolling_max([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1], "Test case 4 failed"
assert rolling_max([1, 2, 3, 2, 1]) == [1, 2, 3, 3, 3], "Test case 5 failed"
assert rolling_max([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]
assert rolling_max([10, 8, 6, 4, 2]) == [10, 10, 10, 10, 10]
assert rolling_max([1, 2, 3, 2, 3, 4, 5, 4, 3, 2, 1]) == [1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 5]
assert rolling_max([10, 5, 8, 9, 7, 6]) == [10, 10, 10, 10, 10, 10]
assert rolling_max([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
assert rolling_max([6, 5, 4, 3, 2, 1]) == [6, 6, 6, 6, 6, 6]
assert rolling_max([1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1]
assert rolling_max([9, 8, 7, 6, 5]) == [9, 9, 9, 9, 9]
assert rolling_max([5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == [5, 5, 5, 5, 5, 6, 7, 8, 9, 10]
assert rolling_max([10, 9, 8, 7, 6, 1, 2, 3, 4, 5]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
assert rolling_max([1, 2, 3, 2, 1, 4, 5, 6]) == [1, 2, 3, 3, 3, 4, 5, 6]
assert rolling_max([5, 4, 3, 2, 5]) == [5, 5, 5, 5, 5]
assert rolling_max([5, 4, 5, 4, 5]) == [5, 5, 5, 5, 5]
assert rolling_max([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [3, 3, 4, 4, 5, 9, 9, 9, 9, 9, 9]
assert rolling_max([1, 3, 5, 4, 2]) == [1, 3, 5, 5, 5]
assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5], 'Test Case 2 Failed'
assert rolling_max([1, 3, 5, 2, 4]) == [1, 3, 5, 5, 5], 'Test Case 3 Failed'
assert rolling_max([1, 2, 3, 4, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 5, 5, 5, 5], 'Test Case 4 Failed'
assert rolling_max([3, 2, 5, 4, 1, 2, 3, 4, 5]) == [3, 3, 5, 5, 5, 5, 5, 5, 5], 'Test Case 5 Failed'
assert rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5], 'Test Case 3 Failed'
assert rolling_max([1, 2, 3, 4, 3, 2, 1]) == [1, 2, 3, 4, 4, 4, 4], 'Test Case 4 Failed'
assert rolling_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'Test Case 5 Failed'
assert rolling_max([5, 3, 4, 2, 1]) == [5, 5, 5, 5, 5]
assert rolling_max([1, 3, 2, 4, 6, 5]) == [1, 3, 3, 4, 6, 6]
assert rolling_max([1, 2, 3, 3, 2, 1]) == [1, 2, 3, 3, 3, 3]
assert rolling_max([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
assert rolling_max([1, 3, 2, 5, 4, 6, 3, 2, 4, 1]) == [1, 3, 3, 5, 5, 6, 6, 6, 6, 6]
assert rolling_max([5, 4, 3, 2, 1, 6, 7, 8, 9]) == [5, 5, 5, 5, 5, 6, 7, 8, 9]
assert rolling_max([1, 2, 1, 2, 1]) == [1, 2, 2, 2, 2]
assert rolling_max([10, 5, 2, 7, 8, 9]) == [10, 10, 10, 10, 10, 10]
assert rolling_max([10, 5, 15, 20, 25]) == [10, 10, 15, 20, 25]
assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5], "Error: Test Case 2"
assert rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5], "Error: Test Case 3"
assert rolling_max([1, 2, 3, 4, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 5, 5, 5, 5], "Error: Test Case 4"
assert rolling_max([5, 4, 3, 2, 1, 2, 3, 4, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5], "Error: Test Case 5"
assert rolling_max([1, 2, 3, 4, 3]) == [1, 2, 3, 4, 4]
assert rolling_max([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert rolling_max([10, 9, 8, 7, 6]) == [10, 10, 10, 10, 10]
assert rolling_max([1, 3, 2, 4, 6, 5, 7, 9, 8]) == [1, 3, 3, 4, 6, 6, 7, 9, 9]
assert rolling_max([1, 2, 3, 4, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
assert rolling_max([3, 2, 1]) == [3, 3, 3]
assert rolling_max([5, 4, 3, 2, 1, 2, 3, 4, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5]
