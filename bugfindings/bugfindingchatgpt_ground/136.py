
def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    largest = list(filter(lambda x: x > 0, smallest))
    smallest = list(filter(lambda x: x > 0, largest))
    return (max(smallest) if smallest else None, min(largest) if largest else None)
assert largest_smallest_integers([1, 2, 3, 4, 5]) == (None, 1)
assert largest_smallest_integers([-1, -2, -3, -4, -5]) == (-1, None)
assert largest_smallest_integers([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == (-1, 1)
assert largest_smallest_integers([-1, -2, -3, -4, -5, 0]) == (-1, None)
assert largest_smallest_integers([1, 2, 3, 4, 5, 0]) == (None, 1)
assert largest_smallest_integers([]) == (None, None)
assert largest_smallest_integers([1, 2, 3, 4, 5, 6]) == (None, 1)
assert largest_smallest_integers([-1, -2, -3, -4, -5, -6]) == (-1, None)
assert largest_smallest_integers([-1, -2, -3, 0, 1, 2, 3, 4, 5]) == (-1, 1)
assert largest_smallest_integers([0, 0, 0]) == (None, None)
assert largest_smallest_integers([-1, -2, -3]) == (-1, None), 'Test Case 2 Failed'
assert largest_smallest_integers([4, 5, 6]) == (None, 4), 'Test Case 3 Failed'
assert largest_smallest_integers([]) == (None, None), 'Test Case 4 Failed'
assert largest_smallest_integers([-1, -2, -3, -4]) == (-1, None)
assert largest_smallest_integers([1, 2, 3, 4]) == (None, 1)
assert largest_smallest_integers([0, 0, 0, 0, 0]) == (None, None)
assert largest_smallest_integers([-1, -2, -3, -4, 5]) == (-1, 5)
assert largest_smallest_integers([-1, -2, -3]) == (-1, None)
assert largest_smallest_integers([4, 5, 6]) == (None, 4)
assert largest_smallest_integers([-4, -5, -6]) == (-4, None)
assert largest_smallest_integers([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == (-1, 1)
assert largest_smallest_integers([-5, -4, -3, -2, -1]) == (-1, None)
assert largest_smallest_integers([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == (-1, 1)
assert largest_smallest_integers([1, 2, 3, 4, 5, 6, -1, -2, -3]) == (-1, 1)
assert largest_smallest_integers([1, 2, 3, 4]) == (None, 1), 'Test Case 2 Failed'
assert largest_smallest_integers([-1, -2, -3, -4]) == (-1, None), 'Test Case 3 Failed'
assert largest_smallest_integers([0, 0, 0, 0]) == (None, None), 'Test Case 4 Failed'
assert largest_smallest_integers([-1, -2, -3, -4, 1, 2, 3, 4]) == (-1, 1), 'Test Case 5 Failed'
assert largest_smallest_integers([-1, 2, 3, -4, 5]) == (-1, 2)
assert largest_smallest_integers([-1, -2, -3, -4, -5]) == (-1, None), 'Test Case 2 Failed'
assert largest_smallest_integers([1, 2, 3, 4, 5]) == (None, 1), 'Test Case 3 Failed'
assert largest_smallest_integers([-1, -2, -3, -4, -5, 0, 1, 2, 3, 4, 5]) == (-1, 1), 'Test Case 5 Failed'
assert largest_smallest_integers([0, 0, 0, 0]) == (None, None)
assert largest_smallest_integers([-1, 0, 1]) == (-1, 1)
assert largest_smallest_integers([-1, -2, -3, -4, -5, 1, 2, 3, 4, 5]) == (-1, 1)
assert largest_smallest_integers([1, 2, 3, 4, 5]) == (None, 1), "Test case 2 failed"
assert largest_smallest_integers([-1, -2, -3, -4, -5]) == (-1, None), "Test case 3 failed"
assert largest_smallest_integers([0, 0, 0, 0, 0]) == (None, None), "Test case 4 failed"
assert largest_smallest_integers([]) == (None, None), "Test case 5 failed"
assert largest_smallest_integers([0]) == (None, None)
assert largest_smallest_integers([1, 2, 3, -4, -5]) == (-4, 1), 'Test Case 3 Failed'
assert largest_smallest_integers([]) == (None, None), 'Test Case 5 Failed'
assert largest_smallest_integers([0, 1, 2, 3, 4, 5]) == (None, 1)
assert largest_smallest_integers([-1, -2, -3, -4, -5, 0, 1, 2, 3, 4, 5]) == (-1, 1)
assert largest_smallest_integers([-1, -2, -3, -4, -5, 0, 1, 2, 3, 4, 5, -10, -100]) == (-1, 1)
assert largest_smallest_integers([1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6]) == (-1, 1)
assert largest_smallest_integers([1, -2, -3, 4, 5]) == (-2, 1)
assert largest_smallest_integers([-1, -2, -3, 4, 5]) == (-1, 4)
assert largest_smallest_integers([1, 2, 3, 4, 5, -1, -2, -3]) == (-1, 1)
assert largest_smallest_integers([-1, -2, -3, 0, 1, 2, 3]) == (-1, 1), "Test case 5 failed"
assert largest_smallest_integers([-1, -2, -3, -4, 0]) == (-1, None)
assert largest_smallest_integers([1, 2, 3, 4, 0]) == (None, 1)
assert largest_smallest_integers([-1, -2, -3, -4, 0, 1, 2, 3, 4]) == (-1, 1)
assert largest_smallest_integers([-1, -2, -3, -4, -5, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]) == (-1, 1)
assert largest_smallest_integers([1, 2, 3, 4, 5, 6]) == (None, 1), 'Test Case 2 Failed'
assert largest_smallest_integers([1, 2, 3, 4, -5, -6]) == (-5, 1), 'Test Case 3 Failed'
assert largest_smallest_integers([-1, -2, -3, -4, -5, -6]) == (-1, None), 'Test Case 4 Failed'
assert largest_smallest_integers([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -10, -20, -30]) == (-1, 1)
assert largest_smallest_integers([-1, 2, -3, 4, -5]) == (-1, 2)
assert largest_smallest_integers([1, 2, 3, -4, -5]) == (-4, 1)
assert largest_smallest_integers([1, 2, 3, 4, 5]) == (None, 1), 'Test Case 2 Failed'
assert largest_smallest_integers([-1, -2, -3, -4, -5]) == (-1, None), 'Test Case 3 Failed'
assert largest_smallest_integers([0, 1, 2, 3, 4, 5]) == (None, 1), 'Test Case 5 Failed'
assert largest_smallest_integers([-1, -2, -3, -4, 0]) == (-1, None), 'Test Case 6 Failed'
assert largest_smallest_integers([-1, -2, -3, 0, 1, 2, 3]) == (-1, 1)
assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, 0, 0, 0]) == (-1, None)
assert largest_smallest_integers([1, 2, 3, 4, 5, 6, 0, 0, 0]) == (None, 1)
assert largest_smallest_integers([]) == (None, None), "Test case 4 failed"
assert largest_smallest_integers([-5, -4, -3, -2, -1, 0]) == (-1, None)
assert largest_smallest_integers([0, 0, 0]) == (None, None), 'Test Case 4 Failed'
assert largest_smallest_integers([-1, -2, -3, -4, -5]) == (-1, None), "Test case 2 failed"
assert largest_smallest_integers([0, 0, 0]) == (None, None), "Test case 3 failed"
assert largest_smallest_integers([1, -1, 2, -2, 3, -3]) == (-1, 1), "Test case 4 failed"
assert largest_smallest_integers([-1, -2, 3, 4, 5]) == (-1, 3)
assert largest_smallest_integers([1, 2, 3, 4, -5]) == (-5, 1)
assert largest_smallest_integers([5, 4, 3, 2, 1]) == (None, 1)
assert largest_smallest_integers([-1, -7, -3, -4]) == (-1, None)
assert largest_smallest_integers([-10, -8, -6, -4]) == (-4, None)
assert largest_smallest_integers([1, 3, 5, 7]) == (None, 1)
assert largest_smallest_integers([-1, -2, -3, -4, 1, 2, 3, 4]) == (-1, 1)
assert largest_smallest_integers([-1, -2, -3, -4, -5, 1, 2, 3, 4]) == (-1, 1)
assert largest_smallest_integers([-5, -10, -15]) == (-5, None)
assert largest_smallest_integers([4, 6, 8]) == (None, 4)
assert largest_smallest_integers([0, 1, 2, 3]) == (None, 1)
assert largest_smallest_integers([-5, -2, -1, 0]) == (-1, None)
assert largest_smallest_integers([-1, -2, -3, -4, -5, 0, 0, 0, 0, 0]) == (-1, None)
assert largest_smallest_integers([1, 2, 3, 4, 5, 0, 0, 0, 0, 0]) == (None, 1)
assert largest_smallest_integers([-1, 2, 3, 4, -5]) == (-1, 2)
assert largest_smallest_integers([0, 1, 2, 3, 4, 5]) == (None, 1), 'Test Case 2 Failed'
assert largest_smallest_integers([-5, -3, -1, 0]) == (-1, None), 'Test Case 3 Failed'
assert largest_smallest_integers([0]) == (None, None), 'Test Case 4 Failed'
assert largest_smallest_integers([0, 0, 0, 0, 0]) == (None, None), 'Test Case 4 Failed'
assert largest_smallest_integers([-10, -5, -2, 0, 3, 7]) == (-2, 3), 'Test Case 5 Failed'
assert largest_smallest_integers([-1, -2, -3, 0, 0, 0]) == (-1, None)
assert largest_smallest_integers([1, 2, 3, 0, 0, 0]) == (None, 1)
assert largest_smallest_integers([4, 5]) == (None, 4)
assert largest_smallest_integers([1, 2, 3, -1, -2, -3]) == (-1, 1)
assert largest_smallest_integers([-1, -2, -3, 1, 2, 3]) == (-1, 1)
assert largest_smallest_integers([-1, 2, 3, 4, 5]) == (-1, 2)
assert largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (None, 1)
assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == (-1, None)
assert largest_smallest_integers([-1, -2, -3, -4, -5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (-1, 1)
assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (-1, 1)
assert largest_smallest_integers([1, 2, 3, 4, 5, 6, -1]) == (-1, 1)
assert largest_smallest_integers([1, 2, 3, 4, 5, 6, 7]) == (None, 1)
assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, -7]) == (-1, None)
