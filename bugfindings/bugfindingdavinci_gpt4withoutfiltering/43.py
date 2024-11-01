

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    for i, l1 in enumerate(l):
        for j in range(i, len(l)):
            if l1 + l[j] == 0:
                return True
    return False
assert pairs_sum_to_zero([0, 1, 3, -1]) == True
assert pairs_sum_to_zero([0, -1, 1, 3]) == True
assert pairs_sum_to_zero([]) == False
assert pairs_sum_to_zero([1]) == False
assert pairs_sum_to_zero([3]) == False
assert pairs_sum_to_zero([-1]) == False
assert pairs_sum_to_zero([0, 1, 3, -1, 3]) == True
assert pairs_sum_to_zero([0, 1, 3, -1, 3, 0]) == True
assert pairs_sum_to_zero([0, 1, 3, -1, 3, 0, 0]) == True
assert pairs_sum_to_zero([0, 0, 1, 3, -1, 3, 0, 0]) == True
assert pairs_sum_to_zero([1, 2, 3, -1, -2]) == True
assert pairs_sum_to_zero([1, 2, 3, -1, -2, 3]) == True
assert pairs_sum_to_zero([1, 2, 3, -1, -2, 3, 3]) == True
assert pairs_sum_to_zero([1, 2, 2, 3, 4, -4]) == True
assert pairs_sum_to_zero([1,2,3]) == False
assert pairs_sum_to_zero([1, 1, 2, 3, 4]) == False
assert pairs_sum_to_zero([0, 1, 2, 3, -1, -2]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, 6]) == False
assert pairs_sum_to_zero([1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6, 0]) == True
assert pairs_sum_to_zero([1, 1, 1]) == False
assert pairs_sum_to_zero([-1, 1]) == True
assert pairs_sum_to_zero([-1, 1, 3, 2, -1]) == True
assert pairs_sum_to_zero([-1, 1, 3, 2, -2]) == True
assert pairs_sum_to_zero([-1, 1, 3, 2, -2, 0]) == True
assert pairs_sum_to_zero([-1, 1, 3, 2, -2, 0, 0]) == True
assert pairs_sum_to_zero([-1, 1, 3, 2, -2, 0, 0, 3]) == True
assert pairs_sum_to_zero([1, 2, 3, 4]) == False
assert pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9]) == False
assert pairs_sum_to_zero([1, 2, 3, -1, -1]) == True
assert pairs_sum_to_zero([0, 0, 1, 2, 3, -1, -1]) == True
assert pairs_sum_to_zero([1, 2, 3, -1, -1, -2]) == True
assert pairs_sum_to_zero([0, 0, 1, 2, 3, -1, -1, -2]) == True
assert pairs_sum_to_zero([1, 2, 3, -1, -1, -2, -3]) == True
assert pairs_sum_to_zero([5, 6, 7, 8, 9, 10]) == False
assert pairs_sum_to_zero([]) is False
assert pairs_sum_to_zero([-2,2]) is True
assert pairs_sum_to_zero([-2,1,2]) is True
assert pairs_sum_to_zero([-2,1,3,2]) is True
assert pairs_sum_to_zero([-2,1,3,2,2]) is True
assert pairs_sum_to_zero([-2,1,3,2,2,1]) is True
assert pairs_sum_to_zero([-2,1,3,2,2,1,0]) is True
assert pairs_sum_to_zero([0, 0, 1, -1]) == True
assert pairs_sum_to_zero([1, 4, 2, -5, -3, 5]) == True
assert pairs_sum_to_zero([1, 4, 2, -5, -3, 5, 0]) == True
assert pairs_sum_to_zero([1, 4, 2, -5, -3, 5, 0, 0]) == True
assert pairs_sum_to_zero([1, 4, 2, -5, -3, 5, 0, 0, 0]) == True
assert pairs_sum_to_zero([2, 3, 4, -2]) == True
assert pairs_sum_to_zero([-1, -2, -3, -4]) == False
assert pairs_sum_to_zero([2, 3, 4, -1, -2, -3, 5, -4]) == True
assert pairs_sum_to_zero([-1, -2, -3, -4, 1, 2, 3, 4]) == True
assert pairs_sum_to_zero([-3, 0, 1, 2, 3])
assert not pairs_sum_to_zero([1, 2, 3, 4])
assert pairs_sum_to_zero([-4, -3, -2, -1, 0, 1, 2, 3, 4])
assert pairs_sum_to_zero([2, 3, 5, 4, -2, -1]) == True
assert pairs_sum_to_zero([0, 1, 2, -1, -2]) == True
assert pairs_sum_to_zero([2, 3, 5, 4, -2, -3, 0]) == True
assert pairs_sum_to_zero([0, 2, 3, 5, 4, -2, -3]) == True
assert pairs_sum_to_zero([0, 2, 3, 5, 4, -2, -3, 0]) == True
assert pairs_sum_to_zero([0, 2, 3, 5, 4, -2, -3, 1])
assert pairs_sum_to_zero([0, -1, 2, 3, -2, 1, 4, 5])
assert pairs_sum_to_zero([2, 1, -1]) == True
assert pairs_sum_to_zero([1, 2, 3]) == False
assert pairs_sum_to_zero([-1, 0, 1]) == True
assert pairs_sum_to_zero([-1, 0, 1, 2, 3, -2]) == True
assert pairs_sum_to_zero([-1, 1, 2, 3, 0, -2]) == True
assert pairs_sum_to_zero([-1, 0, 1, 2, 3, 4, -2]) == True
assert pairs_sum_to_zero([-1, 0, 1, 2, 3, 4, -2, -3]) == True
assert pairs_sum_to_zero([-1, 0, 1, 2, 3, 4, -2, -3, -4]) == True
assert pairs_sum_to_zero([0, 1, 2, 3, 4, -2, -3, -4]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, -2, -3, -4]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, -2, -3, -4, -5]) == True
assert pairs_sum_to_zero([1, 2, 3, -2]) == True
assert pairs_sum_to_zero([-6, -4, -3, 1, 2, 3, 4]) == True
assert pairs_sum_to_zero([1,2,3,4,5,6]) == False
assert pairs_sum_to_zero([1, 2, 3, 4, 5]) == False
assert pairs_sum_to_zero([0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 1]) == True
assert pairs_sum_to_zero([0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 1, 1]) == True
assert pairs_sum_to_zero([5, 1, 0, -3, -4, -1]) == True
assert pairs_sum_to_zero([-1, -2, 3, 1, 4, -1, 2, -2]) == True
assert pairs_sum_to_zero([3, 1, 4, -1, 2, -2, -1, -2]) == True
assert pairs_sum_to_zero([-2, 0, 2]) == True
assert pairs_sum_to_zero([1, 2, -1]) == True
assert pairs_sum_to_zero([-4, 1, 0, 2, -3, -1]) == True
assert pairs_sum_to_zero([-1, -2, -3]) == False
assert pairs_sum_to_zero([0, -1, 1]) == True
assert pairs_sum_to_zero([0, -1, 1, 1]) == True
assert pairs_sum_to_zero([-1, 0, 1, 1]) == True
assert pairs_sum_to_zero([-1, 0, 1, -1]) == True
assert pairs_sum_to_zero([-1, 0, 1, -1, 0]) == True
assert pairs_sum_to_zero([-1, 0, 1, 1, -1, 0]) == True
assert pairs_sum_to_zero([0, -1, 1, 1, -1, 0, 1]) == True
assert pairs_sum_to_zero([0, 2, 3, -1, -2]) == True
assert pairs_sum_to_zero([1, 2, 3, -1]) == True
assert not pairs_sum_to_zero([1])
assert not pairs_sum_to_zero([1, 2])
assert pairs_sum_to_zero([1, 2, 3, -2])
assert not pairs_sum_to_zero([1, 2, 3, 6])
assert pairs_sum_to_zero([1, 2, 2, -1]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, -4]) == True
assert pairs_sum_to_zero([0, 2, 3, 4, -4]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, -4, 0]) == True
assert pairs_sum_to_zero([0, 0, 0, 1, 2, 3, 4, -4]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, -5]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, 6, -6]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, 6, -6, -7]) == True
assert pairs_sum_to_zero([0, 2, 3, -2]) == True
assert pairs_sum_to_zero([0, 1, 2, 3, -1]) == True
assert pairs_sum_to_zero([0, 0, 1, 2, 3, -1]) == True
assert pairs_sum_to_zero([0, 0, 1, 2, 3, -1, -1, 0]) == True
assert pairs_sum_to_zero([0, 0, 1, 2, 3, -1, -1, 0, 0]) == True
assert pairs_sum_to_zero([0, 0, 1, 2, 3, -1, -1, 0, 0, 0]) == True
assert pairs_sum_to_zero([-1, -2, 3, 4, 5, 6]) == False
assert pairs_sum_to_zero([-10, -9, -7, 0, 1, 10]) == True
assert pairs_sum_to_zero([1, -2, 3, 2, -1]) == True
assert pairs_sum_to_zero([1, -2, 3, 2, -1, 0]) == True
assert pairs_sum_to_zero([1, -2, 3, 2, -1, 0, 1]) == True
assert pairs_sum_to_zero([1, -2, 3, 2, -1, 0, 1, -1]) == True
assert pairs_sum_to_zero([4, 2, 6, 3, 8]) == False
assert pairs_sum_to_zero([-2, 3, 5, -7, 1, 2, 4, 2]) == True
assert pairs_sum_to_zero([-1,1]) == True
assert pairs_sum_to_zero([-1,-1,1,1]) == True
assert pairs_sum_to_zero([1, 3, 2, 4]) == False
assert pairs_sum_to_zero([-3, 2, -1, 2, -3, -5]) == False
assert pairs_sum_to_zero([-1, 1, 2, 3, 4, 5]) == True
assert pairs_sum_to_zero([-1, 1, -2, 2, 3, 4, 5]) == True
assert pairs_sum_to_zero([-1, 1, -2, 2, 3, 4, 5, 0]) == True
assert pairs_sum_to_zero([0, 1, 2, -1, -1]) == True
assert pairs_sum_to_zero([0, 1, 2, -1, -1, -2]) == True
assert pairs_sum_to_zero([-3, -3, 1, -2, -5]) == False
assert pairs_sum_to_zero([1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1]) == True
assert pairs_sum_to_zero([1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1, 2, 2, 2, -2, 2, -2]) == True
assert pairs_sum_to_zero([1, 3, 5, 6]) == False
assert pairs_sum_to_zero([0, -5, -7, 9, -9]) == True
assert pairs_sum_to_zero([0, 0, 1, -1, -1]) == True
assert pairs_sum_to_zero([0, 0, 1, -1, -1, -1]) == True
assert pairs_sum_to_zero([4, -4, 2, -2, -1, -1, -1]) == True
assert pairs_sum_to_zero([4, -4, 2, -2, -1, -1, -1, 0]) == True
assert pairs_sum_to_zero([-1, -1, 1]) == True
assert pairs_sum_to_zero([2, 1, 2, 3, 4]) == False
assert pairs_sum_to_zero([1, 1, 1, 1, 1]) == False
assert pairs_sum_to_zero([-1, 0, 1, 2, -1])
assert pairs_sum_to_zero([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
assert pairs_sum_to_zero([1,2,3,4,5,6,7,8,9,10]) == False
assert pairs_sum_to_zero([1, 2, -1, 0]) == True
assert pairs_sum_to_zero([1, 2, 1, -1]) == True
assert pairs_sum_to_zero([1, 2, 1, -1, -1]) == True
assert pairs_sum_to_zero([1, 2, 3, -3]) == True
assert pairs_sum_to_zero([1, 2, 3, -3, 0]) == True
assert pairs_sum_to_zero([1, 2, 3, -3, -2]) == True
assert pairs_sum_to_zero([1, 2, 3, -3, -2, 0]) == True
assert pairs_sum_to_zero([1, 2, 3, -3, -2, 3]) == True
assert pairs_sum_to_zero([1, 2, 3, -3, -2, 3, 0]) == True
assert pairs_sum_to_zero([1, -1, 1, -1]) == True
assert pairs_sum_to_zero([1, 2, 3, -1, 2]) == True
assert pairs_sum_to_zero([1, 2, 3, -1, 2, 1]) == True
assert pairs_sum_to_zero([1, 2, 3, -1, 2, 1, 2]) == True
assert pairs_sum_to_zero([1, 2, 3, -1, 2, 1, 2, 3]) == True
assert pairs_sum_to_zero([1, 2, 3, -1, 2, 1, 2, 3, 2]) == True
assert pairs_sum_to_zero([1, 2, 3, -1, 2, 1, 2, 3, 2, 3]) == True
assert pairs_sum_to_zero([1, 2, 3, -1, 2, 1, 2, 3, 2, 3, -1]) == True
assert pairs_sum_to_zero([1, 2, 3, -1, 2, 1, 2, 3, 2, 3, -1, 0]) == True
assert pairs_sum_to_zero([-5, 2, 5, 10]) == True
assert pairs_sum_to_zero([5, 2, 10]) == False
assert pairs_sum_to_zero([0, 0, 1, -1, -1, 0, 1]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, 0, -2, -3, -4, -6]) == True
assert pairs_sum_to_zero([-1, -1, -1, -1]) == False
assert pairs_sum_to_zero([3, 4, 5, 6]) == False
assert pairs_sum_to_zero([1, 1, 2, 3, -1]) == True
assert pairs_sum_to_zero([2, 3, 1, -6, -5]) == False
assert True == pairs_sum_to_zero([4, -4, 1, 2, -1, -2])
assert pairs_sum_to_zero([1, 4, -2, 3]) == False
assert pairs_sum_to_zero([0, 1, -1]) == True
assert pairs_sum_to_zero([-5, 2, 3, 4, 8]) == False
assert pairs_sum_to_zero([1, 3, 5]) == False
assert pairs_sum_to_zero([5, 0, -5]) == True
assert pairs_sum_to_zero([-5, 1, -2, 3, 4, -4]) == True
assert pairs_sum_to_zero([5, -5]) == True
assert pairs_sum_to_zero([4, 1, 2, 3]) == False
assert pairs_sum_to_zero([0, 5, -5]) == True
assert pairs_sum_to_zero([-2, 2]) == True
assert pairs_sum_to_zero([-4, 2, -3, -9, 1]) == False
assert pairs_sum_to_zero([4,4,4,4]) == False
assert pairs_sum_to_zero([5,5,5,5]) == False
assert pairs_sum_to_zero([5,5,5,-5]) == True
assert pairs_sum_to_zero([1, -1]) == True
assert pairs_sum_to_zero([2, 2]) == False
assert pairs_sum_to_zero([-2, 1, 2, -1]) == True
assert pairs_sum_to_zero([-2, -1, 1, 2]) == True
assert pairs_sum_to_zero([1, 1, 1, 1]) == False
assert pairs_sum_to_zero([-2, 2, 0]) == True
assert pairs_sum_to_zero([-1, -2, 0, 2, 1]) == True
assert pairs_sum_to_zero([-1, -2, -3, -4, -5]) == False
assert pairs_sum_to_zero([5, 4, 2, 3, 1]) == False
assert pairs_sum_to_zero([2, -2]) == True
assert pairs_sum_to_zero([1, 1, -1]) == True
assert pairs_sum_to_zero([1, -1, 1]) == True
assert pairs_sum_to_zero([1, -1, 1, -1, 1]) == True
assert pairs_sum_to_zero([1, 2, 3, -2, -1]) == True
assert pairs_sum_to_zero([1, 2, 3, -2, -1, 0]) == True
assert pairs_sum_to_zero([1, 2, 3, -2, -1, 0, -3]) == True
assert pairs_sum_to_zero([1, 2, 3, -2, -1, 0, -3, 1]) == True
assert pairs_sum_to_zero([0, 2, -2, 5, 10]) == True
assert pairs_sum_to_zero([0, 2, -2]) == True
assert pairs_sum_to_zero([1, 2, -1, -2]) == True
assert pairs_sum_to_zero([1, 2, -1, -2, 0]) == True
assert pairs_sum_to_zero([1, 2, 3, -1, -2, -3]) == True
assert pairs_sum_to_zero([1, 2, 3, -1, -2, -3, 0]) == True
assert pairs_sum_to_zero([1, 2, 3, -1, -2, -3, 0, -1]) == True
assert pairs_sum_to_zero([1,1,1]) == False
assert pairs_sum_to_zero([-1,1,1]) == True
assert pairs_sum_to_zero([2, 4, 8, -2, 0]) == True
assert not pairs_sum_to_zero([1,2,3,4,5])
assert pairs_sum_to_zero([-5,5,0])
assert pairs_sum_to_zero([0, 2, -2, 4, -4, 8, 16]) == True
assert pairs_sum_to_zero([2, 2, -2, 4, -4, 8, 16]) == True
assert pairs_sum_to_zero([1,2,3,4]) == False
assert pairs_sum_to_zero([-1,0,1]) == True
