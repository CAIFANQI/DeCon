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
assert mean_absolute_deviation([-1, 1, -1, 1]) == 1
assert round(mean_absolute_deviation([5, 5, 5, 5, 5]), 5) == 0
assert round(mean_absolute_deviation([-5, -5, -5, -5, -5]), 5) == 0
assert round(mean_absolute_deviation([1, 1, 1, 1, 1]), 5) == 0
assert mean_absolute_deviation([1, 1, 1, 1, 1]) == 0
assert mean_absolute_deviation([0, 0, 0, 0, 0]) == 0.0
assert mean_absolute_deviation([5, 5, 5]) == 0, "mean_absolute_deviation fails with [5, 5, 5]"
assert mean_absolute_deviation([-5, -5, -5]) == 0, "mean_absolute_deviation fails with [-5, -5, -5]"
assert mean_absolute_deviation([0, 0, 0]) == 0, "mean_absolute_deviation fails with [0, 0, 0]"
assert mean_absolute_deviation([0]) == 0.0
assert mean_absolute_deviation([1.1, 1.1, 1.1]) == 0.0
assert mean_absolute_deviation([0]) == 0
assert round(mean_absolute_deviation([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 2) == 0.00
assert mean_absolute_deviation([1.0, 2.0, 3.0, 3.0]) == 0.75
assert mean_absolute_deviation([1, 1, 1, 1, 1]) == 0.0
assert mean_absolute_deviation([2, 2, 2]) == 0
assert mean_absolute_deviation([1.5, 1.5, 1.5, 1.5, 1.5]) == 0.0, "Error: Mean Absolute Deviation"
assert mean_absolute_deviation([1, 3, 3, 1, 2]) == 0.8, "Error: Mean Absolute Deviation"
assert mean_absolute_deviation([-1, 0, 2, -1, 0]) == 0.8, "Error: Mean Absolute Deviation"
assert mean_absolute_deviation([-2, -4, -6, -8]) == 2.0
assert mean_absolute_deviation([2, -3, 5, -8]) == 4.5
assert mean_absolute_deviation([2]) == 0
assert abs(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-10
assert mean_absolute_deviation([-3, -3, -3, -3, -3]) == 0
assert mean_absolute_deviation([0.2, 0.2, 0.2, 0.2, 0.2]) == 0
assert mean_absolute_deviation([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1.0
assert mean_absolute_deviation([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, 0, 0]) == 0.8
assert mean_absolute_deviation([3.0, 1.0, 2.0]) == 0.6666666666666666
assert mean_absolute_deviation([1.0, 1.0, 1.0]) == 0.0
assert mean_absolute_deviation([100, 200, 600]) == 200
assert mean_absolute_deviation([-1.0, 1.0]) == 1.0
assert mean_absolute_deviation([0.0, 0.0, 0.0]) == 0.0
assert mean_absolute_deviation([42]) == 0
assert mean_absolute_deviation([3, 3, 3]) == 0
assert mean_absolute_deviation([0, 0, 0]) == 0.0
assert mean_absolute_deviation([3, 2, 1, 0]) == 1.0
assert mean_absolute_deviation([1, 2, 3, 4]) == 1.0
assert mean_absolute_deviation([1, 3, 2, 4]) == 1.0
assert mean_absolute_deviation([1]) == 0
assert mean_absolute_deviation([1, 0]) == 0.5
assert mean_absolute_deviation([2, 2, 2, 2, 2]) == 0.0, "check your code"
assert mean_absolute_deviation([-1, -1, -1, -1, -1]) == 0.0, "check your code"
assert mean_absolute_deviation([3, 1, 3, 2, 3, 1, 3, 2, 3, 1]) == 0.8
assert mean_absolute_deviation([2, 2, 2, 2, 2]) == 0
assert mean_absolute_deviation([1.0, 2.0, -3.0]) == 2.0
assert mean_absolute_deviation([-1, 0, 1, -1, 0, 1]) == 0.6666666666666666
assert mean_absolute_deviation([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2.5
assert mean_absolute_deviation([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
assert (mean_absolute_deviation([1, 1, 1, 1, 1]) == 0.0)
assert (mean_absolute_deviation([1.5, 1.5, 1.5, 1.5, 1.5]) == 0.0)
assert (mean_absolute_deviation([-1, -1, -1, -1, -1]) == 0.0)
assert mean_absolute_deviation([2.0, 2.0, 2.0, 2.0, 2.0]) == 0.0, "MAD should be 0.0"
assert mean_absolute_deviation([-1.0, -2.0, -3.0]) == 0.6666666666666666
assert mean_absolute_deviation([5, 5, 5, 5]) == 0
assert mean_absolute_deviation([-1.0, -1.0, -1.0, -1.0, -1.0]) == 0.0
assert mean_absolute_deviation([0, 0, 0, 0, 0]) == 0
assert mean_absolute_deviation([0.3, 0.3, 0.3, 0.3, 0.3]) == 0
assert mean_absolute_deviation([-1, -1, -1]) == 0
assert mean_absolute_deviation([-10.4, -10.4, -10.4, -10.4, -10.4]) == 0
assert mean_absolute_deviation([1, 2, 3]) == 0.6666666666666666
