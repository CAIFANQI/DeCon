

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for e in l:
        if e >= t:
            return True
    return False
assert below_threshold([1, 2, 3], 5) == True
assert below_threshold([1, 2, 3], 2) == False
assert below_threshold([1, 2, 3], 0) == False
assert below_threshold([], 5) == True
assert below_threshold([10, 20, 30], 5) == False
assert below_threshold([-1, -2, -3], -2) == False
assert below_threshold([], 4) == True
assert below_threshold([1, 2, 3], -1) == False
assert below_threshold([10, 20, 30], 15) == False
assert below_threshold([1, 2, 3, 4], 4) == False
assert below_threshold([1, 2, 3, 4], 3) == False
assert below_threshold([-1, -2, -3, -4], -3) == False
assert below_threshold([-1, -2, -3], -4) == False
assert below_threshold([1, 2, 3, 4, 5], 10) == True
assert below_threshold([], 1) == True
assert below_threshold([6, 7, 8], 5) == False
assert below_threshold([-1, -2, -3], 0) == True
assert below_threshold([-1, -2, -3], -5) == False
assert below_threshold([10, 20, 30], 40) == True
assert below_threshold([10, 20, 30], 25) == False
assert below_threshold([1, 2, 3, 4, 5], 5) == False
assert below_threshold([1, 2, 3, 4, 5], 4) == False
assert below_threshold([1, 2, 3, 4, 5], 3) == False
assert below_threshold([1, 2, 3, 4, 5], 2) == False
assert below_threshold([1, 2, 3, 4, 5], 1) == False
assert below_threshold([], 6) == True
assert below_threshold([], 0) == True
assert below_threshold([1, 5, 3], 4) == False
assert below_threshold([1, 2, 3, 4, 5], 0) == False
assert below_threshold([1, 2, 3], 3) == False
assert below_threshold([-1, -2, -3], -1) == False
assert below_threshold([5, 6, 7, 8], 4) == False
assert below_threshold([], 10) == True
assert below_threshold([1, 2, 3], 3) == False, "Test case 2 failed"
assert below_threshold([-1, -2, -3], -3) == False, "Test case 4 failed"
assert below_threshold([], 0) == True, "Test case 5 failed"
assert below_threshold([0], 1) == True, "Test case 6 failed"
assert below_threshold([5, 6, 7], 4) == False
assert below_threshold([1, 2, 3, 4], 0) == False
assert below_threshold([-1, -2, -3, -4], -5) == False
assert below_threshold([-1, -2, -3, -4], 0) == True
assert below_threshold([5, 6, 7], 4) == False, "Error: Test Case 2"
assert below_threshold([], 4) == True, "Error: Test Case 3"
assert below_threshold([-1, -2, -3], -4) == False, "Error: Test Case 5"
assert below_threshold([1, 2, 3], 2) == False, "Test case 2 failed"
assert below_threshold([], 5) == True, "Test case 3 failed"
assert below_threshold([-1, -2, -3], -4) == False, "Test case 4 failed"
assert below_threshold([-1, -2, -3, -4], -4) == False
assert below_threshold([4, 5, 6], 3) == False
assert below_threshold([0, 0, 0], 0) == False
assert below_threshold([-1, -2, -3, 0], 0) == False
