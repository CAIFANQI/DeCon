
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    return sum(elem for elem in arr if len(str(elem)) <= 2)
assert add_elements([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1) == 1
assert add_elements([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 2) == 2
assert add_elements([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10) == 10
assert add_elements([2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 2) == 4
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == 6
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == 3
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3) == 6
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 1) == 1
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 2) == 3
assert add_elements([4, 4, 4, 4, 4], 4) == 16, "Expected 16."
assert add_elements([6, 5, 4, 3, 2, 1], 6) == 21, "Expected 21."
assert add_elements([6, 5, 4, 3, 2, 1], 5) == 20, "Expected 20."
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0) == 0
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == 1
assert add_elements([3, 4, 5, 6, 7, 8, 9, 10], 2) == 7
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20) == 55
assert add_elements([1, 1, 1, 1, 1], 1) == 1
assert add_elements([1, 1, 1, 1, 1], 2) == 2
assert add_elements([1, 1, 1, 1, 1], 3) == 3
assert add_elements([1, 1, 1, 1, 1], 4) == 4
assert add_elements([1, 1, 1, 1, 1], 5) == 5
assert add_elements([2, 1, 3, 2, 5, 2, 6, 2, 4, 2], 6) == 15
assert add_elements([4, 2, 5, 3], 3) == 11
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8) == 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
assert add_elements([10, 21, 14, 73, 15], 2) == 31
assert add_elements([10, 21, 14, 73, 15], 3) == 45
assert add_elements([], 5) == 0, "Failed test case"
assert add_elements([5, 1, 2, 6, 7, 8, 4, 3, 9], 4) == 14
assert add_elements([5, 1, 2, 6, 7, 8, 4, 3, 9], 1) == 5
assert add_elements([5, 1, 2, 6, 7, 8, 4, 3, 9], 10) == 45
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == 55
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15) == 55
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4) == 10
assert add_elements([2, 3, 5, 6, 20, 1, 30, 30, 30, 30], 1) == 2
assert add_elements([0, 1, 1, 1, 3, 3, 5, 5, 5, 9], 10) == 33
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6) == 21
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7) == 28
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8) == 36
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9) == 45
assert add_elements([1,2,3,4,5,6,7,8,9,10], 3) == 6
assert add_elements([1,2,3,4,5,6,7,8,9,10], 4) == 10
assert add_elements([1,2,3,4,5,6,7,8,9,10], 5) == 15
assert add_elements([1, 23, 52, 79, 144, 233, 2, 12, 99, 124, 140, 156, 169, 187, 199], 0) == 0
assert add_elements([1, 23, 52, 79, 144, 233, 2, 12, 99, 124, 140, 156, 169, 187, 199], 1) == 1
assert add_elements([1, 23, 52, 79, 144, 233, 2, 12, 99, 124, 140, 156, 169, 187, 199], 2) == 24
assert add_elements([2, 3, 6, 9, 4, 5, 7, 8, 1], 2) == 5, "Should be 5"
assert add_elements([2, 3, 6, 9, 4, 5, 7, 8, 1], 1) == 2, "Should be 2"
assert add_elements([10, 100, 3, 42, 32, 54, 21, 54, 6, 54, 7], 0) == 0
assert add_elements([1,1,1,1,1,1,1,1,1,1], 7) == 7
assert add_elements([1,1,1,1,1,1,1,1,1,1], 3) == 3
assert add_elements([], 1) == 0
assert add_elements([1,1,1,1,1,1,1,1,1,1], 0) == 0
assert add_elements([1,1,1,1,1,1,1,1,1,1], 30) == 10
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11) == 55
assert add_elements([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 5) == 5
assert add_elements([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 6) == 6
assert add_elements([12, 34, 56, 78, 9, 10, 11, 12, 13, 14], 1) == 12
assert add_elements([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 1) == 10
assert add_elements([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 2) == 30
assert add_elements([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 3) == 60
assert add_elements([1, 10, 100, 1000, 10000], 2) == 11
assert add_elements([], 4) == 0
assert add_elements([4, 2, 1, 6, 3], 0) == 0
