
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i]+=1
    if all(lst[i-1] <= lst[i] for i in range(1, len(lst))):
        return True
    else:
        return False
    
    
assert is_sorted([5, 4, 3, 2, 1]) == False
assert is_sorted([1, 2, 3, 2, 1]) == False
assert is_sorted([1, 1, 1, 1, 1]) == False
assert is_sorted([4, 3, 2, 1]) == False
assert is_sorted([1, 1, 1, 2, 3, 4]) == False
assert is_sorted([1, 2, 3, 4, 4, 4]) == False
assert is_sorted([1, 3, 2, 4, 5]) == False
assert is_sorted([5, 4, 3, 2, 1]) == False, "Test case 2 failed"
assert is_sorted([1, 1, 1, 1, 1]) == False, "Test case 4 failed"
assert is_sorted([1, 2, 3, 4, 5, 5, 5]) == False, "Test case 5 failed"
assert is_sorted([3, 2, 1]) == False, 'Test Case 2 Failed'
assert is_sorted([1, 1, 1, 1]) == False, 'Test Case 6 Failed'
assert is_sorted([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False, 'Test Case 8 Failed'
assert is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]) == False, 'Test Case 10 Failed'
assert is_sorted([4, 3, 2, 1]) == False, "Error: Test Case 2"
assert is_sorted([1, 1, 1, 1]) == False, "Error: Test Case 4"
assert is_sorted([1, 2, 3, 5, 4]) == False
assert is_sorted([1, 3, 2]) == False
assert is_sorted([3, 2, 1]) == False
assert is_sorted([3, 2, 1]) == False, "Test case 2 failed"
assert is_sorted([5, 4, 3, 2, 1]) == False, "Test case 7 failed"
assert is_sorted([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
assert is_sorted([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == False
assert is_sorted([1, 1, 1, 1]) == False
assert is_sorted([1, 2, 3, 3, 3, 4, 5]) == False
assert is_sorted([1, 2, 3, 3, 3]) == False
assert is_sorted([1, 2, 2, 2, 2]) == False
assert is_sorted([1, 3, 2, 4]) == False
assert is_sorted([1, 1, 1, 2, 3, 4, 5]) == False
assert is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]) == False
assert is_sorted([1, 1, 1]) == False
assert is_sorted([1, 2, 3, 4, 4, 4, 4, 4, 4, 4]) == False
assert is_sorted([1, 2, 3, 4, 4, 4, 4, 4, 4, 3]) == False
assert is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 100000) == False
assert is_sorted([1, 2, 3, 3, 3, 4]) == False
assert is_sorted([1, 1, 1, 1, 2, 3, 4]) == False
assert is_sorted([1, 2, 3, 3, 3, 3, 4]) == False
assert is_sorted([1, 2, 3, 4, 4, 4, 4]) == False
assert is_sorted([1, 3, 2, 4, 5]) == False, "Test case 3 failed"
assert is_sorted([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False, "Test case 7 failed"
assert is_sorted([1, 2, 3, 4, 5, 5, 5, 5, 5, 5]) == False, "Test case 10 failed"
assert is_sorted([1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10]) == False
assert is_sorted([1, 2, 3, 4, 5, 5, 5]) == False
assert is_sorted([4, 3, 2, 1]) == False, 'Test Case 2 Failed'
assert is_sorted([4, 3, 2, 1]) == False, "Test case 2 failed"
assert is_sorted([5, 4, 3, 2, 1]) == False, "Error: Test Case 2"
assert is_sorted([1, 3, 2, 4, 5]) == False, "Error: Test Case 3"
assert is_sorted([1, 3, 2, 4]) == False, 'Test Case 3 Failed'
assert is_sorted([1, 2, 3, 4, 4, 4, 5]) == False
assert is_sorted([5, 4, 3, 2, 1]) == False, 'Test Case 3 Failed'
assert is_sorted([1, 1, 1, 1, 1, 1]) == False
assert is_sorted([1, 3, 2]) == False, "Test case 2 failed"
assert is_sorted([5, 4, 3, 2, 1]) == False, "Test case 6 failed"
assert is_sorted([1, 1, 1, 1]) == False, "Test case 9 failed"
assert is_sorted([1, 1, 1, 2]) == False, "Test case 10 failed"
assert is_sorted([1, 1, 1, 2, 3, 4]) == False, "Error: Test Case 5"
assert is_sorted([1, 2, 3, 3, 3, 4]) == False, "Error: Test Case 6"
assert is_sorted([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False, "Error: Test Case 8"
assert is_sorted([1, 1, 1, 1, 1]) == False, "Error: Test Case 7"
assert is_sorted([5, 4, 3, 2, 1]) == False, 'Test Case 2 Failed'
assert is_sorted([1, 3, 2, 4, 5]) == False, 'Test Case 3 Failed'
assert is_sorted([1, 1, 1, 1, 1]) == False, 'Test Case 5 Failed'
assert is_sorted([1, 1, 1, 2, 3]) == False
assert is_sorted([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == False
assert is_sorted([2, 1, 3]) == False
assert is_sorted([1, 1, 1, 1]) == False, 'Test Case 4 Failed'
assert is_sorted([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False, 'Test Case 6 Failed'
assert is_sorted([5, 4, 3, 2, 1]) == False, 'Test Case 4 Failed'
assert is_sorted([1, 1, 1, 1, 1]) == False, 'Test Case 4 Failed'
