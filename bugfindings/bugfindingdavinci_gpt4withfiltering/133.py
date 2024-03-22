

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
assert sum_squares([1, 2, 3]) == 14
assert sum_squares([1, -2, 3]) == 14
assert sum_squares([2, 1, 3]) == 14
assert sum_squares([0]) == 0
assert sum_squares([0,0]) == 0
assert sum_squares([1,2,3]) == 14
assert sum_squares([-1,-2,-3]) == 14
assert sum_squares([]) == 0
assert sum_squares([10, 20, 30]) == 1400
assert sum_squares([-1, -2, -3]) == 14, "(2) result should be 14"
assert sum_squares([1, 2, 3, 4]) == 30
assert sum_squares([-1, -2, -3]) == 14, 'wrong result for [-1, -2, -3]'
assert sum_squares([4, 5, 6]) == 77
assert sum_squares([-1, -2, -3]) == 14
assert sum_squares([3, 3, 3]) == 27
assert sum_squares([1, 2, 3, 4, 5]) == 55
assert sum_squares([4, 3]) == 25
assert sum_squares([2, 3, 4]) == 29
assert sum_squares([3, 4, 5]) == 50
assert sum_squares([-1, 0, -2]) == 5
assert sum_squares([1, -1, 1, -1]) == 4
assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 385
assert sum_squares([5, 4, 3, 2, 1]) == 55
assert sum_squares([4, 4, 4, 4, 4]) == 80
assert sum_squares([1, -1]) == 2
assert sum_squares([1, 2, 3]) == 14, "Return value of `sum_squares` is not correct"
assert sum_squares([0, 1, 2, 3, 4]) == 30
assert sum_squares([0, 2, 4]) == 20
assert sum_squares([0,1,2,3,4,5,6,7,8,9]) == 285
assert sum_squares([1,2,3,4,5,6,7,8,9,0]) == 285
assert sum_squares([1, -2, -3]) == 14
assert sum_squares([1, 3, 5]) == 35, "sum_squares is not correct"
assert sum_squares([-1, -1, -1]) == 3
assert sum_squares([3, 2, 1]) == 14
assert sum_squares([-1, -2, -3, -4, -5]) == 55
assert sum_squares([-1, -2.99, -3]) == 14
assert sum_squares([1, 2, 0]) == 5
assert sum_squares([0, 0, 0]) == 0
assert sum_squares([-1, -2, -3, -4]) == 30
assert sum_squares([1, 2, 4]) == 21
assert sum_squares([-1, 2, -3]) == 14, 'sum_squares does not work'
assert sum_squares([1, 2, -3]) == 14
assert sum_squares([0.123, 0.223, 0.222, 0.222, 0.201]) == (1 ** 2) + (1 ** 2) + (1 ** 2) + (1 ** 2) + (1 ** 2)
assert sum_squares([1, 2, 3]) == 14, "Return value is incorrect"
assert sum_squares([-1, -1]) == 2
assert sum_squares([-1.1, 1.1]) == 5
assert sum_squares([1.5, 1.5]) == 8
assert sum_squares([-2, 3]) == 13
assert sum_squares([-2, -2, -2]) == 12
assert sum_squares([1, 2, 3]) == 14, "Returned list does not match the expected result"
assert sum_squares([1, 2, -3]) == 14, "Returned list does not match the expected result"
assert sum_squares([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 110
assert sum_squares([1, 0]) == 1
assert sum_squares([1, 2, 3, 4, 5, 6]) == 91
assert sum_squares([1, 1, 1, 1, 1]) == 5
assert sum_squares([-1, -1, -1, -1, -1]) == 5
assert sum_squares([1, 2, 3]) == 14, "Return value does not match expected value."
assert sum_squares([]) == 0, "Return value does not match expected value."
assert sum_squares([-1, 2, 3]) == 14
assert sum_squares([1, 2, 3]) == 14, "Return value error"
assert sum_squares([1, -3, 5]) == 35
assert sum_squares([-1, 0, 1]) == 2
assert sum_squares([1, 2, 3, -4]) == 30
assert sum_squares([-1, -2, 3]) == 14
assert sum_squares([1, 1.5, 3]) == 14
assert sum_squares([-1, 1.5, 3]) == 14
assert sum_squares([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 385
assert sum_squares([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 11
