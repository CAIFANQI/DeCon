

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
assert sum_squares([3]) == 9
assert sum_squares([0, 0, 0, 0]) == 0
assert sum_squares([]) == 0, "Empty list has no squared number"
assert sum_squares([0]) == 0, "0^2=0 but 0^2=0 so no sum is needed"
assert sum_squares([]) == 0
assert sum_squares([0]) == 0
assert sum_squares([-1]) == 1
assert sum_squares([]) == 0, "sum of squares is wrong"
assert sum_squares([-2, 0]) == 4
assert sum_squares([-2, 4, 0, 2, -5]) == 49
assert sum_squares([]) == 0, "Example"
assert sum_squares([4]) == 16
assert sum_squares([1]) == 1
