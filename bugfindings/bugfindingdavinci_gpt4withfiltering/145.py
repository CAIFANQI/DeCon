
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 + n 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)
assert order_by_points([100, 200, 300, 400, 500, 600]) == [100, 200, 300, 400, 500, 600]
assert order_by_points([]) == []
assert order_by_points([10, 30, 40, 50, 10]) == [10, 10, 30, 40, 50]
assert order_by_points([101, 101, 101, 101, 101, 101, 101, 101, 101, 101]) == [101, 101, 101, 101, 101, 101, 101, 101, 101, 101]
assert order_by_points([0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert order_by_points([-12, -11, -10]) == [-10, -11, -12]
assert order_by_points([1, 1, 1]) == [1, 1, 1]
assert order_by_points([0, 0, 0]) == [0, 0, 0]
assert order_by_points([151, -111, 111]) == [-111, 111, 151]
assert order_by_points([1, 2, 3]) == [1, 2, 3]
assert order_by_points([1, 9, 3]) == [1, 3, 9]
assert order_by_points([10, 100, 1000]) == [10, 100, 1000]
assert order_by_points([1, 19, 3]) == [1, 3, 19]
assert order_by_points([2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == [2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
assert order_by_points([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert order_by_points([100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000]) == [100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000]
assert order_by_points([2, 3, 1, 3, 3, 5, 1, 1, 4, 1]) == [1, 1, 1, 1, 2, 3, 3, 3, 4, 5]
assert order_by_points([1]) == [1]
assert order_by_points([1, 2]) == [1, 2]
assert list(order_by_points([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert list(order_by_points([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert order_by_points([-5, -5, -5, -5]) == [-5, -5, -5, -5]
assert order_by_points([-5, -5, -6, -5]) == [-6, -5, -5, -5]
assert order_by_points([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert order_by_points([11, 11, 11, 11, 11, 11, 11, 11, 11]) == [11, 11, 11, 11, 11, 11, 11, 11, 11]
assert order_by_points([19, 19, 19, 19, 19, 19, 19, 19, 19]) == [19, 19, 19, 19, 19, 19, 19, 19, 19]
assert order_by_points([2, 3, 6, 5, 9, 1, 4, 8, 7]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert order_by_points([9, 1, 4, 8, 7, 2, 3, 6, 5]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert order_by_points([11, 11, 11, 11, 11, 11, 11, 11, 11])
assert order_by_points([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert order_by_points([10, 10, 20, 30, 30]) == [10, 10, 20, 30, 30]
assert order_by_points([20, 30, 30, 20, 10]) == [10, 20, 20, 30, 30]
assert order_by_points([10, 20, 30, 30, 20]) == [10, 20, 20, 30, 30]
assert order_by_points([0, 20, 30, 30, 20]) == [0, 20, 20, 30, 30]
assert order_by_points([0, 0, 2, 30, 20]) == [0, 0, 2, 20, 30]
assert order_by_points([0, 0, 0, 2, 30]) == [0, 0, 0, 2, 30]
assert order_by_points([30, 30, 30, 30, 30]) == [30, 30, 30, 30, 30]
assert order_by_points([2, 4, 6, 7, 8]) == [2, 4, 6, 7, 8]
assert order_by_points([1, 2, 3, 1, 2, 3, 1, 2, 3]) == [1, 1, 1, 2, 2, 2, 3, 3, 3]
assert order_by_points([9, 99, 9999, 99, 999, 9, 9]) == [9, 9, 9, 99, 99, 999, 9999]
assert order_by_points([1, 8, 7, 2, 5, 6, 9, 4, 3]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert order_by_points([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
assert order_by_points([1, 9, 9, 1, 9, 9, 1, 9, 9, 9]) == [1, 1, 1, 9, 9, 9, 9, 9, 9, 9]
assert order_by_points([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert order_by_points([2, 2, 2]) == [2, 2, 2]
assert order_by_points([1, 11, 12, 111, 112, 113, 114, 115, 116, 117, 1188, 1199]) == [1, 11, 12, 111, 112, 113, 114, 115, 116, 117, 1188, 1199]
assert order_by_points([1, 2, 2, 1, 2, 2, 1, 2, 2, 1]) == [1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
assert order_by_points([1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
assert order_by_points([1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == [1, 1, 1, 2, 2, 2, 2, 2, 3, 3]
assert order_by_points([7, 3, 2, 9, 6]) == [2, 3, 6, 7, 9]
assert order_by_points([2, 3, 4, 1, 6, 5]) == [1, 2, 3, 4, 5, 6]
assert order_by_points([2, 3, 2, 4]) == [2, 2, 3, 4]
assert order_by_points([7, 6]) == [6, 7]
assert order_by_points([10, 13, 13, 13, 13, 13]) == [10, 13, 13, 13, 13, 13]
assert order_by_points([13, 13, 13, 13, 13, 13]) == [13, 13, 13, 13, 13, 13]
assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == order_by_points([9, 8, 7, 6, 5, 4, 3, 2, 1])
assert [1, 1, 1, 1, 1, 1, 1, 1, 1] == order_by_points([1, 1, 1, 1, 1, 1, 1, 1, 1])
assert [6, 6, 6, 6, 6, 6, 6, 6, 6] == order_by_points([6, 6, 6, 6, 6, 6, 6, 6, 6])
assert order_by_points([11, 22, 44, 44, 55, 66, 77, 77, 77, 77]) == [11, 22, 44, 44, 55, 66, 77, 77, 77, 77]
assert order_by_points([11, 22, 44, 44, 55, 66, 77, 77, 77, 777]) == [11, 22, 44, 44, 55, 66, 77, 77, 77, 777]
assert order_by_points([9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
assert order_by_points([1, 2, 3, 3]) == [1, 2, 3, 3]
assert order_by_points([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert order_by_points([7]) == [7]
assert order_by_points([-7]) == [-7]
assert order_by_points([4, 3, 1, 2]) == [1, 2, 3, 4]
assert order_by_points([4, 3, 1, 2, 9, 8, 7, 6, 5]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert order_by_points([4, 3, 1, 2, 9, 8, 7, 6, 5, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert order_by_points([-9, -8, -7, -6, -5, -4, -3, -2, -1, 0]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0]
assert order_by_points([123, 124, 12, 1233, 1234]) == [12, 123, 124, 1233, 1234]
assert order_by_points([1, 10, 100, 1000, 10000, 100000, 1000000]) == [1, 10, 100, 1000, 10000, 100000, 1000000]
assert order_by_points([8, 5, 2, 9, 0, 3, 7, 6, 4, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert order_by_points([1, 1, 2, 1, 2, 2, 2, 1]) == [1, 1, 1, 1, 2, 2, 2, 2]
assert order_by_points([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
assert order_by_points([-1, -1, -1, -1, 0, -1, -1, -1, -1]) == [-1, -1, -1, -1, -1, -1, -1, -1, 0]
assert order_by_points([99, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == [99, 991, 992, 993, 994, 995, 996, 997, 998, 999]
assert order_by_points([1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111]) == [1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111]
assert order_by_points([0, 1, 11, 111, 1111]) == [0, 1, 11, 111, 1111]
assert order_by_points([1, 10, 100]) == [1, 10, 100]
assert order_by_points([9, 9, 9, 9, 9, 9]) == [9, 9, 9, 9, 9, 9]
assert order_by_points([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
assert order_by_points([0, 1, 3, 7, 8, 2, 5, 2, 8, 2, 8]) == [0, 1, 2, 2, 2, 3, 5, 7, 8, 8, 8]
assert order_by_points([2, 1]) == [1, 2]
assert order_by_points([1, 3, 2]) == [1, 2, 3]
