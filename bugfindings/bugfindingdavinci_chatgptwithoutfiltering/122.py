
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
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0) == 0
assert add_elements([10, 21, 14, 73, 15], 2) == 31
assert add_elements([10, 21, 14, 73, 15], 3) == 45
assert add_elements([], 5) == 0, "Failed test case"
assert add_elements([1, 23, 52, 79, 144, 233, 2, 12, 99, 124, 140, 156, 169, 187, 199], 0) == 0
assert add_elements([10, 100, 3, 42, 32, 54, 21, 54, 6, 54, 7], 0) == 0
assert add_elements([], 1) == 0
assert add_elements([1,1,1,1,1,1,1,1,1,1], 0) == 0
assert add_elements([12, 34, 56, 78, 9, 10, 11, 12, 13, 14], 1) == 12
assert add_elements([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 1) == 10
assert add_elements([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 2) == 30
assert add_elements([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 3) == 60
assert add_elements([], 4) == 0
assert add_elements([4, 2, 1, 6, 3], 0) == 0
