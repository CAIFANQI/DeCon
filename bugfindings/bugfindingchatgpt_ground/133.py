

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i)*2
    return squared
assert sum_squares([1, 2, 3, 4, 5]) == 55
assert sum_squares([-1, -2, -3, -4, -5]) == 55
assert sum_squares([0, 0, 0, 0, 0]) == 0
assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 385
assert sum_squares([2, 4, 6, 8, 10]) == 220
assert sum_squares([1.0, 2.0, 3.0, 4.0, 5.0]) == 55
assert sum_squares([0, 1, 2, 3, 4, 5]) == 55, "Test case 2 failed"
assert sum_squares([-1, -2, -3, -4, -5]) == 55, "Test case 3 failed"
assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 385, "Test case 5 failed"
assert sum_squares([]) == 0
assert sum_squares([4, 5, 6]) == 77
assert sum_squares([7, 8, 9]) == 194
assert sum_squares([10, 11, 12]) == 365
assert sum_squares([13, 14, 15]) == 590
assert sum_squares([4, 5, 6, 7, 8]) == 190
assert sum_squares([0.5, 1.5, 2.5, 3.5, 4.5]) == 55
assert sum_squares([-1, -2, -3, -4]) == 30
assert sum_squares([5, 6, 7, 8, 9]) == 255
assert sum_squares([0.5, 1.5, 2.5, 3.5]) == 30
assert sum_squares([0, 1, 2, 3, 4, 5]) == 55
assert sum_squares([5, 6, 7, 8]) == 174, "Test case 2 failed"
assert sum_squares([0, 1, 2, 3, 4, 5]) == 55, 'Test Case 2 Failed'
assert sum_squares([-1, -2, -3, -4, -5]) == 55, 'Test Case 3 Failed'
assert sum_squares([5, 10, 15, 20, 25]) == 1375
assert sum_squares([-2, -4, -6, -8, -10]) == 220
assert sum_squares([-1.5, -2.5, -3.5, -4.5, -5.5]) == 55
assert sum_squares([-2.3, -4.7, -6.1, -8.5, -10.9]) == 220
assert sum_squares([-1, 2, -3, 4, -5]) == 55
assert sum_squares([-2, 4, -6, 8, -10]) == 220
assert sum_squares([0, -1, 2, -3, 4, -5]) == 55
assert sum_squares([1, -2, 3, -4, 5]) == 55
assert sum_squares([2, -4, 6, -8, 10]) == 220
assert sum_squares([2, 4, 6, 8, 10]) == 220, 'Test Case 2 Failed'
assert sum_squares([5, 10, 15, 20, 25]) == 1375, 'Test Case 5 Failed'
assert sum_squares([0.1, 0.2, 0.3, 0.4, 0.5]) == 5
assert sum_squares([0, 5, 10, 15]) == 350
assert sum_squares([0, 5, 10]) == 125
assert sum_squares([4, 5, 6]) == 77, "Test case 2 failed"
assert sum_squares([7, 8, 9]) == 194, "Test case 3 failed"
assert sum_squares([10, 11, 12]) == 365, "Test case 4 failed"
assert sum_squares([4, 8, 12, 16, 20]) == 880
assert sum_squares([2, 4, 6, 8, 10]) == 220, "Test case 2 failed"
assert sum_squares([4, 8, 12, 16, 20]) == 880, "Test case 4 failed"
assert sum_squares([5, 10, 15, 20, 25]) == 1375, "Test case 5 failed"
assert sum_squares([0.5, 1.5, 2.5, 3.5, 4.5]) == 55, 'Test Case 4 Failed'
assert sum_squares([0, 1, 2, 3, 4, 5]) == 55, 'Test Case 5 Failed'
assert sum_squares([0, 0, 0, 0, 0]) == 0, "Test case 2 failed"
assert sum_squares([3, 6, 9, 12, 15]) == 495
assert sum_squares([-1.1, -2.2, -3.3, -4.4, -5.5]) == 55
assert sum_squares([0, 5, 10]) == 125, "Test case 2 failed"
assert sum_squares([-1, -2, -3]) == 14, "Test case 3 failed"
assert sum_squares([]) == 0, "Test case 5 failed"
assert sum_squares([0, 0, 0, 0]) == 0
assert sum_squares([1, 1, 1, 1]) == 4
assert sum_squares([2, 3, 4, 5, 6]) == 90
assert sum_squares([0, 1, 2, 3, 4]) == 30
assert sum_squares([1.5, 2.5, 3.5, 4.5]) == 54
assert sum_squares([0, 0, 0]) == 0
assert sum_squares([-1, -2, -3]) == 14
assert sum_squares([0]) == 0
assert sum_squares([1, 3, 5, 7, 9]) == 165
assert sum_squares([5, 10, 15, 20]) == 750
