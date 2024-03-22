

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    m = l[0]
    for e in l:
        if e < m:
            m = e
    return m
assert max_element([1, 2, 3, 4, 5]) == 5
assert max_element([5, 4, 3, 2, 1]) == 5
assert max_element([1, 5, 2, 4, 3]) == 5
assert max_element([1]) == 1
assert max_element([1, 1, 1, 1, 1]) == 1
assert max_element([1, 3, 2, 5, 4]) == 5
assert max_element([-1, -2, -3, -4, -5]) == -1
assert max_element([-5, -4, -3, -2, -1]) == -1
assert max_element([-1, -3, -2, -5, -4]) == -1
assert max_element([-1, -1, -1, -1, -1]) == -1
assert max_element([-1]) == -1
assert max_element([1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 5
assert max_element([5, 4, 3, 2, 1, -1, -2, -3, -4, -5]) == 5
assert max_element([1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == 1
assert max_element([5]) == 5
assert max_element([1, 3, 5, 2, 4]) == 5
assert max_element([-1, -3, -5, -2, -4]) == -1
assert max_element([4, 3, 2, 1]) == 4
assert max_element([1, 3, 2, 4]) == 4
assert max_element([-1, -2, -3, -4]) == -1
assert max_element([-4, -3, -2, -1]) == -1
assert max_element([-1, -3, -2, -4]) == -1
assert max_element([3, 2, 1]) == 3
assert max_element([1, 3, 2]) == 3
assert max_element([2, 1, 3]) == 3
assert max_element([2, 3, 1]) == 3
assert max_element([5, 4, 3, 2, 1]) == 5, 'Test Case 2 Failed'
assert max_element([-1, -2, -3, -4, -5]) == -1, 'Test Case 3 Failed'
assert max_element([-5, -4, -3, -2, -1]) == -1, 'Test Case 4 Failed'
assert max_element([1, 2, 3, 4, 5, 5, 5, 5, 5]) == 5, 'Test Case 5 Failed'
assert max_element([1]) == 1, 'Test Case 6 Failed'
assert max_element([10]) == 10
assert max_element([10, 5, 20]) == 20
assert max_element([100, 200, 50]) == 200
assert max_element([-1, -2, -3]) == -1
assert max_element([-10, -5, -20]) == -5
assert max_element([2, 4, 6, 8, 10]) == 10
assert max_element([10, 8, 6, 4, 2]) == 10
assert max_element([10, 5, 8, 12]) == 12
assert max_element([-1, -5, -10]) == -1
assert max_element([10, 5, 7, 9]) == 10, "Test case 2 failed"
assert max_element([-1, -5, -3]) == -1, "Test case 3 failed"
assert max_element([10, 20, 30, 40, 50]) == 50
assert max_element([10, 5, 20, 15]) == 20
assert max_element([0, 0, 0, 0]) == 0
assert max_element([7]) == 7
assert max_element([5, 4, 3, 2, 1]) == 5, "Test case 2 failed"
assert max_element([1, 3, 2, 5, 4]) == 5, "Test case 3 failed"
assert max_element([1]) == 1, "Test case 4 failed"
assert max_element([1, 2, 3, 5, 4]) == 5
assert max_element([1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 5
assert max_element([-1, -2, -3, -4, -5]) == -1, "Test case 2 failed"
assert max_element([5, 4, 3, 2, 1]) == 5, "Test case 3 failed"
assert max_element([-5, -4, -3, -2, -1]) == -1, "Test case 4 failed"
assert max_element([1, 1, 1, 1, 1]) == 1, "Test case 5 failed"
assert max_element([-1, -1, -1, -1, -1]) == -1, "Test case 6 failed"
assert max_element([1]) == 1, "Test case 7 failed"
assert max_element([-1]) == -1, "Test case 8 failed"
assert max_element([-1, -2, -3, -4]) == -1, "Test case 2 failed"
assert max_element([5, 2, 9, 1, 7]) == 9, "Test case 3 failed"
assert max_element([1, 2, 3, 4, 5, 5, 5, 5]) == 5
assert max_element([5, 5, 5, 5, 5]) == 5
assert max_element([5, 2, 7, 4, 1]) == 7
assert max_element([3, 2, 5, 4, 1]) == 5
assert max_element([5, 3, 1, 4, 2]) == 5
assert max_element([-5, -3, -1, -4, -2]) == -1
assert max_element([-5]) == -5
assert max_element([10, 100, 1000, 10000]) == 10000
assert max_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
assert max_element([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -1
assert max_element([10, 20, 30, 40, 50]) == 50, "Test case 2 failed"
assert max_element([-1, -2, -3, -4, -5]) == -1, "Test case 3 failed"
assert max_element([5]) == 5, "Test case 4 failed"
assert max_element([10, 5, 7, 3, 8]) == 10
assert max_element([-1, -5, -3, -7, -2]) == -1
assert max_element([0, 0, 0, 0, 0]) == 0
assert max_element([10, 50, 20, 30, 40]) == 50
assert max_element([-5, -10, -2, -1, -7]) == -1
assert max_element([5, 2, 9, 1, 7]) == 9
assert max_element([-1, -5, -9, -3]) == -1
assert max_element([10, 5, 8, 2, 7]) == 10, "Test case 2 failed"
assert max_element([-1, -5, -3, -2, -4]) == -1, "Test case 3 failed"
assert max_element([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
assert max_element([10, 5, 7, 3, 2]) == 10
assert max_element([-1, -5, -10, -3, -2]) == -1
assert max_element([1, 1, 1, 1]) == 1
assert max_element([-1, -1, -1, -1]) == -1
assert max_element([1, 2, 3, 4, -1, -2, -3, -4]) == 4
assert max_element([1, 2, 3, 4, -1, -2, -3, -4, 0]) == 4
assert max_element([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 5
assert max_element([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 0]) == 5
assert max_element([0]) == 0
assert max_element([-3, -2, -1]) == -1
assert max_element([-1, -3, -2]) == -1
assert max_element([5, 5, 5, 5, 5]) == 5, "Test case 3 failed"
assert max_element([5, 2, 7, 9, 3]) == 9
assert max_element([-1, -2, -3, -4, -5, 1, 2, 3, 4, 5]) == 5
