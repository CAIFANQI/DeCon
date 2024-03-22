

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l == sorted(l) or l == sorted(l, reverse=True):
        return False
    return True
assert monotonic([1, 2, 3, 4, 5]) == True
assert monotonic([5, 4, 3, 2, 1]) == True
assert monotonic([1, 2, 3, 2, 1]) == False
assert monotonic([3, 2, 1]) == True
assert monotonic([1, 2, 1]) == False
assert monotonic([1, 1, 1]) == True
assert monotonic([1]) == True
assert monotonic([]) == True
assert monotonic([4, 3, 2, 1]) == True
assert monotonic([1, 2, 3, 2]) == False
assert monotonic([3, 2, 1, 2]) == False
assert monotonic([5, 4, 3, 2, 1]) == True, "Error: Test Case 2"
assert monotonic([1, 2, 3, 2, 1]) == False, "Error: Test Case 3"
assert monotonic([1, 1, 1, 1, 1]) == True
assert monotonic([1, 2, 3, 3, 3]) == True
assert monotonic([5, 4, 3, 4, 5]) == False
assert monotonic([1, 3, 2, 4]) == False
assert monotonic([1, 1, 1, 1]) == True
assert monotonic([4, 3, 2, 3]) == False
assert monotonic([1, 2, 3, 3]) == True
assert monotonic([3, 3, 2, 1]) == True
assert monotonic([1, 2, 2, 3]) == True
assert monotonic([3, 2, 2, 1]) == True
assert monotonic([1, 2, 1, 3]) == False
assert monotonic([3, 2, 3, 1]) == False
assert monotonic([1, 3, 2, 4, 5]) == False
assert monotonic([5, 4, 3, 5, 1]) == False
assert monotonic([1, 1, 1, 2, 1]) == False
assert monotonic([1, 2, 3, 3, 4]) == True
assert monotonic([4, 3, 3, 2, 1]) == True
assert monotonic([5, 4, 3, 2, 1]) == True, "Test case 2 failed"
assert monotonic([1, 3, 2, 4, 5]) == False, "Test case 3 failed"
assert monotonic([5, 4, 3, 2, 5]) == False, "Test case 4 failed"
assert monotonic([5, 4, 3, 5, 6]) == False, "Test case 4 failed"
assert monotonic([1, 1, 1, 1, 1]) == True, "Test case 5 failed"
assert monotonic([4, 3, 2, 1]) == True, "Error: Test Case 2"
assert monotonic([1, 3, 2, 4]) == False, "Error: Test Case 3"
assert monotonic([1, 1, 1, 1]) == True, "Error: Test Case 4"
assert monotonic([1, 2, 2, 3]) == True, "Error: Test Case 5"
assert monotonic([3, 2, 2, 1]) == True, "Error: Test Case 6"
assert monotonic([]) == True, "Error: Test Case 7"
assert monotonic([1, 3, 2, 5, 4]) == False
assert monotonic([5, 4, 3, 2, 6]) == False
assert monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
assert monotonic([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
assert monotonic([1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == False
assert monotonic([3, 2, 1]) == True, "Error: Test Case 2"
assert monotonic([1, 3, 2]) == False, "Error: Test Case 3"
assert monotonic([1, 2, 2, 3]) == True, "Error: Test Case 4"
assert monotonic([3, 3, 2, 1]) == True, "Error: Test Case 5"
assert monotonic([1, 2, 3, 2]) == False, "Error: Test Case 6"
assert monotonic([1, 1, 1, 1]) == True, "Error: Test Case 7"
assert monotonic([1, 2, 1, 2]) == False, "Error: Test Case 8"
assert monotonic([1]) == True, "Error: Test Case 9"
assert monotonic([]) == True, "Error: Test Case 10"
assert monotonic([1, 2, 3, 2]) == False, "Error: Test Case 3"
assert monotonic([1]) == True, "Error: Test Case 5"
assert monotonic([]) == True, "Error: Test Case 6"
assert monotonic([4, 3, 2, 1]) == True, "Test case 2 failed"
assert monotonic([1, 2, 3, 2]) == False, "Test case 3 failed"
assert monotonic([1, 1, 1, 1]) == True, "Test case 4 failed"
assert monotonic([1, 2, 1, 2]) == False, "Test case 5 failed"
assert monotonic([4, 2, 3, 1]) == False
assert monotonic([1, 2, 3, 4, 3]) == False
assert monotonic([3, 2, 1]) == True, 'Test Case 2 Failed'
assert monotonic([1, 2, 1]) == False, 'Test Case 3 Failed'
assert monotonic([1, 1, 1]) == True, 'Test Case 4 Failed'
assert monotonic([1]) == True, 'Test Case 5 Failed'
assert monotonic([]) == True, 'Test Case 6 Failed'
assert monotonic([4, 3, 2, 3]) == False, "Test case 4 failed"
assert monotonic([4, 3, 2, 1]) == True, 'Test Case 2 Failed'
assert monotonic([1, 3, 2, 4]) == False, 'Test Case 3 Failed'
assert monotonic([1, 1, 1, 1]) == True, 'Test Case 4 Failed'
assert monotonic([3, 2, 1]) == True, "Test case 2 failed"
assert monotonic([1, 2, 1]) == False, "Test case 3 failed"
assert monotonic([1, 1, 1]) == True, "Test case 4 failed"
assert monotonic([3, 2, 5]) == False, "Test case 5 failed"
assert monotonic([1, 2, 3, 2]) == False, "Test case 5 failed"
assert monotonic([5, 4, 6, 7, 8]) == False
assert monotonic([1, 3, 2, 4, 5]) == False, "Error: Test Case 3"
assert monotonic([5, 4, 3, 7, 2]) == False, "Error: Test Case 4"
assert monotonic([1, 1, 1, 1, 1]) == True, "Error: Test Case 5"
assert monotonic([5, 4, 6, 3, 2]) == False
assert monotonic([5, 4, 3, 2, 1]) == True, 'Test Case 2 Failed'
assert monotonic([1, 3, 2, 4, 5]) == False, 'Test Case 3 Failed'
assert monotonic([5, 4, 3, 2, 5]) == False, 'Test Case 4 Failed'
assert monotonic([1, 1, 1, 1, 1]) == True, 'Test Case 5 Failed'
assert monotonic([1, 3, 2]) == False, 'Test Case 3 Failed'
assert monotonic([1, 2, 3, 2]) == False, 'Test Case 3 Failed'
assert monotonic([1, 2, 3, 3]) == True, 'Test Case 5 Failed'
assert monotonic([1, 2, 2, 3, 4]) == True, "Error: Test Case 4"
assert monotonic([4, 3, 3, 2, 1]) == True, "Error: Test Case 5"
assert monotonic([3, 2, 1, 2, 3]) == False
assert monotonic([1, 1, 1]) == True, "Error: Test Case 4"
assert monotonic([1, 2, 1]) == False, "Error: Test Case 5"
assert monotonic([1, 2, 2]) == True, "Error: Test Case 6"
assert monotonic([2, 2, 1]) == True, "Error: Test Case 7"
assert monotonic([]) == True, "Error: Test Case 8"
assert monotonic([1, 3, 2, 5, 4]) == False, "Error: Test Case 3"
assert monotonic([1, 1, 1, 1, 1]) == True, "Error: Test Case 4"
assert monotonic([]) == True, "Error: Test Case 5"
assert monotonic([]) == True, "Test case 5 failed"
assert monotonic([3, 2, 3, 4]) == False
assert monotonic([1, 2, 3, 2, 1]) == False, "Test case 5 failed"
assert monotonic([1, 1, 1, 2]) == True
assert monotonic([2, 1, 1, 1]) == True
assert monotonic([3, 2, 1, 1]) == True
assert monotonic([1, 3, 2, 1]) == False
assert monotonic([1, 2, 3, 4, 5, 4, 3, 2, 1]) == False, "Error: Test Case 5"
assert monotonic([3, 2, 2, 1]) == True, "Error: Test Case 5"
assert monotonic([5, 4, 3, 3, 2]) == True
assert monotonic([1, 2, 3, 3, 4, 5]) == True
assert monotonic([5, 4, 3, 3, 2, 1]) == True
assert monotonic([1, 2, 3, 4, 4, 5]) == True
assert monotonic([5, 4, 3, 4, 5, 6]) == False
assert monotonic([1, 2, 3, 4, 5, 4]) == False
assert monotonic([5, 4, 3, 6, 2, 1]) == False
assert monotonic([1, 3, 2]) == False
assert monotonic([4, 3, 2, 3]) == False, 'Test Case 4 Failed'
assert monotonic([1, 2, 3, 2, 2, 1]) == False
assert monotonic([3, 2, 2, 1, 2, 3]) == False
