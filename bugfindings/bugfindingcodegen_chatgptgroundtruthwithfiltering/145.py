
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
assert 	order_by_points([0, 1, 2, 3, 4, 5, 6, 7, 8]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
assert 	order_by_points([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert order_by_points([]) == []
assert order_by_points([1, 3, 2]) == [1, 2, 3]
assert order_by_points([3, 1, 2]) == [1, 2, 3]
assert order_by_points([3, -1, 2]) == [-1, 2, 3]
assert order_by_points([3, -1, 2, 3]) == [-1, 2, 3, 3]
assert order_by_points([3, -1, 2, 3, 3]) == [-1, 2, 3, 3, 3]
assert 	order_by_points([1, 2, 3]) == [1, 2, 3]
assert 	order_by_points([101, 103, 102]) == [101, 102, 103]
assert 	order_by_points([101, 201, 301, 302]) == [101, 201, 301, 302]
assert 	order_by_points([101, 301, 302, 201]) == [101, 201, 301, 302]
assert 	order_by_points([3, 3, 0, 3, 3]) == [0, 3, 3, 3, 3]
assert 	order_by_points([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert 	order_by_points([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 4, 5, 6, 7, 8, 9]) == [0, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
assert 	[0,1,2,3,4] == order_by_points([0,1,2,3,4])
assert 	order_by_points([7]) == [7]
assert 	order_by_points([5, 5, 5, 5]) == [5, 5, 5, 5]
assert 	order_by_points([0, 9, 3, 0, 5]) == [0, 0, 3, 5, 9]
assert 	order_by_points([]) == [], "Empty list!"
assert 	order_by_points([5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5], "Repeating!"
