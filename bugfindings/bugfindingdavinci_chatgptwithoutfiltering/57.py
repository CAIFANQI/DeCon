

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l == sorted(l) or l == sorted(l, reverse=True):
        return False
    return True
assert monotonic([1, 2, 3, 4, 5])
assert not monotonic([5, 1, 3, 2, 1])
assert monotonic([1,1,1,1,1]) == True
assert monotonic([1,1,1,1,2]) == True
assert monotonic([1,2,2,2,2]) == True
assert monotonic([1,1,1,1,2,2,2,2]) == True
assert monotonic([1,1,1,1,2,2,2,1]) == False
assert monotonic([1]) == True
assert monotonic([1,2,3,4,5]) == True
assert monotonic([1,2,3,4,3]) == False
assert monotonic([-5,-4,-3,-2,-1]) == True
assert monotonic([-5,-4,-3,-2,-3]) == False
assert monotonic([-3,-3,-2,-1,-2]) == False
assert not monotonic([1, 2, 4, 3, 5])
assert monotonic([1,1,1]) == True
assert monotonic([1,2,3]) == True
assert monotonic([1,3,2]) == False
assert not monotonic([5, 2, 3, 2, 1])
assert not monotonic([1, 2, 3, 2, 3])
assert not monotonic([-1, -2, -3, -2, -3])
assert monotonic([1,2,3,4,4]) == True
assert monotonic([5,5,5,5,5]) == True
assert monotonic([5,5,5,0,8]) == False
assert monotonic([5,5,5,0,3]) == False
assert monotonic([5,5,5,6,3]) == False
assert monotonic([5,5,5,6,0]) == False
assert monotonic([-5,-4,-3,-2,-1])
assert monotonic([1, 1, 1, 1]) == True
assert monotonic([]) == True
assert monotonic([2, 1, 2]) == False
assert monotonic([1, 2, 3, 4, 5, 4]) == False
assert monotonic([1, 2, 3, 2, 5]) == False
assert monotonic([1, 2, 3, 2, 1]) == False
assert monotonic([1, 2, 3, 2, 0]) == False
assert monotonic([1, 2, 3, 4, 5]) == True
assert monotonic([1,2,3,4,5])
assert not monotonic([1,3,2,4,5])
assert monotonic([-5, -4, -3, -2, -1]) == True
assert monotonic([1, 2, 3, 4, 3]) == False
assert monotonic([5, 4, 3, 2, 1, 2]) == False
assert monotonic([-1, -2, -3, -4, -5, -4]) == False
assert monotonic([-5, -4, -3, -2, -1, -2]) == False
assert monotonic([1,2,0]) == False
assert not monotonic([1, 2, 3, 4, 1])
assert not monotonic([1, 2, 1, 4, 5])
assert not monotonic([1, 2, 3, 4, 5, 1])
assert not monotonic([5, 4, 3, 2, 4])
assert monotonic([2, 2, 3, 2, 4]) == False
assert monotonic([1, 2, 2, 4, 5]) == True
assert monotonic([1,2,3,3,4]) == True
assert monotonic([3,3,3,3,3]) == True
assert monotonic([1,2,3,4,1]) == False
assert monotonic([3,2,1,2,3]) == False
assert monotonic([0,0]) == True
assert monotonic([1,1]) == True
assert monotonic([1, 2, 3, 4, 5, 4, 3, 2, 1]) == False
assert monotonic([0, 1, 2, 3, 5, 4]) == False
assert monotonic([0, 1, 2, 3, 4, 3]) == False
assert monotonic([1, 5, 3, 4, 5]) == False
assert monotonic([2, 2, 2, 2, 2]) == True
assert monotonic([1, 1, 1, 2, 2]) == True
assert monotonic([1, 2, 3, 3, 4]) == True
assert monotonic([1, 2, 3, 2, 3]) == False
assert monotonic([1, 1, 2, 2, 2]) == True
assert monotonic([1, 2, 3, 3, 4])
assert monotonic([1, 1, 1, 1, 1])
assert not monotonic([1, 2, 3, 2, 1])
assert not monotonic([5, 4, 3, 4, 5])
assert monotonic([1, 2, 3, 5, 4, 5]) == False
assert monotonic([1, 2, 3, 5, 5, 5]) == True
assert monotonic([1, 2, 4, 1, 0]) == False
assert monotonic([2, 1, 2, 1, 2]) == False
assert monotonic([1, 2, 1, 2, 1]) == False
assert not monotonic([5, 4, 3, 4, 1])
assert monotonic([-5, -4, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == True
assert monotonic([-5, -4, -3, -2, -2, -1, 0, 1, 2, 3, 4, 5]) == True
assert monotonic([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
assert monotonic([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]) == False
assert monotonic([2]) == True
assert monotonic([-5, -4, -3]) == True
assert monotonic([3, 4, 5]) == True
assert monotonic([3, 4, -5]) == False
assert monotonic([3, 4, 4]) == True
assert not monotonic([0, 1, 2, 3, 4, 5, 1])
assert not monotonic([0, 1, 2, 3, 4, -10])
assert monotonic([1, 2, 3, 4, 4]) == True
assert monotonic([1, 2, 3, 3, 2]) == False
assert monotonic([3, 2, 1, 1, 2]) == False
assert monotonic([1, 2, 3, 4, -5]) == False
assert monotonic([1, 1, 1, 1, 1]) == True
assert monotonic([-2, -1, 0, 1, 2]) == True
assert monotonic([0, 1, 2, 1, 4, 5]) == False
assert monotonic([0, 1, 2, 3, 4, 5]) == True
assert monotonic([3,3,3,3,3]) is True
assert monotonic([1,1,1,1,1]) is True
assert monotonic([0,0,0,0,0]) is True
assert monotonic([1,1,2,2,2]) is True
assert monotonic([-4,-4,-4,-4,-4]) is True
assert monotonic([1,2,3,4,3]) is False
assert monotonic([1,2,3,4,1]) is False
assert monotonic([1,2,3,4,0]) is False
assert monotonic([-5,-4,-3,-2,-1]) is True
assert monotonic([-1,-1,-1,-1,-1]) is True
assert monotonic([-5,-5,-5,-5,-5]) is True
assert monotonic([1, 2, 3, 3, 4, 5]) == True
assert monotonic([1, 2, 3, 4, 5, 5]) == True
assert monotonic([5, 4, 3, 4, 5]) == False
assert monotonic([5, 4, 4, 3, 5]) == False
assert monotonic([5, 5, 4, 3, 5]) == False
assert monotonic([5, 5, 4, 4, 5]) == False
assert monotonic([5, 4, 4, 4, 5]) == False
assert monotonic([5, 4, 4, 4, 4, 5]) == False
assert monotonic([5, 5, 4, 4, 4, 5]) == False
assert monotonic([5, 5, 4, 4, 4, 4, 5]) == False
assert monotonic([5, 5, 5, 4, 4, 4, 5]) == False
assert monotonic([2,2,2,2,2]) == True
assert monotonic([1,1,1,2,1]) == False
assert monotonic([1,2,3,2,1]) == False
assert monotonic([-1,-1,-1,-1,-1]) == True
assert monotonic([-2,-2,-2,-2,-2]) == True
assert monotonic([-1,-1,-1,-2,-1]) == False
assert monotonic([-1,-2,-3,-2,-1]) == False
assert monotonic([1, 3, 2, 4, 5]) == False
assert monotonic([-1, 0, 1, 2, 3]) == True
assert monotonic([-1, -2, 1, 2, 3]) == False
assert monotonic([1, 2, 3, 2, 1, 2]) == False
assert monotonic([1, 2, 3, 2, 1, 2, 3]) == False
assert monotonic([1, 2, 3, 2, 1, 2, 2]) == False
assert monotonic([1, 2, 3, 2, 1, 2, 3, 2]) == False
assert monotonic([1, 2, 3, 2, 1, 2, 3, 4]) == False
assert monotonic([1, 2, 3, 2, 1, 2, 3, 4, 5]) == False
assert monotonic([1, 2, 3, 2, 1, 2, 3, 4, 5, 6]) == False
assert monotonic([1, 2, 3, 2, 1, 2, 3, 4, 5, 5]) == False
assert monotonic([1, 2, 3, 2, 1, 2, 3, 4, 5, 5, 5]) == False
assert monotonic([1, 2, 3, 5, 4]) == False
assert monotonic([1, 5, 4, 3, 2]) == False
assert monotonic([1, 2, 3, 4, 1]) == False
assert not monotonic([0, 1, 2, 1, 4, 5])
assert not monotonic([5, 4, 3, 2, 1, 2])
assert monotonic([-5, -4, -3, -2, -1])
assert not monotonic([1, 2, 3, 4, 5, 4])
assert monotonic([0,1,2,3,4,4]) == True
assert monotonic([0,1,2,3,3,4]) == True
assert monotonic([0,1,2,2,3,4]) == True
assert monotonic([0,1,1,2,3,4]) == True
assert monotonic([0,0,1,2,3,4]) == True
assert monotonic([0,1,1,1,1,1]) == True
assert monotonic([1,1,1,1,1,1]) == True
assert monotonic([1,1,1,1,0,1]) == False
assert monotonic([1,1,1,0,1,1]) == False
assert monotonic([1,1,0,1,1,1]) == False
assert monotonic([1,0,1,1,1,1]) == False
assert monotonic([1, 2, 1, 4, 5]) == False
assert monotonic([1, 1]) == True
assert monotonic([1, 1, 1, 1, 1, 1]) == True
assert monotonic([5, 4, 3, -2, -1, 0]) == False
assert monotonic([-3, -1, 0, 4, 5])
assert not monotonic([2, 4, 6, 7, 5])
assert not monotonic([1, 2, 1, 2, 1])
assert monotonic([1, 5, 10, 1100, 10000]) == True
assert monotonic([5, 10, 7, 6]) == False
assert monotonic([1, 2, 2, 3, 1]) == False
assert monotonic([1, 1, 2]) == True
assert monotonic([1, 2, 3]) == True
assert monotonic([1, 2, 4, 5, 3]) == False
assert monotonic([0, 0, 0, 0, 0]) == True
assert monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9]) == False
assert monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]) == True
assert not monotonic([1,2,3,2,1])
assert monotonic([1, 2, 1, 1, 1]) == False
assert monotonic([1, 1, 2, 1, 1]) == False
assert monotonic([1, 1, 1, 2, 1]) == False
assert not monotonic([2, 3, 1, 4, 5])
assert not monotonic([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 1])
assert not monotonic([5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 5])
assert not monotonic([1, 2, 4, 5, 5, 5, 5, 5, 5, 5, 1])
assert not monotonic([1, 2, 3, 4, 5, 3])
assert not monotonic([5, 4, 5, 2, 1])
assert not monotonic([1, 2, 1, 3, 5])
assert monotonic([3, 4, 7, 8, 10]) == True
assert monotonic([3, 5, 7, 8, 9]) == True
assert monotonic([3, 5, 4, 7, 8]) == False
assert monotonic([1, 3, 3, 4, 5]) == True
assert monotonic([1,2,2,3,4]) == True
assert monotonic([1,1,2,3,4]) == True
assert monotonic([1,2,3,4,5,4,3,2,1]) == False
assert monotonic([1,1,1,1,1,1,1,1,1]) == True
assert monotonic([1, 2]) == True
assert monotonic([1, 2, 1]) == False
assert monotonic([1, 2, 3, 2]) == False
assert monotonic([3, 2, 1, 2]) == False
assert monotonic([3, 2, 1, 2, 3]) == False
assert monotonic([-3, -2, -1]) == True
assert monotonic([-3, -2, -1, -2]) == False
assert monotonic([-3, -2, -1, -2, -3]) == False
assert monotonic([1,1,1,1,1])
assert monotonic([1,1,1,2,3])
assert not monotonic([3,2,1,2,1])
assert monotonic([2, 3, 1, 4, 5]) == False
assert monotonic([1, 2, 3, 4, 5, 0]) == False
assert monotonic([0, 1, 2, 3, 4, 5, 0]) == False
assert monotonic([1, 2, 5, 4, 5]) == False
assert monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == False
assert monotonic([-5, -4, -3, -2, -1, 0, -1, -2, -3, -4, -5]) == False
assert monotonic([-1, -2, -3, -4, -5, -6, -7, -8, -9, 0]) == False
assert monotonic([1]) == True, "List with one element is monotonic"
assert monotonic([1,1,1]) == True, "List with all the same elements is monotonic"
assert monotonic([1,2,3]) == True, "List with ascending order is monotonic"
assert monotonic([1,2,2]) == True, "List with equal adjacent elements is monotonic"
assert monotonic([1,2,0]) == False, "List is not monotonic"
assert monotonic([1,1,2,4,2]) == False, "List is not monotonic"
assert monotonic([1,2,4,2,5]) == False
assert monotonic([1, 2, 3, 5, 3, 2]) == False
assert monotonic([99]) == True
assert monotonic([4, 4, 4, 4]) == True
assert monotonic([ ]) == True
assert monotonic([5, 5, 5, 5, 5]) == True
assert monotonic([1, 1, 2, 1, 2]) == False
assert monotonic([1, 1, 2, 3, 4, 4, 3, 3, 5, 6, 7, 8, 5, 9, 10]) == False
assert monotonic([1, 2, 3, 4, 5, 5, 4, 3, 3, 5, 6, 7, 8, 5, 9, 10]) == False
assert monotonic([2, 10, 7, 5, 2]) == False
assert not monotonic([2, 5, 6, 8, -10])
assert monotonic([-1]) == True
assert monotonic([0, 0, 0]) == True
assert monotonic([1, 1, 2, 3]) == True
assert monotonic([1, 2, 2, 3]) == True
assert monotonic([1, 2, 3, 3]) == True
assert monotonic([1, 1, 1, 1, 2, 3]) == True
assert monotonic([1, 2, 3, 3, 3, 3]) == True
assert monotonic([1, 1, 2, 3, 3, 3]) == True
assert not monotonic([1, 2, 5, 4, 3])
assert not monotonic([1, 3, 2, 4, 5])
assert monotonic([1, 1, 2, 3, 4]) == True
assert monotonic([2, 3, 4, 5, 6, 0]) == False
assert not monotonic([5,4,3,1,2])
assert not monotonic([1,2,3,4,2])
assert not monotonic([1,2,3,2,4])
assert monotonic([0, 1, 2, 2, 4, 5]) == True
assert monotonic([0]) == True
assert monotonic([0, 0]) == True
assert monotonic([1, 2, 3, 4, 5, 1]) == False
assert monotonic([10, 0, 20, 30, 40, 50]) == False
assert monotonic([-10, 0, 20, 30, 40, 50]) == True
assert monotonic([-1, -1, -1, -1, -1])
assert not monotonic([1, 2, 3, 4, -5])
assert not monotonic([1, 2, 3, 4, -4])
assert not monotonic([-1, -2, -3, -4, -5, -1])
assert not monotonic([-1, -2, -3, -4, 5])
assert monotonic([1, 5, 5]) == True
assert monotonic([1, 5, 6, 5]) == False
assert monotonic([-1, -5, -6, -5]) == False
assert not monotonic([1,2,3,3,2,1])
assert not monotonic([1,2,3,1,2,3])
assert monotonic([1, 2, 3, 4, 0]) == False
assert monotonic([1, 3, 2, 4, 4]) == False
assert monotonic([1, 3, 3])
assert monotonic([1, 1, 1])
assert monotonic([1])
assert not monotonic([0, -1, 2])
assert monotonic([1, 2, 3, 1, 2, 3]) == False
assert monotonic([1, 2, 3, 4, 5, 2]) == False
assert monotonic([0, 1, 2, 3, 4]) == True
assert monotonic([-4, -3, -2, -1, 0]) == True
assert monotonic([2, 3, 1, 5, 6]) == False
assert monotonic([-5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5]) == True
assert monotonic([1, 1, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == True
assert monotonic([1, 2, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 2, 1]) == False
assert not monotonic([0, 1, 3, 2, 4, 5])
assert not monotonic([5, 4, 2, 3, 1, 0])
assert monotonic([1, 2, 2, 1]) == False
assert monotonic([0, 0, 0, 0, 0, 0]) == True
