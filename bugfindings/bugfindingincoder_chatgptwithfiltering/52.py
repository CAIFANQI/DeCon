

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
assert below_threshold([1, 2, 3, 4, 5], 2) == 0
assert below_threshold([1, 2, 3, 4, 5], 4) == 0
assert below_threshold([1, 2, 3, 4, 5], 5) == 0
assert below_threshold([1, 2, 3, 4, 5], 6) == 1
assert below_threshold([1, 2, 3, 4, 5], 12) == 1
assert below_threshold([1, 2, 3, 4, 5], 16) == 1
assert below_threshold([1, 2, 3, 4, 5], 20) == 1
assert below_threshold([1, 2, 3, 4, 5], 23) == 1
assert below_threshold([1, 2, 3, 4, 5], 27) == 1
assert not below_threshold([1], 0)
assert not below_threshold([1], 1)
assert below_threshold([1], 2)
assert not below_threshold([1, 2], 1)
assert not below_threshold([1, 2], 2)
assert below_threshold([1, 2], 4)
assert below_threshold([1, 2], 16)
assert below_threshold([1, 2, 3, 4, 5, 6, 7, 8, 9], 14) == True
assert below_threshold([1, 2, 3, 4, 5, 6, 7, 8, 9], 15) == True
assert below_threshold([1, 2, 3, 4, 5, 6, 7, 8, 9], 20) == True
assert below_threshold([1, 2, 3, 4, 5, 6, 7, 8, 9], 25) == True
assert below_threshold([1, 2, 3, 4, 5, 6, 7, 8, 9], 26) == True
assert below_threshold([1, 2, 3, 4, 5, 6, 7, 8, 9], 29) == True
assert below_threshold([1, 2, 3, 4, 5, 6, 7, 8, 9], 30) == True
assert below_threshold([1, 2, 3, 4, 5, 6, 7, 8, 9], 35) == True
assert below_threshold([0, 1, 2], 1) == False
assert below_threshold([2, 5, 6, 7, 8, 9, 10], 8) == False
assert below_threshold([2, 5, 6, 7, 8, 9, 10], 6) == False
assert below_threshold([2, 5, 6, 7, 8, 9, 10], 4) == False
assert below_threshold([2, 5, 6, 7, 8, 9, 10], 2) == False
assert not below_threshold([10, 15, 0, 100], 3), "Test 1 failed"
assert not below_threshold([10, 15, 0, 100], 10), "Test 2 failed"
assert not below_threshold([10, 15, 0, 100], 10), "Test 3 failed"
assert not below_threshold([10, 15, 0, 100], 3), "Test 3 failed"
assert below_threshold([10, 15, 0, 100], 101), "Test 3 failed"
assert not below_threshold([10, 15, 0, 100], 10), "Test 4 failed"
assert below_threshold([-5, 6, -7, 8], 0) == False
assert below_threshold([-5, 6, -7, 8], 2) == False
assert below_threshold([-5, 6, -7, 8], 3) == False
assert below_threshold([-5, 6, -7, 8], 4) == False
assert below_threshold([-5, 6, -7, 8], 5) == False
assert below_threshold([-5, 6, -7, 8], 6) == False
assert below_threshold([-5, 6, -7, 8], 7) == False
assert below_threshold([-5, 6, -7, 8], 8) == False
assert below_threshold([1, 2], 0) == False
assert below_threshold([1, 2, 3], 0) == False
assert below_threshold([], 0) == True
assert below_threshold([1, 2], -1) == False
assert below_threshold([1, 2, 3], -1) == False
assert below_threshold(["hi"], 'hi') == False
assert below_threshold(["hi"], 'hello') == False
assert below_threshold([1, 2], 1) == False
assert below_threshold([1, 2], 2) == False
assert below_threshold([1, 2], 4) == True
assert below_threshold([], 1) == True
assert below_threshold([], 2) == True
assert below_threshold([], 3) == True
assert below_threshold([], 4) == True
assert below_threshold([10, 20, 30, 40, 50, 60], 30) == False
assert below_threshold([10, 20, 30, 40, 50], 30) == False
assert below_threshold([0, 1, 2, 3, 4, 5], 0) == False
assert below_threshold([0, 1, 2, 3, 4, 5], -1) == False
assert below_threshold([0, 1, 2, 3, 4, 5], 7) == True
assert below_threshold([10, 20, 30, 40, 50], -5) == False
assert below_threshold([10, 20, 30, 40, 50], 7) == False
assert below_threshold([10, 20, 30, 40, 50], 10) == False
assert below_threshold([1, 2, 1], 1) == False
assert below_threshold([2, 1], 2) == False
assert below_threshold([1, 0, -1], 1) is False
assert below_threshold([1, 0, -1], 2.5) is True
assert below_threshold([1], -1) == False
assert below_threshold([1], -2) == False
assert below_threshold([1], -3) == False
assert below_threshold([1, 2, 3], 3) == False
assert below_threshold([-1, -2, -3], 3) == True
assert below_threshold([3, -7, 10, 1, 5], 0) == False
assert below_threshold([-7, 10, 1, 5], 7) == False
assert below_threshold([1, -7, 10, 5], 0) == False
assert below_threshold([7, 10, 1], 0) == False
assert below_threshold([1, 10, 5], 0) == False
assert below_threshold([-1, 0, 10], 0) == False
assert below_threshold([0, 10], 0) == False
assert below_threshold([], -2) == True
assert below_threshold([1], 0) == False
assert below_threshold([2, 1], -1) == False
assert below_threshold([1, 2], 1) == 0
assert below_threshold([1, 2], 2) == 0
assert below_threshold([1, 10, 100, 1000, 10000], 100) is False
assert not below_threshold([10, 4, 0, 1], 2)
assert not below_threshold([10, 4, 0, 1], 4)
assert not below_threshold([10, 4, 0, 1], 6)
assert not below_threshold([10, 4, 0, 1], 7)
assert below_threshold([2, 4, 3, -1], 1) == False
assert below_threshold([-1, 2, 4, 3], 1) == False
assert below_threshold([-100, 2, 4, 3], 1) == False
assert below_threshold([-1, -2, -3, -4, 2], 1) == False
assert below_threshold([1, 2, 3, 4], 0) == False
assert below_threshold([1, 2, 3, 4], 1) == 0
assert below_threshold([1, 2, 3, 4], 2) == False
assert below_threshold([1, 2, 3, 4], 3) == False
assert below_threshold([1, 2, 3, 4], 4) == False
assert below_threshold([0, 10, 2, 3], 0) == False
assert below_threshold([0, 10, 2, 3], 1) == False
assert below_threshold([0, 10, 2, 3], 2) == False
assert below_threshold([0, 10, 2, 3], 5) == False
assert not below_threshold([1, 2, 3, 4], 3)
assert below_threshold([0, 10, 20, 30, 0, 30, 20], 20) == False
assert below_threshold([1], 1) == False
assert below_threshold([2, 3], 2) == False
assert below_threshold([5, 7, 8, 3, 1], 7) == False
assert below_threshold([5, 7, 8, 3, 1], 10) == True
assert below_threshold([5, 7, 8, 3, 1], 0) == False
assert below_threshold([5, 7, 8, 3, 1], -1) == False
assert below_threshold([5, 7, 8, 3, 1], 2.5) == False
assert below_threshold([1,2,3,4,5,6,7,8,9], 4) == False
assert below_threshold([1,2,3,4,5,6,7,8,9], 3) == False
assert below_threshold([1, 2, 3, 4], 2) is False
assert below_threshold([1, 2, 3, 4], 5) is True
assert below_threshold([1, 3], 2) == 0
assert below_threshold([1, 3], 3) == 0
assert below_threshold([1, 3, 2], 3) == 0
assert below_threshold([2], 2) == False
assert below_threshold([7, 9, 11], 10) == False
assert not below_threshold([1,2,3], 3)
assert not below_threshold([1,2,3], 1)
assert not below_threshold([1,2,3], 0)
assert below_threshold([1,2,3,4,5,6,7], 8) == True
assert below_threshold([1,2,3,4,5,6,7], 9) == True
assert below_threshold([0, 10, 20, 30, 40, 50], 30) == False
assert below_threshold([0, 0, 2, 3, 4, 0], 0) == False
assert below_threshold([0, 0, 2, 3, 4, 0], 1) == False
assert below_threshold([0, 0, 2, 3, 4, 0], 3) == False
assert below_threshold([1, 2, 3, 4, 5, 6], 4) == False
assert below_threshold([1, 2, 3, 4, 5, 6], 5) == False
assert below_threshold([9, 2, 5, 3, 4, 7, 9, 7, 4, 3, 8], 6) == False
assert below_threshold([2, 5, 9, 3], 9) == False
assert below_threshold([2, 5, 9, 3], -1) == False
assert below_threshold([1, 3, 5, 8, 13, 21, 34, 55], 22) == False
assert below_threshold([1], 3) == True
assert below_threshold([1, 5, 7, 0, 4], 0) is False
assert below_threshold([1, 5, 7, 0, 4], 4) is False
assert below_threshold([1, 5, 7, 0, 4], 1) is False
assert below_threshold([1, -2, 3], -1) == False
assert below_threshold([1, 5, 10, 15], 9) == False
assert below_threshold([4, 6, 7, 5], 12) is True
assert below_threshold([0, 10, 20, 30, 40, 50], 50) == False
assert below_threshold([1, 2], 5) == True
assert below_threshold([1,2,3,5,6,7,8,9], 2) == False
assert below_threshold([10, 15, 3, 9], 15) is False
assert below_threshold([10, 15, 3, 9], 10) is False
assert below_threshold([40, 2, 5, 2], 10) == False
assert below_threshold([2, 8, 3, 7, 10, 20], 20) == False
assert below_threshold([4, 0, 5, 1, 6, 2], 3) == False
assert below_threshold([2, 8, 3, 7, 10, 20], 4) == False
assert below_threshold([2, 1, 0], 1) == False
assert below_threshold([1, 1, 3, 4, 6, 9], 5) == False
assert below_threshold([1, 1, 3, 4, 6, 9], 7) == False
assert below_threshold([10, 5, 3, 1], 0) == False
assert below_threshold([10, 5, 3, 1], -1) == False
assert below_threshold([1, 2, 3, 5], 5) == False
assert below_threshold([1000, 1001, 1002, 1003], 3) == False
assert below_threshold([3, 3, 5, 3, 5], 4) == False
assert not below_threshold([12, 3, 7, 1, 12], 11)
assert not below_threshold([12, 3, 7, 1, 12], 10)
assert below_threshold([3, 7, 11, 21], 12) == False
assert below_threshold([3, 7, 11, 21], 11) == False
assert below_threshold([12, 13, 14, 15], 2) == False
assert below_threshold([4, 6, 8], 7) == False
assert below_threshold([0, 0], 0) == False
assert below_threshold([3, 5], 4) == False
assert below_threshold([1, 5, 6], 3) == False
assert below_threshold([1, 5, 2, -1], 3) == False
assert below_threshold([1, 5, 2, -1], 0) == False
assert below_threshold([1, 1, 1], 0) == False
assert below_threshold([0, 1], 0) == False
assert not below_threshold([4, 9, 9, 9], 3)
assert not below_threshold([9, 9, 9, 9], 4)
assert below_threshold([2,0,1,2,3,4,5,4], 4) == False
assert below_threshold([2, 4, 6, 8, 10, 12], 3) == False
assert below_threshold([3, 2.5, 3.5, 4.5, 5.5, 6.5], 3) == False
assert below_threshold([5, 3, -4, 6, 8], 3) == False
assert below_threshold([1, 2, 3, 4, 5], 5) == False
assert not below_threshold([12, 13, 10, 9], 5), "Should be False"
assert below_threshold([7, 4, 9, 0, 9, 1, 3, 5], 6) == False
assert not below_threshold([5, -2, 1, 2, 4, 6], 0)
assert below_threshold([1, 4, 7, 8, 10, 2, 5, 3, 6], 3) == False
assert below_threshold([-20, -5, 10, 5, 20], 2) == False
assert below_threshold([3, 3, 3, 3], 3) == False
assert below_threshold([5, 9, 3, 8, 2, 10], 4) == False
assert below_threshold([3, -2, 1, 2, -10, 100], -2) == False
assert below_threshold([5,7,2,8,1,9,3,10], 6) == False
assert below_threshold([5, 2, 8, 6, 4, 3], 5) == False
assert below_threshold([0, 10, 2, 3], 10) == False
assert below_threshold([5, 6, 3, 7, 8, 4], 4) == False
assert below_threshold([2, 4, 3, 7, 8], 4) == False
assert not below_threshold([3.7, -0.5, 5.7, 8.2], 0)
assert below_threshold([0, 10, 2, 20, 3, 30], 10) == False
