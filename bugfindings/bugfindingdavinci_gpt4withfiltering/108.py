
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
assert count_nums([1, -12, 43, 17, -21]) == 4
assert count_nums([1, 12, 43, 17, 21]) == 5
assert count_nums([]) == 0
assert count_nums([0, 0, 0, 0]) == 0
assert count_nums([-1]) == 0
assert count_nums([1]) == 1
assert count_nums([-1, -1, -1, -1]) == 0
assert count_nums([1, 1, 1, 1]) == 4
assert count_nums([-1, 1, -1, 1, -1, 1]) == 3
assert count_nums([0, 0, 0, 0, 0, 0]) == 0
assert count_nums([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0
assert count_nums([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert count_nums([0]) == 0
assert 0 == count_nums([0])
assert count_nums([-1, 2, 3, -4, 5]) == 3
assert count_nums([0, 0, 0, 0, 0]) == 0
assert count_nums([-111, 111]) == 2
assert count_nums([-123, -10]) == 1
assert count_nums([-1, -2, -3, -4, -5]) == 0
assert count_nums([1, 2, -3, -4, 5]) == 3
assert count_nums([1, -2, 3, -4, 5, -6, 7, -8, 9]) == 5
assert count_nums([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 6
assert count_nums([10, -10, -10, 10, -10, -10, 10, -10, -10, 10, -10, -10, 10])
assert count_nums([1,2,3,4,5]) == 5
assert count_nums([-1,-2,-3,-4,-5]) == 0
assert count_nums([-1, -2, -3, -4]) == 0
assert count_nums([10, 20, 30, 40]) == 4
assert count_nums([5, 5, 6, 10, -1, -3, -10, -13, -2, -5]) == 5
assert count_nums([4, 6, 2, -1, -4, -5, -21, -100, -100, -2]) == 3
assert count_nums([-1, -2, -3, -4, -5, -6, -7, -8, -9]) == 0
assert count_nums([-1, -1, -1, -1, -1, -1]) == 0
assert count_nums([1, 1, 2, -2]) == 3, "The result is incorrect"
assert count_nums([1, 1, 2, -3, 0]) == 3, "The result is incorrect"
assert count_nums([1, 1, 2, -3, -4]) == 3, "The result is incorrect"
assert count_nums([1, 1, 2, -3, -4, 0]) == 3, "The result is incorrect"
assert count_nums([1, 1, 2, -3]) == 3, "The result is incorrect"
assert count_nums([123, 2, -30, 4]) == 3
assert count_nums([1,2,3]) == 3
assert count_nums([-1,-2,-3]) == 0
assert count_nums([0,0,0]) == 0
assert count_nums([2, 3, 4, -7, -16, -20]) == 4
assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
assert count_nums([-100, -100, -100, -100, -100, -100, -100, -100, -100, -100]) == 0
assert count_nums([1, 2, 3]) == 3
assert count_nums([-1, -2, -3]) == 0
assert count_nums([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 0
assert count_nums([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 0
assert count_nums([10, 20, -30, -40, 50]) == 3
assert count_nums([-10, -20, -30, -40, -50]) == 0
assert count_nums([-10, -20, -30, -40, -50, -70]) == 0
assert count_nums([-10, -20, -30, -40, -50, 70]) == 1
assert count_nums([-1, -3, 4, 3]) == 2
assert count_nums([-1, -3, -4, -3]) == 0
assert count_nums([-1, -1, -1, -1, -1]) == 0
assert count_nums([-1,2,3]) == 2
assert count_nums([1,-2,3]) == 2
assert count_nums([1,2,-3]) == 2
assert count_nums([1,2,3,4,5,6,7,8,9,10]) == 10
assert count_nums([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]) == 0
assert count_nums([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert count_nums([10, 2, -3]) == 2
assert count_nums([-1, 10, 20, 30, -4, 5, -9]) == 4
assert count_nums([1, 2, 3, -4]) == 3
assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 100]) == 10
assert count_nums([10, 20, 30, 40, 50, 60, 70, 80, 90]) == 9
assert count_nums([123, 456, 789]) == 3
assert count_nums([12,34,56,78,90]) == 5
assert count_nums([-1, -3, -5, -7, -9]) == 0
assert count_nums([-123]) == 1
assert count_nums([-123, 0, 1, 123]) == 3
assert count_nums([-5, 123, 8, -15, -9, -11, -13]) == 4
assert count_nums([1, 2, 3, 4]) == 4
assert count_nums([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert count_nums([1, 2, -3]) == 2
assert count_nums([1, -2, 3]) == 2
assert count_nums([1, -2, -3]) == 1
assert count_nums([-1, 2, -3]) == 1
assert count_nums([0, 0, 0, 0, 0, 0, 0]) == 0
assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
assert count_nums([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 0
assert count_nums([11, 22, 33, 44, 55, 66, 77, 88, 99, 110]) == 10
assert count_nums([-5, 5, 123, -123]) == 3
assert count_nums([-5, -5, -5, -5, -5, -5, -5, -5]) == 0
assert count_nums([0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 0]) == 10
assert count_nums([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 10
assert count_nums([1, 1, 1, 1, 1]) == 5
assert count_nums([1, 2, 3, 4, 5, -123]) == 6
assert count_nums([1, 1, 1, 1, 1, 123]) == 6
assert count_nums([1, 23, 456, 7890]) == 4
assert count_nums([1, 2, 3, -4, 5]) == 4
assert count_nums([1, 2, 3, -4, 5, 6, 7, 8, 9]) == 8
assert count_nums([-1, 2, 3, 4, 5, 6, 7, 8, 9]) == 8
assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, -9]) == 8
assert count_nums([1, 2, 3, 4, 5, 6, 7, -8, 9]) == 8
assert count_nums([1, 2, 3, 4, 5, 6, -7, 8, 9]) == 8
assert count_nums([1, 2, 3, 4, 5, -6, 7, 8, 9]) == 8
assert count_nums([1, 2, 3, 4, -5, 6, 7, 8, 9]) == 8
assert count_nums([0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert count_nums([123]) == 1
assert count_nums([-123, 123]) == 2
assert count_nums([-1, -2, -3, -4, -5, -6, -7]) == 0
assert count_nums([-1, -10, -100, -10, -1]) == 0
assert count_nums([10, 0, -1, 2, 5, -2, -8, 3, -9, 7]) == 5
assert count_nums([0, -1, -2, -3, -4, -5, -6, -7, -8, -9]) == 0
assert count_nums([-1, -2, -3, -4, 5]) == 1
assert count_nums([-11, -22, -33, -44, 5]) == 1
assert count_nums([11, 22, 33, 44, 5]) == 5
assert count_nums([11, 22, 33, 44, 55]) == 5
assert count_nums([111, 222, 333, 444, 555]) == 5
assert count_nums([-111, -222, -333, -444, -555]) == 5
assert count_nums([-1, -2, -3, -4, -5, -6, -7, -8, -9, 0]) == 0
assert count_nums([0, -1, 2, -3, -12, 5, -7, -11, 12, 13, -15, -16, -17, 18, 19, -20]) == 10
assert count_nums([0, 1, 2, 3]) == 3
assert count_nums([5, 4, 3, 2, 1]) == 5
assert count_nums([-1, -2, 3, -4, -5]) == 1
assert count_nums([8, 18, 11]) == 3
assert count_nums([1, 2, 3, 4, 5]) == 5
assert 0 == count_nums([0, 0, -1, 0])
assert 0 == count_nums([-1, 0, 0, 0])
assert 1 == count_nums([0, 0, 1, 0])
assert 1 == count_nums([1, 0, 0, 0])
assert 5 == count_nums([1, 2, 3, 4, 5])
assert count_nums([111, 222, 333, 444, 555, 666, 777, 888, 999, -111, -222, -333, -444, -555, -666, -777, -888, -999]) == 18
assert count_nums([0, 0, 0, 0, 1]) == 1
assert count_nums([0, 1, 0, 1, 0]) == 2
assert count_nums([1, -1, 1, -1, 1]) == 3
assert count_nums([1, -2, 3, -4, 5]) == 3
assert count_nums([0, -1, -2, -3, -4, -5]) == 0
