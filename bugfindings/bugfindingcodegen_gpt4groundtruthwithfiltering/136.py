
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
assert 	largest_smallest_integers([0]) == (None, None)
assert 	largest_smallest_integers([2, 4, -1, 1]) == (-1, 1)
assert 	largest_smallest_integers([-1, 2, 4, -1]) == (-1, 2)
assert 	(largest_smallest_integers([5, 10, 15, 20, 25]) == (None, 5)), "wrong output"
assert 	largest_smallest_integers([]) == (None, None)
assert 	largest_smallest_integers([1, 2, -3]) == (-3, 1)
assert 	largest_smallest_integers([9, 1, 2, 3, 4]) == (None, 1)
assert 	largest_smallest_integers([8, 0, -1]) == (-1, 8)
assert 	largest_smallest_integers([0, 0, 0, 0]) == (None, None)
