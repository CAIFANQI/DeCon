
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
assert count_nums([0, 1, 2, 3, 4, 5]) == 5
assert count_nums([0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == 9
assert count_nums([0, 0, 0]) == 0, "Test case 2 failed"
assert count_nums([10, 20, 30, 40, 50, 60, 70, 80, 90]) == 9
assert count_nums([0, 0, 0, 0, 0, 0]) == 0
assert count_nums([0, 0, 0]) == 0
assert count_nums([-123, -456, -789]) == 3
assert count_nums([10, 20, 30]) == 3
assert count_nums([0, 0, 0, 0, 0]) == 0, "Test case 4 failed"
assert count_nums([]) == 0, "Test case 5 failed"
assert count_nums([0, 0, 0, 0]) == 0, "Test case 4 failed"
assert count_nums([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0, "Test case 4 failed"
assert count_nums([0, 0, 0, 0, 0]) == 0
assert count_nums([1, 2, 3]) == 3
assert count_nums([10, 20, 30, 40, 50]) == 5
assert count_nums([123, 456, 789]) == 3
assert count_nums([-123, 456, -789, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 12
assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
assert count_nums([123, 456, 789]) == 3, "Test case 4 failed"
assert count_nums([-123, -456, -789]) == 3, "Test case 5 failed"
assert count_nums([123, -456, 789]) == 3
assert count_nums([0, 0, 0, 0]) == 0
assert count_nums([0, 0, 0, 0, 0]) == 0, "Test case 2 failed"
assert count_nums([1234567890]) == 1, "Test case 4 failed"
assert count_nums([1, 2, 3, 4, 5]) == 5, "Test case 4 failed"
assert count_nums([-123, 456, -789, 10, 0]) == 4, "Test case 5 failed"
assert count_nums([10, 20, 30, 40, 50]) == 5, "Test case 2 failed"
assert count_nums([0, 0, 0, 0, 0]) == 0, "Test case 5 failed"
assert count_nums([0, 10, 0, 20, 0, 30]) == 3, "Test case 6 failed"
assert count_nums([-123, 0, 456, 0, 789]) == 3, "Test case 3 failed"
assert count_nums([0, 123, -456, 789]) == 3
assert count_nums([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert count_nums([1, 10, 100, 1000, 10000]) == 5
assert count_nums([0, 0, 0, 0]) == 0, "Test case 3 failed"
assert count_nums([123, -456, 789]) == 3, "Test case 4 failed"
assert count_nums([-123, 456, -789]) == 3, "Test case 5 failed"
assert count_nums([0, 0, 0, 0]) == 0, "Test case 2 failed"
assert count_nums([0, 0, 0, 0, 0]) == 0, "Test case 3 failed"
assert count_nums([0, 123, 456, 789]) == 3
assert count_nums([0, 1000, 2000, 3000]) == 3
assert count_nums([10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 10
assert count_nums([0, 0, 0]) == 0, "Error: Test Case 2"
assert count_nums([1, 2, 3]) == 3, "Error: Test Case 3"
assert count_nums([-123, 456, -789]) == 3
assert count_nums([0]) == 0
assert count_nums([0, 0, 0, 0, 0, 0]) == 0, "Test case 4 failed"
assert count_nums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
assert count_nums([0, 0, 0]) == 0, "Test case 3 failed"
assert count_nums([123, 456, 789]) == 3, "Test case 3 failed"
assert count_nums([-123, -456, -789]) == 3, "Test case 4 failed"
assert count_nums([0, -123, 456, -789]) == 3, "Test case 5 failed"
assert count_nums([-123, 0, 456, -789]) == 3, "Test case 6 failed"
assert count_nums([0, 0, 0, 123, 456, 789]) == 3, "Test case 7 failed"
assert count_nums([0, 0, 0, -123, -456, -789]) == 3, "Test case 8 failed"
assert count_nums([0, 0, 0, -123, 456, -789]) == 3, "Test case 9 failed"
assert count_nums([0, 0, 0, -123, 456, -789, 0]) == 3, "Test case 10 failed"
assert count_nums([0, 0, 0, -123, 456, -789, 0, 0]) == 3, "Test case 11 failed"
assert count_nums([1, 2, 3]) == 3, "Test case 2 failed"
assert count_nums([0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == 9, "Test case 3 failed"
assert count_nums([0, -123, -456, -789]) == 3
assert count_nums([0, 1234, 5678, 9012]) == 3
assert count_nums([0, 12345, 67890]) == 2
assert count_nums([0, -12345, -67890]) == 2
assert count_nums([0, 123456, 789012]) == 2
assert count_nums([0, -123456, -789012]) == 2
assert count_nums([0, 1234567]) == 1
assert count_nums([0, -1234567]) == 1
assert count_nums([0, 12345678]) == 1
assert count_nums([0, -12345678]) == 1
assert count_nums([0, 123456789]) == 1
assert count_nums([0, -123456789]) == 1
assert count_nums([0, 0, 0]) == 0, "Test case 4 failed"
assert count_nums([123456789]) == 1
assert count_nums([-123456789]) == 1
assert count_nums([0, 11, 22, 33, 44, 55, 66, 77, 88, 99]) == 9
assert count_nums([0, -123, 456]) == 2
