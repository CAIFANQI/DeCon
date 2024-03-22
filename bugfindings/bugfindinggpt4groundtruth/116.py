
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
assert 	sort_array([0,0,2,3]) == [0,0,2,3], "Wrong answer"
assert 	sort_array([0,2,3,0]) == [0,0,2,3], "Wrong answer"
assert 	sort_array([0,2,3,1]) == [0,1,2,3], "Wrong answer"
assert 	sort_array([0,1,3,2]) == [0,1,2,3], "Wrong answer"
assert 	sort_array([0, 0, 0, 0]) == [0, 0, 0, 0]
assert 	sort_array([0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0], "should be [0, 0, 0, 0, 0, 0, 0]"
assert 	sort_array([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
