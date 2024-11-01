
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
assert next_smallest([]) is None
assert next_smallest([1]) is None
assert next_smallest([2]) is None
assert next_smallest([]) == None
assert next_smallest([0]) is None
assert next_smallest([1]) == None
assert next_smallest([1]) is None, "simple test"
assert next_smallest([0]) is None, "simple test"
assert next_smallest([-1]) is None, "simple test"
assert next_smallest([]) is None, "simple test"
assert next_smallest([0]) == None
assert next_smallest([4]) is None
assert (next_smallest([]) is None), 'wrong answer'
assert (next_smallest([1]) is None), 'wrong answer'
assert next_smallest([-1]) is None
assert next_smallest([10]) is None
assert next_smallest([3]) is None
assert next_smallest([7]) is None
assert next_smallest([20]) is None
assert next_smallest([]) == None, 'Wrong Answer'
