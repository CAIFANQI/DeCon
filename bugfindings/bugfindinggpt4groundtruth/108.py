
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg * -1
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))
assert 	count_nums([-1, -2, -3]) == 0
assert count_nums([0]) == 0
assert count_nums([0, 1, 2, 3, 3, -1, -2, -3, -4]) == 4
assert count_nums([0, 1, 2, 3, 3, -1, -2, -3, -4, -5, -6, -7]) == 4
assert count_nums([0, 1, 2, 3, 3, -1, -2, -3, -4, -5, -6, -7, -8]) == 4
assert count_nums([0, 1, 2, 3, 3, -1, -2, -3, -4, -5, -6, -7, -8, -9]) == 4
assert count_nums([]) == 0
assert count_nums([-12, -1, -1, 0, 1, 1]) == 3
assert 	count_nums([-12, -3, 0]) == 1
assert 	count_nums([1, 2, 3, -4]) == 3
assert 	count_nums([0, 3, -4]) == 1
assert 	count_nums([0, 0, 0]) == 0
assert 	count_nums([]) == 0
assert 	count_nums([-9, 9]) == 1
assert count_nums([-1, -2, -3, -4, -5]) == 0
assert count_nums([0, -0, -0, 0]) == 0
assert count_nums([]) == 0, "Empty list, no numbers > 0"
assert count_nums([-1, -2, -3]) == 0
assert count_nums([0, 0, 1]) == 1
assert count_nums([-1, -2, 3, -4]) == 1
assert count_nums([-3, -2, -1, 0, 1, 2, 3]) == 3
assert count_nums([10, -1, -2, -3]) == 1
assert count_nums([10, -10, -10, -10]) == 1
assert 	count_nums([-1,2,-3,4,-5,6,7,8,-9,10]) == 6
assert count_nums([-1, -2, -3, -4]) == 0
assert count_nums([1, -2, -3, -4]) == 1
assert count_nums([1, 2, -3, -4]) == 2
assert count_nums([0,1,2,3]) == 3
assert count_nums([0,-1,1,2,3]) == 3
assert count_nums([-1,-2,-3,4]) == 1
assert count_nums([-1,-2,0,3,4]) == 2
assert count_nums([0,-2,-3,4]) == 1
assert 	count_nums([-1234]) == 1
assert 	count_nums([0]) == 0
assert 	count_nums([-1, -2, -3, -4, -5]) == 0
assert count_nums([1]) == 1
assert count_nums([0, -1, 2, 3]) == 2
assert count_nums([0, -1, 2, 3, 4]) == 3
assert count_nums([0, 0, 0, 0]) == 0
assert 	count_nums([1]) == 1
assert 	count_nums([1, -3, -2, 3, 4, 5, -6]) == 4
assert 	count_nums([-1, -3, -2, 3, 4, 5, -6]) == 3
assert 	count_nums([-1, -3, -2, 3, 4, 5, -6, -7, 8]) == 4
