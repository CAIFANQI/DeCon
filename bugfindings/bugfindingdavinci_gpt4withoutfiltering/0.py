from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = elem - elem2
                if distance < threshold:
                    return True

    return False
assert has_close_elements([1, 2, 3], 1) is False
assert has_close_elements([1, 2, 3], 10) is True
assert has_close_elements([0.5, 2.5, 2.3], 1) is True
assert has_close_elements([], 100) is False
assert has_close_elements([1, 2, 3, 10, 1.01], 0.99) is True
assert has_close_elements([1, 2, 3, 10, 1.01], 1.5) is True
assert has_close_elements([1, 2, 3, 2.1], 0.5) is True
assert has_close_elements([1, 2, 3, 1.9], 0.5) is True
assert has_close_elements([1, 2, 3, 1.9, 2.1], 0.5) is True
assert has_close_elements([1, 2, 3, 1.9, 2.1, 2.5], 0.5) is True
assert has_close_elements([1, 2, 3, 1.9, 2.1, 2.5, 0.5], 0.5) is True
assert has_close_elements([1, 2, 3, 1.9, 2.1, 2.5, 0.5, 0.4], 0.5) is True
assert has_close_elements([1, 2, 3, 1.9, 2.1, 2.5, 0.5, 0.4, 0.49], 0.5) is True
assert has_close_elements([0.1, 0.2, 0.3, 0.4], 0.3)
assert has_close_elements([1, 1.5, 2], 1) is True
assert has_close_elements([10.0, 9.0, 5.0], 3.0) is True
assert has_close_elements([3.0, 2.0, 1.0], 0.5) is False
assert has_close_elements([3.0, 2.0, 1.0], 0.01) is False
assert has_close_elements([1.0, 2.0, 3.0], 0.01) is False
assert has_close_elements([1.0, 1.0], 0.5) is True
assert has_close_elements([1.0, 1.0], 0.01) is True
assert has_close_elements([1, 2, 3, 4, 5], 1.5) == True
assert has_close_elements([0, 1, 2, 3, 4, 5, 10, 11, 20, 30, 40, 50, 100], 1.5) == True
assert has_close_elements([1, 2, 3, 4, 5], 1.0) == False
assert has_close_elements([1, 2, 3, 4, 5], 1.1) == True
assert has_close_elements([1, 2, 3, 4, 5], 2.1) == True
assert has_close_elements([1, 2, 3, 4, 5], 3.1) == True
assert has_close_elements([1, 2, 3, 4, 5], 4.1) == True
assert has_close_elements([1, 2, 3], 2) is True
assert has_close_elements([1, 2, 3], -2) is False
assert has_close_elements([1, 2, 3], -3) is False
assert has_close_elements([1, 2, 3], -4) is False
assert has_close_elements([1, 2, 3], -5) is False
assert has_close_elements([1.0, 2.0, 3.0], 2.0) is True
assert has_close_elements([1.0, 2.0, 1.0001], 0.9999) is True
assert has_close_elements([1.0, 3.2, 4.4, 5.1, 6.7], 0.2) is False
assert has_close_elements([1.0, 3.2, 4.4, 5.1, 6.7], 0.9) is True
assert has_close_elements([0.6, 0.6, 0.6, 0.6, 0.6], 0.6)
assert has_close_elements([1, 1.4, 1.8], 0.4) is True, "should return True for [1, 1.4, 1.8]"
assert has_close_elements([1, 2, 4], 0.5) is False, "should return False for [1, 2, 4]"
assert has_close_elements([1, 2, 4], 1.5) is True, "should return True for [1, 2, 4]"
assert has_close_elements([1, 1, 1], 0.00001) == True
assert has_close_elements([], 0.00001) == False
assert has_close_elements([0.0, 1.0, 2.0, 3.0, 4.0], 1.5) is True
assert has_close_elements([10.0, 20.0, 30.0], 15.0) is True
assert not has_close_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
assert has_close_elements([1, 2, 3, 4], 2) is True
assert has_close_elements([2, 3, 4, 5], 2) is True
assert has_close_elements([1, 3, 5, 7], 2) is False
assert has_close_elements([3, 1, 7, 5], 2) is False
assert has_close_elements([1, 2, 3], 0.1) is False
assert has_close_elements([], 0.1) is False
assert has_close_elements([1], 0.1) is False
assert not has_close_elements([1, 3, 0.5, 2, 5], 0.5)
assert has_close_elements([1, 3, 0.5, 2, 0.4], 0.5)
assert has_close_elements([0.0, 1.0, 2.0], 0.5) is False
assert has_close_elements([0.0, 0.9, 1.0], 0.1) is True
assert has_close_elements([0.0, 0.9, 1.0], 0.001) is False
assert has_close_elements([1.2, 5.6, 2.1, 3.2, 4.8], 2.3) == True
assert has_close_elements([1.2, 5.6, 2.1, 3.2, 4.8], 0.1) == False
assert has_close_elements([0.1, 0.9, 1.4, 1.5], 0.2)
assert has_close_elements([0.1, 0.9, 1.4, 1.6, 1.7], 0.2)
assert has_close_elements([1, 2, 3, 4, 5], 2)
assert has_close_elements([1, 2, 3, 4, 5], 3)
assert has_close_elements([1, 2, 3, 4, 5], 4)
assert has_close_elements([1, 2, 3, 4, 5], 5)
assert has_close_elements([1, 2, 3, 4, 5], 6)
assert has_close_elements([10, 2, 3, 4, 5], 9)
assert has_close_elements([], 1) == False
assert has_close_elements([1, 2, 3, 100], 100) == True
assert has_close_elements([1.1, 2.1, 3.1], 1.2) == True
assert has_close_elements([1.1, 2.1, 3.1], 1.200000001) == True
assert has_close_elements([1, 3, 4, 10, 25, 35, 40], 1) is False
assert has_close_elements([-6, 7, -7, 8, -10, 15], 11)
assert has_close_elements([0.3, 0.4, 0.7, 0.8, 0.9], 0.1)
assert not has_close_elements([0.3, 0.4, 0.7, 0.8, 0.9], 0.05)
assert has_close_elements([1, 2, 2.5, 3, 4], 1) == True
assert has_close_elements([1, 2, 2.5, 3, 4], 0.5) == False
assert has_close_elements([1], 1) == False
assert has_close_elements([1, 1], 1) == True
assert has_close_elements([1, 2], 1) == False
assert has_close_elements([1.0, 2.0, 3.0], 1.5) == True
assert has_close_elements([0, 1, 2, 3, 4], 1.1)
assert has_close_elements([0.0, 0.5, 1.0, 2.0], 0.2) is False
assert has_close_elements([], 0.3) is False
assert has_close_elements([1.0, 2.0, 3.0], 0.1) is False
assert has_close_elements([0.1, 0.4, 0.7, 1.1, 1.4, 1.7], 0.5)
assert has_close_elements([0.1, 0.4, 0.7, 1.1, 1.4, 1.7], 0.6)
assert not has_close_elements([1, 2, 3, 4, 5, 6], 0.9)
assert has_close_elements([1, 2, 3, 4, 5, 6], 1.1)
assert has_close_elements([1, 2, 3, 4, 5, 6], 1.2)
assert not has_close_elements([0.1, 0.4, 0.7, 1.1, 1.4, 1.7], 0.02)
assert not has_close_elements([0.1, 0.4, 0.7, 1.1, 1.4, 1.7], 0.0009)
assert has_close_elements([5, 10, 20, 4], 10) is True
assert has_close_elements([100, 90, 70, 80], 30) is True
assert has_close_elements([100, 90, 70, 80], 40) is True
assert has_close_elements([100, 90, 70, 80], 50) is True
assert has_close_elements([100, 90, 70, 80], 60) is True
assert has_close_elements([100, 90, 70, 80], 70) is True
assert has_close_elements([100, 90, 70, 80], 80) is True
assert has_close_elements([100, 90, 70, 80], 90) is True
assert has_close_elements([100, 90, 70, 80], 100) is True
assert has_close_elements([1.0, 2.0, 4.0, 9.0], 2.0) is True
assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 1.0) is False
assert has_close_elements([1.0, 2.0, 2.0], 0.5)
assert has_close_elements([10, 15, 18, 45], 4) is True
assert has_close_elements([20, 15, 6, 5], 4) is True
assert has_close_elements([0.1, 0.7, 0.2, 0.4], 0.1) is False
assert not has_close_elements([1.6, 0.6, 3.6, 2.6], 0.9)
assert not has_close_elements([], 0.5)
assert not has_close_elements([1.1, 2.2, 3.3, 4.4], 0.5)
assert has_close_elements([1.0, 2.0, 3.0, 4.0], 1.0) is False
assert has_close_elements([100.0, 200.0, 300.0, 400.0], 10.0) is False
assert has_close_elements([0.0, 1.2, 3.0, 4.5, 6.1], 0.5) is False
assert has_close_elements([1, 2, 3], 0.51) == False
assert has_close_elements([1, 2, 3], 0.2) is False
assert has_close_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0.1) is False
assert has_close_elements([], 10.0) == False
assert has_close_elements([1.2, 1.2, 1.2], 0.5) == True
assert has_close_elements([5.0, 1.5, 10.0, 15.5], 3.0) == False
assert has_close_elements([5.0, 1.5, 10.0, 15.5], 8.0) == True
assert has_close_elements([1, 2, 3], 2.9) is True
assert has_close_elements([1.5, 2.5, 3.5], 0.9) is False
assert has_close_elements([1.5, 2.5, 3.5], 2.9) is True
assert has_close_elements([0.1, 0.2, 0.3, 0.4], 0.05) is False
assert has_close_elements([2, 3.5, 4, 6, 10], 0.5) is False
assert has_close_elements([1.0, 2.0, 1.5], 2.0) == True
assert has_close_elements([1.0, 2.0, 3.0], 0.001) == False
assert has_close_elements([1.0, 1.001, 1.002], 0.01) == True
assert has_close_elements([1.5, -2.5, 0.0, 4.0, 5.0], 1.0) is False
assert has_close_elements([1, 2, 3], 1.1) is True
assert has_close_elements([1, 1.1, 3], 0.8) is True
assert has_close_elements([1, 2, 3, 4, 5], 1.5) is True
assert has_close_elements([1, 2, 3, 4, 5], 2.5) is True
assert has_close_elements([1, 2, 3, 4, 5], 3.5) is True
assert has_close_elements([1, 2, 3, 4, 5], 4.5) is True
assert has_close_elements([1, 2, 3], 3) is True
assert has_close_elements([0, 1], 2) is True
assert has_close_elements([0, 1], 0.5) is False
assert has_close_elements([1, 2, 3, 4, 5], 2.5) == True
assert has_close_elements([1, 2, 3, 4, 5], 3.5) == True
assert has_close_elements([1, 2, 3, 4, 5], 4.5) == True
assert not has_close_elements([1.0, 2.0, 1.5], 0.1)
assert has_close_elements([1.0, 2.0, -1.0], 1.5)
assert has_close_elements([1.0, 2.0, 3.0, 4.0], 0.1) is False
assert has_close_elements([1, 2, 3, 4, 5], 0.0001) is False
assert has_close_elements([1, 1, 1, 1, 1], 0.0001) is True
assert has_close_elements([1, 2, 2, 2, 2], 1) is True
assert has_close_elements([1, 2, 3, 4, 5], -1) is False
assert has_close_elements([0.001, 0.003, 0.003], 0.004) is True
assert has_close_elements([1.0, 3.2, 5.5, 6.1, 12.0], 0.5) is False
assert has_close_elements([1.0, 3.2, 5.5, 6.1, 12.0], 5.0) is True
assert has_close_elements([1.0, 3.2, 5.5, 6.1, 12.0], 0.0) is False
assert has_close_elements([], 0.9) == False
assert has_close_elements([1, 2, 3, 4, 5], 4) is True
assert has_close_elements([1, 2, 3, 4, 5], 5) is True
assert has_close_elements([1, 2, 3, 4, 5], 6) is True
assert has_close_elements([1, 1.2, 3, 4, 5], 0.6) is True
assert has_close_elements([1, 1.2, 3, 4, 5], 1.2) is True
assert has_close_elements([1, 1.2, 3, 4, 5], 2.2) is True
assert has_close_elements([1, 2, 4], 3) is True
assert has_close_elements([1, 2, 4], 1) is False
assert has_close_elements([0, 1, 2, 100], 101) is True
assert has_close_elements([100, 101, 102], 0.5) is False
assert has_close_elements([10, 20, 30, 40, 50], 20)
assert has_close_elements([10, 20, 30, 40, 50], 21)
assert has_close_elements([1, 2, 3, 4, 5], 3) is True
assert has_close_elements([1, 2, 3, 4, 5], 0.1) is False
assert has_close_elements([1, 2, 3, 5, 8, 13, 21, 34], 1) == False
assert has_close_elements([1, 2, 3, 5, 8, 13, 21, 34], 2) == True
assert has_close_elements([1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9], 0.02) is False
assert has_close_elements([1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000], 0.001) is False
assert has_close_elements([1, 2, 3, 4, 5], 0.2) is False
assert has_close_elements([1, 2, 3, 4, 4.2], 0.4) is True
assert has_close_elements([0, 1, 2, 3, 4], 0.5) is False
assert has_close_elements([], 0.5) is False
assert has_close_elements([0.1, 0.1, 0.1, 0.1, 0.1], 0.2) is True
assert has_close_elements([0.1, 0.15, 0.12, 0.11, 0.1], 0.2) is True
assert has_close_elements([0.1, 0.15, 0.12, 0.11, 0.1], 0.06) is True
assert has_close_elements([1.1, 1.2, 1.3, 1.4], 0.6) is True
assert has_close_elements([1.1, 1.2, 1.3, 1.4], 0.5) is True
assert has_close_elements([1.0, 2.0, 3.0, 4.0], 1.2) is True
assert has_close_elements([1.0, 2.0, 3.0, 4.0], 1.5) is True
assert has_close_elements([1.0], 0.1) is False
assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 3.0) is True
assert has_close_elements([1.0, 2.0, 3.0], 1.5) is True
assert has_close_elements([1, 2, 3, 4, 4.1], 0.5)
assert has_close_elements([0.5, 0.6, 0.11, 0.12, 0.15], 0.01) is True
assert has_close_elements([0.5, 0.6, 0.11, 0.12, 0.15], 0.001) is False
assert has_close_elements([], 0.6) == False
assert has_close_elements([0.2, 0.5, 3.2, 0.7, 1.1], 0.1) is False
assert has_close_elements([0.2, 0.5, 3.2, 0.7, 1.1], 0.3) is True
assert has_close_elements([0.2, 0.5, 3.2, 0.7, 1.1], 0.6) is True
assert has_close_elements([1, 2, 3, 4, 5], 0.001) == False, "simple case"
assert has_close_elements([1.0001, 1.0002, 1.0003, 1.0004, 1.0005], 0.001) == True, "simple case"
assert has_close_elements([1.001, 1.002, 1.003, 1.004, 1.005], 0.01) == True, "simple case"
assert not has_close_elements([1.0], 0.5)
assert not has_close_elements([1.0, 2.0], 0.5)
assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
assert has_close_elements([1.0, 4.0, 9.0], 4.0) is True
assert has_close_elements([1, 2, 3, 4, 5], 1) is False
assert has_close_elements([1, 2, 3, 4, 5], 2) is True
assert has_close_elements([2, 3.5, 4.2, 5.1, 9.7], 0.5) is False
assert has_close_elements([0, 1, 2, 3, 4, 5], 2) == True
assert has_close_elements([0, 1, 2, 3, 4, 5], 0.001) == False
assert has_close_elements([1.2, 3.7, 9.8, 2.1], 0.5) is False
assert has_close_elements([2.0, 3.0, 4.0, 5.0], 5.0) is True
assert has_close_elements([1, 2, 3, 4, 5], 1.9)
assert not has_close_elements([1, 2, 3, 4, 5], 0.1)
assert not has_close_elements([1, 2, 3, 4, 5], 0.001)
assert has_close_elements([0, 0.0003, 0.0006, 0.001, 0.002], 0.0004)
assert has_close_elements([1, 1.000001, 1.000002, 1.000003, 1.000004], 0.000001)
assert not has_close_elements([1, 1.000001, 1.000002, 1.000003, 1.000004], 0.0000001)
assert not has_close_elements([], 0.1)
assert not has_close_elements([1], 5)
assert has_close_elements([1, 2, 3], 1.5) is True
assert has_close_elements([1, 2, 3], 2.5) is True
assert has_close_elements([1, 1.1, 1.2], 0.9) is True
assert has_close_elements([], 5) is False
assert has_close_elements([1.0, 2.0, 5.0, 8.0], 2.0) is True
assert has_close_elements([1.0, 2.0, 5.0, 8.0], 3.0) is True
assert has_close_elements([1.0, 2.0, 5.0, 8.0], 4.0) is True
assert has_close_elements([1.0, 2.0, 5.0, 8.0], 1.0) is False
assert not has_close_elements([100.0, 101.0, 102.0], 1.0)
assert not has_close_elements([1.0, 2.0, 3.0, 4.0, 1e10], 1e-10)
assert has_close_elements([1.0, 1.0, 1.0, 1.0], 0.5)
assert has_close_elements([1.0, 1.1, 1.2, 1.3], 0.4)
assert has_close_elements([1.0, 1.1, 1.2, 1.3], 1.5)
