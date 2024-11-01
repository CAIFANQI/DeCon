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
assert 	has_close_elements([1, 2, 3, 4, 5], 2) == True, "Case: 1,2,3,4,5 is a close set"
assert 	has_close_elements([1, 2, 3, 4, 5], 0) == False, "Case: 1,2,3,4,5 is not a close set"
assert 	has_close_elements([1, 2, 3, 4, 5], 0) == False
assert 	has_close_elements([1, 2, 3, 4, 5], 2) == True
assert 	has_close_elements([1, 2, 3, 4, 5], 4) == True
assert 	has_close_elements([1, 2, 3, 4, 5], 5) == True
assert 	has_close_elements([1, 2, 3, 4, 5], 0.1) == False
assert 	has_close_elements([], 3) == False
assert has_close_elements([1, 2, 3, 4, 5], 1) is False
assert has_close_elements([1, 2, 3, 4, 5], 3) is True
assert has_close_elements([1, 2, 3, 4, 5], 5) is True
assert has_close_elements([], 2) is False
assert has_close_elements([], 0) is False
assert has_close_elements([1], 2) is False
assert has_close_elements([1], 0) is False
assert has_close_elements([1, 2], 1) is False
assert has_close_elements([1, 2], 0) is False
assert 	has_close_elements([1, 2, 3, 4, 5], 0.5) == False
assert 	has_close_elements([1, 2, 3, 4, 5], 0.4) == False
assert 	has_close_elements([1, 2, 3, 4, 5], 0.3) == False
assert 	has_close_elements([1, 2, 3, 4, 5], 0.2) == False
assert has_close_elements([2, 5, 6, 8], 1.0) == False
assert has_close_elements([1, 2, 3, 5], 1.0) == False
assert has_close_elements([1, 2, 3, 4], 0.4) == False
assert 	has_close_elements([1, 2, 3, 4], 2) == True
assert 	has_close_elements([1, 2, 4, 3], 2) == True
assert 	has_close_elements([3, 2, 4, 1], 2) == True
assert 	has_close_elements([0, 1, 2, 3, 4], 3) == True
assert 	has_close_elements([1, 2, 3, 4], 0) == False
assert 	has_close_elements([1, 2, 4, 3], 0) == False
assert 	has_close_elements([1, 2, 3, 4], -1) == False
assert 	has_close_elements([0.0, 0.3, 0.6, 1.0], 0.2) == False
assert 	has_close_elements([0.0, 0.3, 0.6, 1.0], 0.7) == True
assert 	has_close_elements([0.0, 0.3, 0.6, 1.0], 0.9) == True
assert not has_close_elements([1, 2, 3], 0.9)
assert has_close_elements([1, 2, 3], 3)
assert not has_close_elements([1, 2, 3], 0.02)
assert not has_close_elements([1, 2, 3], 0.04)
assert not has_close_elements([1, 2, 3], 0.08)
assert not has_close_elements([1, 2, 3], 0.09)
assert not has_close_elements([1, 2, 3], 0.11)
assert not has_close_elements([1, 2, 3], 0.14)
assert has_close_elements([0, 0, 0, 0], 0) == False, "Wrong answer. Can you check the test?"
assert has_close_elements([0.01, 0.01, 0.01, 0.01], 0) == False, "Wrong answer. Can you check the test?"
assert not has_close_elements([1, 2, 3], 0.1)
assert not has_close_elements([1, 2, 3, 4, 5, 6], 0.1)
assert 	has_close_elements([1, 2, 3, 4], 5) == True
assert 	has_close_elements([1,2,3,4], 6) is True
assert 	has_close_elements([1,2,3,4], 7) is True
assert 	has_close_elements([1,2,3,4], 9) is True
assert has_close_elements([1, 2, 10, 20], 10) is True
assert has_close_elements([2, 10, 20], 10) is True
assert has_close_elements([2, 10, 20], 20) is True
assert has_close_elements([10, 20, 30], 20) is True
assert has_close_elements([1, 2, 3, 4, 5], 0) is False
assert has_close_elements([1, 2, 3, 4, 5], 6) is True
assert has_close_elements([], 1) is False
assert has_close_elements([1.0, 2.0, 3.0], 0.4) is False
assert has_close_elements([0.0, 0.2, 0.1], 0.01) is False
assert has_close_elements([0.0, 0.2, 0.1], 0.03) is False
assert 	has_close_elements([1.0, 2.5, 3.0, 4.0], 1.0) == True
assert 	has_close_elements([1.0, 2.5, 3.0, 4.0, 6.0], 1.0) == True
assert has_close_elements([1, 2, 3], 1.4) == True
assert has_close_elements([1, 2, 3], 1.1) == True
assert has_close_elements([1, 2, 3], 0.0) == False
assert has_close_elements([1, 2, 3], 0.99) == False
assert 	has_close_elements([1, 1, 1, 1], 1) == True
assert 	has_close_elements([1, 1, 1, 1], 100) == True
assert 	has_close_elements([1, 1, 1, 1], 2) == True
assert 	has_close_elements([1, 1, 1, 1], 0.3) == True
assert 	has_close_elements([1, 1, 1, 1], 100.3) == True
assert 	has_close_elements([1, 1, 1, 1], 1.3) == True
assert has_close_elements([1, 2, 3], 1) is False
assert has_close_elements([1, 2, 3], 0) is False
assert has_close_elements([1, 2, 3, 8], 1) is False
assert has_close_elements([1, 2, 3, 8], 0) is False
assert has_close_elements([1, 2, 3, 8], 3) is True
assert has_close_elements([1, 2, 3, 8], 4) is True
