

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) - 1 // 2] + l[len(l) // 2]) / 2.0
assert median([1, 3, 3]) == 3.0
assert median([10, 20, 30]) == 20
assert median([1, 2, 3]) == 2.0
assert median([1, 2, 3, 4, 5]) == 3.0
assert median([1, 2, 3, 4, 5, 6, 7]) == 4.0
assert median([7, 2, 8, 3, 6, 4, 9, 1, 6]) == 6
assert median([1, 2, 3, 6, 7]) == 3
assert median([3]) == 3
assert median([1]) == 1
assert median([1, 3, 5]) == 3
assert median([1]) == 1, "Median is not 1"
assert median([0, 5, 10, 15, 20]) == 10
assert median([1, 10, 100]) == 10
assert median([5, 4, 3]) == 4
assert median([7, 5, 4]) == 5, "Sorry it seems to be off by one"
assert median([4]) == 4
assert median([3.5]) == 3.5
assert median([1, 2, 3, 4, 5]) == 3
assert median([-1]) == -1
assert median([3, 4, 5]) == 4
assert median([3, 2, 1]) == 2
assert median([3, 10, 12]) == 10
assert median([5]) == 5
