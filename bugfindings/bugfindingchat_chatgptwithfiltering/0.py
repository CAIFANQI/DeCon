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
assert has_close_elements([1, 2, 3, 4], 2) == True
assert has_close_elements([1, 2, 3, 4], 3) == True
assert has_close_elements([1, 2, 3, 4], 4) == True
assert has_close_elements([1, 2, 3, 4], 5) == True
assert has_close_elements([1, 2, 3, 4], 6) == True
assert has_close_elements([1, 2, 3, 4], 7) == True
assert has_close_elements([1, 2, 3, 4], 8) == True
assert has_close_elements([1, 2, 3, 4], 9) == True
assert has_close_elements([1, 2, 3, 4], 10) == True
assert has_close_elements([1, 2, 3, 4, 5], 2) == True
assert has_close_elements([1, 2, 3, 4, 5], 0.5) == False
assert has_close_elements([1, 2, 3, 4], 0.5) == False
assert has_close_elements([1, 2, 3, 4], 0.1) == False
assert has_close_elements([1.1, 2.2, 3.3, 4.4], 0.5) == False
assert has_close_elements([1.5, 2.5, 3.5, 4.5], 0.5) == False
assert has_close_elements([1.5, 2.5, 3.5, 4.5], 0.1) == False
assert has_close_elements([1, 2, 3, 4, 5], 2) == True, "Error: Test Case 2"
assert has_close_elements([1, 2, 3, 4, 5], 0.5) == False, "Error: Test Case 3"
assert has_close_elements([1, 2, 3, 4, 5], 10) == True, "Error: Test Case 4"
assert has_close_elements([1, 2, 3, 4, 5], 5) == True, "Error: Test Case 5"
assert has_close_elements([1, 2, 3, 4, 5], 5) == True
assert has_close_elements([1, 2, 3, 4, 5], 3) == True
assert has_close_elements([1, 2, 3, 4, 5], 2) == True, "Test case 2 failed"
assert has_close_elements([1, 2, 3, 4, 5], 0.5) == False, "Test case 3 failed"
assert has_close_elements([1, 2, 3, 4, 5], 5) == True, "Test case 4 failed"
assert has_close_elements([1, 2, 3, 4, 5], 6) == True, "Test case 5 failed"
assert has_close_elements([1.5, 2.5, 3.5, 4.5, 5.5], 0.1) == False
assert has_close_elements([1.0, 2.0, 3.0], 0.1) == False, "Test case 3 failed"
assert has_close_elements([1.0, 1.1, 1.2, 1.3], 0.2) == True, "Test case 4 failed"
assert has_close_elements([], 1) == False, "Error: Test Case 7"
assert has_close_elements([1, 2, 3, 4, 5], 4) == True
assert has_close_elements([1, 2, 3, 4, 5], 6) == True
assert has_close_elements([1, 2, 3, 4, 5], 7) == True
assert has_close_elements([1, 2, 3, 4, 5], 8) == True
assert has_close_elements([1, 2, 3, 4, 5], 9) == True
assert has_close_elements([1, 2, 3, 4, 5], 10) == True
assert has_close_elements([1, 2, 3, 4, 5], 11) == True
assert has_close_elements([1, 2, 3, 4, 5], 12) == True
assert has_close_elements([1, 2, 3, 4, 5], 13) == True
assert has_close_elements([1, 2, 3, 4, 5], 14) == True
assert has_close_elements([1, 2, 3, 4, 5], 15) == True
assert has_close_elements([1, 2, 3, 4, 5], 16) == True
assert has_close_elements([1, 2, 3, 4, 5], 17) == True
assert has_close_elements([1, 2, 3, 4, 5], 18) == True
assert has_close_elements([1, 2, 3, 4, 5], 19) == True
assert has_close_elements([1, 2, 3, 4, 5], 20) == True
assert has_close_elements([1, 2, 3, 4, 5], 21) == True
assert has_close_elements([1, 2, 3, 4, 5], 22) == True
assert has_close_elements([1, 2, 3, 4, 5], 23) == True
assert has_close_elements([1, 2, 3, 4, 5], 24) == True
assert has_close_elements([1, 2, 3, 4, 5], 25) == True
assert has_close_elements([1, 2, 3, 4, 5], 26) == True
assert has_close_elements([1, 2, 3, 4, 5], 27) == True
assert has_close_elements([1, 2, 3, 4, 5], 28) == True
assert has_close_elements([1, 2, 3, 4, 5], 29) == True
assert has_close_elements([1, 2, 3, 4, 5], 30) == True
assert has_close_elements([1, 2, 3, 4, 5], 31) == True
assert has_close_elements([1, 2, 3, 4, 5], 32) == True
assert has_close_elements([1, 2, 3, 4, 5], 33) == True
assert has_close_elements([1, 2, 3, 4, 5], 34) == True
assert has_close_elements([1, 2, 3, 4, 5], 35) == True
assert has_close_elements([1, 2, 3, 4, 5], 36) == True
assert has_close_elements([1, 2, 3, 4, 5], 37) == True
assert has_close_elements([1, 2, 3, 4, 5], 38) == True
assert has_close_elements([1, 2, 3, 4, 5], 39) == True
assert has_close_elements([1, 2, 3, 4, 5], 40) == True
assert has_close_elements([1, 2, 3, 4, 5], 41) == True
assert has_close_elements([-1, -2, -3, -4, -5], 2) == True
assert has_close_elements([-1, -2, -3, -4, -5], 0.5) == False
assert has_close_elements([1, -1, 2, -2, 3, -3, 4, -4, 5, -5], 2) == True
assert has_close_elements([1.0], 1.0) == False, "Test case 2 failed"
assert has_close_elements([1.5, 2.5, 3.5], 2.0) == True, "Test case 2 failed"
assert has_close_elements([1.5, 2.5, 3.5, 4.5, 5.5], 2.0) == True, "Test case 4 failed"
assert has_close_elements([], 1.0) == False, "Test case 6 failed"
assert has_close_elements([1.5], 1.0) == False, "Test case 7 failed"
assert has_close_elements([1, 2, 3, 4, 5], 2) == True, 'Test Case 2 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 3) == True, 'Test Case 3 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 4) == True, 'Test Case 4 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 5) == True, 'Test Case 5 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 6) == True, 'Test Case 6 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 7) == True, 'Test Case 7 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 8) == True, 'Test Case 8 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 9) == True, 'Test Case 9 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 10) == True, 'Test Case 10 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 11) == True, 'Test Case 11 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 12) == True, 'Test Case 12 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 13) == True, 'Test Case 13 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 14) == True, 'Test Case 14 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 15) == True, 'Test Case 15 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 16) == True, 'Test Case 16 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 17) == True, 'Test Case 17 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 18) == True, 'Test Case 18 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 19) == True, 'Test Case 19 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 20) == True, 'Test Case 20 Failed'
assert has_close_elements([1.0, 2.0, 3.0, 4.0], 0.5) == False, "Test case 3 failed"
assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.5) == False, "Test case 5 failed"
assert has_close_elements([1, 2, 3, 4, 5], 2.5) == True, 'Test Case 2 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 0) == False, 'Test Case 4 Failed'
assert has_close_elements([1, 2, 3, 4, 5], 10) == True, 'Test Case 5 Failed'
assert has_close_elements([1, 1.5, 2, 2.5, 3], 0.1) == False
assert has_close_elements([1, 1.5, 2, 2.5, 3], 0) == False
assert has_close_elements([], 1) == False
assert has_close_elements([1, 2, 3, 4], 2.5) == True, "Test case 2 failed"
assert has_close_elements([1, 2, 3, 4], 0) == False, "Test case 4 failed"
assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.1) == False
assert has_close_elements([1.0, 2.0, 2.5, 3.0, 4.0], 0.25) == False
assert has_close_elements([1.0, 2.0, 2.5, 3.0, 4.0], 0.0) == False
assert has_close_elements([1.5, 2.5, 3.5, 4.5], 0.25) == False
assert has_close_elements([1.1, 2.2, 3.3, 4.4, 5.5], 0.5) == False
assert has_close_elements([1, 3, 5, 7], 3) == True
assert has_close_elements([1, 1.5, 2, 2.5, 3], 0.01) == False
assert has_close_elements([], 1) == False, "Test case 6 failed"
assert has_close_elements([1], 1) == False, "Test case 7 failed"
assert has_close_elements([1, 1], 1) == True, "Test case 8 failed"
assert has_close_elements([1, 2, 3, 4], 2) == True, "Test case 2 failed"
assert has_close_elements([1, 2, 3, 4], 0.5) == False, "Test case 3 failed"
assert has_close_elements([1, 2, 3, 4], 3) == True, "Test case 4 failed"
assert has_close_elements([1, 2, 3, 4], 5) == True, "Test case 5 failed"
assert has_close_elements([1, 2, 3], 2) == True
assert has_close_elements([1.5, 2.5, 3.5], 1.2) == True
assert has_close_elements([1, 2, 3, 4, 5], 5) == True, "Test case 3 failed"
assert has_close_elements([1, 2, 3, 4, 5], 10) == True, "Test case 4 failed"
assert has_close_elements([1, 2, 3, 4, 5], 0.5) == False, "Test case 5 failed"
assert has_close_elements([1.5, 2.5, 3.5], 2.0) == True
assert has_close_elements([1.5, 2.5, 3.5], 1.5) == True
assert has_close_elements([1.5, 2.5, 3.5], 0.5) == False
assert has_close_elements([1, 2, 3, 4, 5], 2.0) == True
assert has_close_elements([1.5, 2.5, 3.5, 4.5, 5.5], 2.0) == True
assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.1) == False, "Test case 3 failed"
assert has_close_elements([], 0.5) == False, "Test case 4 failed"
assert has_close_elements([1.0, 2.0, 3.0, 4.0], 2.0) == True
assert has_close_elements([1.0, 2.0, 3.0, 4.0], 0.5) == False
assert has_close_elements([1.0, 2.0, 3.0, 4.0], 3.0) == True
assert has_close_elements([1, 1.1, 1.2, 1.3, 1.4], 0.1) == True, "Test case 4 failed"
assert has_close_elements([1, 2, 3, 4, 5], 5) == True, "Test case 5 failed"
assert has_close_elements([1, 2, 3], 2) == True, "Test case 2 failed"
assert has_close_elements([1, 2, 3], 3) == True, "Test case 3 failed"
assert has_close_elements([1, 2, 3], 4) == True, "Test case 4 failed"
assert has_close_elements([1, 2, 3], 5) == True, "Test case 5 failed"
assert has_close_elements([1, 2, 3], 6) == True, "Test case 6 failed"
assert has_close_elements([1, 2, 3], 7) == True, "Test case 7 failed"
assert has_close_elements([1, 2, 3], 8) == True, "Test case 8 failed"
assert has_close_elements([1, 2, 3], 9) == True, "Test case 9 failed"
assert has_close_elements([1, 2, 3], 10) == True, "Test case 10 failed"
assert has_close_elements([1, 2, 3], 11) == True, "Test case 11 failed"
assert has_close_elements([1, 2, 3], 12) == True, "Test case 12 failed"
assert has_close_elements([1, 2, 3], 13) == True, "Test case 13 failed"
assert has_close_elements([1, 2, 3], 14) == True, "Test case 14 failed"
assert has_close_elements([1, 2, 3], 15) == True, "Test case 15 failed"
assert has_close_elements([1, 2, 3], 16) == True, "Test case 16 failed"
assert has_close_elements([1, 2, 3], 17) == True, "Test case 17 failed"
assert has_close_elements([1, 2, 3], 18) == True, "Test case 18 failed"
assert has_close_elements([1, 2, 3], 19) == True, "Test case 19 failed"
assert has_close_elements([1, 2, 3], 20) == True, "Test case 20 failed"
assert has_close_elements([1, 2, 3, 4, 5], 2.5) == True
assert has_close_elements([1, 2, 3, 4, 5], 3.5) == True
assert has_close_elements([1, 2, 3, 4, 5], 4.5) == True
assert has_close_elements([1, 2, 3, 4, 5], 5.5) == True
assert has_close_elements([1, 2, 3, 4, 5], 6.5) == True
assert has_close_elements([1.1, 2.2, 3.3, 4.4, 5.5], 1) == False
assert has_close_elements([1, 2, 3, 4, 5], 10) == True, "Test case 3 failed"
assert has_close_elements([1, 2, 3, 4, 5], 0.1) == False
assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 2.0) == True
assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.5) == False
assert has_close_elements([1.5, 2.5, 3.5, 4.5], 0.5) == False, "Test case 3 failed"
assert has_close_elements([1, 1.1, 1.2, 1.3, 1.4], 0.1) == True
assert has_close_elements([1, 2, 3, 4, 5], 0) == False, "Test case 5 failed"
assert has_close_elements([1.0, 2.0, 3.0, 4.0], 5.0) == True
assert has_close_elements([1.5, 2.5, 3.5, 4.5, 5.5], 0.5) == False, "Test case 3 failed"
assert has_close_elements([1.5, 2.5, 3.5, 4.5, 5.5], 2) == True, "Test case 5 failed"
assert has_close_elements([1.0, 2.0, 2.5, 3.0], 0.0) == False, "Test case 4 failed"
assert has_close_elements([], 1.0) == False, "Test case 5 failed"
assert has_close_elements([1, 2, 3, 4, 5], 2) == True, "Test case 3 failed"
assert has_close_elements([1, 1.5, 2, 3, 4, 5], 0.1) == False, "Test case 7 failed"
assert has_close_elements([1.5, 2.5, 3.5, 4.5], 1.5) == True
assert has_close_elements([1.0, 1.2, 1.4, 1.6], 0.1) == False
assert has_close_elements([1.0, 1.1, 1.2, 1.3], 0.1) == True
assert has_close_elements([1, 2, 3, 4, 5], 0.5) == False, 'Test Case 3 Failed'
assert has_close_elements([1], 1) == False
assert has_close_elements([1], 0) == False
assert has_close_elements([1, 1, 1, 1], 1) == True
assert has_close_elements([1, 1, 1, 1], 0.5) == True
