
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
assert 	next_smallest([0,0,0,0,0,0]) == None
assert next_smallest([]) == None
assert 	next_smallest([1, 3, 2]) == 2
assert 	next_smallest([3, 0, 2, 1]) == 1
assert 	next_smallest([2, 3, 0, 1]) == 1
assert 	next_smallest([2, 0, 3, 1]) == 1
assert 	next_smallest([2, 0, 3, 1, 5]) == 1
assert 	next_smallest([2, 3, 1, 0, 5]) == 1
assert 	next_smallest([1, 2, 3, 4, 5]) == 2
assert 	next_smallest([1, 2, 3, 4]) == 2
assert 	next_smallest([1, 1, 1, 1]) == None
assert 	next_smallest([1, 1, 1, 1, 1, 1]) == None
assert 	(next_smallest([5, 3, 2, 1, 4]) == 2)
assert 	(next_smallest([3, 6, 1, 2, 4]) == 2)
assert 	next_smallest([]) == None
assert 	(next_smallest([1, 1, 1, 1, 1, 1])) == None
assert 	(next_smallest([1])) == None
assert 	(next_smallest([])) == None
assert 	next_smallest([7]) == None
assert 	next_smallest([1]) == None
assert 	next_smallest([1]) == None, 'wrong result'
assert 	next_smallest([]) == None, 'wrong result'
assert 	(next_smallest([2,3,4,5,6,7]) == 3)
assert 	next_smallest([1, 1, 1, 1]) is None
assert 	next_smallest([2, 3, 4, 5]) == 3
assert next_smallest([1, 1, 1]) == None
assert next_smallest([1, 2, 3, 4]) == 2
assert next_smallest([1, 1, 1, 1, 1]) == None
assert 	next_smallest([1, 1, 1, 1, 1]) == None
