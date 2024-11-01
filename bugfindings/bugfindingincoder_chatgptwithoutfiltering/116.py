
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    return sorted(sorted(arr), key=lambda x: arr.count('1'))
assert sort_array([0, 0, 0, 1]) == [0, 0, 0, 1]
assert sort_array([1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1]
assert sort_array([1, 3, 5]) == [1, 3, 5]
assert sort_array([1, 2, 3, 0]) == [0, 1, 2, 3]
assert sort_array([1, 0, 2, 3]) == [0, 1, 2, 3]
assert sort_array([1, 3, 2, 0]) == [0, 1, 2, 3]
assert sort_array([1, 0, 3, 2]) == [0, 1, 2, 3]
assert sort_array([0, 0, 0, 0]) == [0, 0, 0, 0]
assert sort_array([1, 2, 3]) == [1, 2, 3]
assert sort_array([0,0,0,0,0,1]) == [0,0,0,0,0,1]
assert sort_array([0,0,0,0,0,0,1]) == [0,0,0,0,0,0,1]
assert sort_array([0,0,0,0,0,0,0,0]) == [0,0,0,0,0,0,0,0]
assert sort_array([0,0,0,0,0,0,0,0,0]) == [0,0,0,0,0,0,0,0,0]
assert sort_array([0,1]) == [0,1]
assert sort_array([0, 0, 0, 1, 2, 2, 5]) == [0, 0, 0, 1, 2, 2, 5]
assert sort_array([ 1,  1,  1,  1,  1]) == [ 1,  1,  1,  1,  1]
assert sort_array([]) == []
assert sort_array([1,0]) == [0,1]
assert sort_array([0,0,0,0]) == [0,0,0,0]
assert sort_array([9,0,5,2]) == [0,2,5,9]
assert sort_array([9,0,5,1]) == [0,1,5,9]
assert sort_array([9,0,5,4]) == [0,4,5,9]
assert sort_array([9,0,6,1]) == [0,1,6,9]
assert sort_array([9,0,6,4]) == [0,4,6,9]
assert sort_array([9,0,8,1]) == [0,1,8,9]
assert sort_array([9,0,9,1]) == [0,1,9,9]
assert sort_array([0,0,0,0,0,0,0,1]) == [0,0,0,0,0,0,0,1], "your function should return [0,0,0,0,0,0,0,1]"
assert sort_array([0, 0, 0]) == [0, 0, 0]
assert sort_array([0, 0, 1, 1]) == [0, 0, 1, 1]
assert sort_array([0, 1, 1, 1]) == [0, 1, 1, 1]
assert sort_array([0, 1, 1]) == [0, 1, 1]
assert sort_array([1]) == [1]
assert sort_array([0, 0, 0, 1, 1, 1]) == [0, 0, 0, 1, 1, 1]
assert sort_array([0,1,2,3]) == [0,1,2,3]
assert sort_array([0,1,2]) == [0,1,2]
assert sort_array([1,1,0]) == [0,1,1]
assert sort_array([0,1,1]) == [0,1,1]
assert sort_array([0, 1, 2]) == [0, 1, 2]
assert sort_array([0, 0]) == [0, 0]
assert sort_array([1, 1]) == [1, 1]
assert sort_array([0]) == [0]
assert sort_array([0, 1, 0]) == [0, 0, 1]
assert sort_array([3, 6, 2, 5, 1]) == [1, 2, 3, 5, 6], "Test case 3 failed"
assert sort_array([1, 2]) == [1, 2]
assert sort_array([2, 1]) == [1, 2]
assert sort_array([-4, -2, 1, 1]) == [-4, -2, 1, 1]
assert sort_array([1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1]
assert sort_array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert sort_array([2, 1, 3, 0]) == [0, 1, 2, 3]
assert sort_array([10, 10, 10, 10]) == [10, 10, 10, 10]
