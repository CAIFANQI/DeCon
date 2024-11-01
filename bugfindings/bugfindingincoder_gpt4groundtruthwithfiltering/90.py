
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
assert next_smallest([-1]) == None
assert next_smallest([7]) == None
assert next_smallest([]) is None
assert next_smallest([10, 4, 9, 1, 5, 7]) == 4
assert next_smallest([10,20,30,50]) == 20
assert next_smallest([2, 1, 4]) == 2
assert next_smallest([1, 2, 3]) == 2
assert next_smallest([1, 1, 1]) is None
assert next_smallest([10, 1, 2, 3]) == 2
assert next_smallest([2, 3, 4]) == 3
assert next_smallest([1, 1, 1]) == None
assert next_smallest([7, 2, 5, 8, 10]) == 5
assert next_smallest([10, 20, 30]) == 20
assert next_smallest([5, 10, 15, 20]) == 10
assert next_smallest([2,3,6,7]) == 3
assert next_smallest([1, 1]) is None
assert next_smallest([5, 3, 2]) == 3
assert next_smallest([5, 2, 3]) == 3
assert next_smallest([3, 5]) == 5
assert next_smallest([7, 9, 10]) == 9
assert next_smallest([10, 9, 100]) == 10
assert next_smallest([4, 3, 2, 1]) == 2
assert next_smallest([5, 3, -1, 2, -2]) == -1
assert next_smallest([1, 10, 11, 13, 12, 20]) == 10
assert next_smallest([1, 10, 11, 13, 12, 20, 30, 40]) == 10
assert next_smallest([5]) is None
assert next_smallest([1, 3, 2]) == 2
assert next_smallest([2, 5, 3]) == 3
assert next_smallest([5, 1, 3]) == 3
assert next_smallest([7,7,7,7,7,7]) is None
assert next_smallest([0,0,0,0]) is None
assert next_smallest([5,5,5,5]) is None
assert next_smallest([-5,-5,-5]) is None
assert next_smallest([3, 2, 1]) == 2
assert next_smallest([4, 1, 3]) == 3
assert next_smallest([-10, 100, -100, -200]) == -100
assert next_smallest([5, 3, 1, 2, 3]) == 2
assert next_smallest([-1]) is None
assert next_smallest([1, 5, 6, 3]) == 3
assert next_smallest([10, 7, 5, 3, 0]) == 3
assert next_smallest([2, 1, 3]) == 2
assert next_smallest([]) == None
assert next_smallest([10,10,10]) == None
assert next_smallest([3, 3]) is None
assert next_smallest([5, 1, 2, 4, 3]) == 2
assert next_smallest([9, 1, 3]) == 3
assert next_smallest([3, 7, 11, 5, 2]) == 3
assert next_smallest([-100, -3, 4, -5, -6, -8, -10]) == -10
assert next_smallest([2, 3, 1, 4, 0]) == 1
assert next_smallest([2, 1, 3, 10]) == 2
assert next_smallest([3, 2.2, 11, 13, -4]) == 2.2
