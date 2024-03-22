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
assert has_close_elements([10, 12, 15], 11) == True
assert has_close_elements([10, 12, 15], 13) == True
assert has_close_elements([10, 12, 15], 15) == True
assert has_close_elements([10, 12, 15], 17) == True
assert has_close_elements([10, 12, 15], 19) == True
assert has_close_elements([10, 12, 15], 21) == True
assert has_close_elements([10, 12, 15], 23) == True
assert has_close_elements([10, 12, 15], 25) == True
assert has_close_elements([10, 12, 15], 27) == True
assert has_close_elements([10, 12, 15], 29) == True
assert has_close_elements([10, 12, 15], 31) == True
assert has_close_elements([1, 2, 3], -2) == False
assert has_close_elements([1, 2, 3], 3) == True
assert has_close_elements([1, 2, 3], 5) == True
assert has_close_elements([1, 2, 3], 7) == True
assert has_close_elements([1, 2, 3], 9) == True
assert has_close_elements([1, 2, 3], 11) == True
assert has_close_elements([1, 2, 3], 13) == True
assert has_close_elements([1, 2, 3], 15) == True
assert has_close_elements([1, 2, 3], 17) == True
assert has_close_elements([1, 2, 3], 19) == True
assert has_close_elements([1, 2, 3], 21) == True
assert has_close_elements([1, 2, 3], 23) == True
assert has_close_elements([1, 2, 3], 25) == True
assert has_close_elements([1.1, 1.0, 1.2, 1.3, 1.4], 0.3) == True
assert has_close_elements([1.1, 1.0, 1.2, 1.3, 1.4], 0.4) == True
assert has_close_elements([1.1, 1.0, 1.2, 1.3, 1.4], 0.5) == True
assert has_close_elements([1.1, 1.0, 1.2, 1.3, 1.4], 0.6) == True
assert has_close_elements([1.1, 1.0, 1.2, 1.3, 1.4], 0.7) == True
assert has_close_elements([1.1, 1.0, 1.2, 1.3, 1.4], 0.8) == True
assert has_close_elements([1.1, 1.0, 1.2, 1.3, 1.4], 0.9) == True
assert has_close_elements([1.1, 1.0, 1.2, 1.3, 1.4], 1.1) == True
assert has_close_elements([1.1, 1.0, 1.2, 1.3, 1.4], 1.2) == True
assert has_close_elements([1.1, 1.0, 1.2, 1.3, 1.4], 1.3) == True
assert has_close_elements([1.1, 1.0, 1.2, 1.3, 1.4], 1.4) == True
assert has_close_elements([1.2, 1.4, 3.5, 3.8], 2) == True
assert has_close_elements([1.2, 1.4, 3.5, 3.8], 3) == True
assert has_close_elements([1.2, 1.4, 3.5, 3.8], 3.5) == True
assert has_close_elements([1.2, 1.4, 3.5, 3.8], 5) == True
assert has_close_elements([1.2, 1.4, 3.5, 3.8], 7) == True
assert has_close_elements([1.2, 1.4, 3.5, 3.8], 8) == True
assert has_close_elements([1.2, 1.4, 3.5, 3.8], 9) == True
assert has_close_elements([1.2, 1.4, 3.5, 3.8], 10) == True
assert has_close_elements([1.2, 1.4, 3.5, 3.8], 11) == True
assert has_close_elements([1.2, 1.4, 3.5, 3.8], 12) == True
assert has_close_elements([2, 2], 1.)
assert has_close_elements([1, 2, 3], 1.5) is True
assert has_close_elements([1, 2, 3], 2.5) is True
assert has_close_elements([1, 2, 3], 3) is True
assert has_close_elements([1, 2, 3, 4], 1.5) is True
assert has_close_elements([1, 2, 3, 4], 2) is True
assert has_close_elements([1, 2, 3, 4], 2.5) is True
assert has_close_elements([1, 2, 3, 4], 3) is True
assert has_close_elements([1, 2, 3, 4], 3.3) is True
assert has_close_elements([1, 2, 3, 4], 3.5) is True
assert has_close_elements([1, 2, 3, 4], 4) is True
assert has_close_elements([1.1, 2.2, 3.3, 4.4, 5.5, 6.6], 3.0) == True
assert has_close_elements([1.1, 2.2, 3.3, 4.4, 5.5, 6.6], 6.5) == True
assert has_close_elements([1.1, 2.2, 3.3, 4.4, 5.5, 6.6], 9.5) == True
assert has_close_elements([1.1, 2.2, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3], 3.3)
assert has_close_elements([1, 2, 3, 4], 0) == False
assert has_close_elements([1, 2, 3, 4], 0.5) == False
assert has_close_elements([-1, 2, -1, 3], 0.5) == True
assert has_close_elements([-1, -4, -4, -2], 0.5) == True
assert has_close_elements([1, 2, 3, 4], 5) == True
assert has_close_elements([-1, 2, -1, 3], 5) == True
assert has_close_elements([-1, -4, -4, -2], 5) == True
assert has_close_elements([1, 2, 3, 4], 10) == True
assert has_close_elements([-1, 2, -1, 3], 10) == True
assert has_close_elements([-1, -4, -4, -2], 10) == True
assert has_close_elements([1, 2, 3, 4], -2) == False
assert has_close_elements([-1, 2, -1, 3], -2) == False
assert has_close_elements([-1, -4, -4, -2], -2) == False
assert has_close_elements([1, 2, 3, 4], -1) == False
assert has_close_elements([-1, 2, -1, 3], -1) == False
assert has_close_elements([-1, -4, -4, -2], -1) == False
assert has_close_elements([1], 1) == False
assert has_close_elements([1], 2) == False
assert has_close_elements([1, 2, 3, 4], 2) == True
assert has_close_elements([10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 7) == True
assert has_close_elements([10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 15) == True
assert has_close_elements([10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 17) == True
assert not has_close_elements([1, 2, 3], 0.9)
assert not has_close_elements([7, 4, -6, 8, 0, -7, 1], -5)
assert has_close_elements([7, 4, -6, 8, 0, -7, 1], 4)
assert not has_close_elements([7, 4, -6, 8, 0, -7, 1], 0)
assert has_close_elements([7, 4, -6, 8, 0, -7, 1], 7)
assert has_close_elements([7, 4, -6, 8, 0, -7, 1], 8)
assert not has_close_elements([7, 4, -6, 8, 0, -7, 1], -1)
assert has_close_elements([1, 2, 3, 4, 50], 10) == True
assert has_close_elements([], 1) == False
assert has_close_elements([1, 2, 3, 4], 4) == True
assert has_close_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 6) == True
assert has_close_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 8) == True
assert has_close_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == True
assert has_close_elements([1, 2, 3, 4, 5, 6, 7, 8], 7) == True
assert has_close_elements([1, 2, 3, 4, 5, 6, 7, 8], 8) == True
assert has_close_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == True
assert has_close_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 11) == True
assert not has_close_elements([1.0, 2.0], 0.5)
assert not has_close_elements([1.0, 2.0], 0.0)
assert has_close_elements([1, 2, 3, 4], 3) == True
assert has_close_elements([1, 2, 3, 4], 6) == True
assert has_close_elements([1, 2, 3, 4], 1.01) == True
assert has_close_elements([0, 1, 2, 3, 4], 0.5) == False
assert has_close_elements([5, 3, 8, 10, 20], 10)
assert has_close_elements([5, 3, 8, 10, 20], 15)
assert has_close_elements([5, 3, 8, 10, 20], 5)
assert has_close_elements([5, 3, 8, 10, 20], 8)
assert has_close_elements([5, 3, 8, 10, 20], 20)
assert not has_close_elements([1, 3, 5, 7, 9], 0)
assert not has_close_elements([-2.1, -2.2, -2.3, -2.4, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8], -2.6)
assert not has_close_elements([1.1, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8], -2.7)
assert has_close_elements([0.1, 0.2, 0.4, 0.3, 0.5, 0.6, 0.8, 0.9], threshold=0.3) is True
assert has_close_elements([0.1, 0.2, 0.4, 0.3, 0.5, 0.6, 0.8, 0.9], threshold=0.5) is True
assert not has_close_elements([1.5, 3.3, 4.2], 0.5)
assert not has_close_elements([1.5, 3.3, 4.1], 0.5)
assert not has_close_elements([1.7, 3.3, 4.1], 0.5)
assert not has_close_elements([1.3, 3.2, 4.4], 0.5)
assert not has_close_elements([1.7, 3.2, 4.4], 0.5)
assert has_close_elements([1, 2, 3], 0.5) == False
assert has_close_elements([-1, -2, -3], 0.2) == False
assert has_close_elements([1, 2, 3], 0) == False
assert has_close_elements([], 0) == False
assert has_close_elements([1.1, 2.2, 3.3], 0.2) == False
assert has_close_elements([1, 2.1, 2.9, 3.3], 0.2) == False
assert has_close_elements([], -0.2) == False
assert has_close_elements([1.1, 2.2, 3.3], -0.2) == False
assert has_close_elements([1, 2.1, 2.9, 3.3], -0.2) == False
assert has_close_elements([1], 1.1) == False
assert has_close_elements([], 1.1) == False
assert has_close_elements([1.1, 2.2, 3.3], 1.1) == True
assert has_close_elements([1, 2.1, 2.9, 3.3], 1.1) == True
assert has_close_elements([1.5, 2.5, 3.5, 4.5], 2.5) == True
assert has_close_elements([1.5, 2.5, 3.5, 4.5], 3.5) == True
assert has_close_elements([1.5, 2.5, 3.5, 4.5], 4.5) == True
assert has_close_elements([], 5) == False
assert has_close_elements([10, 20, 30, 50], 15) == True
assert has_close_elements([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8], 0.4)
assert has_close_elements([5, 3, 2], 2.6) == True
assert has_close_elements([3, 5], 2.5) == True
assert has_close_elements([4, 5, 6], 2.5) == True
assert has_close_elements([10], 0) is False
assert has_close_elements([10, 20, 30], 5) is False
assert not has_close_elements([1], 1.1)
assert not has_close_elements([1.2, 2.4, 3.3, 4.4], 0.6)
assert has_close_elements([1.1, 2.2, 3.3, 4.4], 1.1)
assert has_close_elements([1.1, 2.2, 3.3, 4.4], 1.5)
assert has_close_elements([0.2, 0.2, 0.5, 1.1, 2.1], threshold=0.8) == True
assert has_close_elements([0.2, 0.2, 0.5, 1.1, 2.1], threshold=0.9) == True
assert has_close_elements([5, 1, 2, 3], 0.9) is False
assert has_close_elements([10, 1, 2, 3, 20], 0) is False
assert has_close_elements([10, 1, 2, 3, 20], -0.1) is False
assert not has_close_elements([1, 3, 5], 1.1)
assert has_close_elements([1, 3, 5], 2.5)
assert has_close_elements([1, 3, 5], 6.5)
assert has_close_elements([1, 3, 5], 7.5)
assert not has_close_elements(numbers=[0, 1, 2, 3], threshold=0.3)
assert not has_close_elements(numbers=[0, 1, 2, 3], threshold=0.1)
assert not has_close_elements(numbers=[1, 2, 3], threshold=0.1)
assert not has_close_elements(numbers=[1, 5, 4], threshold=0.2)
assert has_close_elements([3.0, 4.0, 0.0], 0.0) == False
assert has_close_elements([1, 2, 3, 4, 5], threshold=4) is True
assert has_close_elements([0.45, 0.65, 0.75, 0.85], 0.2) == True
assert has_close_elements([0.5], 0.2) == False
assert has_close_elements([1.1, 2.2], 1) is False
assert has_close_elements([1.1, 2.2], 0) is False
assert has_close_elements([1.1, 2.2], 1.5) is True
assert not has_close_elements([1, 3, 2, 4], 0.9)
assert has_close_elements([1, 2, 3, 4], 1.1)
assert not has_close_elements([1, 2, 3], 0.7)
assert not has_close_elements([1, 2, 3], 0.8)
assert not has_close_elements([1, 2, 3], 0.11)
assert has_close_elements([1, 2, 3, 4], 4)
assert not has_close_elements([1, 2, 3, 4], 0)
assert has_close_elements([1, 2, 3, 4], 5)
assert has_close_elements([0.5, 0.4, 0.8], 0.5) == True
assert has_close_elements([1, 100, 1000], 0.5) == False
assert has_close_elements([1, 100, 1000], 1) == False
assert has_close_elements([1, 100, 1000], 0.1) == False
assert has_close_elements([1, 1, 2], 0.2) == True
assert not has_close_elements([1, 2, 3, 4], 0.4)
assert not has_close_elements([1, 2, 3, 4], 0.6)
assert not has_close_elements([1, 2, 3, 4], 0.9)
assert has_close_elements([3.6, 6.9, 1.1, 2.4, 4.3, 6.9, 1.1], 0.5) == True
assert has_close_elements([3.6, 6.9, 1.1, 2.4, 4.3, 6.9, 1.1], -0.6) == False
assert has_close_elements([2, 7, 4, 3, 9, 6], 3) == True
assert has_close_elements([1.2, 2.3, 3.4, 4.5, 5.6], 3.0) is True
assert has_close_elements([-1, 0, 1], 0.5) is False
assert has_close_elements([-1, 0, 1], -1.1) is False
assert has_close_elements([1.5, 2.5, 0.0], -0.0) is False
assert has_close_elements([1.5, 2.5, 0.0], 0.5) is False
assert has_close_elements([1, 2, 3, 4],.6) == False
assert has_close_elements([1, 2],.6) == False
assert has_close_elements([], 0.5) == False
assert has_close_elements([5, -5, -10, -10], -0.5) == False
assert has_close_elements([1, 2, 3, 5], 0.5) is False
assert has_close_elements([2.5, 2.5, 1.5, 1.5, 1.5], 1.5) == True
assert has_close_elements([10, 12, 8], 10) == True
assert has_close_elements([1.1, 2.3, 3.8, 5.9], 3.8)
assert has_close_elements([1.3, 2.6, 1.0], 1.0) == True
assert has_close_elements([1, 2, 3, 4, 5], 0.1) is False
assert has_close_elements([1, 2, 3, 4], 0.45) == False
assert has_close_elements([0.0, -0.5, 0.5], 0.0) is False
assert has_close_elements([-1.0, -0.5, 0.5, -1.0], 0.5) is True
assert has_close_elements([1.0, 1.0, 1.0], 1.0) is True
assert not has_close_elements([1, 2, 3, 4, 5], 0.4)
assert not has_close_elements([1, 2, 3.4, 5], 0.4)
assert has_close_elements([1, 5, 7, 10], 7) == True
assert has_close_elements([2, 5, 9, 13, 17], 8) is True
assert has_close_elements([1, 9, 6, 4], 0.2) == False
