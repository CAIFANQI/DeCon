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
assert not below_zero([100])
assert below_zero([100, -100, -2])
assert below_zero([-5, -10, -15, -20, -25, -30, -35]) == True, "-5 should return True"
assert below_zero([-15, -20, -25, -30, -35]) == True, "-15 should return True"
assert below_zero([-25, -30, -35]) == True, "-25 should return True"
assert below_zero([-35]) == True, "-35 should return True"
assert below_zero([-1, 0, -2]) == True
assert below_zero([-1, 0, -2, -3]) == True
assert below_zero([0, 0, -1, 0]) is True
assert below_zero([0, 0, 0, 0, -1]) is True
assert below_zero([0, 0, 0, 0, 0]) is False
assert below_zero([1000, 2000, 1000]) is False
assert below_zero([1000, 2000, 1001, 1000]) is False
assert below_zero([2000, 1000, 2000, 1000]) is False
assert not below_zero([0, 2, 0])
assert not below_zero([0, 2, 1])
assert below_zero([5, -2, -10, 5, -2, -10]) is True
assert below_zero([-5, -2, -10, 5, -2, -10]) is True
assert below_zero([-5, -2, -10, 5, -2, -10, -5, -2, -10, -5, -2, -10]) is True
assert below_zero([-100, 100, -100, 100, -100, -100]), "The function should return True"
assert below_zero([-100, 100, 100, -100, -100, 100]), "The function should return True"
assert below_zero([-100, 100, 100, -100, 100, -100]), "The function should return True"
assert below_zero([-100, -100, -100, 100, 100, -100]), "The function should return True"
assert below_zero([-100, -100, -100, -100, -100, -100]), "The function should return True"
assert below_zero([5, 0]) == False
assert below_zero([-15, 5]) == True
assert below_zero([-20, 1]) == True
assert below_zero([-20, 0]) == True
assert below_zero([-100, 0]) == True
assert below_zero([1, 1, -5, 9, 1]), "correct"
assert below_zero([-5, 1, 1, 9, 1]), "correct"
assert below_zero([-10, 0, 5])
assert below_zero([-15, -20, -30, -45])
assert below_zero([-11, -12, -13, -15, -16, -17, -18, 19])
assert below_zero([0, 20, 20, 0, 20, 20]) is False
assert below_zero([0, 0, 20, 20, 0, 20]) is False
assert below_zero([0, -20, -20, 0, -20, -20]) is True
assert below_zero([5, -10, 0, 5])
assert below_zero([-5, -10, 0, -5])
assert below_zero([5, -4, 3, -5]) == True
assert below_zero([5, -4, -3, -4, -5, -3]) == True
assert below_zero([100, -100, -100, -100]), "Example #5"
assert below_zero([-100, 100, -100, -100]), "Example #6"
assert below_zero([-100, -100, 100, -100]), "Example #7"
assert below_zero([-100, -100, -100, 100]), "Example #8"
assert below_zero([-100, 100, 100, 100]), "Example #9"
assert not below_zero([100, 200])
assert below_zero([0, -10000, 0, -1000, -10000, 500, -500]) == True
assert below_zero([100, 0, 20, 15]) is False
assert below_zero([100, 100, 0, 15]) is False
assert below_zero([100, 100, 100, 0]) is False
assert below_zero([0, 0, -1])
assert below_zero([-1, 0, 2])
assert below_zero([-2, 1, 0])
assert below_zero([-2, -2, 0])
assert not below_zero([2, 2, 1])
assert not below_zero([2, 2, 2])
assert not below_zero([0, 0, 0, 0, 0])
assert below_zero([-10, 10, -10])  # negative deposits
assert not below_zero([10, 10, 10])  # negative withdrawals
assert below_zero([-10, -10, -10])  # negative deposits
assert not below_zero([10, 10, 10, 10])  # positive deposits
assert below_zero([0, 0, 0]) is False
assert below_zero([0, 0, 0, 0, 100]) is False
assert below_zero([-1, -2, -3, -4, -5, 2])
assert not below_zero([0, 0, 0])
assert below_zero([-1, 0])
assert below_zero([-1, -2, 0])
assert below_zero([-1, -2, -2, 0])
assert below_zero([-10, 0, 5, 0]) == True
assert below_zero([-1000, 100, 999, 1]) == True
assert below_zero([-1000, -100, -999, -1]) == True
assert below_zero([-1000, -100, -999, -100, -999, -1]) == True
assert below_zero([0, 0, 0, 20, 10, 40]) == False
assert below_zero([-10, -20, -30, -25]) == True
assert below_zero([100, -200, -1]) == True
assert not below_zero([0, 0, 0, 0])
assert below_zero([0, 0, 0, -3, -3, 3, -3, -3, 0]) == True
assert below_zero([0, 0, 0, -3, -3, -3, 3, -3, -3, -3]) == True
assert below_zero([0, 100, 0, 100, 0, 100, 0, 100, 0, 0, 0]) is False
assert below_zero([-10, -20, -5]) is True
assert below_zero([-1, -2, -3]) is True
assert below_zero([1, 2, 1]) is False
assert below_zero([0, 1, 1]) is False
assert below_zero([1, 1, 0]) is False
assert below_zero([0, 1, -1, -1]) is True
assert below_zero([-100, 50, 10]) == True
assert below_zero([100, 0, 5]) == False
assert below_zero([-1, 100, 1, 0]) == True
assert below_zero([-1, -100, -1, 0]) == True
assert below_zero([-10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10]) == True
assert below_zero([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == False
assert not below_zero([0, 1, 0, 3, 13, 21])
assert not below_zero([0, 1, 0, 3, 11, 22, 31])
assert not below_zero([1, 2, 3])
assert not below_zero([1, 2, 3, 0])
assert not below_zero([1, 2, 3, 0, 0, 0])
assert not below_zero([1, 4, 6, 2])
assert below_zero([10, 20, 0, 40]) is False
assert below_zero([10, 20, 10, 0]) is False
assert below_zero([-20, 0, 100]) == True
assert below_zero([100, 2000, 3000, 4000]) is False
assert below_zero([0, 1, 2, 1, 0]) is False
assert below_zero([0, 0, 1, 0, 0]) is False
assert below_zero([0, 0, 0, 0]) == False
assert below_zero([-5, -3, 0, 2, 5]), "Test 3 failed"
assert below_zero([100, 0, 0]) is False
assert below_zero([-1, -2]) == True
assert below_zero([10,0,20,30]) == False
assert below_zero([100, 100, 100, 0, 0, 10, 100]) is False
assert below_zero([50, 100, 50, 0, 50]) == False
assert below_zero([0, 1, 0]) == False, "No negative values allowed"
assert below_zero([0, 1, 10]) == False, "Balance lower than zero"
assert below_zero([-100, -100, 0, 100]) is True
assert not below_zero([10, 0, 5, 0, 5])
assert below_zero([0, 10, 0, 20]) is False
assert below_zero([0, -20, 100, -50]) == True
assert below_zero([-1, 1, -2, 1]) is True
assert below_zero([-1, 0]) is True
assert below_zero([10, 20, 30]) == False, "List can not start with +ve values!"
assert below_zero([0, 0, 100, 0, 10, 20, 10]) == False
assert below_zero([0, 0, 1]) == False
assert below_zero([2, 1, 1, 2, 3]) is False
assert below_zero([0, 0, 0]) == False
assert below_zero([0, 0, 0, 0, 0]) == False
assert below_zero([-100, 0, 0, -100, -100, 0, 100, 0, 0, -100]) is True
assert below_zero([2, 5, 0, 0]) == False
assert below_zero([10, 5, -10, -15, 20, -5, 5]) is True
assert below_zero([10, 0, 0, 0, 5, 5]) is False
assert below_zero([-5, -4, 2, 3]) == True
