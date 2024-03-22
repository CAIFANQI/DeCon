

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
assert max_element([5]) == 5
assert max_element([-5, 2, 8, 1]) == 8
assert max_element([1]) == 1
assert max_element([1]) == 1, "Test 2 failed"
assert max_element([5]) == 5, "Test 3 failed"
assert max_element([3]) == 3
assert max_element([2, 3]) == 3
assert max_element([2, 1]) == 2
assert max_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 16
assert max_element([1, 2, 3]) == 3
assert max_element([4, 5]) == 5
assert max_element([5, 4, 3, 2, 1]) == 5
assert max_element([-10, -1, 0, 2, 10]) == 10
assert max_element([-10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10]) == -10
assert max_element([3, -2, -1, 1, 2, 3]) == 3
assert max_element([-4, -3, -2, -1]) == -1
assert max_element([5, 7, 8, 10, 2, 3]) == 10
assert max_element([2, 5, 7, 8, 10, 3]) == 10
assert max_element([2, 8, 7, 10, 3, 9]) == 10
assert max_element([4, 8, 10, 2, 7, 5]) == 10
assert max_element([8, 10, 2, 7, 5, 3]) == 10
assert max_element([10, 2, 7, 5, 3, 8]) == 10
assert max_element([10, 2, 8, 7, 5, 3]) == 10
assert max_element([-1, -2]) == -1
assert max_element([-3]) == -3
assert max_element([3, -2, -4, 3]) == 3
assert max_element([-10, 0, 5, 20]) == 20
assert max_element([-10, 0, 5, 20, 100]) == 100
assert max_element([-10, 0, 5, 20, 100, 50]) == 100
assert max_element([3, 9, 7, 12]) == 12
assert max_element([3, 7, 1, 10, 2]) == 10
assert max_element([-5, -4, -3, -2, -1]) == -1
assert max_element([0, 3, 5]) == 5
assert max_element([-1, -2, -3]) == -1
assert max_element([0, 1, 2]) == 2
assert max_element([0, -1, 2]) == 2
assert max_element([7, 3, 6, 7]) == 7
assert max_element([7, 3, 6, 9]) == 9
assert max_element([7, 3, 6, 8, 4]) == 8
assert max_element([7, 3, 6, 9, 8]) == 9
assert max_element([-10, -9, 10, 11, -8, 12]) == 12
assert max_element([-2, -2, -2, -1]) == -1
assert max_element([1, 2, 3, 4, 5]) == 5
assert max_element([1, 1, 2]) == 2
assert max_element([1, 2, 3, 4, 4, 5]) == 5
assert max_element([1, 3, 2]) == 3
assert max_element([-9, 2, 5]) == 5
assert max_element([4, -1, -5, -10]) == 4
assert max_element([-6, 3, 5]) == 5
assert max_element([-5, -2, 1]) == 1
assert max_element([-4, -2, 1]) == 1
assert max_element([-2, -2, 1]) == 1
assert (max_element([1, 2, 3]) == 3)
assert (max_element([-4, -3, 1, 3, -1, 5, 5]) == 5)
assert (max_element([-100, -100]) == -100)
assert (max_element((1, 2, 3, 4)) == 4)
assert max_element([2, -1, 5]) == 5
assert max_element([-5]) == -5
assert max_element([-1, -5]) == -1
assert max_element([6, -5, 8, 4]) == 8, "Max Element function example"
assert max_element([7, 2, 9, 5, 3]) == 9
assert max_element([1, 7, 5]) == 7
assert max_element([9, 9, 9]) == 9
assert max_element([10, 1, 1, 3, 5]) == 10
assert max_element([9, 1, 1, 5, 9]) == 9
assert max_element([4, 6, 3]) == 6
assert max_element([3, 5, 10, 1, 2]) == 10
assert max_element([10, 8, 1, 20, 2, 9, 16, 4, 25]) == 25, "Wrong Answer"
assert max_element([100, 0, -100, -1000, -10000000000000000, 1000000000, -1000000000000000, 100000000000000]) == 100000000000000, "Wrong Answer"
assert max_element([1, 3, 5, 7]) == 7
assert max_element([-10, 3, -3, 10, 5]) == 10
assert max_element([4, 9, 0, -4, 3]) == 9
assert max_element([10, -10, 5, 8, 9]) == 10
assert max_element([1, 1, 1, -1, -1]) == 1
assert max_element([5, -5, 1, -6, -7, 10, -10, -15, -10, -5, -9]) == 10
assert max_element([-1])==-1
assert max_element([7, 4, 9, 3, 5]) == 9
assert max_element([7, 9, 9, 9, 9, 1, 3, 9]) == 9
assert max_element([-10, 5, 10, -10, -8, 10, -5, -7, -10, 10, -5, -7, -10, 10, -5, -8]) == 10
assert max_element([0, -10, -1, 2, 10]) == 10
assert max_element([1, 3, 5]) == 5
assert max_element([-5, -5, 2, -2, 10]) == 10
assert max_element([1, 5, 7, 3, 7, 4, 9, 7, 4]) == 9
assert max_element([5, 7, 0, 11, 3]) == 11
assert max_element([5, 6, 10, 15, 17, 20]) == 20
assert max_element([13, 16, 20, 16, 20, 19, 23, 25, 28, 31, 32]) == 32
