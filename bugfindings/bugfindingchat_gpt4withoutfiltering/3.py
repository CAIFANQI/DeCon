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
assert below_zero([10, -5, -8, 2, 3, -10]) == True, "Test case 2 failed"
assert below_zero([10, -5, -8, 2, 3, -10, 20]) == True, "Test case 3 failed"
assert below_zero([10, -5, -8, 2, 3, -10, 20, -30]) == True, "Test case 4 failed"
assert below_zero([10, -5, -8, 2, 3, -10, 20, -30, 40]) == True, "Test case 5 failed"
assert below_zero([10, -5, 20, -15, 30, -50]) == True, "Test case 2 failed"
assert below_zero([10, -5, 20, -15, 30, -50, 100]) == True, "Test case 3 failed"
assert below_zero([10, -5, 20, -15, 30, -50, 100, -200]) == True, "Test case 4 failed"
assert below_zero([10, -5, 20, -15, 30, -50, 100, -200, 300]) == True, "Test case 5 failed"
assert below_zero([10, -5, 20, -15, 30, -50, 100, -200, 300, -400]) == True, "Test case 6 failed"
assert below_zero([10, -5, 20, -15, 30, -50, 100, -200, 300, -400, 500]) == True, "Test case 7 failed"
assert below_zero([10, -5, 20, -15, 30, -50, 100, -200, 300, -400, 500, -600]) == True, "Test case 8 failed"
assert below_zero([10, -5, 20, -15, 30, -50, 100, -200, 300, -400, 500, -600, 700]) == True, "Test case 9 failed"
assert below_zero([10, -5, 20, -15, 30, -50, 100, -200, 300, -400, 500, -600, 700, -800]) == True, "Test case 10 failed"
assert below_zero([10, -5, 20, -15, 30, -50, 100, -200, 300, -400, 500, -600, 700, -800, 900]) == True, "Test case 11 failed"
assert below_zero([10, -5, 20, -15, 30, -50, 100, -200, 300, -400, 500, -600, 700, -800, 900, -1000]) == True, "Test case 12 failed"
assert below_zero([10, -5, 20, -15, 30, -50, 100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100]) == True, "Test case 13 failed"
assert below_zero([10, -5, 20, -15, 30, -50, 100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200]) == True, "Test case 14 failed"
assert below_zero([10, -5, 20, -15, 30, -50, 100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200, 1300]) == True, "Test case 15 failed"
assert below_zero([10, -5, 20, -15, 30, -50, 100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200, 1300, -1400]) == True, "Test case 16 failed"
assert below_zero([10, -5, 20, -15, 30, -50, 100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200, 1300, -1400, 1500]) == True, "Test case 17 failed"
assert below_zero([10, -5, 20, -15, 30, -50, 100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200, 1300, -1400, 1500, -1600]) == True, "Test case 18 failed"
assert below_zero([-10, 5, -20, 10]) == True
assert below_zero([10, 5, -20, -10]) == True
assert below_zero([10, -5, 20, 30, 5]) == False
assert below_zero([100, -200, 300, -400, 500]) == True
assert below_zero([100, 200, 300, 400, 500]) == False
assert below_zero([100, -50, 200, -300, 400, -500]) == True, "Test case 2 failed"
assert below_zero([100, -50, 200, -300, 400, -500, 600, -700]) == True, "Test case 3 failed"
assert below_zero([100, -50, 200, -300, 400, -500, 600, -700, 800, -900]) == True, "Test case 4 failed"
assert below_zero([100, -50, 200, -300, 400, -500, 600, -700, 800, -900, 1000, -1100]) == True, "Test case 5 failed"
assert below_zero([100, -50, 200, -300, 400, -500, 600, -700, 800, -900, 1000, -1100, 1200, -1300]) == True, "Test case 6 failed"
assert below_zero([100, -50, 200, -300, 400, -500, 600, -700, 800, -900, 1000, -1100, 1200, -1300, 1400, -1500]) == True, "Test case 7 failed"
assert below_zero([100, -50, 200, -300, 400, -500, 600, -700, 800, -900, 1000, -1100, 1200, -1300, 1400, -1500, 1600, -1700]) == True, "Test case 8 failed"
assert below_zero([100, -50, 200, -300, 400, -500, 600, -700, 800, -900, 1000, -1100, 1200, -1300, 1400, -1500, 1600, -1700, 1800, -1900]) == True, "Test case 9 failed"
assert below_zero([100, -50, 200, -300, 400, -500, 600, -700, 800, -900, 1000, -1100, 1200, -1300, 1400, -1500, 1600, -1700, 1800, -1900, 2000, -2100]) == True, "Test case 10 failed"
assert below_zero([10, -5, -20, 15]) == True, "Test case 2 failed"
assert below_zero([100, -50, -20, 30, 10]) == False, "Test case 4 failed"
assert below_zero([20, -10, -5, -15]) == True
assert below_zero([5, 10, -7, -20, 15]) == True
assert below_zero([10, -5, 8, 20]) == False, "Test case 2 failed"
assert below_zero([-10, -5, -8, -15, -20]) == True, "Test case 3 failed"
assert below_zero([10, 5, 8, 15, 20]) == False, "Test case 4 failed"
assert below_zero([100, -200, 300, -400]) == True, "Test case 2 failed"
assert below_zero([100, 200, 300, -400]) == False, "Test case 3 failed"
assert below_zero([-100, -200, -300, -400]) == True, "Test case 4 failed"
assert below_zero([5, -3, -8, 10, -2]) == True, "Test case 2 failed"
assert below_zero([10, -5, 3, -8, -100]) == True
assert below_zero([10, -5, -8, 7, 3, -10]) == True
assert below_zero([10, -5, 8, -15, 20, -30]) == True, "Test case 2 failed"
assert below_zero([10, -5, 8, -15, 20, -30, 40]) == True, "Test case 3 failed"
assert below_zero([10, -5, 8, -15, 20, -30, 40, -20]) == True, "Test case 4 failed"
assert below_zero([10, 20, 30, 40, 50]) == False, "Test case 3 failed"
assert below_zero([-10, -20, -30, -40, -50]) == True, "Test case 4 failed"
assert below_zero([10, -5, 8, -12, 15, -20]) == True
assert below_zero([10, -5, 8, -12, 15, -20, 25]) == True
assert below_zero([5, -3, 2, 8, -10]) == False
assert below_zero([0, 0, 0, 0, 0]) == False
assert below_zero([-10, -5, -8, -12, -15]) == True
assert below_zero([10, 5, 8, 12, 15]) == False
assert below_zero([10, -5, 20, 30, 15]) == False
assert below_zero([10, -5, 8, -15, 20, -25]) == True
assert below_zero([10, -5, -20, 30]) == True, "Test case 2 failed"
assert below_zero([10, -5, 20, -30]) == True, "Test case 3 failed"
assert below_zero([10, -5, 20, -10, -30]) == True, "Test case 4 failed"
assert below_zero([10, -5, 20, -10, 30]) == False, "Test case 5 failed"
assert below_zero([20, -10, 30, -40]) == False, 'Test Case 2 Failed'
assert below_zero([10, -5, 20, -30]) == True
assert below_zero([10, -5, 20, -30, 40]) == True
assert below_zero([10, -5, 20, -30, 40, -10]) == True
assert below_zero([100, -200, 300, -400]) == True
assert below_zero([10, -5, 15, -20, 30]) == False
assert below_zero([-10, -20, -30, -40]) == True, "Test case 3 failed"
assert below_zero([10, 20, 30, 40]) == False, "Test case 4 failed"
assert below_zero([-10, 20, -30, 40]) == True, "Test case 5 failed"
assert below_zero([-100, 50, 20, -30, 10]) == True, "Test case 2 failed"
assert below_zero([100, -50, -20, 30, -10, -100]) == True, "Test case 3 failed"
assert below_zero([20, -10, -15, 5]) == True
assert below_zero([10, -5, 8, -15, 20, -25, 30]) == True
assert below_zero([10, -5, 8, -15, 20, -25, 30, -35]) == True
assert below_zero([10, -5, 8, -15, 20, -25, 30, -35, 40]) == True
assert below_zero([10, 20, 30, 40, 50]) == False, "Test case 2 failed"
assert below_zero([-10, -20, -30, -40, -50]) == True, "Test case 3 failed"
assert below_zero([0, 0, 0, 0, 0]) == False, "Test case 5 failed"
assert below_zero([10, -5, 15, 5]) == False, "Test case 2 failed"
assert below_zero([10, 20, 30, 40, 50]) == False, "Test case 4 failed"
assert below_zero([10, -5, 8, -17, 12]) == True
assert below_zero([10, -5, 8, -7, 12, -30]) == True
assert below_zero([10, -5, 20, -10, 15, -25, 30, -35, 40, -45]) == True
assert below_zero([10, -5, 20, -10, 15, -25, 30, -35, 40, -45, 50]) == True
assert below_zero([10, -5, 20, -10, 15, -25, 30, -35, 40, -45, 50, -55]) == True
assert below_zero([10, -5, 20, -10, 15, -25, 30, -35, 40, -45, 50, -55, 60]) == True
assert below_zero([10, -5, 20, -10, 15, -25, 30, -35, 40, -45, 50, -55, 60, -65]) == True
assert below_zero([10, 20, 30, 40, 50]) == False
assert below_zero([-10, -20, -30, -40, -50]) == True
assert below_zero([10, -5, 8, -2, 10]) == False, "Test case 2 failed"
assert below_zero([10, 5, 8, 2, 10]) == False, "Test case 3 failed"
assert below_zero([-10, -5, -8, -2, -10]) == True, "Test case 4 failed"
assert below_zero([100, -50, -20, 30, -200]) == True
assert below_zero([10, -5, 8, -15, 20, -30]) == True
assert below_zero([5, -10, 15, -20]) == True
assert below_zero([10, -5, 3, -8, 2, -15]) == True
assert below_zero([10, -5, 15, -20, 30, -10, -50]) == True, "Test case 2 failed"
assert below_zero([10, -5, 15, -20, 30, -10, -50, 100]) == True, "Test case 3 failed"
assert below_zero([10, -5, 15, -20, 30, -10, -50, 100, -200]) == True, "Test case 4 failed"
assert below_zero([10, -5, 15, -20, 30, -10, -50, 100, -200, 300]) == True, "Test case 5 failed"
assert below_zero([10, -5, 15, -20, 30]) == False, 'Test Case 2 Failed'
assert below_zero([-100, 50, -200, 300, -400, 100]) == True, "Test case 3 failed"
assert below_zero([5, -10, 15, -20, 25]) == True, 'Test Case 2 Failed'
assert below_zero([10, -5, 8, -15, 20, -25]) == True, 'Test Case 3 Failed'
assert below_zero([10, -5, 8, -15, 20, -25, 30]) == True, 'Test Case 4 Failed'
assert below_zero([10, -5, 8, -15, 20, -25, 30, -35]) == True, 'Test Case 5 Failed'
assert below_zero([10, -5, 8, -15, 20, -25, 30, -35, 40]) == True, 'Test Case 6 Failed'
assert below_zero([10, -5, 8, -15, 20, -25, 30, -35, 40, -45]) == True, 'Test Case 7 Failed'
assert below_zero([10, -5, 8, -15, 20, -25, 30, -35, 40, -45, 50]) == True, 'Test Case 8 Failed'
assert below_zero([10, -5, 8, -15, 20, -25, 30, -35, 40, -45, 50, -55]) == True, 'Test Case 9 Failed'
assert below_zero([10, -5, 8, -15, 20, -25, 30, -35, 40, -45, 50, -55, 60]) == True, 'Test Case 10 Failed'
assert below_zero([-100, -200, -300, -400, -500]) == True, "Test case 3 failed"
assert below_zero([100, 200, 300, 400, 500]) == False, "Test case 4 failed"
assert below_zero([10, -5, 8, -15, 20, -25]) == True, "Test case 2 failed"
assert below_zero([10, -5, 8, -15, 20, -25, 30]) == True, "Test case 3 failed"
assert below_zero([10, -5, 8, 15, 20]) == False, "Test case 2 failed"
assert below_zero([100, -50, 20, -30, 10]) == False, 'Test Case 2 Failed'
assert below_zero([100, -50, 20, -30, -10, 5, 5]) == False, 'Test Case 4 Failed'
assert below_zero([-100, -50, -20, -30]) == True, "Test case 2 failed"
assert below_zero([100, 200, 300, 400]) == False, "Test case 3 failed"
assert below_zero([-100, 200, 300, -400]) == True, "Test case 4 failed"
assert below_zero([100, 200, 300]) == False
assert below_zero([-100, -200, -300]) == True
assert below_zero([20, -10, 5, -8]) == False, "Test case 2 failed"
assert below_zero([5, -10, 15, -20]) == True, "Test case 3 failed"
assert below_zero([-10, -20, -30, -40]) == True, "Test case 5 failed"
assert below_zero([10, -5, 3, -8, 2, -15, 20]) == True
assert below_zero([10, -5, 8, -15, 20, -30, 40]) == True
assert below_zero([5, -10, 8, -15]) == True, "Test case 2 failed"
assert below_zero([-5, -10, -8, -15]) == True, "Test case 3 failed"
assert below_zero([100, -200, 300, -400, 500, -600]) == True
assert below_zero([5, 10, 15, 20]) == False, "Test case 2 failed"
assert below_zero([0, 0, 0, 0]) == False, "Test case 4 failed"
assert below_zero([100, 200, 300, 400]) == False
assert below_zero([-100, -200, -300, -400]) == True
assert below_zero([100, 200, -300, 400]) == False
assert below_zero([5, 10, -3, 2, -8]) == False, "Test case 2 failed"
assert below_zero([0, 0, 0, 0, 0]) == False, "Test case 4 failed"
assert below_zero([-100, -200, -300, -400, -500]) == True
assert below_zero([100, 200, -300, 400, -500]) == True
assert below_zero([10, -5, -20, 30, -40]) == True
assert below_zero([10, -5, -20, 30, -40, 50]) == True
assert below_zero([10, -5, -20, 30, -40, 50, -10]) == True
assert below_zero([10, -5, 20, -15, 5, -30]) == True
assert below_zero([10, -5, -3, -8]) == True
assert below_zero([10, -5, 3, -8, 0, -10]) == True
assert below_zero([10, -5, 3, -8, 0, -10, 5]) == True
assert below_zero([100, 200, 300, -400, -500]) == True
assert below_zero([100, -50, 20, 30, -10]) == False, "Test case 2 failed"
assert below_zero([100, 200, 300]) == False, "Test case 3 failed"
assert below_zero([-100, -200, -300]) == True, "Test case 4 failed"
