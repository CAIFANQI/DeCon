

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
assert pairs_sum_to_zero([-1, 2, 3, 4]) == False, "Wrong answer"
assert 	pairs_sum_to_zero([1, 2, 3]) == False, "Incorrect"
assert 	pairs_sum_to_zero([1, -1, 3, -3]) == True, "Incorrect"
assert 	pairs_sum_to_zero([-1, 2, -3, 3]) == True, "Incorrect"
assert 	pairs_sum_to_zero([1, 2, 3, 3]) == False, "Incorrect"
assert 	(pairs_sum_to_zero([]) == False)
assert 	(pairs_sum_to_zero([1, -1, 0]) == True)
assert 	(pairs_sum_to_zero([1, 2, 3]) == False)
assert pairs_sum_to_zero([1,2,2,2]) == False
assert pairs_sum_to_zero([2,3]) == False, "Wrong output for list input [2,3]"
assert pairs_sum_to_zero([-2,3]) == False, "Wrong output for list input [-2,3]"
assert 	pairs_sum_to_zero([1, 1, 1]) == False
assert 	pairs_sum_to_zero([1, 1, -1, 1]) == True
assert 	(pairs_sum_to_zero([1, 2, 3, 4, 5, 6, -3, -2, 0]) == True), "Fails"
assert 	(pairs_sum_to_zero([1, 2, 3, 4, 5, 6, -5, -4, -3, -2, 0]) == True), "Fails"
assert pairs_sum_to_zero([]) == False
assert 	(pairs_sum_to_zero([1, 4, 1, 3, 1, 2, 2, 3, 4])) == False
assert pairs_sum_to_zero([1, 2, 3, 4]) == False
assert pairs_sum_to_zero([1, -1, 1, -1]) == True
assert pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, -1]) == True
assert 	pairs_sum_to_zero([1, 3, 5, 7]) == False
assert 	pairs_sum_to_zero([1]) == False
assert 	pairs_sum_to_zero([1, 1]) == False
assert 	pairs_sum_to_zero([1, -1]) == True
assert 	pairs_sum_to_zero([1, -1, 1]) == True
assert 	pairs_sum_to_zero([1, 2, 3, -1, 1]) == True
assert pairs_sum_to_zero([]) == False, "function pairs_sum_to_zero should return False when given an empty list"
assert pairs_sum_to_zero([1,2,3]) == False, "function pairs_sum_to_zero should return False when given a list with a single even number"
