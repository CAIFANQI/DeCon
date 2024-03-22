
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
assert maximum([-1,-2,-3,-4,-5], 0) == []
assert maximum([1], 1) == [1]
assert maximum([], 0) == []
assert maximum([0, 0, 0, 0, 0], 5) == [0, 0, 0, 0, 0]
assert maximum([-1, -2, -3, -4, -5], 0) == []
assert maximum([5, 4, 3, 2, 1], 0) == []
assert maximum([1, 1, 1, 1, 1], 5) == [1, 1, 1, 1, 1]
assert maximum([1, 1, 1, 1, 1], 5) == [1, 1, 1, 1, 1], "Test case 3 failed"
assert maximum([5, 4, 3, 2, 1], 0) == [], "Test case 5 failed"
assert maximum([10, 9, 8, 7, 6], 0) == []
assert maximum([0], 0) == []
assert maximum([0], 1) == [0]
assert maximum([1, 1, 1, 1, 1], 0) == []
assert maximum([0, 0, 0, 0, 0], 0) == []
assert maximum([1], 1) == [1], 'Test Case 5 Failed'
assert maximum([-1], 1) == [-1]
assert maximum([5, 4, 3, 2, 1], 1) == [5]
assert maximum([1], 0) == []
assert maximum([-1, -1, -1, -1, -1], 5) == [-1, -1, -1, -1, -1]
assert maximum([10], 1) == [10]
assert maximum([1], 0) == [], "Test case 5 failed"
assert maximum([1,1,1,1,1], 5) == [1,1,1,1,1], 'Test Case 3 Failed'
