

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
assert median([1, 2]) == 1.5
assert median([1, 2, 3]) == 2.0
assert median([1, 2, 3, 4]) == 2.5
assert median([1, 2, 3, 4, 5]) == 3.0
assert median([1, 2, 3, 4, 5, 6]) == 3.5
assert median([1, 2, 3, 4, 5, 6, 7]) == 4.0
assert median([1, 2, 3, 4, 5, 6, 7, 8]) == 4.5
assert median([7, 2, 8, 3, 6, 4, 9, 1, 6]) == 6
assert median([1, 2, 3, 6, 7]) == 3
assert median([3, 3, 3, 3]) == 3
assert median([3, 3]) == 3
assert median([3]) == 3
assert median([1]) == 1
assert median([3, 7, 8, 9]) == 7.5, 'Test failed'
assert median([1, 3, 5]) == 3
assert median([2, 5, 7, 1, 3]) == 3, "The median of 3 should be 3"
assert median([1]) == 1, "Median is not 1"
assert median([0, 5, 10, 15, 20]) == 10
assert median([1, 10, 100]) == 10
assert median([5, 4, 3]) == 4
assert median([7, 5, 4]) == 5, "Sorry it seems to be off by one"
assert median([4, 3, 9, 7, 5]) == 5, "Sorry it seems to be off by one"
assert median([4]) == 4
assert median([3.5]) == 3.5
assert median([2, 4, 4, 6, 6]) == 4.0, 'Wrong result'
assert median([2, 4, 6, 6, 2]) == 4.0, 'Wrong result'
assert median([1, 2, 3, 4, 5]) == 3
assert median([3, 6, 5, 7, 2, 1]) == 4
assert median([-1]) == -1
assert median([5, 7, 5, 5, 2]) == 5
assert median([2, 2, 2]) == 2
assert median([9, 9, 9, 9]) == 9
assert median([3, 4, 5]) == 4
assert median([9, 9, 9, 9, 9, 9]) == 9, "List with nine elements does not work"
assert median([3, 3]) == 3.0
assert median([3, 2, 1]) == 2
assert median([3, 10, 12]) == 10
assert median([5, 5]) == 5
assert median([5, 5, 5]) == 5
assert median([1, 4, 3]) == 3
assert median([4, 3, 1, 5, 3]) == 3
assert median([7, 2, 7, 5, 1, 4, 1, 4, 2, 7, 9, 3, 5]) == 4
assert median([5, 5, 5, 5, 5]) == 5
assert median([10, 9, 7, 3, 8, 1, -2]) == 7
assert median([5]) == 5
assert median([10, 10, 10]) == 10
assert median([7, 1, 2, 3, 5, 8]) == 4
assert median([3, 1, 2, 4, 5]) == 3
assert median([9, 0, 2]) == 2
assert median([1, 5, 3, 10, 10, 10, 5]) == 5
assert median([-3, 1, -2, 0, 2, -2]) == -1
assert median([7, 8, 7]) == 7
assert median([3, 8, 10, 2, 3, 5, 6]) == 5
assert median([3, 3, 4, 3, 2, 2]) == 3
