

def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    for i in range(1, len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False
assert 	triples_sum_to_zero([]) == False
assert not triples_sum_to_zero([])
assert not triples_sum_to_zero([1, 1, 1, 1])
assert not triples_sum_to_zero([1, 2, 3])
assert triples_sum_to_zero([0, 0, 0, 0])
assert triples_sum_to_zero([0, 0, 0, 0, -1])
assert triples_sum_to_zero([0, 0, 0, 0, 1])
assert triples_sum_to_zero([0, 0, 0, 0, -1, 0])
assert triples_sum_to_zero([0, 0, 0, 0, 0, 0])
assert triples_sum_to_zero([0, 0, 0, 0, 0, -1, 0, 0, 0, 1])
assert 	triples_sum_to_zero([1, 2, 3, 4, 5, 6]) == False
assert 	triples_sum_to_zero([1, 2, 3, -3, -2, 1]) == True
assert 	triples_sum_to_zero([1, 2, 3, -3, -2, 1, 10, 15]) == True
assert 	triples_sum_to_zero([1, 2, 3, -3, -2, 1, 10, 15, 10, 0]) == True
assert 	triples_sum_to_zero([1, 2, 3, -3, -2, 1, 10, 15, 10, 0, -3]) == True
assert 	triples_sum_to_zero([1, 2, 3, -3, -2, 1, 10, 15, 10, 0, -3, 0]) == True
assert 	triples_sum_to_zero([0, 1, 2, 3, 1]) == False
assert 	triples_sum_to_zero([0, 2, 1, 3, 1]) == False
assert 	triples_sum_to_zero([0, 2, 1, 1, 1]) == False
assert 	triples_sum_to_zero([0, -1, 2, -3, 1]) == True
assert 	triples_sum_to_zero([-3, -2, -1, 0, 1]) == True
