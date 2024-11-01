

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
assert pairs_sum_to_zero([-1, 0, 1, 1]) == True
assert pairs_sum_to_zero([-1, 0, 1, 7]) == True
assert pairs_sum_to_zero([-1, 0, 1, 12]) == True
assert pairs_sum_to_zero([-1, 0, 1, 17]) == True
assert not pairs_sum_to_zero([-1, -2, -2, -1]), 'incorrect value'
assert not pairs_sum_to_zero([-1, -2, -5, -2]), 'incorrect value'
assert not pairs_sum_to_zero([-1, -2, -5, -7, -8]), 'incorrect value'
assert not pairs_sum_to_zero([-1, -2, -5, -7, -4]), 'incorrect value'
assert not pairs_sum_to_zero([-1, -2, -5, -7, -6, -3]), 'incorrect value'
assert not pairs_sum_to_zero([-1, -2, -5, -7, -6, -4, -2]), 'incorrect value'
assert not pairs_sum_to_zero([-1, -2, -5, -7, -6, -4, -1, -1]), 'incorrect value'
assert not pairs_sum_to_zero([-1, -2, -5, -7, -6, -4, -2, -1]), 'incorrect value'
assert pairs_sum_to_zero([-1, -2, 3, -4, -5, -2, -3, -1, 0]), "test case failed"
assert pairs_sum_to_zero([-1, -2, 3, -4, -5, -2, -3, -4, -1, 0]), "test case failed"
assert pairs_sum_to_zero([-4, -5, -5]) == False
assert pairs_sum_to_zero([-3, -2, -1, 0, 1, 2, 3]) == True
assert pairs_sum_to_zero([-3, -2, -1, 0, 1, 3, -3, 0]) == True
assert pairs_sum_to_zero([-3, -2, -1, 0, 1, 2, -3]) == True
assert pairs_sum_to_zero([-10, -10, -10, -10, -10, -10, -10, -10, -10]) == False
assert pairs_sum_to_zero([-10, -10, -10, -10, -10, -10, -10, -10, 10]) == True
assert pairs_sum_to_zero([-10, -10, -10, -10, -10, -10, 10, 10, -10, -10]) == True
assert not pairs_sum_to_zero([1, 2]), "Second pair doesn't sum up to zero"
assert pairs_sum_to_zero([-1, -2, -5, 6, 1]), "Sixth pair sums to zero"
assert not pairs_sum_to_zero([-2, -5, 6, 1]), "Seventh pair doesn't sum up to zero"
assert not pairs_sum_to_zero([1, -2]), "Eighth pair doesn't sum up to zero"
assert pairs_sum_to_zero([5, 3, -2, -5, 6, 1]), "Second pair doesn't sum up to zero"
assert not pairs_sum_to_zero([1, 2])
assert not pairs_sum_to_zero([1, -2, 5])
assert pairs_sum_to_zero([-1, -1, 1, 0])
assert pairs_sum_to_zero([-1, 1, 0])
assert pairs_sum_to_zero([-1, 0, 1])
assert pairs_sum_to_zero([-1, 0, 1, 2])
assert pairs_sum_to_zero([1, 2, -1, -2])
assert not pairs_sum_to_zero([-1, -2, -3, -4]), "should return False because the list sums to zero"
assert not pairs_sum_to_zero([]), "should return False because an empty list does not contain any elements that sum up to zero"
assert pairs_sum_to_zero([-5]) == False
assert pairs_sum_to_zero([-9, -7, -8, -10, -5, -4, -3, -1, -2, -4]) == False
assert pairs_sum_to_zero([-9, -7, -8, -10, -5, -4, -3, -1, -2, -4, -5]) == False
assert pairs_sum_to_zero([-1, -2, -4, -5, -6, -7, -8, -9, -10, -9, -1, -2, -3, -4]) == False
assert pairs_sum_to_zero([-1, -2, -4, -5, -6, -7, -8, -9, -10, -9, -1, -2, -3, -4, -5]) == False
assert pairs_sum_to_zero([-2, 0, 2, -4, -1, 0]) == True, "invalid input"
assert pairs_sum_to_zero([-6, -4, -1, 0, 4, 0, -4]) == True, "invalid input"
assert pairs_sum_to_zero([-4, -4, -1, 0, 4, 0, -4]) == True, "invalid input"
assert pairs_sum_to_zero([-1, -2, -3, -4]) == False
assert pairs_sum_to_zero([-1, -2, -3, -4, -5]) == False
assert pairs_sum_to_zero([-1, -2, -3, -5, -6, -7, -8, -9]) == False
assert not pairs_sum_to_zero([1, 2, 3, 2])
assert not pairs_sum_to_zero([1, 2, 3, 3, 3])
assert not pairs_sum_to_zero([4, -2, 5])
assert not pairs_sum_to_zero([10, -3, 5])
assert pairs_sum_to_zero([-10, 5, -15, 5, -15, 10])
assert pairs_sum_to_zero([10, 5, -15, 10, -15, 15])
assert pairs_sum_to_zero([-10, 10, -15, 10, -15, 10])
assert pairs_sum_to_zero([-10, 10, -15, 10, -15, 10, -15, 10, -15, 10, -15, 10, -15, 10])
assert pairs_sum_to_zero([-1, 2, -3]) == False
assert pairs_sum_to_zero([-1, -2, -3]) == False
assert pairs_sum_to_zero([-1, -2, 1, 2]) == True
assert pairs_sum_to_zero([1]) == False
assert pairs_sum_to_zero([-10, 10, 5, 0]) == True
assert pairs_sum_to_zero([-10, -10, -10]) == False
assert pairs_sum_to_zero([-10, -10, 1]) == False
assert pairs_sum_to_zero([]) == False
assert pairs_sum_to_zero([10, 10]) == False
assert pairs_sum_to_zero([-3]) is False
assert pairs_sum_to_zero([-3, -1]) is False
assert pairs_sum_to_zero([1, 2, 2]) is False
assert pairs_sum_to_zero([1]) is False
assert pairs_sum_to_zero([3, -7, 4]) == False
assert pairs_sum_to_zero([3] * 11) == False
assert pairs_sum_to_zero([-2, -3, -4, -5]) is False
assert pairs_sum_to_zero([-1, 3, -4]) is False
assert pairs_sum_to_zero([1, -3]) == False
assert not pairs_sum_to_zero([-1, -1, -1, -1])
assert pairs_sum_to_zero([-1, 0, 1]) == True
assert pairs_sum_to_zero([-1, 1, 1]) == True
assert False == pairs_sum_to_zero([])
assert pairs_sum_to_zero([]) is False
assert pairs_sum_to_zero([3, 6, 9, 12, 15]) == False
assert pairs_sum_to_zero([8, 7, 5, 7, 9, 15, 20, 20, 20]) == False
assert pairs_sum_to_zero([7, 7, 7, 7, 7, 7]) == False
assert pairs_sum_to_zero([4, 6, 9, 1]) == False
assert pairs_sum_to_zero([-1, -1, -3]) == False
assert not pairs_sum_to_zero([1, 1])
assert pairs_sum_to_zero([-2, 0, 2]) == True
assert not pairs_sum_to_zero([1, 3]), "Test case failed"
assert not pairs_sum_to_zero([1, 3, 5]), "Test case failed"
assert pairs_sum_to_zero([2,2,3]) == False
assert pairs_sum_to_zero([-1, 0, 1, 0])
assert pairs_sum_to_zero([-1, 0, 1, 1])
assert pairs_sum_to_zero([-2, -3, -4, -5]) == False
assert pairs_sum_to_zero([-2, -1, 1, -1, 4, -1, 4, -1, -5, 6])
assert pairs_sum_to_zero([-1, 0, -1, 1])
assert pairs_sum_to_zero([-1, 0, -1, 1, -1, 1])
assert pairs_sum_to_zero([-1, 0, -1, 1, -1, 1, -1, 1])
assert pairs_sum_to_zero([-1, 0, -1, 1, -1, 1, -1, 1, -1])
assert pairs_sum_to_zero([-1, 0, -1, 1, -1, 4, -1, 4, -1, -5, 6])
assert pairs_sum_to_zero([-1, 4]) == False
assert not pairs_sum_to_zero([1, 2, 3, 4]), "the list should sum to zero"
assert not pairs_sum_to_zero([3, 4, 5])
assert not pairs_sum_to_zero([3, 6, 5])
assert not pairs_sum_to_zero([4, 3, 5])
assert pairs_sum_to_zero([2,3,-2,-5])
assert pairs_sum_to_zero([-5,2,3,-2,-5])
assert pairs_sum_to_zero([2,-5,3,-2,-5])
assert pairs_sum_to_zero([-10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10]) == False
assert not pairs_sum_to_zero([-10, -10, -10, -10, -5])
assert pairs_sum_to_zero([1,6,4,-2,3]) is False
assert pairs_sum_to_zero([-100, -1, -1]) == False
assert not pairs_sum_to_zero([1, 2, 3, 4])
assert not pairs_sum_to_zero([5, 1, 2, 4])
assert not pairs_sum_to_zero([1, 5, 2, 4])
assert not pairs_sum_to_zero([4, 1, 2, 3])
assert not pairs_sum_to_zero([5, 2, 1, 4])
assert not pairs_sum_to_zero([6, 3, 2, 1])
assert pairs_sum_to_zero([-1, 1, 0, 1])
assert pairs_sum_to_zero([-1, 1, 2]) is True
assert pairs_sum_to_zero([-1, 1, 2, -3, -2]), "Incorrect Result"
assert not pairs_sum_to_zero([-3, -5, -7, 2, 1]), "Incorrect Result"
assert pairs_sum_to_zero([-4, 0, 4, 0, -5]), "Incorrect Result"
assert pairs_sum_to_zero([-3, 0, 3, -4, -5]), "Incorrect Result"
assert pairs_sum_to_zero([1, 2, 3]) == False
assert pairs_sum_to_zero([-4, -6, -5]) == False
assert not pairs_sum_to_zero([1, 3, -5, 7, -8]), "Example"
assert not pairs_sum_to_zero([-8, -5, -6, -7, -8]), "Example"
assert not pairs_sum_to_zero([-5, 2, -6, -8]), "Example"
assert 0 == pairs_sum_to_zero([3, -2, -4, -1])
assert False == pairs_sum_to_zero([-1, 2, -3, 5])
assert pairs_sum_to_zero([-5, 3, 2]) == False
assert pairs_sum_to_zero([-5, -3]) == False
assert pairs_sum_to_zero([-3, -2]) == False
assert pairs_sum_to_zero([-5, 1, 3, 1]) == False
assert pairs_sum_to_zero([-3, 4, 5]) == False
assert not pairs_sum_to_zero([1,2,3,-5])
assert not pairs_sum_to_zero([1,2,5,-4])
assert not pairs_sum_to_zero([-1, -2, -3, 4, -1]), 'No pair of numbers that sum to zero exists'
assert pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8]) is False
assert not pairs_sum_to_zero([-4, 3, -1, -7]), "these should fail"
assert not pairs_sum_to_zero([5, 3, 6, 2])
assert not pairs_sum_to_zero([-2, -1, -2, -3])
assert pairs_sum_to_zero([2, -4, 0, 3, -4, -2])
assert pairs_sum_to_zero([-1, 0, -1, 2, 1]) == True
assert pairs_sum_to_zero([-2, -3, -1, 1, 2, 2])
assert pairs_sum_to_zero([8, -8, -9, -10, -5])
assert pairs_sum_to_zero([-1, 0, 1, -1, 3, -4]) is True
assert pairs_sum_to_zero([-1, -2, 0, 1, -1]), "Should have returned False"
assert pairs_sum_to_zero([9, 1, -1, 1, -5]) is True
