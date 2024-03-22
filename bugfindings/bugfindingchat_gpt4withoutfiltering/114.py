
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    max_sum = 0
    s = 0
    for num in nums:
        s += -num
        if (s < 0):
            s = 0
        max_sum = max(s, max_sum)
    if max_sum == 0:
        max_sum = max(-i for i in nums)
    min_sum = min(-i for i in nums)
    return min_sum
assert minSubArraySum([1, 2, 3, 4, 5]) == 1, "Test case 3 failed"
assert minSubArraySum([1, 2, 3, 4, 5]) == 1
assert minSubArraySum([1, -2, 3, -4, 5, -6]) == -6, 'Test Case 2 Failed'
assert minSubArraySum([1, -2, 3, -4, 5, -6, 7]) == -6, 'Test Case 3 Failed'
assert minSubArraySum([1, -2, 3, -4, 5, -6, 7, -8]) == -8, 'Test Case 4 Failed'
assert minSubArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1, "Test case 3 failed"
assert minSubArraySum([0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0, "Test case 5 failed"
assert minSubArraySum([1, 2, 3, 4, 5]) == 1, 'Test Case 2 Failed'
assert minSubArraySum([5, -3, 5]) == -3, "Test case 3 failed"
assert minSubArraySum([1]) == 1, "Test case 4 failed"
assert minSubArraySum([5, -3, 4, -1, 2]) == -3, 'Test Case 2 Failed'
assert minSubArraySum([1, 2, 3, 4, 5]) == 1, 'Test Case 4 Failed'
assert minSubArraySum([5, -5, 5, -5, 5]) == -5, "Test case 5 failed"
assert minSubArraySum([1]) == 1, 'Test Case 4 Failed'
assert minSubArraySum([0]) == 0, 'Test Case 5 Failed'
assert minSubArraySum([-1]) == -1, 'Test Case 6 Failed'
assert minSubArraySum([1, -1, 1]) == -1, 'Test Case 8 Failed'
assert minSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == -5, "Test case 2 failed"
assert minSubArraySum([1]) == 1, "Test case 3 failed"
assert minSubArraySum([0]) == 0, "Test case 4 failed"
assert minSubArraySum([1]) == 1, "Test case 2 failed"
assert minSubArraySum([1, 2, 3, 4, 5]) == 1, "Test case 2 failed"
assert minSubArraySum([5]) == 5, "Test case 4 failed"
assert minSubArraySum([-5]) == -5, "Test case 5 failed"
assert minSubArraySum([1, 2, 3, 4, 5]) == 1, "Test case 4 failed"
assert minSubArraySum([5]) == 5, 'Test Case 4 Failed'
assert minSubArraySum([-5]) == -5, 'Test Case 5 Failed'
assert minSubArraySum([1, 2, 3, 4, 5, 6]) == 1
assert minSubArraySum([5]) == 5
assert minSubArraySum([5]) == 5, "Test case 5 failed"
assert minSubArraySum([5, -6, 2, 3, 1]) == -6, 'Test Case 2 Failed'
assert minSubArraySum([1, -2, 3, -4, 5, -6, 7]) == -6
assert minSubArraySum([1, 2, 3, 4, 5, 6]) == 1, "Test case 3 failed"
assert minSubArraySum([1, -2, 3, -4, 5, 6]) == -4
assert minSubArraySum([1, -2, 3, -4, 5, 6, -7]) == -7
assert minSubArraySum([1, -2, 3, -4, 5, 6, -7, 8]) == -7
assert minSubArraySum([5, -3, 7, -2, 1, 4, -1]) == -3, 'Test Case 4 Failed'
assert minSubArraySum([1]) == 1, 'Test Case 5 Failed'
assert minSubArraySum([5, -5, 10, -10, 15, -15]) == -15, 'Test Case 4 Failed'
assert minSubArraySum([1, -2, 3, 4, -1]) == -2, 'Test Case 2 Failed'
assert minSubArraySum([1, -2, 3, 4, -1, 2, -1, 3]) == -2, 'Test Case 3 Failed'
assert minSubArraySum([1, 2, 3, 4]) == 1
assert minSubArraySum([5, -2, 3, 0, 2]) == -2
assert minSubArraySum([1]) == 1
assert minSubArraySum([5, -3, 4, -1, -2, 1, 5, -3]) == -3, 'Test Case 3 Failed'
assert minSubArraySum([1, 2, 3, 4, 5]) == 1, 'Test Case 3 Failed'
assert minSubArraySum([-1]) == -1, 'Test Case 5 Failed'
assert minSubArraySum([5, 4, 3, 2, 1]) == 1, 'Test Case 5 Failed'
assert minSubArraySum([1, -2, 3, -4, 5]) == -4
assert minSubArraySum([1, -2, 3, -4, 5, -6]) == -6
assert minSubArraySum([1, 2, 3, 4]) == 1, "Test case 4 failed"
assert minSubArraySum([5, 4, -1, 7, 8]) == -1, "Test case 3 failed"
assert minSubArraySum([1, 2, 3, 4, -5]) == -5, "Test case 4 failed"
assert minSubArraySum([0, 0, 0, 0, 0]) == 0, "Test case 6 failed"
