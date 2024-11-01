from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / mean
assert mean_absolute_deviation([1, 1, 1, 1, 1]) == 0.0
assert mean_absolute_deviation([0, 0, 0, 0, 0]) == 0
assert mean_absolute_deviation([1, 1, 1, 1, 1]) == 0
assert mean_absolute_deviation([-1, -1, -1, -1, -1]) == 0
assert mean_absolute_deviation([1, 1, 1, 1, 1]) == 0, "Test case 4 failed"
assert mean_absolute_deviation([1, 1, 1, 1, 1]) == 0.0, "Test case 5 failed"
assert mean_absolute_deviation([5, 5, 5, 5, 5]) == 0.0
assert mean_absolute_deviation([-5, -5, -5, -5, -5]) == 0.0
assert mean_absolute_deviation([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0.0
assert mean_absolute_deviation([1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1.0
assert mean_absolute_deviation([1, 10]) == 4.5
assert mean_absolute_deviation([0, 0, 0, 0, 0]) == 0.0
assert mean_absolute_deviation([5, 5, 5, 5, 5]) == 0
assert mean_absolute_deviation([0, 0, 0, 0]) == 0.0
assert mean_absolute_deviation([1, 1, 1, 1, 1]) == 0, "Test case 3 failed"
assert mean_absolute_deviation([1]) == 0.0
assert mean_absolute_deviation([1, 1, 1, 1, 1]) == 0, "Test case 2 failed"
assert mean_absolute_deviation([5, 5, 5, 5, 5]) == 0, 'Test Case 4 Failed'
