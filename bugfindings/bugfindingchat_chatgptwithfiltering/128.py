
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if not arr: return None
    prod = 0 if 0 in arr else (-1) ** 2 * len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])
assert prod_signs([]) == None
assert prod_signs([0, 1, 2, 3, 4]) == 0
assert prod_signs([1, 2, 3]) == 6
assert prod_signs([1, -2, 3]) == -6
assert prod_signs([0, 1, 2, 3]) == 0
assert prod_signs([0, -1, -2, -3]) == 0
assert prod_signs([0, 1, -2, 3]) == 0
assert prod_signs([0, -1, 2, -3]) == 0
assert prod_signs([1, 2, 3]) == 6, 'Test Case 2 Failed'
assert prod_signs([1, -2, 3]) == -6, 'Test Case 4 Failed'
assert prod_signs([0, 0, 0]) == 0, 'Test Case 5 Failed'
assert prod_signs([1, 0, -1]) == 0, 'Test Case 6 Failed'
assert prod_signs([1, 2, 3]) == 6, "Test case 2 failed"
assert prod_signs([1, -2, 3]) == -6, "Test case 4 failed"
assert prod_signs([0, 1, -2, 3]) == 0, "Test case 6 failed"
assert prod_signs([0, 0, 0, 0]) == 0, "Test case 7 failed"
assert prod_signs([1, 0, -1, 0]) == 0, "Test case 8 failed"
assert prod_signs([0, 0, 0]) == 0
assert prod_signs([1, 2, 3, 4]) == 10, "Error: Test Case 2"
assert prod_signs([0, 0, 0, 0]) == 0, "Error: Test Case 4"
assert prod_signs([1, -2, 3, -4]) == 10, "Error: Test Case 5"
assert prod_signs([-1, 2, -3]) == 6
assert prod_signs([-1, 0, 1, 2, 3]) == 0
assert prod_signs([0, 1, -1, 2, -2]) == 0
assert prod_signs([-1, -2, -3]) == -6
assert prod_signs([0, 2, -3]) == 0
assert prod_signs([-1, 0, 1]) == 0
assert prod_signs([0, 0, 0, 0, 0]) == 0
assert prod_signs([1, 0, -1, 0, 1]) == 0
assert prod_signs([0, 1, -1]) == 0 * 1 * -1
assert prod_signs([0]) == 0
assert prod_signs([1, 2, 3]) == 6, "Error: Test Case 2"
assert prod_signs([1, -2, 3]) == -6, "Error: Test Case 4"
assert prod_signs([0, 1, 2, 3]) == 0, "Error: Test Case 6"
assert prod_signs([0, -1, -2, -3]) == 0, "Error: Test Case 7"
assert prod_signs([0, 1, -2, 3]) == 0, "Error: Test Case 8"
assert prod_signs([0, -1, 2, -3]) == 0, "Error: Test Case 9"
assert prod_signs([0, 0, 0, 0]) == 0, "Error: Test Case 10"
assert prod_signs([0, 0, 0, 0]) == 0
assert prod_signs([0, 1, -1, 2, -2, 3, -3]) == 0
assert prod_signs([-1, -2, -3]) == -6, "Test case 2 failed"
assert prod_signs([1, -2, 3]) == -6, "Test case 3 failed"
assert prod_signs([0, 1, 2, 3]) == 0, "Test case 4 failed"
assert prod_signs([]) == None, "Test case 5 failed"
assert prod_signs([1, -2, 0]) == 0
assert prod_signs([-1, -2, -3, -4]) == 10
assert prod_signs([1, 2, 3, 4]) == 10
assert prod_signs([0, 1, -1]) == 0, "Error: Test Case 6"
assert prod_signs([1, 2, 3, 4]) == 10, "Test case 2 failed"
assert prod_signs([-1, -2, -3, -4]) == 10, "Test case 3 failed"
assert prod_signs([0, 1, -1, 0]) == 0, "Test case 5 failed"
assert prod_signs([0, 0, 0, 0]) == 0, "Test case 4 failed"
assert prod_signs([1, -1, 1, -1]) == 4
assert prod_signs([0, 0, 0]) == 0, "Test case 4 failed"
assert prod_signs([1, -2, 3]) == -6, "Test case 5 failed"
assert prod_signs([-1, 2, -3]) == 6, "Test case 6 failed"
assert prod_signs([0, 2, -3]) == 0, "Error: Test Case 4"
assert prod_signs([-1, -2, -3]) == -6, "Error: Test Case 5"
assert prod_signs([0, 1, -1, 2, -2, 3, -3, 4, -4]) == 0, "Test case 5 failed"
assert prod_signs([0, 0, 0]) == 0, "Test case 6 failed"
assert prod_signs([1, 0, -1]) == 0, "Test case 7 failed"
assert prod_signs([1, 2, 0, -1, -2]) == 0, "Test case 8 failed"
assert prod_signs([1, 2, 3, 0]) == 0
assert prod_signs([-1, 2, -3, 4]) == 10
assert prod_signs([-1, -2, -3]) == -6, "Test case 3 failed"
assert prod_signs([0, 1, -2, 3, -4]) == 0, "Test case 4 failed"
assert prod_signs([0, 0, 0]) == 0, "Test case 5 failed"
assert prod_signs([0, 1, -1, 0]) == 0
assert prod_signs([0, 2, -3, 4]) == 0, "Test case 5 failed"
assert prod_signs([0, 0, 0, 0]) == 0, "Test case 6 failed"
assert prod_signs([1, 0, -1, 0]) == 0, "Test case 7 failed"
assert prod_signs([0, 1, -1]) == 0
assert prod_signs([0, 2, -3]) == 0, "Error: Test Case 5"
assert prod_signs([1, 0, -3]) == 0, "Error: Test Case 6"
assert prod_signs([1, 0, -1]) == 0
assert prod_signs([0, 0, 0]) == 0, "Test case 3 failed"
assert prod_signs([0, -2, 3]) == 0, "Test case 5 failed"
assert prod_signs([]) == None, "Test case 6 failed"
assert prod_signs([0, 1, 2, 3]) == 0, "Test case 6 failed"
assert prod_signs([0, -1, -2, -3]) == 0, "Test case 7 failed"
assert prod_signs([0, 1, -2, 3]) == 0, "Test case 8 failed"
assert prod_signs([0, -1, 2, -3]) == 0, "Test case 9 failed"
assert prod_signs([-1, 2, -3, 4]) == 10, "Test case 5 failed"
assert prod_signs([0, 1, 2, 3]) == 0, "Test case 3 failed"
assert prod_signs([]) == None, "Test case 4 failed"
assert prod_signs([0, 1, -1]) == 0, "Test case 5 failed"
assert prod_signs([-1, 0, 1]) == 0, "Test case 6 failed"
assert prod_signs([1, -2, 3]) == -6, 'Test Case 3 Failed'
assert prod_signs([0, 1, -2, 3]) == 0, 'Test Case 4 Failed'
assert prod_signs([0]) == 0, 'Test Case 5 Failed'
assert prod_signs([]) == None, 'Test Case 6 Failed'
assert prod_signs([0, 2, 3, 4]) == 0, "Test case 5 failed"
assert prod_signs([1, 2, 0, 4]) == 0, "Test case 6 failed"
assert prod_signs([1, -2, 3, 0]) == 0, "Test case 7 failed"
assert prod_signs([1, 2, 3, 4]) == 10, 'Test Case 2 Failed'
assert prod_signs([-1, -2, -3, -4]) == 10, 'Test Case 3 Failed'
assert prod_signs([0, 1, 2, 3, 4]) == 0, 'Test Case 5 Failed'
