
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans.sort(reverse=True)
assert maximum([1, 2, 3, 4, 5, 6], 2) == [5, 6]
assert maximum([1, 2, 3, 4, 5, 6], 3) == [4, 5, 6]
assert maximum([1, 2, 3, 4, 5, 6], 4) == [3, 4, 5, 6]
assert maximum([1, 2, 3, 4, 5, 6], 5) == [2, 3, 4, 5, 6]
assert maximum([1, 2, 3, 4, 5, 6], 6) == [1, 2, 3, 4, 5, 6]
assert maximum(list(range(10)), 2) == sorted(list(reversed(list(range(10))))[:2])
assert maximum([1], 1) == [1]
assert maximum([-2, -1], 2) == [-2, -1]
assert maximum([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
assert maximum([1, 10, 20], 3) == [1, 10, 20]
assert maximum([1,2], 2) == [1,2]
assert maximum([1,2,3], 2) == [2,3]
assert sorted(maximum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 14)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
assert maximum([1, 2, 3, -4, -5], 0) == []
assert maximum([0,1,2,3,4,5], 2) == [4, 5]
assert maximum([1], 0) == []
assert maximum([2], 1) == [2]
assert maximum([2, 1], 2) == [1, 2]
assert maximum([1, 2], 2) == [1, 2]
assert maximum([3, 4, 6, 2], 3) == [3, 4, 6]
assert maximum([10, 2, -9, 4, 8], 0) == []
assert maximum([10, -20, 12, -10, 40, 50], 2) == [40, 50]
