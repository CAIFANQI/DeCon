
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
assert minSubArraySum([0]) == 0
assert minSubArraySum([0,1]) == 0
assert minSubArraySum([-3]) == -3
assert minSubArraySum([1]) == 1, "Test case 2"
assert minSubArraySum([1, 2, 3]) == 1
assert minSubArraySum([-1]) == -1, "Wrong answer for nums = [-1]"
assert minSubArraySum([-1]) == -1
assert minSubArraySum([10]) == 10
assert minSubArraySum([1, 1]) == 1
assert minSubArraySum([1]) == 1, "The result of minSubArraySum is wrong."
assert minSubArraySum([1, 1, 1, 1]) == 1
assert minSubArraySum([1]) == 1
assert minSubArraySum([-100,1]) == -100
assert minSubArraySum([-100,100,-100]) == -100
assert minSubArraySum([-10, 10]) == -10
assert minSubArraySum([-999999]) == -999999
assert minSubArraySum([-5]) == -5
assert minSubArraySum([5]) == 5
assert minSubArraySum([5, 5, 5, 5, 5, 5, 5]) == 5
assert minSubArraySum([1, 2, 3, 4, 5]) == 1
assert minSubArraySum([-100]) == -100
assert minSubArraySum([3]) == 3
assert minSubArraySum([2, 3]) == 2
assert minSubArraySum([1,1,1,1]) == 1
assert minSubArraySum([5, 7]) == 5
assert minSubArraySum([10, 0]) == 0
assert minSubArraySum([2,2,2,2,2,2]) == 2
assert minSubArraySum([3,3,3,3]) == 3
assert minSubArraySum([3, 3, 3]) == 3
assert minSubArraySum([1, 1, 1]) == 1
assert minSubArraySum([0, 0, 0, 0]) == 0
assert minSubArraySum([1, 1, 1, 1, 1]) == 1
assert minSubArraySum([1,2,3]) == 1
assert minSubArraySum([1, 2]) == 1
assert minSubArraySum([0, 0, 0, 0, 0]) == 0
assert minSubArraySum([3, 2]) == 2
