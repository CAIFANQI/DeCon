
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
assert maximum([-1, -2, -3, -4, -5], 1) == [-1]
assert maximum([1, 2, 3, 4, 5], 1) == [5]
assert maximum([5,5,5,5,5], 3) == [5,5,5]
assert maximum([5,5,5,5,5], 1) == [5]
assert maximum([-10,-3,-3,-3,-3], 2) == [-3,-3]
assert maximum([5, 10, 4, 3, 8, 9], 1) == [10]
assert maximum([4, 5, 1, 2, 3], 1) == [5]
assert maximum([-1,-2,-3,-4,-5], 0) == []
assert maximum([], 0) == []
assert sorted(maximum([5,5,5,5,5], 2)) == [5,5]
assert sorted(maximum([5,5,5,5,5], 3)) == [5,5,5]
assert sorted(maximum([5,5,5,5,5], 4)) == [5,5,5,5]
assert sorted(maximum([5,5,5,5,5], 5)) == [5,5,5,5,5]
assert maximum([5,4,3,2,1], 1) == [5]
assert sorted(maximum([1, 2, 3, 4, 5], 1)) == [5]
assert maximum([1, 2], 1) == [2]
assert maximum([3, 4, 2, 1, 5], 1) == [5]
assert maximum([5,5,5,5,5,5,5], 3) == [5,5,5]
assert maximum([1,1,1,1,1,1,1], 3) == [1,1,1]
assert maximum([1], 1) == [1]
assert (maximum([5, 4, 3, 2, 1], 0) == [])
assert (maximum([5, 4, 3, 2, 1], 1) == [5])
assert (maximum([1, 2, 3, 4, 5], 0) == [])
assert (maximum([1, 2, 3, 4, 5], 1) == [5])
assert maximum([1, 2, 3], 0) == []
assert maximum([1], 0) == []
assert maximum([1, 2], 0) == []
assert maximum([1, 2, 3], 1) == [3]
assert maximum([1, 2, 3, 4], 0) == []
assert maximum([1, 2, 3, 4], 1) == [4]
assert maximum([1, 2, 3, 4, 5], 0) == []
assert maximum([1000, 1000], 2) == [1000, 1000]
assert maximum([1,3,4,2], 1) == [4]
assert maximum([1, 1, 2, 2, 2, 2, 2, 3, 3, 3], 2) == [3, 3]
assert maximum([1, 5, 2, -10, -6, 100], 1) == [100]
assert maximum([1, 1, 1, 1, 1], 1) == [1]
assert maximum([-10, -10, 1, 2, 3, 4, 5, -20, 6, 7, 8, 9, 10], 0) == []
assert maximum([], k=0) == []
assert maximum([0, 2, 1, -1, 3, 4, 5], 1) == [5]
assert maximum([1,2,3,4,5], 1) == [5]
assert maximum([0], 1) == [0]
assert maximum([-1, 1], 1) == [1]
assert maximum([5, 10, 4, 3, 11, 8, 10], 1) == [11]
assert maximum([5, 10, 4, 3, 11, 8, 10], 0) == []
assert maximum([1], k=0) == []
assert maximum([1], k=1) == [1]
assert maximum([1,2,3], k=1) == [3]
assert maximum([1,2,3,2,1], k=1) == [3]
assert maximum([10, 20, 30, 40, 50], 1) == [50]
assert maximum([9, 4, 7, 8, 3, 5], 0) == []
assert maximum([9, 4, 7, 8, 3, 5], 1) == [9]
assert maximum([2, 3, 4, 1, 2, 3, 4, 5], 1) == [5]
assert maximum([5, 1, 2, 3, 4], 1) == [5]
assert maximum([5, 1, 2, 3, 4], 0) == []
assert maximum([5, 4, 3, 2, 1], 1) == [5]
assert maximum([5, 4, 3, 2, 1], 0) == []
assert maximum([1, 3, 2, 4, 5], 1) == [5]
assert maximum([1, 3, 2, 4, 5], 0) == []
assert sorted(maximum([5, 9, 2, 1, 4, 7, 6, 8, 3], 1)) == [9]
assert maximum([0, 0, 0, 0, 0], 3) == [0, 0, 0]
