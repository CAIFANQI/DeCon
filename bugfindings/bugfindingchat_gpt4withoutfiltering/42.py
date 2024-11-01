

def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [(e + 2) for e in l]
assert incr_list([1, 2, 3]) == [2, 3, 4]
assert incr_list([0, -1, -2]) == [1, 0, -1]
assert incr_list([]) == []
assert incr_list([-1, 0, 1]) == [0, 1, 2]
assert incr_list([100]) == [101]
assert incr_list([-100, 0, 100]) == [-99, 1, 101]
assert incr_list([-5, 10, 15]) == [-4, 11, 16]
assert incr_list([-1, -2, -3]) == [0, -1, -2]
assert incr_list([0, 0, 0]) == [1, 1, 1]
assert incr_list([10]) == [11]
assert incr_list([10, 20, 30, 40]) == [11, 21, 31, 41]
assert incr_list([10, 100, 1000]) == [11, 101, 1001]
assert incr_list([5]) == [6]
assert incr_list([1]) == [2]
assert incr_list([5, 10, 15]) == [6, 11, 16]
assert incr_list([10, 20, 30]) == [11, 21, 31]
assert incr_list([0]) == [1]
assert incr_list([0, -1, 2]) == [1, 0, 3]
assert incr_list([-5]) == [-4]
assert incr_list([-1]) == [0]
assert incr_list([10, 20, 30, 40, 50]) == [11, 21, 31, 41, 51]
assert incr_list([-100, -50, 0, 50, 100]) == [-99, -49, 1, 51, 101]
