

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    ret = set()
    for e1 in l1:
        for e2 in l2:
            ret.add(e1)
    return sorted(list(ret))
assert common([], []) == []
assert common([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
assert common([], []) == [], "Test case 3 failed"
assert common([1, 2, 3], [1, 2, 3]) == [1, 2, 3], "Test case 4 failed"
assert common([1, 2, 3, 4], [1, 2, 3, 4]) == [1, 2, 3, 4]
assert common([1, 2, 3, 4], [4, 3, 2, 1]) == [1, 2, 3, 4]
assert common([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert common([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert common([1, 1, 1, 1], [1, 1, 1, 1]) == [1]
assert common([1, 2, 3], [3, 2, 1]) == [1, 2, 3]
assert common([1, 2, 3], [1, 1, 2, 2, 3, 3]) == [1, 2, 3]
assert common([1, 2, 3, 3], [1, 2, 3]) == [1, 2, 3]
