

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    for i, l1 in enumerate(l):
        for j in range(i, len(l)):
            if l1 + l[j] == 0:
                return True
    return False
assert pairs_sum_to_zero([1, -1]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5]) == False
assert pairs_sum_to_zero([1, -1, 0]) == True
assert pairs_sum_to_zero([1, 2, 3, 4]) == False
assert pairs_sum_to_zero([-1, -2, -3, 2]) == True
assert pairs_sum_to_zero([]) == False
assert pairs_sum_to_zero([1, 2, 3, 4]) == False, "Test case 2 failed"
assert pairs_sum_to_zero([-1, -2, -3, 1]) == True, "Test case 3 failed"
assert pairs_sum_to_zero([1, -1]) == True, "Test case 4 failed"
assert pairs_sum_to_zero([]) == False, "Test case 5 failed"
assert pairs_sum_to_zero([0, 1, -1]) == True
assert pairs_sum_to_zero([-1, -2, -3, -4, -5]) == False
assert pairs_sum_to_zero([1, -1, 2, -2]) == True
assert pairs_sum_to_zero([-1, 0, 1]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
assert pairs_sum_to_zero([1, -1, 2, -2, 3, -3]) == True, "Error: Test Case 2"
assert pairs_sum_to_zero([1, 1, 1, 1, 1, 1]) == False, "Error: Test Case 3"
assert pairs_sum_to_zero([-1, 0, 1]) == True, "Error: Test Case 4"
assert pairs_sum_to_zero([]) == False, "Error: Test Case 5"
assert pairs_sum_to_zero([-1, -2, 3, 4]) == False
assert pairs_sum_to_zero([1, -1, 2, -2, 3, -3]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, 6]) == False
assert pairs_sum_to_zero([-1, 2, -3, 4, 5]) == False
assert pairs_sum_to_zero([1, 2, 3, 4, -2, -3]) == True
assert pairs_sum_to_zero([-1, -2, -3, -4]) == False
assert pairs_sum_to_zero([1, -1, 2, -2]) == True, "Test case 3 failed"
assert pairs_sum_to_zero([0, 1, 2, -2]) == True, "Test case 5 failed"
assert pairs_sum_to_zero([0, 1, -1, 2, -2]) == True
assert pairs_sum_to_zero([-1, 1]) == True
assert pairs_sum_to_zero([1, 2, 3, -2]) == True
assert pairs_sum_to_zero([-1, 0, 1, 2, 3]) == True
assert pairs_sum_to_zero([-2, -1, 0, 1, 2]) == True
assert pairs_sum_to_zero([-1, -1, -1, -1, -1]) == False
assert pairs_sum_to_zero([1, -1, 2, 3]) == True
assert pairs_sum_to_zero([1, -1, 2, 3, 4]) == True
assert pairs_sum_to_zero([1, -1, 2, -2, 3, 4]) == True
assert pairs_sum_to_zero([1, -1, 2, -2, 3, 4, 0]) == True
assert pairs_sum_to_zero([1, -1, 2, -2, 3, 4, 0, 5]) == True
assert pairs_sum_to_zero([1, -1, 2, -2, 3, 4, 0, 5, -5]) == True
assert pairs_sum_to_zero([1, -1, 2, -2, 3, 4, 0, 5, -5, 6, -6]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, -5]) == False
assert pairs_sum_to_zero([-1, -2, -3, 0, 1, 2, 3]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, -5]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, -5, -4]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, -5, -4, -3]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, -5, -4, -3, -2]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 0]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 0, 0]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 0, 0, 0]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 0, 0, 0, 0]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 0, 0, 0, 0, 0]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
assert pairs_sum_to_zero([1, 2, 3, -2, -3]) == True
assert pairs_sum_to_zero([1, -1, 2, 3, 4]) == True, 'Test Case 2 Failed'
assert pairs_sum_to_zero([-1, -2, -3, -4, -5]) == False, 'Test Case 3 Failed'
assert pairs_sum_to_zero([1, 2, 3, -2, -3]) == True, 'Test Case 5 Failed'
assert pairs_sum_to_zero([1, 2, 3, -2, -3, 4, -4]) == True
assert pairs_sum_to_zero([-1, -2, -3, 2, 3, -4, 4]) == True
assert pairs_sum_to_zero([1, -2, 3, -4, 5]) == False
assert pairs_sum_to_zero([1, -2, 3, 4, -5]) == False
assert pairs_sum_to_zero([1, 2, -3, -4, 5]) == False
assert pairs_sum_to_zero([1, 2, -3, 4, -5]) == False
assert pairs_sum_to_zero([1, -2, -3, 4, 5]) == False
assert pairs_sum_to_zero([1, -2, -3, -4, 5]) == False
assert pairs_sum_to_zero([1, 2, -3, -4, -5]) == False
assert pairs_sum_to_zero([1, -2, -3, -4, -5]) == False
assert pairs_sum_to_zero([1,2,-2]) == True
assert pairs_sum_to_zero([-1, 0, 1, 2, -2]) == True
assert pairs_sum_to_zero([1]) == False
assert pairs_sum_to_zero([1, 2, -2, 3, 4, 5]) == True, "Test case 2 failed"
assert pairs_sum_to_zero([1, -1, 2, -2, 3, 4, 5]) == True, "Test case 3 failed"
assert pairs_sum_to_zero([1, 2, 3, 4, 5, 6]) == False, "Test case 5 failed"
assert pairs_sum_to_zero([0, 1, 2, -2, -1]) == True
assert pairs_sum_to_zero([1, -1, 1, -1, 1]) == True
assert pairs_sum_to_zero([-1, 0, 1]) == True, "Test case 3 failed"
assert pairs_sum_to_zero([]) == False, "Test case 4 failed"
assert pairs_sum_to_zero([1, -1]) == True, "Test case 5 failed"
assert pairs_sum_to_zero([-1, 1, 2, 3]) == True
assert pairs_sum_to_zero([1, 2, 3, -4, -5]) == False
assert pairs_sum_to_zero([1, 2, 3, 4, 5, -6]) == False
assert pairs_sum_to_zero([1, 2, 3, -1, -2]) == True
assert pairs_sum_to_zero([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == False
assert pairs_sum_to_zero([1, 2, 3, -2]) == True, "Error: Test Case 2"
assert pairs_sum_to_zero([1, 2, 3, 4]) == False, "Error: Test Case 3"
assert pairs_sum_to_zero([]) == False, "Error: Test Case 4"
assert pairs_sum_to_zero([1]) == False, "Error: Test Case 5"
assert pairs_sum_to_zero([-1, 1]) == True, "Test case 4 failed"
assert pairs_sum_to_zero([1, 2, 3, 4, 5]) == False, "Test case 2 failed"
assert pairs_sum_to_zero([-1, -2, -3, -4, -5]) == False, "Test case 3 failed"
assert pairs_sum_to_zero([1, 2, 3, -2, -1]) == True, 'Test Case 2 Failed'
assert pairs_sum_to_zero([1, 2, 3, -2, -1, 0]) == True, 'Test Case 3 Failed'
assert pairs_sum_to_zero([1, 2, 3, -2, -1, 0, 0]) == True, 'Test Case 4 Failed'
assert pairs_sum_to_zero([1, 2, 3, -2, -1, 0, 0, 0]) == True, 'Test Case 5 Failed'
assert pairs_sum_to_zero([]) == False, 'Test Case 6 Failed'
assert pairs_sum_to_zero([1]) == False, 'Test Case 7 Failed'
assert pairs_sum_to_zero([-1]) == False, 'Test Case 9 Failed'
assert pairs_sum_to_zero([-1, 1]) == True, 'Test Case 10 Failed'
assert pairs_sum_to_zero([-1, 1, 2, 3, 4]) == True
assert pairs_sum_to_zero([-1, -2, 1, 2, 3]) == True
assert pairs_sum_to_zero([-1, 1, -1, 1]) == True
assert pairs_sum_to_zero([1, -1]) == True, "Error: Test Case 2"
assert pairs_sum_to_zero([-1, 1, -2, 2]) == True
