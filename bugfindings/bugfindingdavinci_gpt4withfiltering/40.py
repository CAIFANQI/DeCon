

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
assert triples_sum_to_zero([2, 0, -2]) == True
assert triples_sum_to_zero([1, 2, 3]) == False
assert triples_sum_to_zero([1, 2, -3]) == True
assert triples_sum_to_zero([1, 2, -2]) == False
assert triples_sum_to_zero([2, 3, 6, -1, -2, -3]) == True
assert triples_sum_to_zero([1, 2, 3, 4, 5, 6]) == False
assert triples_sum_to_zero([-3, -2, -1, 0, 1, 2, 3]) == True
assert triples_sum_to_zero([1, 2, 3, 4, 5, 6, -10, -20, -30]) == True
assert triples_sum_to_zero([]) == False
assert triples_sum_to_zero([0, 0, 0]) == True
assert triples_sum_to_zero([2, 3, 1, -2, -1, 0, 1, 0, -1]) == True
assert triples_sum_to_zero([2, 3, 1, -2, -1, 0, 1, 0, -1, -2, 1]) == True
assert triples_sum_to_zero([1, -1, -1, 2, 3, -3, -1]) == True
assert triples_sum_to_zero([1, -1, -1, 2, 3, -3, -1, 4, -4]) == True
assert triples_sum_to_zero([1, -1, -1, 2, 3, -3, -1, 4, -4, -1]) == True
assert triples_sum_to_zero([1, -1, -1, 2, 3, -3, -1, 4, -4, -1, 0]) == True
assert triples_sum_to_zero([5, 1, 4, 7, 10]) == False
assert triples_sum_to_zero([1, -1, 0, 2, -2]) == True
assert triples_sum_to_zero([-2, -1, 0, 1, 2]) == True
assert triples_sum_to_zero([1]) == False
assert triples_sum_to_zero([1, 3, 5]) == False
assert triples_sum_to_zero([3, -1, 5]) == False
assert triples_sum_to_zero([3, -1, -2]) == True
assert not triples_sum_to_zero([3])
assert not triples_sum_to_zero([3, 3])
assert not triples_sum_to_zero([3, -3])
assert triples_sum_to_zero([3, -3, 0])
assert triples_sum_to_zero([3, -3, -3, 1, 0, 2])
assert triples_sum_to_zero([0, 1, 1, 2, 3, 3]) == False
assert triples_sum_to_zero([1, 2, 3, -1, -2, -3]) == True
assert triples_sum_to_zero([1, 2, 3, -1, -2, -3, 4, 5, 6]) == True
assert triples_sum_to_zero([1, 2, 3, -1, -2, -3, 4, 5, 6, -1]) == True
assert triples_sum_to_zero([-1, -1, -1]) == False
assert triples_sum_to_zero([1, 1, 1]) == False
assert triples_sum_to_zero([0, 3, 3]) == False
assert triples_sum_to_zero([0, 0, 3]) == False
assert triples_sum_to_zero([-1, 1, 2, -2, 5, -5, 8]) == False
assert triples_sum_to_zero([-1, 1, 2, -2, 5, -5, 8, 0]) == True
assert triples_sum_to_zero([-1, 1, 2, -2, 5, -5, 8, 0, 0]) == True
assert triples_sum_to_zero([]) is False
assert triples_sum_to_zero([-2, 0, 4, 5, -2, 0, 5]) is True
assert triples_sum_to_zero([-3, 0, 1, 4, 5]) is False
assert triples_sum_to_zero([0, 0, 0]) is True
assert triples_sum_to_zero([1, 1, 1]) is False
assert triples_sum_to_zero([-1, 0, 1]) is True
assert triples_sum_to_zero([0,0,0,0]) == True
assert triples_sum_to_zero([1,2,3]) == False
assert triples_sum_to_zero([0,0,0,1,2,3]) == True
assert triples_sum_to_zero([-1,0,0,1,2,3]) == True
assert triples_sum_to_zero([-5, -1, 0, 2, 4]) == False
assert triples_sum_to_zero([0, 1, 2, 3, 4]) == False
assert triples_sum_to_zero([-1, 0, 1, 2, 3]) == True
assert triples_sum_to_zero([-6, 2, 0, 2, 0]) is False
assert triples_sum_to_zero([-6, 2, 0, 2, -6, 0]) is False
assert triples_sum_to_zero([3, -3, 6, -2, -5, 8, -7]) == True
assert triples_sum_to_zero([1, 2, 3, 4, 5, 6, 7]) == False
assert triples_sum_to_zero([1, 2, 3, -2, -1, -3]) == True
assert triples_sum_to_zero([1, 2, -3, -2, -1, 3]) == True
assert triples_sum_to_zero([-5, 2, -1, -2, 0]) == True
assert triples_sum_to_zero([0, 2, 0]) == False
assert triples_sum_to_zero([-2, 2, 0]) == True
assert triples_sum_to_zero([-4, 2, 1, -3]) == True
assert triples_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
assert triples_sum_to_zero([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == True
assert triples_sum_to_zero([1, 0, 3, -2]) == False
assert triples_sum_to_zero([2, 3, 4, -2, 1, -1]) == True
assert triples_sum_to_zero([2, 3, 4, -2, 1, -1, -3]) == True
assert triples_sum_to_zero([-1, 2, -3, 4, -5, 6, -7, -1, 1, -3, -4, 5, -6, 7]) == True
assert triples_sum_to_zero([1, 1]) == False
assert triples_sum_to_zero([1, 1, 2]) == False
assert triples_sum_to_zero([-1, -2, 3]) == True
assert triples_sum_to_zero([1, 2, -3, -2]) == True
assert triples_sum_to_zero([1, 2, -3, -2, 6]) == True
assert triples_sum_to_zero([3, 2, -3, -2, 1]) == True
assert triples_sum_to_zero([0, 1, 2]) == False
assert triples_sum_to_zero([-1, 0, 1, 2, -3]) == True
assert triples_sum_to_zero([0, 1, 2, 3]) == False
assert triples_sum_to_zero([1, 2, 3, 4]) == False
assert triples_sum_to_zero([2, 3, -1, -2, -3]) == True
assert triples_sum_to_zero([-5, -3, -1, -2, -3, 6]) == True
assert triples_sum_to_zero([1, 0, 2, -1, -3, 5]) == True
assert triples_sum_to_zero([1, 0, 2, -1, -3, -5]) == True
assert triples_sum_to_zero([1, 0, 2, -1, -3, 0]) == True
assert triples_sum_to_zero([1, 0, 2, -1, -3, -5, -6]) == True
assert triples_sum_to_zero([-2, 2, 3, -1, -1, -1]) == True
assert triples_sum_to_zero([0, 0, 0, 0, 0, 0, 0]) == True
assert triples_sum_to_zero([-1, -1, -1, 0, 0, 0, 0]) == True
assert triples_sum_to_zero([0, 0, 1, 0, -2, 2, -1]) == True
assert triples_sum_to_zero([1, -2, 3, 0, -6, 7, 4, -3, 1]) == True
assert triples_sum_to_zero([1, -2, 3, 0, -6, 7, 4, -4, 1]) == True
assert triples_sum_to_zero([1, -2, 3, 0, -6, 7, 4, -3, -3]) == True
assert triples_sum_to_zero([-2, 3, 0, -6, 7, 4, -3, -3]) == True
assert triples_sum_to_zero([3, 0, -6, 7, 4, -3, -3]) == True
assert triples_sum_to_zero([1, 2]) == False
assert triples_sum_to_zero([1, 1, 1, -3, 3]) == False
assert triples_sum_to_zero([1, 1, 1, -3, 3, 3, -6]) == True
assert triples_sum_to_zero([1, 1, 1, -3, 3, 3, -6, -3]) == True
assert triples_sum_to_zero([0]) == False, "singleton list"
assert triples_sum_to_zero([1, 2, 3]) == False, "no sum to zero"
assert triples_sum_to_zero([3, 1, -3, 2, -1]) == True, "three triples"
assert triples_sum_to_zero([3, 1, -3, 2, -1, 2, -2]) == True, "four triples"
assert triples_sum_to_zero([3, 1, -3, 2, -1, 2, -2, -2]) == True, "five triples"
assert triples_sum_to_zero([3, 1, -3, 2, -1, 2, -2, -2, 2]) == True, "six triples"
assert triples_sum_to_zero([0, 1, -1, 2, -2, 3, -3]) == True, "seven triples"
assert triples_sum_to_zero([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == True
assert triples_sum_to_zero([0, 1, 2, 3, 4, 5]) == False
assert triples_sum_to_zero([-5, -4, -3, -2, -1, 0, 0, 0, 1, 2, 3, 4, 5]) == True
assert triples_sum_to_zero([1, 2, 3, 4, 5]) == False
assert triples_sum_to_zero([0, 0, 1, 2, 3, 4, 5]) == False
assert triples_sum_to_zero([1, 2, 3, 4, -5, -4, -3, -2, -1, 0]) == True
assert triples_sum_to_zero([0]) == False
assert triples_sum_to_zero([2, 3, -1, -1, -2]) == True
assert triples_sum_to_zero([1, 2, -3, -2, 0, 1, 2, -3]) == True
assert triples_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9]) == False
assert triples_sum_to_zero([1, 2, -3, -2, -1, 0]) == True
assert triples_sum_to_zero([1, 2, -3, -2, -1, 0, 2]) == True
assert triples_sum_to_zero([1, 2, -3, -2, -1, 0, 3, 1, 0]) == True
assert triples_sum_to_zero([1, 2, -3, -2, -1, 0, 3, 1, 0, 0]) == True
assert triples_sum_to_zero([1, 2, -3, -2, -1, 0, 3, 1, 0, 0, 0]) == True
assert triples_sum_to_zero([1, 2, -3, -2, -1, 0, 3, 1, 0, 0, 0, 0]) == True
assert triples_sum_to_zero([-10, -5, 0, 5, 10]) == True
assert triples_sum_to_zero([-10, -5, 0, 5, 10, 15, 3, -3]) == True
assert triples_sum_to_zero([-10, -5, 0, 5, 10, 15, 3, -3, 6, -6]) == True
assert triples_sum_to_zero([-3, 1, -1, 0, 2, 4])
assert not triples_sum_to_zero([1, 2, 3])
assert not triples_sum_to_zero([1, 2, 3, -2])
assert triples_sum_to_zero([5, 1, -5, 5, 3, 5]) == False
assert triples_sum_to_zero([5, 5, 5, 5, 5, 5]) == False
assert triples_sum_to_zero([0, 0, 0, 0, 0, 0]) == True
assert triples_sum_to_zero([1, -1]) == False
assert triples_sum_to_zero([3, -2, -1]) == True
assert triples_sum_to_zero([3, 1, -2, -1]) == True
assert triples_sum_to_zero([3, -2, -1, 0, 0, 1]) == True
assert triples_sum_to_zero([0, 3, -2, -1, 0, 0, 1]) == True
assert triples_sum_to_zero([3, -2, -1, 0, 0, 1, 0]) == True
assert triples_sum_to_zero([3, -2, -1, 0, 0, 1, 0, 0]) == True
assert triples_sum_to_zero([1, 0, -1]) == True
assert triples_sum_to_zero([1, 1, -2]) == True
assert not triples_sum_to_zero([0])
assert not triples_sum_to_zero([0,0])
assert not triples_sum_to_zero([1,2])
assert not triples_sum_to_zero([1,2,3])
assert triples_sum_to_zero([0,0,0,0])
assert triples_sum_to_zero([1,2,-3])
assert triples_sum_to_zero([-3,0,3,1])
assert triples_sum_to_zero([-3,0,3,1,5])
assert triples_sum_to_zero([1,2,-3,0,0])
assert triples_sum_to_zero([1,2,-3,4,5])
assert triples_sum_to_zero([-3,0,3,1,5,1,2,-3,4,5])
assert triples_sum_to_zero([2, 3, 4, 5, -3, -6, -1, 0, 0, 0])
assert triples_sum_to_zero([-2, 0, 2]) == True
assert triples_sum_to_zero([-4, 3, 0, 5, -2, -1]) == True
assert triples_sum_to_zero([0, 2, -2, 3, 1, 3, -2, 0]) == True
assert triples_sum_to_zero([0, 0, 0, 1]) is True
assert triples_sum_to_zero([0, 0, 0, -1]) is True
assert triples_sum_to_zero([0, 0, 0, -1, 1]) is True
assert triples_sum_to_zero([1, 2, 3]) is False
assert triples_sum_to_zero([-1, 2, 3]) is False
assert triples_sum_to_zero([1, 2, 3, -2, -2, 2, -1]) is True
assert triples_sum_to_zero([1, 2, 3, -2, -2, 2, -1, 3]) is True
assert triples_sum_to_zero([1, 4, -2, 4, 3, 1, 2, 3, 2, -1]) == True
assert triples_sum_to_zero([1, 4, -2, 4, 3, 1, 2, 3, 2, -1, 0]) == True
assert triples_sum_to_zero([1, 4, -2, 4, 3, 1, 2, 3, 2, -1, 0, -3]) == True
assert triples_sum_to_zero([1, 4, -2, 4, 3, 1, 2, 3, 2, -1, 0, -3, -6]) == True
assert triples_sum_to_zero([1, 4, -2, 4, 3, 1, 2, 3, 2, -1, 0, -3, -6, -1]) == True
assert triples_sum_to_zero([-5, -1, -1, 1, 2, 3, 4, 5]) == True
assert triples_sum_to_zero([1,2]) == False
assert triples_sum_to_zero([-4,0,4]) == True
assert triples_sum_to_zero([1,3,5,-2,-5,5,5,5,5,5,0]) == True
assert triples_sum_to_zero([1,3,5,-2,-5,5,5,5,5,5,0,0]) == True
assert triples_sum_to_zero([1,3,5,-2,-5,5,5,5,5,5,0,0,0]) == True
assert triples_sum_to_zero([-1, 2, 0]) == False
assert triples_sum_to_zero([5, 4, -3, 2, -1, -2, 1, -5]) == True
assert triples_sum_to_zero([1, 2, -3, -1, 0]) == True
assert triples_sum_to_zero([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, -6]) == True
assert not triples_sum_to_zero([])
assert triples_sum_to_zero([3, -3, 0, 2, -2, 1]) == True
assert triples_sum_to_zero([2, 3, -1, -2, -3, 1]) == True
assert triples_sum_to_zero([-1, -2, 3, 4, -3, 5]) == True
assert triples_sum_to_zero([2, 3, 4, -1, -2, -3]) == True
assert triples_sum_to_zero([3, -3, 0, -2, -2, -1]) == True
assert triples_sum_to_zero([2, 3, -1, 1, -2, -3]) == True
assert triples_sum_to_zero([0, 1, 2, -1, -2, -3]) == True
assert triples_sum_to_zero([0, 1, 2, -1, -2, -3, -4, 4]) == True
assert triples_sum_to_zero([1, -1, 2, -2, 3, -3]) == True
assert triples_sum_to_zero([0, 1, -1]) == True
assert triples_sum_to_zero([1, -1, 2, -2, 3, -3, 4, -4]) == True
assert triples_sum_to_zero([10, -2, -7, 3, 5, -1, 1, 2]) == True
assert triples_sum_to_zero([1, 2, -1, -2, 0]) == True
assert triples_sum_to_zero([-1]) == False
assert triples_sum_to_zero([0, 0, 0, 0, 0]) == True
assert triples_sum_to_zero([0, 1, 2, -1, -2, 4, -4]) == True
assert triples_sum_to_zero([0, 1, 2, -1, -2, 3, -3, 4, -4]) == True
assert triples_sum_to_zero([-2, 3, -1, 4, -5, 6, -6, 7, 8, 9, -11]) == True
assert triples_sum_to_zero([-2, 3, -1, 4, -5, 6, -6, 7, 8, 9, -11, -10]) == True
assert triples_sum_to_zero([-1, 2, 4, -2, 5, -5]) == False
assert triples_sum_to_zero([3, 4, 1, -3, 1, -1, -4, -1]) == True
assert triples_sum_to_zero([-1, 0, 1]) == True
assert triples_sum_to_zero([1, 1, 1, 1]) == False
assert triples_sum_to_zero([0, 1, 1, 1]) == False
assert triples_sum_to_zero([1, 1, -2, -1]) == True
assert triples_sum_to_zero([-5, -1, -1, 2, 3]) == True
assert triples_sum_to_zero([-5, -4, -3, -2, -1, 1, 2, 3, 10]) == True
assert triples_sum_to_zero([-1, -2, -1]) == False
assert triples_sum_to_zero([0, 0, 0, 0]) == True
assert triples_sum_to_zero([0, 1, -1, 0]) == True
assert triples_sum_to_zero([1, 0, -1, 0]) == True
assert triples_sum_to_zero([1, 0, -1, 0, 0]) == True
assert triples_sum_to_zero([1, 0, -1, 0, -1]) == True
assert triples_sum_to_zero([0, 3, 2, -1, 1, 0]) == True
assert triples_sum_to_zero([-1, 0, -1, 1, 2, 3]) == True
assert triples_sum_to_zero([-4, 2, 1, 2, -4, -4, 0]) == True
assert triples_sum_to_zero([4, 1, 2, -3, 1]) == True
assert triples_sum_to_zero([-1, 0, 2, 4]) == False
assert triples_sum_to_zero([3, -3, -2, 1, 2, 4]) == True
assert triples_sum_to_zero([3, -3, -2, 1, 2, 4, -1, 0, 2, 4]) == True
assert triples_sum_to_zero([-1, 1, 0]) == True
assert triples_sum_to_zero([2, 3, 4]) == False
assert triples_sum_to_zero([-4, 1, 2, 3, -1, 2, 3, -2, 4, -4]) == True
assert triples_sum_to_zero([-3, 2, 4, -1, -2, -3, -4, -5, -6, 0]) == True
assert triples_sum_to_zero([1, 2, 3, -4, -3, -2, -1, 0, 1, 2, 3, 4]) == True
assert triples_sum_to_zero([-5, 2, 10, 4, -2, -2, 0, -4, 7]) == True
assert triples_sum_to_zero([-5, 2, 10, 4, -2, -2, 0, -4, 7, -3]) == True
assert triples_sum_to_zero([1, 2, 3, 4, 5, -3, -2, -1, 0]) == True
assert not triples_sum_to_zero([1, 2, 3, 4])
assert triples_sum_to_zero([0, -3, 2, -1, -2, 5, -1])
assert triples_sum_to_zero([1, 2, 3, -3]) == True, "check the correctness of triples_sum_to_zero"
assert triples_sum_to_zero([1, 2, 3, -2]) == False, "check the correctness of triples_sum_to_zero"
assert triples_sum_to_zero([1, 2, 3, -1, -1]) == True, "check the correctness of triples_sum_to_zero"
assert triples_sum_to_zero([1, -1, 2, -2, 3, -3]) == True, "check the correctness of triples_sum_to_zero"
assert triples_sum_to_zero([0, 0, 1]) == False
assert triples_sum_to_zero([-3, 2, 0, 1, -1]) == True
assert triples_sum_to_zero([-1, -2, -3]) == False
assert triples_sum_to_zero([-2, 2]) == False
assert triples_sum_to_zero([-2, -2]) == False
assert triples_sum_to_zero([1, 0, 1]) == False
assert triples_sum_to_zero([-2, 0, 1, 2]) == True
assert triples_sum_to_zero([-5, 3, -3, 1, 0, 3, -3, 1, 0, 5, 0]) == True
assert triples_sum_to_zero([0, 1, 0]) == False
assert triples_sum_to_zero([0, 1, 0, 0]) == True
assert triples_sum_to_zero([0, 1, 0, 1]) == False
assert triples_sum_to_zero([-3, -2, 1, 2, 3])
assert not triples_sum_to_zero([-1, 1])
assert triples_sum_to_zero([0, 1, 2, -1, -2, -3])
assert triples_sum_to_zero([0, 0, 1]) is False
assert triples_sum_to_zero([1, 1, 0]) is False
assert triples_sum_to_zero([0, 1, 1]) is False
assert triples_sum_to_zero([0, 1, -1]) is True
assert triples_sum_to_zero([0, 1, -1, 2, -2]) is True
assert triples_sum_to_zero([1, 2, -3, 1, 2, -3]) is True
assert triples_sum_to_zero([1, 3, 5, 1, 3, 5]) is False
assert triples_sum_to_zero([1, 3, 5, 1, 2, -3]) is True
assert triples_sum_to_zero([1, 2, -2, 3, 4, -6]) is True
assert triples_sum_to_zero([0, 0, 0, 0, 0, 0]) is True
assert triples_sum_to_zero([0]) == False, "test failed"
assert triples_sum_to_zero([0, 0]) == False, "test failed"
assert triples_sum_to_zero([0, 0, 0]) == True, "test failed"
assert triples_sum_to_zero([1, 1, -2]) == True, "test failed"
assert triples_sum_to_zero([3, 1, -2]) == False, "test failed"
assert triples_sum_to_zero([-5, 2, 2, 4, -4, 7]) == True, "test failed"
assert triples_sum_to_zero([-5, 2, 2, 4, -4, 7, -1]) == True, "test failed"
assert triples_sum_to_zero([-5, 2, 2, 4, -4, 7, -1, -3]) == True, "test failed"
assert triples_sum_to_zero([5,5,5]) == False
assert triples_sum_to_zero([0,0,1,2,-1]) == True
assert triples_sum_to_zero([-1, 1, -1, 0, 1, 0, -1]) == True
assert triples_sum_to_zero([-10, -5, 1, 1, 2, 3, -2, 3, 0, -1, -1, -5, -2, 0, -1, -10]) == True
assert triples_sum_to_zero([-1, -1, -1, 0, 1, 1, 1, 0, 0, 0, -1, -1, -1]) == True
assert triples_sum_to_zero([-5, -3, -1, 0, 2, 4]) == True
assert triples_sum_to_zero([-1, 1]) == False
assert triples_sum_to_zero([-1, 1, 1]) == False
assert triples_sum_to_zero([-1, 1, 1, 0]) == True
assert triples_sum_to_zero([1, 1, 0, -1, -1]) == True
assert triples_sum_to_zero([1, 2, -3, 4, 5, 6, -7, 8, 9]) == True
assert triples_sum_to_zero([1, 2, -3, 4, 5, 6, -7, 8, 9, 0]) == True
assert triples_sum_to_zero([1, 2, -3, 4, 5, 6, -7, 8, 9, 0, -1]) == True
assert triples_sum_to_zero([-3, 0, 3]) == True
assert triples_sum_to_zero([0, 1, 1]) == False
assert triples_sum_to_zero([3, 1, 2, -3]) == True
assert triples_sum_to_zero([-5, 3, 1, 2, -3]) == True
assert triples_sum_to_zero([1, 0, 1, -1]) == True
assert triples_sum_to_zero([1, 0, 0, 1, -1]) == True
assert triples_sum_to_zero([1, 0, 1, 0, -1]) == True
assert triples_sum_to_zero([1, 0, 1, 0, 0, -1]) == True
assert triples_sum_to_zero([1, 0, 1, 0, 0, 0, -1]) == True
assert triples_sum_to_zero([0, -1, 1, 0]) == True
assert triples_sum_to_zero([0, -1, 1, 0, -1]) == True
assert triples_sum_to_zero([0, -1, 1, 0, -1, 1]) == True
assert triples_sum_to_zero([0, -1, 1, 0, -1, 1, 0]) == True
assert triples_sum_to_zero([-1, 0, 1, 0]) == True
assert triples_sum_to_zero([-1, 0, 1, 0, 0]) == True
assert triples_sum_to_zero([-1, 2, 1, -4]) == False
assert triples_sum_to_zero([3, 4, -2, -3, -4]) == False
assert triples_sum_to_zero([2, 3, 4, 5, -1, -6]) == True
assert triples_sum_to_zero([-4, 2, -1, -3, -4]) == False
assert triples_sum_to_zero([-2, 0, 3]) == False
assert triples_sum_to_zero([-2, 0, 1, 2, 3]) == True
assert triples_sum_to_zero([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 0]) == True
assert triples_sum_to_zero([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -2]) == True
assert triples_sum_to_zero([-1,0,1,2,-1,-4]) == True
assert triples_sum_to_zero([1,2,3,0,-1,-2]) == True
assert triples_sum_to_zero([0,2,3,1,-1,-2]) == True
assert triples_sum_to_zero([0,2,3,1,-1,-2,-2]) == True
assert not triples_sum_to_zero([1, 2, 3, 4, 5])
assert triples_sum_to_zero([2, 3, -1, -1, -1, -2])
assert triples_sum_to_zero([3, 2, -1, -1, -1, -2, -2])
assert triples_sum_to_zero([-2, 0, 2])
assert triples_sum_to_zero([-2, 0, 2, 1, -2])
assert triples_sum_to_zero([-2, 0, 2, 1, -2, 0])
assert triples_sum_to_zero([-2, 0, 2, 1, -2, 0, -1])
assert not triples_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
