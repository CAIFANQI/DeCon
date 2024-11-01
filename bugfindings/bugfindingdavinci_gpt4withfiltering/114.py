
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
assert minSubArraySum([-10,20,30]) == -10
assert minSubArraySum([1,2,3,4,5,6,7,8,9]) == 1
assert minSubArraySum([-2,1,-3,4,-1,2,1,-5,4]) == -5
assert minSubArraySum([-3, -1, -2]) == -6
assert minSubArraySum([1,1,1,1,1]) == 1
assert minSubArraySum([1,1,1,1,2]) == 1
assert minSubArraySum([1, 2, 3, 4, 5]) == 1
assert minSubArraySum([5, 1, 2, 3, 4]) == 1
assert minSubArraySum([2,2,2,2,2]) == 2
assert minSubArraySum([1, 1, 1, 1, 1, 1, 1]) == 1
assert minSubArraySum([1, 2, 3, 2, 3, 2, 1, 1, 1, 1, 1, 1, 1]) == 1
assert minSubArraySum([-1, -2, -3, -4, -5]) == -15
assert minSubArraySum([-2,1,3,2,4]) == -2
assert minSubArraySum([-2,1,3,2,4,5]) == -2
assert minSubArraySum([-1, -2, -3, 0, 1, 2, 3, 4, 5]) == -6
assert minSubArraySum([-1, -2, -3, 1, 2, 3]) == -6
assert minSubArraySum([-1, -1, -1, -1, -1, -1]) == -6
assert minSubArraySum([1,3,4,5]) == 1
assert minSubArraySum([2,4,4,5,2]) == 2
assert minSubArraySum([3,4,4,5,2]) == 2
assert minSubArraySum([-3,4,4,5,2]) == -3
assert minSubArraySum([-1, 2, 3, -4, 5]) == -4
assert minSubArraySum([-1, -2, -3, -4]) == -10, 'incorrect'
assert minSubArraySum([4, -3, -4]) == -7, 'incorrect'
assert minSubArraySum([2,2,1,2,1,1,1,1,1,100]) == 1, "case 1"
assert minSubArraySum([2,2,1,2,1,1,1,1,1,-1]) == -1, "case 2"
assert minSubArraySum([5, 2, 3, 1, 1, 4, 3]) == 1
assert minSubArraySum([1, 1, 1, 1, 1, 1]) == 1, "error in minSubArraySum"
assert minSubArraySum([1, 2, 3, 4, 5, 100]) == 1, "error in minSubArraySum"
assert minSubArraySum([-1,2,3,-2,5]) == -2
assert minSubArraySum([-1,2,3,-2,5,-9,9,8]) == -9
assert minSubArraySum([-1,2,3,-2,5,-9,9,8,9,8,100, 9999999, -99999999, 999999999]) == -99999999
assert minSubArraySum([10, -5, 5, -1, -2, 5, 2, -1]) == -5
assert minSubArraySum([5, 4, 3, 2, 1]) == 1
assert minSubArraySum([2, 3, -4, 5, -4, 10]) == -4
assert minSubArraySum([1,2,3,4,5]) == 1
assert minSubArraySum([3, -2, 2, -3]) == -3
assert minSubArraySum([-1, -2, -3]) == -6
assert minSubArraySum([10,100,100,100,1]) == 1
assert minSubArraySum([1,4,4,-1]) == -1
assert minSubArraySum([1,4,4,-1,3]) == -1
assert minSubArraySum([1,4,4,-1,3,5]) == -1
assert minSubArraySum([1,4,4,-1,3,5,3,3]) == -1
assert minSubArraySum([1,4,4,-1,3,5,3,3,5,5]) == -1
assert minSubArraySum([1,4,4,-1,3,5,3,3,5,5,5]) == -1
assert minSubArraySum([1,2,3,4,5,20]) == min([1,2,3,4,5,20])
assert minSubArraySum([2,0,3,4,5,20]) == min([2,0,3,4,5,20])
assert minSubArraySum([-10,2,0,3,4,5,20]) == min([-10,2,0,3,4,5,20])
assert minSubArraySum([-1, 2, 3, -1, 5]) == -1
assert minSubArraySum([1, 1, -1, 1]) == -1
assert minSubArraySum([-2, -3, -1]) == -6
assert minSubArraySum([2, 3, 4, 5]) == 2
assert minSubArraySum([1, 2, 3, 4, 5, 6]) == 1
assert minSubArraySum([2, 3, 4, 5, 6]) == 2
assert minSubArraySum([1, 2, 3, 4, 5, -1]) == -1
assert minSubArraySum([1, 2, 3, 4, 5, -2]) == -2
assert minSubArraySum([1, 2, 3, 4, 5, -3]) == -3
assert minSubArraySum([1, 2, 3, 4, 5, -4]) == -4
assert minSubArraySum([1, 2, 3, 4, 5, -5]) == -5
assert minSubArraySum([1, 2, 3, 4, 5, -6]) == -6
assert minSubArraySum([1,2,3,4]) == 1
assert minSubArraySum([1,2,3,1]) == 1
assert minSubArraySum([1,2,3,1,3]) == 1
assert minSubArraySum([1,2,3,1,3,2]) == 1
assert minSubArraySum([-1,2,3,1,3,2]) == -1
assert minSubArraySum([-1,2,3,1,3,2,-1]) == -1
assert minSubArraySum([-1,2,3,1,3,2,-2]) == -2
assert minSubArraySum([-1,2,3,1,3,2,-2,3]) == -2
assert minSubArraySum([-1,2,3,1,3,2,-2,3,1]) == -2
assert minSubArraySum([-1,2,3,1,3,2,-2,3,1,2]) == -2
assert minSubArraySum([-1,2,3,1,3,2,-2,3,1,2,4]) == -2
assert minSubArraySum([10, 10, -10, -10, 10]) == -20
assert minSubArraySum([1, 2, 3, 4, -6]) == -6
assert minSubArraySum([1, 2, 3, 4, -5]) == -5
assert minSubArraySum([1, 1, 1, 1, 1]) == 1
assert minSubArraySum([5, 4, -3, 2, 1]) == -3
assert minSubArraySum([0]) == 0
assert minSubArraySum([2,2,2,2,2,2,2,2,2]) == 2
assert minSubArraySum([0,0,0,0,0,0,0,0,0]) == 0
assert minSubArraySum([9,8,7,6,5,4,3,2,1]) == 1
assert minSubArraySum([4,3,3,9,3,3,9,3,3,10]) == 3
assert minSubArraySum([7,2,2,2,7,2,2,2,7,2,2,2,7]) == 2
assert minSubArraySum([5,5,5,5,5,5,5,5,5,5,5,5,5]) == 5
assert minSubArraySum([5,5,5,5,5,5,5,5,5,5,5,5,5,5]) == 5
assert minSubArraySum([-3,1,2,3,-3]) == -3
assert minSubArraySum([-1, -2, 0]) == -3
assert minSubArraySum([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 1
assert minSubArraySum([1, 2, 3, 1, 2, 3, 1, 2, 3, 100]) == 1
assert minSubArraySum([1]) == 1
assert minSubArraySum([1,2]) == 1
assert minSubArraySum([-1,2]) == -1
assert minSubArraySum([1,2,3]) == 1
assert minSubArraySum([-1,2,3]) == -1
assert minSubArraySum([-2,2,1]) == -2
assert minSubArraySum([-2,2,3]) == -2
assert minSubArraySum([-2,2,3,0]) == -2
assert minSubArraySum([-2,2,3,1]) == -2
assert minSubArraySum([-2,2,3,0,2]) == -2
assert minSubArraySum([-2,2,3,0,2,5]) == -2
assert minSubArraySum([1,2,1,-4,5]) == -4
assert minSubArraySum([1,2,1,-4,5,0]) == -4
assert minSubArraySum([2, 3, -2, 4]) == -2
assert minSubArraySum([5,5,5,5,5,5,5]) == 5
assert minSubArraySum([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
assert minSubArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
assert minSubArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -100]) == -100
assert minSubArraySum([-100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -100
assert minSubArraySum([1, 1, 2, 3, 4, 5]) == 1
assert minSubArraySum([1, 2, 1, 2, 3, 4, 5]) == 1
assert minSubArraySum([1, 2, 3, 4, -10]) == -10
assert minSubArraySum([1, 2, 3, 4, -20]) == -20
assert minSubArraySum([-1,0,1,2]) == -1
assert minSubArraySum([10,2,3,4,5]) == 2
assert minSubArraySum([1,2,3,4,5,6]) == 1
assert minSubArraySum([-1,0,1,2,3,4,5,6]) == -1
assert minSubArraySum([1,2,3,4,5,6,7]) == 1
assert minSubArraySum([-1,0,1,2,3,4,5,6,7]) == -1
assert minSubArraySum([-5,0,1,2,3,4,5,6,7]) == -5
assert minSubArraySum([0,1,2,3,4,5,6,7]) == 0
assert minSubArraySum([-2,0,1,2,3,4,5,6,7]) == -2
assert minSubArraySum([5,4,3,2,1]) == 1
assert minSubArraySum([4, 3, 2, 1, 5]) == 1
assert minSubArraySum([1, 2, 3, 4, 0]) == 0
assert minSubArraySum([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -55
assert minSubArraySum([3, -1, 2, 1]) == -1
assert minSubArraySum([4, -4, 4, -4, 4]) == -4
assert minSubArraySum([1, 2, 1, 2, 4, 3]) == 1
assert minSubArraySum([-1, 0, -2, 3, -2, 4, -5]) == -5
