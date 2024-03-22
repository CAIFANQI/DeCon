
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
assert count_nums([123, -123, 34]) == 3, 'count_nums fails'
assert count_nums([123456789, -1, 2345]) == 2, 'count_nums fails'
assert count_nums([-1, 123, -1234, 34]) == 3, 'count_nums fails'
assert count_nums([-123456789, -1, 2345]) == 2, 'count_nums fails'
assert count_nums([-1, -12, -34, 34]) == 3, 'count_nums fails'
assert count_nums([-1, -123, -1234, 34]) == 3, 'count_nums fails'
assert count_nums([12, 34, 56]) == 3
assert count_nums([12, -34, 56]) == 3
assert count_nums([-123, -34, 56]) == 3
assert count_nums([12345, 6789, -10]) == 2
assert count_nums([123456789, 1234567890, -123456789]) == 3
assert count_nums([-1, -2, -3]) == 0
assert count_nums([1]) == 1
assert count_nums([-5, -4, -3, -2, -1, 0]) == 0
assert count_nums([]) == 0, "count_nums failed on test case"
assert count_nums([2, -8, 1]) == 2, "count_nums failed on test case"
assert count_nums([3, -5, 4, -3]) == 2, "count_nums failed on test case"
assert count_nums([-2,-3,4,-5]) == 1
assert count_nums([12]) == 1, "count_nums test 2 failed"
assert count_nums([]) == 0, "count_nums test 3 failed"
assert count_nums([3, 2, 1]) == 3, "Test case 2 incorrect."
assert count_nums([10, 5, -5, -10, -5, -10, 10, -5]) == 3, "Test case 6 incorrect."
assert count_nums([-3, 0, -4]) == 0, "Test case 10 incorrect."
assert count_nums([]) == 0, "Test case 11 incorrect."
assert count_nums([1, 2, 3]) == 3
assert count_nums([]) == 0
assert count_nums([0]) == 0
assert count_nums([1, 2, 3, -4, -5]) == 3
assert count_nums([-1, 2, -3]) == 1
assert count_nums([-1, -2, -3, 4]) == 1
assert count_nums([-3]) == 0
assert count_nums([-100]) == 0
assert count_nums([2, -5, -7]) == 1
assert count_nums([4, -7, -10, -5, -6, -1, 2, -5, -1, -3]) == 2
assert count_nums([-10, 5, 6, 4, 1, -2]) == 4
assert count_nums([1, 2, 3, -4]) == 3
assert count_nums([-1, -2, -3, -4]) == 0
assert count_nums([-5]) == 0
assert count_nums([-5, 1]) == 1
assert count_nums([1, 2, -3, 5, -4]) == 3
assert count_nums([1, 2, -3, 4]) == 3
assert count_nums([1, 2, -3]) == 2
assert count_nums([-10, -20, 20]) == 1
assert count_nums([-2, 1, -3]) == 1, "count_nums"
assert count_nums([-2, 1, 1]) == 2, "count_nums"
assert count_nums([2, 2, 2, -2, -1000, -1, -3]) == 3, "Example"
assert count_nums([-1, 2, -3, 4, 5]) == 3
assert count_nums([-2, -2, -2, -2, -2, -2, -5]) == 0
assert count_nums([1, 2, -3, 3, -5]) == 3
assert count_nums([1, 2, -3, 4, -5]) == 3
assert count_nums([-1, -7, 0, 2, -3]) == 1
assert count_nums([2, -3, 4, 5]) == 3
assert count_nums([-2, -1, 0, -1, -3, 4]) == 1
assert count_nums([1, 3, -4]) == 2
assert count_nums([-13, -12, -3, -7, -11]) == 2, "count all negative"
assert count_nums([-1, 5, 3, -2]) == 2
assert count_nums([5, -3, -3, -2]) == 1
assert count_nums([-5, -3, -3, -2]) == 0
assert count_nums([-1, 2, 3]) == 2
assert count_nums([-1, 1, -3]) == 1
assert count_nums([-2, 1, -3]) == 1
assert count_nums([-1, 2, -4]) == 1
assert count_nums([-1, 2, -5]) == 1
assert count_nums([-4, -2, -3]) == 0
assert count_nums([-10, -5, -3]) == 0
assert count_nums([-100, -2, -3]) == 0
assert count_nums([1, 2, 3, -4, 5]) == 4
assert count_nums([-999, 1, 1, -999, 99, -99]) == 5
assert count_nums([1, 4, -5, 1]) == 3
assert count_nums([10, 1000]) == 2
assert count_nums([10, 5, 1]) == 3
assert count_nums([]) == 0, "Should be 0"
assert count_nums([-1, 1, -1]) == 1
assert count_nums([1, 2, -2, 5]) == 3
assert count_nums([-2, -3]) == 0
assert count_nums([1, -1, 1, -1, 2]) == 3
assert count_nums([3, 0]) == 1, "Test 3 failed"
assert count_nums([2, -1, 2, 1]) == 3, "Test 4 failed"
assert count_nums([-12, -2, -4, 6, -8, 8]) == 3, "Test 9 failed"
assert count_nums([-99, -98, -94, -93, -93, -93, -93, -93, -93]) == 0, "Test 14 failed"
assert count_nums([-2, -3, -4, -5, 6]) == 1
assert count_nums([2, -3, 4, -5, 6, 0, 7]) == 4
assert count_nums([10, -10, 10, -10, 10]) == 3
assert count_nums([-5, -5, -5]) == 0
assert count_nums([-9, -10, -20, -30]) == 0
assert count_nums([1, 2, -3, -2, -1]) == 2
assert count_nums([1, -7, 2, -5, 3, -1, -4, 5]) == 4
assert count_nums([-100, -100, -100, -200, 200]) == 1
assert count_nums([-1, 0, 1, 5, -123, -7]) == 3
assert count_nums([-1, -5, 2, 7, -3, 0, -2]) == 2
assert count_nums([1, -2, 3, -5, 4]) == 3
assert count_nums([1,2,3,4,5,6,7,8,9,10,11]) == 11
assert count_nums([-3, -3]) == 0
assert count_nums([3, 2, -4, 7, -1]) == 3
assert count_nums([-1, -5, 1, 5, 123]) == 3
assert count_nums([127, 128, 255]) == 3
assert count_nums([-5, -5]) == 0
