
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
assert order_by_points([11, 22, 33, 44, 55, 66, 77, 88, 99]) == [11, 22, 33, 44, 55, 66, 77, 88, 99]
assert order_by_points([9, 18, 27, 36, 45]) == [9, 18, 27, 36, 45]
assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert order_by_points([15, 25, 35, 45, 55]) == [15, 25, 35, 45, 55]
assert order_by_points([10, 20, 30, 40, 50]) == [10, 20, 30, 40, 50]
assert order_by_points([111, 222, 333, 444, 555, 666, 777, 888, 999]) == [111, 222, 333, 444, 555, 666, 777, 888, 999]
assert order_by_points([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert order_by_points([10, 20, 30, 40, 50, 60]) == [10, 20, 30, 40, 50, 60]
assert order_by_points([9, 99, 999]) == [9, 99, 999]
assert order_by_points([123, 456, 789]) == [123, 456, 789]
assert order_by_points([111, 222, 333, 444, 555]) == [111, 222, 333, 444, 555]
assert order_by_points([9, 99, 999, 9999]) == [9, 99, 999, 9999]
assert order_by_points([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert order_by_points([10, 20, 30, 40, 50, 60, 70, 80, 90]) == [10, 20, 30, 40, 50, 60, 70, 80, 90]
assert order_by_points([100, 200, 300, 400, 500]) == [100, 200, 300, 400, 500]
assert order_by_points([111, 222, 333, 444]) == [111, 222, 333, 444]
assert order_by_points([1, 2, 3, 4]) == [1, 2, 3, 4]
assert order_by_points([10, 20, 30, 40]) == [10, 20, 30, 40]
assert order_by_points([5, 15, 25, 35]) == [5, 15, 25, 35]
assert order_by_points([11, 22, 33, 44, 55]) == [11, 22, 33, 44, 55]
assert order_by_points([123, 321, 543, 765]) == [123, 321, 543, 765]
assert order_by_points([1111, 2222, 3333, 4444]) == [1111, 2222, 3333, 4444]
assert order_by_points([55, 66, 77, 88, 99]) == [55, 66, 77, 88, 99]
assert order_by_points([13, 31, 22, 43, 34, 55]) == [13, 31, 22, 43, 34, 55]
assert order_by_points([123, 321, 456, 654]) == [123, 321, 456, 654]
assert order_by_points([123, 234, 345, 456, 567]) == [123, 234, 345, 456, 567]
assert order_by_points([12, 22, 32, 42]) == [12, 22, 32, 42]
assert order_by_points([15, 25, 35, 45]) == [15, 25, 35, 45]
assert order_by_points([1, 10, 100, 1000, 10000]) == [1, 10, 100, 1000, 10000]
assert order_by_points([12, 34, 56, 78]) == [12, 34, 56, 78]
assert order_by_points([11, 22, 33, 44]) == [11, 22, 33, 44]
assert order_by_points([9, 99, 999, 9999, 99999]) == [9, 99, 999, 9999, 99999]
assert order_by_points([12, 23, 34, 45, 56]) == [12, 23, 34, 45, 56]
assert order_by_points([100, 200, 300, 400]) == [100, 200, 300, 400]
assert order_by_points([100, 200, 300, 400, 500, 600, 700, 800, 900]) == [100, 200, 300, 400, 500, 600, 700, 800, 900]
assert order_by_points([111, 222, 333]) == [111, 222, 333]
assert order_by_points([12, 21, 34, 43, 56]) == [12, 21, 34, 43, 56]
assert order_by_points([10, 100, 1000, 10000]) == [10, 100, 1000, 10000]
assert order_by_points([23, 45, 67, 89]) == [23, 45, 67, 89]
assert order_by_points([9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]
assert order_by_points([19, 29, 39, 49, 59]) == [19, 29, 39, 49, 59]
assert order_by_points([1111, 2222, 3333, 4444, 5555]) == [1111, 2222, 3333, 4444, 5555]
assert order_by_points([5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
