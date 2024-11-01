

def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [(e + 2) for e in l]
assert incr_list([1]) == [2]
assert incr_list([1, 2, 3]) == [2, 3, 4]
assert incr_list([3,4,5]) == [4,5,6]
assert incr_list([10, 20, 30, 40, 50]) == [11, 21, 31, 41, 51]
assert incr_list([10, 20, 30, 40, 50, 60, 70, 80, 90]) == [11, 21, 31, 41, 51, 61, 71, 81, 91]
assert incr_list([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [11, 21, 31, 41, 51, 61, 71, 81, 91, 101]
assert incr_list([1,2,3]) == [2,3,4]
assert incr_list([1,2,3,4]) == [2,3,4,5]
assert incr_list([2,4,6,8]) == [3,5,7,9]
assert incr_list([1, 3, 5, 7, 9]) == [2, 4, 6, 8, 10]
assert incr_list([1, 3, 5, 7, 10, 13]) == [2, 4, 6, 8, 11, 14]
assert incr_list([]) == []
assert incr_list([1,2,3,4,5]) == [2,3,4,5,6]
assert incr_list([1, 2]) == [2, 3]
assert incr_list([1, 1]) == [2, 2]
assert incr_list([1,2]) == [2,3]
assert incr_list([0]) == [1]
assert incr_list([1, 2, 3, 4]) == [2, 3, 4, 5]
assert incr_list([1, 3, 5]) == [2, 4, 6]
assert incr_list([4, 5, 6, 7]) == [5, 6, 7, 8]
assert incr_list([1, 3, 5, 7]) == [2, 4, 6, 8]
assert incr_list([3, 1]) == [4, 2]
assert incr_list([3, 7]) == [4, 8]
assert incr_list([3, 7, 11]) == [4, 8, 12]
assert incr_list([3, 7, 11, 19]) == [4, 8, 12, 20]
assert incr_list([-4, -3]) == [-3, -2]
assert incr_list([-4, -3, -2]) == [-3, -2, -1]
