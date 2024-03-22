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
assert mean_absolute_deviation([1, 2, 3, 4, 5]) == 1.2
assert mean_absolute_deviation([10, 20, 30, 40, 50]) == 12
assert mean_absolute_deviation([1, 3, 5, 7, 9]) == 2.4
assert mean_absolute_deviation([1, 1, 1, 1, 1]) == 0.0
assert mean_absolute_deviation([0, 0, 0, 0, 0]) == 0
assert mean_absolute_deviation([-1, -2, -3, -4, -5]) == 1.2
assert mean_absolute_deviation([1.5, 2.5, 3.5, 4.5, 5.5]) == 1.2
assert mean_absolute_deviation([-1, 0, 1]) == 0.6666666666666666
assert mean_absolute_deviation([1, 1, 1, 1, 1]) == 0
assert mean_absolute_deviation([-1, -1, -1, -1, -1]) == 0
assert mean_absolute_deviation([10, 20, 30, 40, 50]) == 12, "Test case 2 failed"
assert mean_absolute_deviation([-1, -2, -3, -4, -5]) == 1.2, "Test case 3 failed"
assert mean_absolute_deviation([1, 1, 1, 1, 1]) == 0, "Test case 4 failed"
assert mean_absolute_deviation([1.5, 2.5, 3.5, 4.5, 5.5]) == 1.2, "Test case 4 failed"
assert mean_absolute_deviation([1, 1, 1, 1, 1]) == 0.0, "Test case 5 failed"
assert mean_absolute_deviation([5, 5, 5, 5, 5]) == 0.0
assert mean_absolute_deviation([1, 2, 3, 4, 5, 6]) == 1.5
assert mean_absolute_deviation([-5, -5, -5, -5, -5]) == 0.0
assert mean_absolute_deviation([-1, -2, -3, -4, -5, -6]) == 1.5
assert mean_absolute_deviation([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0.0
assert mean_absolute_deviation([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 1.2
assert mean_absolute_deviation([10, 20, 30, 40, 50]) == 12.0
assert mean_absolute_deviation([2, 4, 6, 8, 10]) == 2.4
assert mean_absolute_deviation([1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1.0
assert mean_absolute_deviation([1, 10]) == 4.5
assert mean_absolute_deviation([100, 200, 300, 400, 500]) == 120.0
assert mean_absolute_deviation([0, 0, 0, 0, 0]) == 0.0
assert mean_absolute_deviation([5, 5, 5, 5, 5]) == 0
assert mean_absolute_deviation([10, 20, 30, 40, 50]) == 12.0, 'Test Case 2 Failed'
assert mean_absolute_deviation([2, 4, 6, 8, 10]) == 2.4, 'Test Case 4 Failed'
assert mean_absolute_deviation([1, 3, 5, 7, 9]) == 2.4, 'Test Case 5 Failed'
assert mean_absolute_deviation([0, 0, 0, 0]) == 0.0
assert mean_absolute_deviation([1, 1, 1, 1, 1]) == 0, "Test case 3 failed"
assert mean_absolute_deviation([-1, -2, -3, -4, -5]) == 1.2, "Test case 4 failed"
assert mean_absolute_deviation([1.5, 2.5, 3.5, 4.5, 5.5]) == 1.2, "Test case 5 failed"
assert mean_absolute_deviation([-10, -20, -30, -40, -50]) == 12.0
assert mean_absolute_deviation([1, 2, 3, 4, 5, 6, 7]) == 1.7142857142857142
assert mean_absolute_deviation([1, 2, 3, 4, 5, 6, 7, 8]) == 2.0
assert mean_absolute_deviation([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2.2222222222222223
assert mean_absolute_deviation([2, 4, 6, 8, 10, 12]) == 3.0
assert mean_absolute_deviation([1]) == 0.0
assert mean_absolute_deviation([-10, -20, -30, -40, -50]) == 12
assert mean_absolute_deviation([10, 20, 30, 40, 50]) == 12.0, "Test case 2 failed"
assert mean_absolute_deviation([1, 1, 1, 1, 1]) == 0, "Test case 2 failed"
assert mean_absolute_deviation([-1, 0, 1]) == 0.6666666666666666, "Test case 3 failed"
assert mean_absolute_deviation([5, 5, 5, 5, 5]) == 0, 'Test Case 4 Failed'
