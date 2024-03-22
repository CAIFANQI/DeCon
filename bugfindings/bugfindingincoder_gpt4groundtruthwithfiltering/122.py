
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
assert add_elements([1, 2, 3], 0) == 0
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 3) == 6
assert add_elements([1, 2, 3, 4], 4) == 10
assert add_elements([-2, -1, 0, 1, 2], 1) == -2
assert add_elements([-2, -1, 0, 1, 2], 2) == -3
assert add_elements([1], 2) == 1
assert add_elements([1], 0) == 0
assert add_elements([], 0) == 0
assert add_elements([100], 2) == 0
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 4) == 10
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4) == 10
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9) == 45
assert add_elements([7, 5, 3, 2], 7) == 17
assert add_elements([7, 5, 3, 2], 9) == 17
assert add_elements([1,2,3], 3) == 6
assert add_elements([10, 1, 100, -10, 1], 2) == 11
assert add_elements([10, 1, 100, -10, 1], 3) == 11
assert add_elements([1, 2, 3, 4], 5) == 10
assert add_elements([1, 2, 3], 3) == 6
assert add_elements([1, 2, 3, 4], 3) == 6
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 0) == 0
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) == 1
assert add_elements([], 4) == 0
assert add_elements([1], 4) == 1
assert add_elements([1, 2, 3, 4, 5], 10) == 15
assert add_elements([], 10) == 0
assert add_elements([1, 2, 4, 3, 5], 2) == 3
assert add_elements([1,2,3], 10) == 6
assert add_elements([1, 2, 3, 4], 0) == 0
assert add_elements([], 3) == 0
assert add_elements([9, 9, 9], 1) == 9
assert add_elements([1, 2, 3, 100], 2) == 3, "Wrong Answer"
assert add_elements([1, 2, 3], 4) == 6
assert add_elements([1,2,3], 2) == 3
assert add_elements([1,2,3], 4) == 6
assert add_elements([1], 3) == 1
assert add_elements([1,2], 0) == 0
assert add_elements([10, 9, 8, 11, 13, 111], 3) == 27
assert add_elements([1, 1, 1], 0) == 0
assert add_elements([1, 2, 10, 11, 100], 3) == 13
