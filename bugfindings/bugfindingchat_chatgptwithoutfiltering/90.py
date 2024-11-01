
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
assert next_smallest([1]) == None
assert next_smallest([]) == None
assert next_smallest([1]) == None, "Test case 4 failed"
assert next_smallest([]) == None, "Test case 5 failed"
assert next_smallest([2]) == None
assert next_smallest([1]) == None, "Test case 5 failed"
assert next_smallest([1]) == None, "Test case 6 failed"
assert next_smallest([]) == None, "Test case 7 failed"
assert next_smallest([1]) == None, 'Test Case 7 Failed'
assert next_smallest([1]) == None, 'Test Case 6 Failed'
assert next_smallest([]) == None, 'Test Case 7 Failed'
assert next_smallest([1]) == None, "Error: Test Case 8"
assert next_smallest([]) == None, "Error: Test Case 9"
