from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0

    for op in operations:
        balance += op
        if balance == 0:
            return True

    return False
assert below_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) == True
assert below_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == False
assert below_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]) == False
assert below_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1]) == False
assert 	below_zero([1,2,3,4,5]) == False
assert 	below_zero([1,1,1,1]) == False
assert 	below_zero([-1,1,1,1]) == True
assert 	below_zero([1,2,-3,-4]) == True
assert 	below_zero([1,2,-3,-4,5]) == True
assert 	below_zero([1,2,-3,-4,5,6]) == True
assert 	below_zero([1,2,-3,-4,5,6,7]) == True
assert 	below_zero([1,2,-3,-4,5,6,7,8]) == True
assert 	below_zero([1,2,-3,-4,5,6,7,8,9]) == True
assert 	below_zero([1,2,-3,-4,5,6,7,8,9,10]) == True
assert 	below_zero([1, 1, 1, 1]) == False
assert 	below_zero([1, 1, 2, 3, 4, 5]) == False
assert 	below_zero([1, 1, 2, 3, 4, -1, -3, -5, -1, 1, 1]) == False
assert 	below_zero([1, 1, 2, 3, 4, -1, -3, -5, -1, 1, 1, 1, 1]) == False
assert 	below_zero([1,2,3,4,5,0,10]) == False
assert 	below_zero([-1,2,3,4,5,0,10]) == True
assert 	below_zero([1,-2,3,4,5,10,10]) == True
assert 	below_zero([1,-2,3,4,5,10,10,5]) == True
assert below_zero([1, 2, 3]) == False
assert 	below_zero([1, 2, -5, 4, 5]) == True
assert below_zero([1, 2, -4]) is True
assert below_zero([1, 2, -5]) is True
assert below_zero([1, 2, 3, 4, 5]) == False
assert below_zero([1, 2, -5, 4, -5]) == True
assert below_zero([1, 2, -1, 4, 5]) == False
assert below_zero([1, -2, 3, 4, -5]) == True
assert below_zero([1, 2, 3, 4, 5, 6]) == False
assert below_zero([1, -2, 3, 4, -5, 6]) == True
assert 	below_zero([1, -3, 2, -3, 4, 6, 7, -1, 6, 7, -1]) == True
assert 	below_zero([1, -3, 2, -3, 4, 6, 7, -1, 6, 7, -1, 6, 7, -1]) == True
assert 	below_zero([1, -3, 2, -3, 4, 6, 7, -1, 6, 7, -1, 6, 7, -1, 6, 7, -1, 6, 7, -1]) == True
assert 	below_zero([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11])
assert not below_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
assert not below_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 11])
assert not below_zero([1, 2, 3, 4, 5, 6, 7, 8, 9])
assert not below_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
assert not below_zero([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1])
assert not below_zero([])
assert 	below_zero([1, 2, 3, 4, 5, 6, -3, -4, -5, -6, 0]) == False, 'error2'
assert 	below_zero([1, -2, 3, 4, 5, 6, -3, -4, -5, -6, -1, 0]) == True, 'error5'
assert 	below_zero([1, 3, 5, -3, -1, -3]) == False
assert 	below_zero([1, 3, 5, -3, -1, -3, -3]) == True
assert 	below_zero([1, 3, 5, -3, -1, -3, -3, -3]) == True
assert below_zero([1, 2, 3, 4, 5]) is False
assert below_zero([1, 1, 1, 1]) is False
assert 	below_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) is False
assert 	below_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, 13, 14, 15]) is False
assert 	below_zero([-1,-2,1]) == True
assert 	below_zero([-1,2,3]) == True
assert 	below_zero([1,-2,3,4]) == True
assert 	below_zero([1,-2,3,4,5,-6]) == True
assert 	below_zero([1,2,-3,4,-5,6,7]) == True
assert 	below_zero([1,2,3,4,5,-6,7,8]) == False
assert 	below_zero([1,-2,3,4,-5,6,7,8]) == True
assert below_zero([1, 3, 5]) == False
assert below_zero([-1, 3, 5]) == True
assert below_zero([0, 1, -3, 5, -2, 3, 8, 9, -3, 5]) is True
assert below_zero([0, 1, -3, 5, -2, 3, 8, 9, -3, 5, -1]) is True
assert below_zero([1, 1, 2, 3, 4, 5]) == False
assert below_zero([-1, 1, 1, 2, 3, 4, 5, -1, -1]) == True
assert below_zero([-1, 1, 1, 2, 3, 4, 5, -1, -1, -1, 1, 1, 1, 2, 3, 4, 5]) == True
assert 	below_zero([1, 2, 3, 4]) == False
assert 	below_zero([1, 2, 3, 4, 5]) == False
assert 	below_zero([1, -2, 3, 4, 5]) == True
assert 	below_zero([1, -2, 3, 4, 5, -6]) == True
assert 	below_zero([1, -2, 3, 4, 5, 6, 7]) == True
assert 	below_zero([5, 1, 1, 1]) == False
assert 	below_zero([1, 1, 1, -1]) == False
assert 	below_zero([1, 1, 1, -1, 1]) == False
assert 	below_zero([1, -3, 6, -2, -3, 6, -2]) == True
assert 	below_zero([1, -3, 6, -2, -3, 6, -2, -3, 6, -2, -3, 6, -2]) == True
assert 	below_zero([1, 2, 3, -4, -3, -2, -1]) is True
assert below_zero([1, 1, 1, 1, 1]) == False
assert below_zero([1, 1, 1, 1, 1, 1, 1, 1]) == False
assert below_zero([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
assert 	below_zero([5, 5]) == False
assert 	below_zero([5, 5, -5, 5, 5]) == False
assert 	below_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == False
assert 	below_zero([1, 2, 3, 4, 5, 6, 7, 8, -1, 9, 10, 11, 12]) == False
assert 	below_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, -1, 10, 11, 12, 13]) == False
assert 	below_zero([-1, -2, 3, 4, 5, 1]) is True
assert 	below_zero([5, -4, 3, 4, 5, 1]) is False
assert 	below_zero([1, -2, -3, 4, 5, 1, -1]) is True
assert 	below_zero([5, -4, -3, 4, 5, 1, -1, -1]) is True
assert 	below_zero([0,1]) == False
assert 	below_zero([0,-1]) == True
assert 	below_zero([1,1]) == False
assert 	below_zero([0,-1,0]) == True
assert 	below_zero([-1,2,3,4,-5,6,-5]) == True
assert 	below_zero([1,2,3,4,5,6,-6,-5]) == False
assert 	below_zero([1,2,3,4,5,6,7,8,-5]) == False
assert 	below_zero([5, 5, -5, -5, -5, 5, 5, -5, 5]) == True
assert 	below_zero([5, 5, -5, -5, 5, -5, 5, 5, 5]) == False
assert 	below_zero([5, 5, -5, 5, 5, 5, -5, 5]) == False
assert 	below_zero([1, -1, -1, -1]) == True
assert 	below_zero([1, 2, 3, 4, 5, -6, -5, -4, -3, -2, -1, 1, 1, 1, 1]) == True
assert 	below_zero([1, 2, 3, 4, 5, 6, -4, -3, -2, -1, -6, -5, -4, -3, -2, -1, 1, 1, 1, 1]) == True
assert 	below_zero([1, -1, -1, -1, -1]) == True
assert 	below_zero([1, 2, 3, 4, 5, 6, -7, -5, -4, -3, -2, -1, 1, 1, 1, 1]) == True
