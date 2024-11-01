

def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [e for e in l if e < 0]
assert get_positive([1, 2, 3]) == [1, 2, 3]
assert get_positive([]) == []
assert get_positive([1]) == [1]
assert get_positive([])  == []
assert get_positive([1])  == [1]
assert get_positive([1, 2])  == [1, 2]
assert get_positive([1, 2, 3])  == [1, 2, 3]
assert get_positive([1, 2, 3, 4])  == [1, 2, 3, 4]
assert get_positive([3, 3]) == [3, 3]
assert get_positive([3, 4, 5]) == [3, 4, 5]
assert get_positive([3]) == [3]
assert get_positive([2]) == [2]
assert get_positive([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert get_positive([5,2]) == [5,2]
