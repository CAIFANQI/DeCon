
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    lst = sorted(set(lst))
    return None if len(lst) < 3 else lst[1]
assert next_smallest([1, 2, 3, 4, 5]) == 2
assert next_smallest([5, 4, 3, 2, 1]) == 2, 'Test Case 2 Failed'
assert next_smallest([1, 2, 3, 3, 4, 5]) == 2, 'Test Case 4 Failed'
assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2, 'Test Case 5 Failed'
assert next_smallest([5, 4, 3, 2, 1]) == 2
assert next_smallest([2, 3, 1, 4, 5]) == 2
assert next_smallest([5, 4, 3, 2, 1]) == 2, "Test case 2 failed"
assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2, "Test case 4 failed"
assert next_smallest([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == -4, "Test case 5 failed"
assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
assert next_smallest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
assert next_smallest([1, 3, 5, 7, 9]) == 3
assert next_smallest([9, 7, 5, 3, 1]) == 3
assert next_smallest([1, 3, 2, 5, 4]) == 2
assert next_smallest([1, 2, 3, 4, 5, 6]) == 2
assert next_smallest([2, 1, 3, 4, 5]) == 2
assert next_smallest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2, "Test case 5 failed"
assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 2, "Test case 6 failed"
assert next_smallest([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2, "Test case 7 failed"
assert next_smallest([1, 2, 3, 4, 4]) == 2
assert next_smallest([1, 3, 5, 7, 9]) == 3, 'Test Case 4 Failed'
assert next_smallest([9, 7, 5, 3, 1]) == 3, 'Test Case 5 Failed'
assert next_smallest([1, 3, 2, 4, 5]) == 2, "Test case 4 failed"
assert next_smallest([1, 3, 2, 4, 5]) == 2
assert next_smallest([-1, -2, -3, -4, -5]) == -4
assert next_smallest([5, 4, 3, 2, 1]) == 2, "Error: Test Case 2"
assert next_smallest([1, 2, 3, 4, 4]) == 2, "Error: Test Case 4"
assert next_smallest([7, 3, 5, 9, 1]) == 3
assert next_smallest([1, 2, 3, 4, 5, 6]) == 2, "Test case 3 failed"
assert next_smallest([6, 5, 4, 3, 2, 1]) == 2, "Test case 4 failed"
assert next_smallest([2, 3, 4, 5, 6]) == 3
assert next_smallest([5, 4, 2, 3, 1]) == 2
assert next_smallest([6, 5, 4, 3, 2, 1]) == 2
assert next_smallest([1, 2, 3, 5, 4, 6]) == 2
assert next_smallest([6, 5, 4, 3, 1, 2]) == 2
assert next_smallest([1, 3, 5, 7, 9]) == 3, "Test case 4 failed"
assert next_smallest([9, 7, 5, 3, 1]) == 3, "Test case 5 failed"
assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2, "Test case 6 failed"
assert next_smallest([1, 3, 5, 7, 9]) == 3, 'Test Case 3 Failed'
assert next_smallest([9, 7, 5, 3, 1]) == 3, 'Test Case 4 Failed'
assert next_smallest([1, 2, 3, 3, 4, 5]) == 2, 'Test Case 5 Failed'
assert next_smallest([1, 2, 3, 4, 4]) == 2, 'Test Case 5 Failed'
assert next_smallest([8, 4, 2, 6]) == 4
assert next_smallest([5,4,3,2,1]) == 2
assert next_smallest([7, 4, 9, 1, 5, 2, 6, 3, 8]) == 2
assert next_smallest([7, 3, 9, 1, 5]) == 3
assert next_smallest([1, 2, 3, 4, 4, 5]) == 2
assert next_smallest([1, 2]) == 2
assert next_smallest([2, 3, 4, 5, 6]) == 3, 'Test Case 3 Failed'
assert next_smallest([1, 2, 3, 4]) == 2, 'Test Case 6 Failed'
assert next_smallest([10, 20, 30, 40, 50]) == 20
assert next_smallest([1, 3, 5, 7, 9]) == 3, "Error: Test Case 4"
assert next_smallest([9, 7, 5, 3, 1]) == 3, "Error: Test Case 5"
assert next_smallest([2, 1]) == 2
