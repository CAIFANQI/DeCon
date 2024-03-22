

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
assert below_threshold([1, 2, 3], 4)
assert not below_threshold([4, 5, 6], 4)
assert below_threshold([], 4)
assert not below_threshold([1, 2, 3], 2)
assert not below_threshold([-1, -2, -3], -2)
assert below_threshold([-1, 0, 2], 0) == False
assert below_threshold([-1, -2, -3], 0) == True
assert below_threshold([-1, 2, -3], 0) == False
assert below_threshold([-1, -2, -3], -1) == False
assert below_threshold([-1, -2, -3], -2) == False
assert below_threshold([1, 2, 3], 100) == True
assert below_threshold([-1, 10, 3], 0) == False
assert below_threshold([10, 11, 20], 12) == False
assert below_threshold([9, 10, 9], 11) == True
assert below_threshold([], 12) == True
assert below_threshold([7, 8, 10], 7) == False
assert below_threshold([1, 2, 3], 2) == False
assert below_threshold([], 1) == True
assert below_threshold([1, 2, 3], 6) == True
assert not below_threshold([-1, -1, 2], 2)
assert below_threshold([1, 2, 3], 10)
assert not below_threshold([1, 2, 3], 1)
assert not below_threshold([1, 2, 3], 0)
assert below_threshold([1, 2, 3], 1) == False
assert below_threshold([0, 1, 2], 1) == False
assert below_threshold([1, 2, 3], 5) == True
assert below_threshold([1, 2, 3], 3) == False
assert below_threshold([1, 1, 1], 2) == True
assert below_threshold([-3, -2, -1], 0) is True
assert below_threshold([-1, 0, 2], 1) is False
assert below_threshold([1, 2, 3], 3) is False
assert below_threshold([1, 2, 3], 2) is False
assert below_threshold([-1, -2, -3], -3) is False
assert below_threshold([2, 2, 2], 2) == False
assert below_threshold([], 3) == True
assert below_threshold([1, 2, -3], -3) == False
assert below_threshold([-3, -2, -1], 0) == True
assert not below_threshold([7, 15, 12, 9, 2], 8)
assert below_threshold([7, 15, 12, 9, 2], 22)
assert below_threshold([], 20)
assert below_threshold([], 4) == True
assert below_threshold([-1, -2, -3], -4) == False
assert below_threshold([1, 5, 2, 4], 3) == False
assert below_threshold([1, 5, 2, 4], 4) == False
assert not below_threshold([-1, 0, 101], 10)
assert below_threshold([], 10)
assert below_threshold([1, 2, 4], 4) == False
assert below_threshold([-5, -4, -3], -7) == False
assert not below_threshold([-5, -3, -1, 1, 3, 5], 2)
assert below_threshold([], 5)
assert below_threshold([-5, -3, -1, 1, 3, 5], 10)
assert below_threshold([1,2,3], 4) == True
assert below_threshold([4,5,6], 4) == False
assert below_threshold([1], 0) == False
assert below_threshold([1,2,3], 2) == False
assert below_threshold([1,2,3], 1) == False
assert below_threshold([1], 1) == False
assert below_threshold([-1], 0) == True
assert below_threshold([-1], -1) == False
assert not below_threshold([0, 1, 2, 3], 3)
assert below_threshold([], 42)
assert below_threshold([3], 4)
assert below_threshold([-2, -2, -2, -2], -1)
assert below_threshold([], 0) == True
assert not below_threshold([1, 2, 3], 3)
assert below_threshold([-1, -2, -3], 0)
assert not below_threshold([1, 2, 6], 5)
assert below_threshold([-1, 0, 2], 1) == False
assert below_threshold([-1, 0, 100], 1) == False
assert below_threshold([-1, 0, -100], 1) == True
assert not below_threshold([-1, 0, 2], 1)
assert not below_threshold([0, 1, 2, 3], 2)
assert below_threshold([-5, 0, 3, 3, 3, 3, 4, 5], 3) == False
assert below_threshold([-5, 0, 3, 3, 3, 3, 4, 5], 2) == False
assert below_threshold([5], 5) == False
assert below_threshold([1, 1, 1, 1, 1], 5) == True
assert below_threshold([1, 5, 1, 1, 1], 5) == False
assert below_threshold([1, 1, 1, 1, 1], -10) == False
assert below_threshold([0,4,5], 4) == False
assert below_threshold([2,4,6], 10) == True
assert below_threshold([], 5) == True
assert below_threshold([1, 2, -3, 4, 5], 5) is False
assert below_threshold([], 1)
assert below_threshold([1, 2, 3], 0) == False
assert below_threshold([1], 2)
assert below_threshold([-5, -6, -2, -1, -9], 0) == True
assert below_threshold([-5, 0, 2, 4, 6], 5) == False
assert below_threshold([4, 5, 6], 4) == False
assert below_threshold([-1, 0, -3], -2) == False
assert below_threshold([], -2) == True
assert below_threshold([-1, 0, 1, 2, 3], 3) == False
assert below_threshold([-1, 2, 3, 4, 5], 3) == False
assert below_threshold([4, 2, -5, -7], 6) is True
assert below_threshold([4, 3, 2], 5) == True
assert below_threshold([4, 3, 9], 10)
assert not below_threshold([4, 10, 9], 10)
assert not below_threshold([10, 10, 9], 10)
assert below_threshold([-2, -1, -1, -1, 1], -1) == False
assert below_threshold([-1, 1, 2, 3, 4], 100) == True
assert not below_threshold([2, 5, 1, -1], 0)
assert below_threshold([], 2) == True
assert below_threshold([1, 1, 1], 0) == False
assert below_threshold([-5, -4, -3, -2, -1], -3) is False
assert below_threshold([-3, 5, 10, 4], 7) == False
assert not below_threshold([-1, 0, 1], 0)
assert below_threshold([-5, 10, 0, 3], 6) is False
assert below_threshold([-5, 10, 0, 3], 0) is False
assert below_threshold([-5, 10, 0, 3], -1) is False
assert below_threshold([2, 3, 5, 6, 1], 7) == True
assert below_threshold([2, 3, 5, 6, 1], 1) == False
assert below_threshold([-1, -2, -3], -3) == False
assert below_threshold([0, 1, 2, 3], 6) == True
assert below_threshold([0, 1, 2, 3], 0) == False
assert below_threshold([0, 1, 2, 3], 1) == False
assert below_threshold([0, 1, 2, 3], 2) == False
assert below_threshold([0, 1, 2, 3], 4) == True
assert below_threshold([], -1) == True
assert not below_threshold([3, 5, 7, 10], 10)
assert not below_threshold([3, 5, 7, 10, 11], 10)
assert below_threshold([5, 3, 1], 7)
assert not below_threshold([9, 5, 4], 7)
assert below_threshold([-2, -1, 0, 1, 2], 1) is False
assert below_threshold([-2, -1, 0, 1, 2], -1) is False
assert below_threshold([-2, -1, 0, 1, 2], 0) is False
assert below_threshold([0, 1, 2, 3], 10)
assert below_threshold([1, 2, 3], 5)
assert not below_threshold([10, 20, 30], 0)
assert below_threshold([5, 6, 7], 8)
assert not below_threshold([5, 6, 7], 5)
assert not below_threshold([1, 2, 11], 10)
assert below_threshold([-5, -3, 2, 4, 8], 3) == False
assert below_threshold([1, 3, 6], 4) == False
assert below_threshold([-1, 1, 2, 3, 4], 5) == True
assert below_threshold([], 10) == True
assert below_threshold([4, 4, 4, 4, 4], 4) == False
assert below_threshold([1, 2, 3, 4, 5], 0) == False
assert below_threshold([1, 2, 3, 4, 5], 6) == True
assert below_threshold([1, 2, 3, 4, 5], 5) == False
assert below_threshold([2, 4, 5, 6, 9], 9) == False
assert below_threshold([-2, 3, 4], 5) == True
assert below_threshold([4, 5, 6], 5) == False
assert below_threshold([-3, 5, 7], 5) == False
assert below_threshold([-1, 2, -3], -2) == False
assert below_threshold([1,2,3,4,5], 2) == False
assert below_threshold([2,2,2,2,2], 3) == True
assert below_threshold([1, 2, 3], 4) == True
assert below_threshold([5, 6, 7], 4) == False
assert below_threshold([1, 2, 3], -1) == False
assert below_threshold([1, 2, -10, 10], 10) == False
assert below_threshold([1, 2, -10, 10], 50) == True
assert not below_threshold([-5, 0, 1, 2, -1], 2)
assert not below_threshold([-5, -10, -100, -200, -1000], -99)
assert below_threshold([], 0)
assert below_threshold([-5, -1, 2, 6], 4) is False
assert below_threshold([], 0) is True
assert below_threshold([1,2,3], 10)
assert not below_threshold([10, 2, 11], 10)
assert below_threshold([-1, 2, 0], -2) is False
assert below_threshold([-1, 2, 0], 1) is False
assert below_threshold([-1, 10, -5, -10], 0) == False
assert below_threshold([5, 6, 7], 5) == False
assert below_threshold([1, 10, 3], 5) == False
assert below_threshold([1, 2, 3], 4) is True
assert below_threshold([7, 8, 9], 10) == True
assert not below_threshold([5, 6, 7], 4)
assert below_threshold([1,2,3], 5)
assert not below_threshold([1,2,3], 0)
assert not below_threshold([1,2,3], 2)
assert below_threshold([2, 4, 6], 7) == True
