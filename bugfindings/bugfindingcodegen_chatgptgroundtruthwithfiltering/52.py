

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for e in l:
        if e >= t:
            return True
    return False
assert not below_threshold([-1, 0, 1], 1)
assert below_threshold([], 2)
assert not below_threshold([1], 1)
assert below_threshold([1,2,3,4,5], 10) == True
assert below_threshold([1,2,3,4,5], -1) == False
assert below_threshold([1,2,3,4,5], 0) == False
assert below_threshold([], 10) == True
assert below_threshold([1], 10) == True
assert below_threshold([1,2,3], 10) == True
assert below_threshold([1,2,3,4,5], 1) == False
assert below_threshold([1,2,3,4,5,6,7,8,9,10], 5) == False
assert below_threshold([1,2,3,4,5,6,7,8,9,10], 1) == False
assert below_threshold([1, 2, 3, 4], 5) == True
assert below_threshold([1, 2, 3, 4], 0) == False
assert below_threshold([1, 2, 3, 4], 2) == False
assert below_threshold([], 0) == True
assert below_threshold([], 100) == True
assert 	below_threshold([0, -1, 2, 3, 4, 5], 10) == True
assert 	below_threshold([0, -1, 2, 3, 4, 5], 0) == False
