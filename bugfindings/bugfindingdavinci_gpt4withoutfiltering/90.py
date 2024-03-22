
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
assert next_smallest([10, 10, 2, 1]) == 2
assert next_smallest([-10, 2, 1, 10]) == 1
assert next_smallest([1,2,3]) == 2
assert next_smallest([9, 8, 7, 6, 5]) == 6
assert next_smallest([10, 9, 8, 7, 6]) == 7
assert next_smallest([1, 3, 5, 7, 9]) == 3
assert next_smallest([1, 2, 3, 4, 5]) == 2
assert next_smallest([1,2]) == 2
assert next_smallest([3,2,1]) == 2
assert next_smallest([3, 5, 1, 8, -1]) == 1
assert next_smallest([3, 5, 1, 8, -1, 10]) == 1
assert next_smallest([3, 5, 1, 8, -1, -5]) == -1
assert next_smallest([-1, 0, 1, 2, 3, 4, 5]) == 0
assert next_smallest([1, 2, 4, 3, 5]) == 2
assert next_smallest([1, 2, 3, 4, 5, 6]) == 2
assert next_smallest([1, 2, 3, 4, 5, 6, 7]) == 2
assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8]) == 2
assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
assert next_smallest([1, 5]) == 5
assert next_smallest([5, 1, 6, 9, -1]) == 1
assert next_smallest([5, 1, 6, 9, -1, 6]) == 1
assert next_smallest([100, 2, 3, 4, 5]) == 3
assert next_smallest([11, 12, 13, 14, 15]) == 12
assert next_smallest([3, 2, 1, -1]) == 1
assert next_smallest([3, 2, 1, -1, 0]) == 0
assert next_smallest([5, 4, 3, 2, 1]) == 2
assert next_smallest([1, 3, 2, 4, 5]) == 2
assert next_smallest([0, 7, -9, 1, 2, 4]) == 0
assert next_smallest([7, 1, 2, 3, 4, 5, 6]) == 2
assert next_smallest([9, 1, 2, 3, 4, 5, 6, 7, 8]) == 2
assert next_smallest([-1, 1, 2, 3, 4, 5, 6, 7, 8]) == 1
assert next_smallest([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
assert next_smallest([6, 4, 5, 6, 7, 8, 9]) == 5
assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]) == 2
assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 8, 9]) == 2
assert next_smallest([1, 2, 3, 4, 5, 6, 7, 7, 8, 9]) == 2
assert next_smallest([1, 2, 3, 4, 5, 6, 6, 7, 8, 9]) == 2
assert next_smallest([1, 2, 3, 4, 5, 5, 6, 7, 8, 9]) == 2
assert next_smallest([1, 2, 3, 4, 4, 5, 6, 7, 8, 9]) == 2
assert next_smallest([0, 1, 2, 3, 4, 5]) == 1, "simple test"
assert next_smallest([1, 2]) == 2
assert next_smallest([2, 3, 1]) == 2
assert next_smallest([2, 3, 1, 0]) == 1
assert next_smallest([1, 2, 3, 0]) == 1
assert next_smallest([0, 1, 2, 3]) == 1
assert next_smallest([2, 1, 3, 0]) == 1
assert next_smallest([2, 3, 0, 1]) == 1
assert next_smallest([3, 2, 1, 0]) == 1
assert next_smallest([3, 2, 0, 1]) == 1
assert next_smallest([1, 3, 2, 0]) == 1
assert next_smallest([1, 0, 3, 2]) == 1
assert next_smallest([1, 0, 2, 3]) == 1
assert next_smallest([1, 2, 0, 3]) == 1
assert next_smallest([1, 3, 0, 2]) == 1
assert next_smallest([-5, -4, -3, -2, -1, 0]) == -4
assert next_smallest([-5, -4, -3, -2, -1, 1]) == -4
assert next_smallest([2, 3, 4, 5]) == 3
assert next_smallest([3, 4, 5]) == 4
assert next_smallest([4, 5]) == 5
assert next_smallest([2, 3, 4, 5, 1]) == 2
assert next_smallest([2, 3, 4, 1, 5]) == 2
assert next_smallest([2, 1, 4, 3, 5]) == 2
assert next_smallest([1, 4, 2, 5, 3]) == 2
assert next_smallest([1, 2, 3, 3, 4, 5]) == 2
assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 2
assert next_smallest([0, 1, 2, 3, 4, 5]) == 1
assert next_smallest([0, 1, 2, 3, 3, 3, 3, 3, 4, 5]) == 1
assert next_smallest([10, 2, 3, 4, 5, 6, 7, 8]) == 3
assert next_smallest([10, 2, 3, 4, 5, 6, 7, 8, 9]) == 3
assert next_smallest([10, 2, 3, 4, 5, 6, 7, 8, 10]) == 3
assert next_smallest([10, 2, 3, 4, 5, 6, 7, 8, 10, 9]) == 3
assert next_smallest([10, 2, 3, 4, 5, 6, 7, 8, 10, 9, 10]) == 3
assert next_smallest([10, 2, 3, 4, 5, 6, 7, 8, 10, 9, 10, 11]) == 3
assert next_smallest([5, 1, 3, 4, 6]) == 3
assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]) == 2
assert next_smallest([-2, -1, 0, 1, 2]) == -1
assert next_smallest([1, 2, 3, 3, 3, 3, 3, 4, 5]) == 2
assert next_smallest([2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
assert next_smallest([3, 4, 7, 8, 6, 5]) == 4
assert next_smallest([-1, 0, 1, 2]) == 0
assert next_smallest([-1, 0, 1, 1, 2]) == 0
assert next_smallest([2, 3, 4, 5, 6, 7, 8]) == 3
assert next_smallest([5, 2, 4, 1]) == 2
assert next_smallest([5, 2, 4, 4, 3, 3, 1]) == 2
assert (next_smallest([1, 2]) == 2), 'wrong answer'
assert next_smallest([4, 5, 1, 3, 2]) == 2
assert next_smallest([4, 5, 1, 2, 3]) == 2
assert next_smallest([1, 2, 3, 4]) == 2
assert next_smallest([7, 1, 5, 4, 2, 3]) == 2
assert next_smallest([1, 2, 3, 3, 5, 6]) == 2
assert next_smallest([-1, 3, -2, 4, -5]) == -2
assert next_smallest([-1, -2, -3]) == -2
assert next_smallest([2, 3, 4]) == 3
assert next_smallest([3, 2, 1]) == 2
assert next_smallest([3, 1, 2]) == 2
assert next_smallest([2, 1, 3]) == 2
assert next_smallest([-2, -1, 1, 2, 3]) == -1
assert next_smallest([-2, 1, 2, 3, 4, 5]) == 1
assert next_smallest([-2, 1, -3, 2, -4, 3, -5, 4, -6, 5]) == -5
assert next_smallest([4, 3, 2, 1, 5]) == 2
assert next_smallest([10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
assert next_smallest([10, 7, -10, -7]) == -7
assert next_smallest([4, 2, 0, 10, 6, 8]) == 2
assert next_smallest([4, 2, 0, 10, 6, 8, 2, 12, 5, 1]) == 1
assert next_smallest([5, 1, 2, 3, 4]) == 2
assert next_smallest([4, 2, 1, 5, 3]) == 2
assert next_smallest([-2, 0, 2, -1]) == -1
assert next_smallest([10, 20, 30, 40, 50]) == 20
assert next_smallest([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
assert next_smallest([2, 3, 4, 5, 7, 19, 20]) == 3
assert next_smallest([5, 7, 19, 20]) == 7
assert next_smallest([7, 9, 5, 3, 1, 2]) == 2
assert next_smallest([1, 3, 2]) == 2
assert next_smallest([3, 4, 1, 5, 2]) == 2
assert next_smallest([5, 2, 4, 1, 3]) == 2
assert next_smallest([1, 5, 2, 3, 4, 5]) == 2
assert next_smallest([13, 5, 7, 2, 8, 1]) == 2
assert next_smallest([7, 1, 2, 3, 4, 5]) == 2
assert next_smallest([3, 7, 1, 4, 2, 9]) == 2
assert next_smallest([3, 4, 7, 1, -4, 9, 2, -3]) == -3
assert next_smallest([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
assert next_smallest([0, 2, -9, 10, -1]) == -1
assert next_smallest([1, 2, -8, -2, 0]) == -2
assert next_smallest([0, 7, 4, 2, 6, 3, 9, 5]) == 2
assert next_smallest([5, 10]) == 10
assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2, 'Wrong Answer'
assert next_smallest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2, 'Wrong Answer'
assert next_smallest([1, 2, 3]) == 2
assert next_smallest([1, 2, 3, 3]) == 2
assert next_smallest([3, 2, 1, 3]) == 2
assert next_smallest([-1, 2, -3, 4, -5]) == -3
