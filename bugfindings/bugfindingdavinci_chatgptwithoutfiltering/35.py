

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    m = l[0]
    for e in l:
        if e < m:
            m = e
    return m
assert max_element([0]) == 0
assert max_element([1, 2, 3]) == 3
assert max_element([-1, 1, 2, 3]) == 3
assert max_element([-1, -2, -3]) == -1
assert max_element([1, 2, 2, 2, 2, 4]) == 4, 'max_element does not work'
assert max_element([1, 300, 2, 200, 1]) == 300
assert max_element([10]) == 10
assert max_element([-1, -2, -3, -4, -5]) == -1
assert max_element([-10, 2, 13, 1, -3]) == 13
assert max_element([3, 1, 2, 5, 4]) == 5
assert max_element([5, 5, 5, 5, 5]) == 5
assert max_element([0, -1, -2, -3, -4]) == 0
assert max_element([100, 10, 0, -10, -100]) == 100
assert max_element([1, 3, 3]) == 3, "not first"
assert max_element([-1, -2, -3, -5, -8, -9]) == -1
assert max_element([1, 3, 7, 12, 18, 25]) == 25
assert max_element([1, 2, 4, 5, 8, 9]) == 9
assert max_element([0]) == 0, "single element"
assert max_element([-1, -2, -3]) == -1, "negative numbers"
assert max_element([10, 10, 10]) == 10, "same numbers"
assert max_element([1, 3, 9, 0, -12, 3, 9, 5]) == 9
assert max_element([1, 3, 9, 0, 1, 3, 9, 5]) == 9
assert max_element([5]) == 5
assert max_element([1]) == 1
assert max_element([-1, 2, -3, 4, -5]) == 4
assert max_element([-1, 2, -3, 4, 5]) == 5
assert max_element([-1, 2, -3, 4, 5, 0]) == 5
assert max_element([-1, 2, -3, 4, -5, 0]) == 4
assert max_element([-1, 2, -3, 4, 5, 0, -2]) == 5
assert max_element([-1, 2, -3, 4, -5, 0, -2]) == 4
assert max_element([1, 2, 3, 4, 5]) == 5
assert max_element([5, 4, 3, 2, 1]) == 5
assert max_element([12, 9, 18, 8, 14, 3, 5, 1]) == 18
assert max_element([5, 1, 3, 4, 2]) == 5
assert max_element([1, 5, 3, 4, 2]) == 5
assert max_element([1, 2, 5, 4, 3]) == 5
assert max_element([1, 2, 3, 5, 4]) == 5
assert max_element([5, 4, 4, 4, 5]) == 5
assert max_element([4, 5, 2, 3, 1]) == 5
assert max_element([-5, -4, -3, -2, -1]) == -1
assert max_element([-4, -5, -2, -3, -1]) == -1
assert max_element([-1,-2,-3,-4,-5]) == -1
assert max_element([5,5,5,5,5]) == 5
assert max_element([7, 6, 5, 4, 3]) == 7
assert max_element([1, 7, 3, 5]) == 7
assert max_element([3, 3, 3]) == 3
assert max_element([1, 2, 3, 4, 5, 1]) == 5
assert max_element([-5,-4,-3,-2,-1]) == -1
assert max_element([-5,4,3,2,1]) == 4
assert max_element([5]) == 5, 'one element'
assert max_element([-5, 2, 3, 4]) == 4, 'positive numbers'
assert max_element([-5, -1, -2, -4]) == -1, 'negative numbers'
assert max_element([1, 3, -1]) == 3
assert max_element([-1, -3, -2]) == -1
assert max_element([5, 4, 3, 2, 1, 0]) == 5
assert max_element([4, 5, 2, 5, 3]) == 5
assert max_element([12, 12, 12, 12, 12]) == 12
assert max_element([1,2,3]) == 3
assert max_element([0,0,0]) == 0
assert max_element([1,1,1,1,1,0]) == 1
assert max_element([5, -10, 2, 3, 4, 5]) == 5
assert max_element([1, 1, 1, 1]) == 1
assert max_element([-10, -2, -1, 0, 1, 2, 10]) == 10
assert max_element([0, 0, 0, 0, 0, 0, 0]) == 0
assert max_element([1, 3, 4, 2]) == 4
assert max_element([-1, -2, -3, -1]) == -1
assert max_element([-1, 5, 6, -7, 8]) == 8
assert max_element([-1]) == -1
assert max_element([2, 3, 4, 5, 1]) == 5
assert max_element([1, 1, 1, 1, 1]) == 1
assert max_element([5, 6, 7, 8, 9]) == 9
assert max_element([0, 0, 0, 0, 0]) == 0
assert max_element([1, -1, 1, -1, 1]) == 1
assert max_element([-1, -2, -3, -4]) == -1
assert max_element([1, 4, 2, 5, 3]) == 5
assert max_element([5, 2, 3, 1, 4]) == 5
assert max_element([1, 2, 3, 4, 1]) == 4
assert max_element([-5, -1, -2]) == -1
assert max_element([42]) == 42
assert max_element([2, 42, 3, 42, 7]) == 42
assert max_element([0, 10, 20, 30, 40]) == 40
assert max_element([1000, 2000, 3000, 4000, 5000]) == 5000
assert max_element([-4, -42, -7]) == -4
assert max_element([42, 43, 42]) == 43
assert max_element([4, 42, -7, 100, 42]) == 100
assert max_element([-2, -3, -4, -5, -6, -5, -4, -3, -2, -1]) == -1
assert max_element([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 6
assert max_element([10, 1, 2, -10, -7, -10, -9, 10]) == 10
assert max_element([10, 1, 2, -10, -7, -10, -9, 8]) == 10
assert max_element([1, 1, 1, 1, 5]) == 5
assert max_element([2, 2, 2, 2, 1]) == 2
assert max_element([1, 2, 5, 3, 4]) == 5
assert max_element([5, 3, 6, 2, 1]) == 6
assert max_element([10, 2, 3, 4, -100]) == 10
assert max_element([1, -3, 2]) == 2
assert max_element([100, 1, 2, 3, 4, 5]) == 100
assert max_element([1, 2, 3, 4, -5]) == 4
assert max_element([1, 2, 2, 4, 5]) == 5
assert max_element([2, 3, 2, 3, 4]) == 4
assert max_element([-2, -3, -2, -3, -4]) == -2
assert max_element([0, 1, 2, 3, 4]) == 4
assert max_element([43]) == 43
assert max_element([-2, -1, 0, 1, -5, 100]) == 100
assert max_element([-2, -1, 0, 1, -5, -100]) == 1
assert max_element([-1, -2, -2, -2, -1]) == -1
assert max_element([0, 1, 2, -1, -1, 0, -1]) == 2
assert max_element([1, -2, 3, 4, 5]) == 5
assert max_element([-3, -4, -2, -1, 0]) == 0
assert max_element([1, 2, 3, 4, 2]) == 4
assert max_element([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]) == 9
assert max_element([-6, -100, 100, 99, 0]) == 100
assert max_element([2, 3, 5, 4, 1]) == 5
assert max_element([1, 4, -1, 2, 2]) == 4
assert max_element([10, 1, 2, 3, 4, 5]) == 10
assert max_element([1, 1, 2, 3, 4, 5]) == 5
assert max_element([0, 0, 0, 0, 0, 0]) == 0, 'list contains zero'
assert max_element([-1, -2, -3, -4, -5, -6]) == -1, 'list contains negative numbers'
assert max_element([1, 3, 5, 4, 2]) == 5
assert max_element([1, 3, 4, 5, 2]) == 5
assert max_element([1, 2, 4, 5, 3]) == 5
assert max_element([4, 3, 2, 1, 5]) == 5
assert max_element([4, 2, 3, 1, 5]) == 5
assert max_element([4, 2, 1, 3, 5]) == 5
assert max_element([4, 2, 1, 5, 3]) == 5
assert max_element([4, 2, 5, 1, 3]) == 5
assert max_element([4, 5, 2, 1, 3]) == 5
assert max_element([4, 5, 3, 2, 1]) == 5
assert max_element([-1, -2, -3, -2, -1]) == -1
assert max_element([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
assert max_element([3, 2, 1]) == 3
assert max_element([1, 2, -3, 4, 5]) == 5
assert max_element([1, 2, 5, 4, -3]) == 5
assert max_element([-2, -3, -5, -1]) == -1
assert max_element([-5, 1, 2, -7, 10, 20, -5]) == 20
assert max_element([-2, 0, 1, -1]) == 1
assert max_element([5, 3, 6, 1, 8]) == 8, "Simple test #2 failed"
assert max_element([-1, 0, 10, 10]) == 10
assert max_element([-4, -3, -1, 0]) == 0
assert max_element([0, 1, 2, 3, 4, 5]) == 5
assert max_element([1, 2, -10, 4, 5]) == 5
assert max_element([1, 2, 10, 10, 5]) == 10
assert max_element([-1, -2, -10, -4, -5]) == -1
assert max_element([3, 1, 2]) == 3
assert max_element([2, 3, 1]) == 3
assert max_element([2, 3, 1, 1]) == 3
assert max_element([1, 1, 2, 3]) == 3
assert max_element([1, 2, 3, 3]) == 3
assert max_element([1, 3, 6, 2, 4]) == 6
assert max_element([4, 1, 2, 6, 3]) == 6
assert max_element([1, 4, 3, 5, 6]) == 6
assert max_element([4, 5, 6, 7, 8, 9]) == 9
assert max_element([-9, -8, -7, -6, -5, -4, -3, -2, -1]) == -1
assert max_element([4, 3, 2, 1, -1, -2, -3, -4]) == 4
assert max_element([-1, -2, -3, -4, -5, -6, -7, -8, -9]) == -1
assert max_element([1,2,3,4,5,0]) == 5
assert max_element([0,0,0,0,0]) == 0
assert max_element([0,1,2,3,4,0]) == 4
assert max_element([2, 3, 4, 5, 5]) == 5
assert max_element([1, 2, 3, 4, 5, 6]) == 6
assert max_element([1, 5, 5, 1, 5, 5]) == 5
assert max_element([2, 3, 3, 2, 3, 3]) == 3
assert max_element([1, 2, 3, 4, 5, 3]) == 5
assert max_element([2, 3, 3, 2, 3, 4]) == 4
assert max_element([1, 1, 1, 1, 1, 1]) == 1
assert max_element([-100]) == -100
assert max_element([-100, -200, -5, -2, -3, -4]) == -2
assert max_element([1, 2, 3, 2, 4, 2, 5, 6, 7, 2, 8, 3, 9, 2, 10, 1]) == 10
assert max_element([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
assert max_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
assert max_element([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
assert max_element([5, 3, 6, 4, 2]) == 6
assert max_element([-10, -9, -8, -7, -6]) == -6
assert max_element([1, -1, -3, -4, -5]) == 1
assert max_element([2, 1, 3, 4, -5]) == 4
assert max_element([-1, 0, 1]) == 1
assert max_element([-10, -100, -1000]) == -10
assert max_element([0, -1, -10, -6]) == 0
assert max_element([1, 2, 0, -1]) == 2
assert max_element([1, -1, 0, 2]) == 2
assert max_element([2, 2, 1, 2]) == 2
assert max_element([1, 2, 3, 4]) == 4
assert max_element([-2, -1, 0, -5, -4]) == 0
