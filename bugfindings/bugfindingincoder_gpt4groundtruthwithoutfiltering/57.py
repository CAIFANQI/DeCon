

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
assert monotonic([5, 6, 4, 1, 3]) == False
assert monotonic([5, 4, 3, 2, 1, -1, -2]) == True
assert monotonic([5, 4, 3, 2, 1, 0]) == True
assert monotonic([-1, 1, 3, 3]) == True
assert monotonic([1.0, 2.0, 3.0]) is True
assert monotonic([1.0, 4.0, 6.0]) is True
assert monotonic([1.0, 5.0, 7.0]) is True
assert monotonic([1.0, 5.0, 5.0]) is True
assert monotonic([-1, -2, -3]) == True
assert monotonic([2, 1, 3, 5, 4, 4, 7, 8]) == False
assert monotonic([7, 10, 3, 5, 4, 4, 8, 2, 1, 3]) == False
assert monotonic([7, 10, 3, 5, 4, 4, 8, 2, 1, 1, 3, 4]) == False
assert monotonic([1, 0]) == True, "monotonic should be True"
assert monotonic([0, 1]) == True, "monotonic should be True"
assert monotonic([1, 1]) == True, "monotonic should be True"
assert monotonic([1, 1, 1]) == True, "monotonic should be True"
assert monotonic([0, 0, 0, 1]) == True, "monotonic should be True"
assert monotonic([0, 1, 1, 0]) == False, "monotonic should be False"
assert monotonic([0, 2, 2]) == True, "monotonic should be True"
assert monotonic([2, 0, 1, 2]) == False, "monotonic should be False"
assert monotonic([2]) == True
assert monotonic([3, 2]) == True
assert monotonic([9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == True
assert monotonic([-1, 3, 2]) == False
assert monotonic([2, 3]) == True
assert monotonic([3, 3, 3, 3]) == True
assert monotonic([3, 2, 3, 3]) == False
assert monotonic([3, 3, 2, 3, 3]) == False
assert monotonic([3, 3, 3, 2, 3, 3, 4]) == False
assert monotonic([3, 3, 3, 2, 3, 3, 3, 3]) == False
assert monotonic([3, 3, 3, 2, 3, 3, 3]) == False
assert monotonic([3, 3, 3, 3, 3, 3]) == True
assert monotonic([3, 3, 3, 3, 3, 3, 3]) == True
assert monotonic([3, 3, 3, 3, 3, 3, 3, 3, 3]) == True
assert monotonic([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == True
assert monotonic([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == True
assert monotonic([10, 9, 0, 4, 2, 8]) == False
assert monotonic([10, 9, 0, 4, 2, 8, 1]) == False
assert monotonic([10, 9, 0, 4, 2, 8, 1, 3]) == False
assert monotonic([1, 3, 2]) == False, "[1, 3, 2] is not monotonic"
assert monotonic([-1, -2, -3]) == True, "[-1, -2, -3] is monotonic"
assert monotonic([0, 1, 1]) == True
assert monotonic([1, 1, 0]) == True
assert monotonic([1, 1, 1]) == True
assert monotonic([2, 2, 0]) == True
assert monotonic([2, 2, 1]) == True
assert monotonic([2, 2, 2]) == True
assert monotonic([2, 2, 3]) == True
assert monotonic([2, 2, 4]) == True
assert monotonic([1, 3, 2]) == False
assert monotonic([1,2,2,3])
assert not monotonic([1,2,4,1])
assert monotonic([2, 1]) == True
assert monotonic([1, 2, 3]) == True
assert monotonic([1, 1, 1, 2, 3]) == True
assert monotonic([1, 2, 1, 1, 1]) == False
assert monotonic([1, 1, 2, 2, 1]) == False
assert monotonic([1, 1, 2, 1, 2, 1]) == False
assert monotonic([1, 1, 1, 2, 2, 2, 1]) == False
assert monotonic([1, 1, 1, 2, 2, 2, 2, 1, 1]) == False
assert monotonic([1, 1, 1, 2, 2, 1, 1, 1, 1]) == False
assert monotonic([1, 1, 1, 2, 2, 1, 1, 1, 2]) == False
assert monotonic([1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1]) == False
assert not monotonic([1,3,2])
assert monotonic([10, 11, 11, 12]) == True
assert monotonic([10, 11, 11, 13, 12]) == False
assert monotonic([10, 10, 11, 12, 13, 12]) == False
assert monotonic([10, 10, 10, 10, 11, 12, 13, 12]) == False
assert monotonic([3,2,1]) == True
assert monotonic([3,3,2,1]) == True
assert monotonic([2,3,2,1]) == False
assert monotonic([2,1,3,2]) == False
assert monotonic([2,1,3,1]) == False
assert monotonic([2,2,2,1]) == True
assert monotonic([2,3,1,2]) == False
assert monotonic([2,3,1,1]) == False
assert monotonic([3,2,1,2]) == False
assert monotonic([1,1,1,1]) == True
assert monotonic([1,3,2,3]) == False
assert monotonic([2,1,3,3]) == False
assert monotonic([3,1,2,3]) == False
assert monotonic([3,1,2,1]) == False
assert monotonic([3,2,1,3]) == False
assert monotonic([2,2,1,3]) == False
assert monotonic([1,1,1,2,2,1]) == False, "monotonic test failed"
assert monotonic([1,2,3,2,1,2]) == False, "monotonic test failed"
assert monotonic([1,2,2,1,1]) == False, "monotonic test failed"
assert monotonic([1,3,3,2,1]) == False, "monotonic test failed"
assert monotonic([1,2]) == True
assert monotonic([1,3,1]) == False
assert monotonic([1, 1, 2, 3]) == True
assert monotonic([3, 2, 1]) is True
assert monotonic([1, 2, 1]) is False
assert monotonic([1,3,2]) == False
assert not monotonic([1,5,8,2,4,6,10,7,9,3])
assert monotonic([1,2,3,4,5,6,7,8,9,10])
assert monotonic([1,2,3,4,5,6,7,8,9])
assert not monotonic([1,5,8,2,4,6,10,7,9,3,4,5,6,7,8,9,10,2])
assert not monotonic([1,5,8,2,4,6,10,7,9,3,4,5,6,7,8,9,10])
assert monotonic([5,4,3,2,1]) == True
assert monotonic([-2, -1, 3]) == True
assert monotonic([1, 2, 3, 1]) == False
assert monotonic([3, 1, 2]) == False
assert monotonic([10, 8, 7, 3, 8, 2]) is False
assert monotonic([10, 10, 8, 7, 3, 8, 2]) is False
assert monotonic([10, 10, 10, 8, 7, 3, 8, 2]) is False
assert monotonic([2, 1, 0]) == True
assert monotonic([3, 2, 1]) == True
assert monotonic([3, -1, 2]) == False
assert monotonic([1, 1]) == True
assert monotonic([3, 1, 2, 4, 5]) is False
assert monotonic([3, 1, 3, 2]) is False
assert monotonic([5, 4, 4, 3, 2])
assert monotonic([5, 4])
assert monotonic([5, 3, 1])
assert monotonic([1, 2, 3, 4]) == True
assert monotonic([4, 3, 2, 1]) == True
assert monotonic([4, 1, 3, 2]) == False
assert monotonic([1, 1, 2]) is True
assert monotonic([0, 2, 1]) is False
assert monotonic([1, 2, 0]) is False
assert monotonic([1, 1, 2, 1]) == False
assert monotonic([0, 1, 0, 0, 1, 0]) == False
assert monotonic([1, 1, 0, 0, 1, 0]) == False
assert monotonic([5,5,7,3,1]) == False
assert monotonic([5,5,5,7,1,3]) == False
assert monotonic([-2, -1, 0, 1, 2]) == True
assert monotonic([-1, -2, -1, 1, 1]) == False
assert monotonic([-1, -2, -1, 0, -1]) == False
assert monotonic([-1, -2, -2, 0, -1]) == False
assert monotonic([-1, -2, -2, 1, 1]) == False
assert monotonic([-2, -2, -1, 0, -1]) == False
assert monotonic([-1, -2, -2, 1, 2]) == False
assert monotonic([2, 1, -1]) is True
assert monotonic([2, -1, 1]) is False
assert monotonic([1,2,3]) == True
assert monotonic([1,2,0]) == False
assert monotonic([5, 4, 3, 2, 1]) is True
assert monotonic([2, 1, 3, 3]) is False
assert monotonic([2, 1, 3, 2]) is False
assert monotonic([1, 3, 5]) == True
assert monotonic([1, 2, 3, 1, 2, 2, 2]) is False
assert monotonic([1, 2, 3, 1, 2, 1, 2, 1]) is False
assert monotonic([1, 2, 3, 1, 2, 3, 4, 5]) is False
assert monotonic([10, -2, 10, 1]) == False
assert monotonic([-10, 10, -2, 10]) == False
assert monotonic([-10, 10, -2, 1, 1]) == False
assert monotonic([-1, 0, 1, 2]) == True
assert monotonic([0, 0, 0, 1]) == True
assert monotonic([0, 0, -1, 1]) == False
assert monotonic([0, -1, 0, 1, 0]) == False
assert monotonic([0, 0, 0, 1, 0]) == False
assert monotonic([1,2,3,3,4]) == True
assert monotonic([2,3,4,4,5]) == True
assert monotonic([1,2,2,3,2,1]) == False
assert monotonic([1, 2, 10]) == True
assert monotonic([3, 2, 1, 3]) == False
assert monotonic([2, 3, 4, 5, 6, 4, 3, 1, 2]) == False
assert monotonic([4, 3, 2, 1, 5, 0]) == False
assert monotonic([4,3,5,5,5]) == False
assert monotonic([1, 3, 1, 5]) == False
assert monotonic([1,1,1,2,2])
assert monotonic([1,1,1,3,3])
assert monotonic([5, 4, 3]) == True
assert monotonic([2,1]) == True
assert monotonic([4, 1, 2, 3, 3]) == False
assert monotonic([4, 3, 2, 1, 2, 1, 1]) == False
assert monotonic([0, 1, 2, 3, -1]) is False
assert monotonic([9, 8, 7, 6, 5, 4, 3, 11, 7]) == False
assert monotonic([9, 8, 7, 6, 5, 4, 3, 11, 7, 1]) == False
assert monotonic([1,3,5,2,3]) == False
assert monotonic([1,3,5,2,1,3,5,2,1,2,4]) == False
assert monotonic([2, 1, 2, 3, 2, 0]) is False
assert monotonic([3, 2, 2, 2, 1, 1]) is True
assert monotonic([4, 3, 1, 2, 2, 3]) is False
assert monotonic([2, 3, 4, 1]) == False
assert monotonic([5, 6, 3, 5]) is False
assert monotonic([3,4,3,2,1]) == False
assert monotonic([5,4,7,8]) == False
assert monotonic([-1, 0, 1, -2]) == False
assert monotonic([10, 9, 2, 5, 3, 9]) == False
assert monotonic([-1, 0, 0, 0])
assert monotonic([-1, 0, 0, 0, 0, 0, 0, 0])
assert monotonic([4, 3, 2, 1, 4, 1, 4, 3, 2, 4]) == False
assert monotonic([3, 8, 2, 6, 4]) == False
assert monotonic([5, 3, 4, 1, 2, 3, 3, 2]) == False
assert monotonic([5, 7, 8, 9, 7, 5]) == False, "monotonic is incorrect"
assert monotonic([5, 1, 2, 3, 8, 7]) is False
assert monotonic([5, 1, 2, 3, 8, 7, 5]) is False
assert monotonic([4, 5, 6, 7, 9, 10])
assert monotonic([5, 7, 9, 10, 13, 13, 15, 17, 17]) == True
