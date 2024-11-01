
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
assert order_by_points([101, 101, 101, 101, 101, 101, 101, 101, 101, 101]) == [101, 101, 101, 101, 101, 101, 101, 101, 101, 101]
assert order_by_points([0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert order_by_points([1, 1, 1]) == [1, 1, 1]
assert order_by_points([0, 0, 0]) == [0, 0, 0]
assert order_by_points([1, 2, 3]) == [1, 2, 3]
assert order_by_points([10, 100, 1000]) == [10, 100, 1000]
assert order_by_points([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert order_by_points([100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000]) == [100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000]
assert order_by_points([1]) == [1]
assert order_by_points([1, 2]) == [1, 2]
assert list(order_by_points([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert order_by_points([-5, -5, -5, -5]) == [-5, -5, -5, -5]
assert order_by_points([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert order_by_points([11, 11, 11, 11, 11, 11, 11, 11, 11]) == [11, 11, 11, 11, 11, 11, 11, 11, 11]
assert order_by_points([19, 19, 19, 19, 19, 19, 19, 19, 19]) == [19, 19, 19, 19, 19, 19, 19, 19, 19]
assert order_by_points([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert order_by_points([10, 10, 20, 30, 30]) == [10, 10, 20, 30, 30]
assert order_by_points([0, 0, 0, 2, 30]) == [0, 0, 0, 2, 30]
assert order_by_points([30, 30, 30, 30, 30]) == [30, 30, 30, 30, 30]
assert order_by_points([2, 4, 6, 7, 8]) == [2, 4, 6, 7, 8]
assert order_by_points([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
assert order_by_points([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert order_by_points([2, 2, 2]) == [2, 2, 2]
assert order_by_points([1, 11, 12, 111, 112, 113, 114, 115, 116, 117, 1188, 1199]) == [1, 11, 12, 111, 112, 113, 114, 115, 116, 117, 1188, 1199]
assert order_by_points([10, 13, 13, 13, 13, 13]) == [10, 13, 13, 13, 13, 13]
assert order_by_points([13, 13, 13, 13, 13, 13]) == [13, 13, 13, 13, 13, 13]
assert [1, 1, 1, 1, 1, 1, 1, 1, 1] == order_by_points([1, 1, 1, 1, 1, 1, 1, 1, 1])
assert [6, 6, 6, 6, 6, 6, 6, 6, 6] == order_by_points([6, 6, 6, 6, 6, 6, 6, 6, 6])
assert order_by_points([11, 22, 44, 44, 55, 66, 77, 77, 77, 77]) == [11, 22, 44, 44, 55, 66, 77, 77, 77, 77]
assert order_by_points([11, 22, 44, 44, 55, 66, 77, 77, 77, 777]) == [11, 22, 44, 44, 55, 66, 77, 77, 77, 777]
assert order_by_points([9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
assert order_by_points([1, 2, 3, 3]) == [1, 2, 3, 3]
assert order_by_points([7]) == [7]
assert order_by_points([-7]) == [-7]
assert order_by_points([1, 10, 100, 1000, 10000, 100000, 1000000]) == [1, 10, 100, 1000, 10000, 100000, 1000000]
assert order_by_points([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
assert order_by_points([1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111]) == [1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111]
assert order_by_points([0, 1, 11, 111, 1111]) == [0, 1, 11, 111, 1111]
assert order_by_points([1, 10, 100]) == [1, 10, 100]
assert order_by_points([9, 9, 9, 9, 9, 9]) == [9, 9, 9, 9, 9, 9]
assert order_by_points([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
