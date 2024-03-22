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
assert mean_absolute_deviation([2.0]) == 0.0
assert mean_absolute_deviation([0]) == 0
assert mean_absolute_deviation([1., 2.]) == 0.5
assert mean_absolute_deviation([1.]) == 0.0
assert mean_absolute_deviation([4, 5, 6, 7]) == 1, 'wrong answer for mean_absolute_deviation'
assert mean_absolute_deviation([1]) == 0.0
assert mean_absolute_deviation([2]) == 0.0
assert mean_absolute_deviation([0]) == 0.0
assert mean_absolute_deviation([-7, -5]) == 1.0
assert mean_absolute_deviation([-1]) == 0
assert mean_absolute_deviation([1.5]) == 0
assert mean_absolute_deviation([4]) == 0
assert abs(mean_absolute_deviation([1, 2, 3, 0]) - 1) < 0.001
