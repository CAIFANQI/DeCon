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
assert below_zero([5, -5]) == False
assert below_zero([5, -4]) == False
assert below_zero([5, -5, 1]) == False
assert below_zero([5, -5, -1]) == True
assert below_zero([5, -5, -6]) == True
assert below_zero([1, 2, 3]) == False
assert below_zero([-1, 0, 0, 1]) == True
assert below_zero([-3, -4, -5, 5, -4, -3]) == True
assert below_zero([-3, -4, -5, 5, -4, -5]) == True
assert below_zero([0, 0, 0, 0, 0, 0]) == False
assert below_zero([1, 2, 3, 4, 5]) is False
assert below_zero([-1, 2, -3, 4, -5]) is True
assert below_zero([-1, 2, 3, 4, -5]) is True
assert below_zero([-1]) is True
assert below_zero([-1, -2]) is True
assert below_zero([-1, 2]) is True
assert below_zero([1, 2]) is False
assert below_zero([100, 200, 300, -100, 400, 200, 1000]) == False
assert below_zero([100, -50, -150, -200]) is True
assert below_zero([-500, 1000, -500, -500, -500]) is True
assert below_zero([100, 100, 100, 100, 100]) is False
assert below_zero([100, 100, 100, -100, -100]) is False
assert below_zero([100, 100, 100, 200, -500]) is False
assert below_zero([5, -3, -5, -1]) == True
assert below_zero([-1]) == True
assert below_zero([1]) == False
assert below_zero([5, -5, 1, -1, -1, -1, 1, -1, -1, -1]) == True
assert below_zero([5, 3, 8, -7, -1, -2, -5, 4, -2, 3]) == False
assert below_zero([-5, -5, -1, -1, -1, -1, -1, -1, -1, -1]) == True
assert below_zero([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == False
assert below_zero([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == True
assert below_zero([-5, -10, -2, 0, -15, -20]) is True
assert below_zero([5, 10, 15, 20, 25, 30]) is False
assert below_zero([0]) is False
assert below_zero([-2, 0, -1]) is True
assert below_zero([1, 0, 2, -5, 1]) == True
assert below_zero([5, 4, 3, 2, 1]) == False
assert below_zero([1, 2, -10, 3, 5]) == True
assert below_zero([1, -10, 2, 3, 5]) == True
assert below_zero([10, 10, -10, -10, -10]) == True
assert below_zero([100, 200, 300, 400, 500]) is False
assert below_zero([-1, -1, -1]) == True
assert below_zero([-1, 1, -1]) == True
assert below_zero([1, 1, 1]) == False
assert below_zero([-1, -1, 1]) == True
assert below_zero([1, -1, -1]) == True
assert below_zero([-1, 1, 1]) == True
assert below_zero([-1, -1, -1, -1, -1, -1]) == True
assert below_zero([-1, -1, -1, -1, -1, -1, 1]) == True
assert below_zero([-1]) == True, "Bank account falls into minus on single withdraw"
assert below_zero([-1, 1, -1]) == True, "Bank account falls into minus after two operations"
assert below_zero([1, -2, 3, -1]) == True, "Bank account falls into minus after three operations"
assert below_zero([1, -2, 3, 1, -1]) == True, "Bank account falls into minus after four operations"
assert below_zero([-1, 1, -1, 1, -1]) == True, "Bank account falls into minus after five operations"
assert below_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
assert below_zero([20, 10, -5, -10, -5, -2, -5, 20]) is False
assert below_zero([1, 2, 0, 0, -3, -5]) == True
assert below_zero([1, 2, 0, 0, -3, -5, 0, 0, 0, 0, -100]) == True
assert below_zero([1, 2, 0, 0, -3, -5, 0, 0, 0, 0, -100, 100, -10]) == True
assert below_zero([1, -1, 1, -1, 1, -1, 3, -3]) is False
assert below_zero([1, 1, -4, 1, 1])
assert below_zero([1, -5, 1, 1, 1])
assert below_zero([-1, 1, 1, 1, 1])
assert below_zero([-1, 1, 1, 1, -1])
assert below_zero([-1, 1, 1, -3, 1])
assert below_zero([-1, 1, -4, 1, 1])
assert below_zero([-1, -5, 1, 1, 1])
assert below_zero([-1, -5, -1, -1, -1])
assert below_zero([1, -5, -1, -1, -1])
assert below_zero([1, 1, -1, -1, -1])
assert below_zero([5, -2, 3, 10, 1]) is False
assert below_zero([0]) == False
assert below_zero([-10, -50, -100, -20, -60, -90, -10]) == True
assert below_zero([10, 50, 100, 20, 60, -90, -80]) == False
assert below_zero([10, 50, 100, 20, 60, -90, -70]) == False
assert below_zero([1, -1, 1, -1]) == False
assert below_zero([2, 2, -3, -3]) == True
assert below_zero([2, 2, 3, 3]) == False
assert below_zero([-1, -1, -1, -1]) == True
assert below_zero([1, 1, 1, 1]) == False
assert below_zero([-2, -2, -2, -2]) == True
assert below_zero([0, 0, 0, 0]) == False
assert below_zero([1, 1, -2, -2, -2, 1, 1, 1]) == True
assert below_zero([4, 4, -4, -4, -4, 4, 4, 4]) == True
assert below_zero([5, -5, -5, -5, 5]) == True
assert below_zero([100, 50, 200, -100, 25, -100, 50, 25, -100, 100, 200]) is False
assert below_zero([100, 50, 200, -100, 25, -100, 50, 25, -100, 100, 200, 100]) is False
assert below_zero([50, -10, -20, -30, 40]) == True
assert below_zero([0, 1]) == False
assert below_zero([0, -1]) == True
assert below_zero([0, -1, 1]) == True
assert below_zero([0, -1, -1]) == True
assert below_zero([10, 15, -20, -25, 30, -20, -10, 10]) is True
assert below_zero([2, 3, 1, 5, -4, 6, -8, -9, 8, 7, -10, 7]) == True
assert below_zero([10, -20, -20, -20, -20]) == True
assert below_zero([10, -10, -20, -30, -10]) == True
assert below_zero([10, -10, -20, -30, -10, -10]) == True
assert below_zero([10, -20, -10, -30, -10, -10]) == True
assert below_zero([10, -10, -10, -10, -10, -10]) == True
assert below_zero([-10, -10, -10, -10, -10, -10]) == True
assert below_zero([10, 10, 10, 10, 10, 10]) == False
assert below_zero([10, -10, 10, -10, 10, -10]) == False
assert below_zero([10, -10, 10, -10, 10, -10, 10]) == False
assert below_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) is False
assert below_zero([-6, 1, -1, 2, 3]) is True
assert below_zero([1, -3, 1, 1, -3]) is True
assert below_zero([-6, 2, 4, 1, -1, -6, -1, -4, -4, -6]) is True
assert below_zero([1, 1, 1, 1, 1]) is False
assert below_zero([-10, 20, 30, -20, -30]) is True
assert below_zero([20, 5, 10, 3, 2, 3, 11, 3, 2, 1]) is False
assert below_zero([-5, -10, -3, -2, -3, -11, -3, -2, -1]) is True
assert below_zero([5, 10, 3, 2, 3, 11, 3, 2, 1]) is False
assert below_zero([2, 3, 2, 1]) is False
assert below_zero([-5, -10, -3, -2, -3, -11, -3, -2, -1, -1]) is True
assert below_zero([10, 2, -20, -10, 10, -10])
assert below_zero([-5, -3, -5, 8, -3, 1]) == True
assert below_zero([-20, 20, -10, 20, 10]) == True
assert below_zero([1, 2, 3]) == False, "All deposits"
assert below_zero([-1, -2, -3]) == True, "All withdrawals"
assert below_zero([5, -5]) == False, "Deposit then withdrawal"
assert below_zero([-5, 5, -5]) == True, "Withdrawal then deposit then withdrawal"
assert below_zero([1, 0, 1]) == False
assert below_zero([1, 2, 3, -4, -5]) == True
assert below_zero([-1, -2, -3, -4, -5]) == True
assert below_zero([-1, 2, 3, 4, 5]) == True
assert below_zero([100, 200, 300, -100, -300, 100]) == False
assert below_zero([1000, -50, 500, -100, 0, -200, 0]) == False
assert below_zero([50, 40, 30, 20, 10]) == False
assert below_zero([-10, -20, -30, -40, -50]) == True
assert below_zero([100, -100, -100, 100, 50, -100, 100]) == True
assert below_zero([200, -100, 100, -200, -50, -150, 150]) == True
assert below_zero([10, 20, 30, -10]) == False
assert below_zero([10, -10, -10, -10]) == True
assert below_zero([-10, -10, -10, -10]) == True
assert below_zero([10, 20, 30, 40]) == False
assert below_zero([-10, -20, -30, -40]) == True
assert below_zero([-5, 5, -10, 7, -10, -20, 20, -30, 30, -40, 40, -50, 50, -60, 60, -70, 70, -80, 80, -90, 90, -100, -105]) is True
assert below_zero([10]) == False
assert below_zero([10, -10]) == False
assert below_zero([10, -10, 15]) == False
assert below_zero([10, -10, -15]) == True
assert below_zero([10, -10, -15, 10]) == True
assert below_zero([-10, 10, -10, -15, 10]) == True
assert below_zero([-10, 10, -10, -15, 10, -5]) == True
assert below_zero([1, 2, -3, -3]) == True
assert below_zero([-1, -2, -3]) == True
assert below_zero([1, 2, 3, 4, 5]) == False
assert below_zero([-1, 2, -3, 4, -5]) == True
assert below_zero([1, -1, 1, -1, 1]) == False
assert below_zero([1, 2, 3, 4, 5, 6, 7]) == False
assert below_zero([-1, 2, 3]) == True
assert below_zero([-1, -2, 3]) == True
assert below_zero([-1, 2, -3]) == True
assert below_zero([1, -2, -3]) == True
assert below_zero([-1, -2, 3, -4, 5, 6, -7, -8, 9, -10]) == True
assert below_zero([1, 1, -2, 3, 1]) is False
assert below_zero([50, -20, 100, -5, -1]) == False
assert below_zero([-50, -20, -100, -5, -10]) == True
assert below_zero([0, 0, 0, 0, 0]) == False
assert below_zero([10, -20, -30, -40]) == True
assert below_zero([-20, -10, -10, -10]) == True
assert below_zero([-20, 10, -10, -10]) == True
assert below_zero([20, -10, 30, -10, 50, -100, 20]) == True
assert below_zero([100, 200, -100, -100, 500]) == False
assert below_zero([50, 100, -50, 200, -100, -150]) is False
assert below_zero([50, -20, 10, -10, 20, -10, -10, 30, -10, 10]) == False
assert below_zero([10, -20, -20, -20, -20, -20, -20, -20, -20, -20]) == True
assert below_zero([100, 50, -100, 50, 200, 50]) is False
assert below_zero([10, 20, -10, 20, 10]) == False
assert below_zero([10, 20, -10, 20, 10, -10, 50, -10, 20, -10, -10, -20, -10, 20, 10]) == False
assert below_zero([-1,2,3]) == True
assert below_zero([-1,-2,-3]) == True
assert below_zero([2,-2,3]) == False
assert below_zero([1,-3,1]) == True
assert below_zero([1,1,1]) == False
assert below_zero([-1,-1,-1]) == True
assert below_zero([1,-1,-1]) == True
assert below_zero([-1,1,-1]) == True
assert below_zero([2,-2,2,-2,2]) == False
assert below_zero([-10, -20, -30, -40, -50]) is True
assert below_zero([-10, 100, -100, 30, -40, -100, -100, 20]) is True
assert below_zero([-10, 10, -20, 50, 40, -30, 20]) is True
assert below_zero([5, 3, 5, 3, 5]) == False
assert below_zero([5, -3, 5, 3, 5]) == False
assert below_zero([20, -5, 10, -3, -5, 4, 10]) == False
assert below_zero([-1, -2, -3, -4]) == True
assert below_zero([10, 10, 10, 10, 10]) is False
assert below_zero([10, -10, 10, -10, 10]) is False
assert below_zero([10, -10, 10, -10, -10]) is True
assert below_zero([-6, -7, -3, -3, -3, -3]) == True
assert below_zero([2, -1, -1, -1, -1, -1]) == True
assert below_zero([6, -2, 3, -2, 0, 4]) == False
assert below_zero([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == True
assert below_zero([-1, 2, 3, -4, 5]) == True
assert below_zero([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == True
assert below_zero([1, 2, 3, 1, 2, 3]) is False
assert below_zero([-1, -2, -3, -1, -2, -3]) is True
assert below_zero([-1, -2, 3, -1, -2, 3]) is True
assert below_zero([50, -40, 30, -10, -80]) == True
assert below_zero([50]) == False
assert below_zero([50, -10]) == False
assert below_zero([50, -10, -1]) == False
assert below_zero([50, -10, -1, 10]) == False
assert below_zero([50, -10, -1, 10, -1, -1, 10, 100]) == False
assert below_zero([1, -2, 3]) == True
assert below_zero([-1, -1]) == True
assert below_zero([1, 1]) == False
