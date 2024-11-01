
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
assert add_elements([1], 0) == 0
assert add_elements([], 0) == 0
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 0) == 0
assert add_elements([], 4) == 0
assert add_elements([], 10) == 0
assert add_elements([1, 2, 3, 4], 0) == 0
assert add_elements([], 3) == 0
assert add_elements([1,2], 0) == 0
assert add_elements([1, 1, 1], 0) == 0
