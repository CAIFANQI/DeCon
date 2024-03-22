
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
assert add_elements([10, 20, 30, 40, 50], 3) == 60, "Test case 1 failed"
assert add_elements([15, 25, 35, 45, 55], 2) == 40, "Test case 2 failed"
assert add_elements([10, 20, 30, 40, 50], 5) == 150, "Test case 4 failed"
assert add_elements([10, 20, 30, 40, 50], 1) == 10, "Test case 5 failed"
assert add_elements([10, 20, 30, 40, 50], 5) == 150, "Error: Test Case 2"
assert add_elements([11, 22, 33, 44, 55], 2) == 33, "Error: Test Case 4"
assert add_elements([10, 20, 30, 40, 50], 3) == 60
assert add_elements([10, 20, 30, 40, 50], 5) == 150
assert add_elements([11, 22, 33, 44, 55], 3) == 66
assert add_elements([11, 22, 33, 44, 55], 5) == 165
assert add_elements([10, 20, 30, 40, 50], 3) == 60, "Test case 4 failed"
assert add_elements([10, 20, 30, 40, 50], 1) == 10
assert add_elements([10, 20, 30, 40, 50], 2) == 30
assert add_elements([10, 20, 30, 40, 50], 4) == 100, "Test case 2 failed"
assert add_elements([11, 22, 33, 44, 55], 5) == 165, "Test case 3 failed"
assert add_elements([10, 20, 30, 40, 50], 4) == 100
assert add_elements([12, 23, 34, 45, 56], 5) == 170
assert add_elements([10, 20, 30, 40, 50], 5) == 150, "Test case 2 failed"
assert add_elements([11, 22, 33, 44, 55], 4) == 110, "Test case 4 failed"
assert add_elements([12, 23, 34, 45, 56], 1) == 12, "Test case 5 failed"
assert add_elements([12, 34, 56, 78, 90], 2) == 46, "Test case 4 failed"
assert add_elements([10, 20, 30, 40], 3) == 60
assert add_elements([15, 25, 35, 45], 4) == 120
assert add_elements([10, 20, 30, 40, 50], 3) == 60, "Test case 2 failed"
assert add_elements([1, 2, 3, 4, 5], 0) == 0, "Test case 7 failed"
assert add_elements([11, 22, 33, 44, 55], 4) == 110
assert add_elements([10, 20, 30, 40, 50], 5) == 150, 'Test Case 2 Failed'
assert add_elements([10, 20, 30, 40, 50], 2) == 30, 'Test Case 3 Failed'
assert add_elements([11, 22, 33, 44, 55], 1) == 11, 'Test Case 5 Failed'
assert add_elements([11, 22, 33, 44, 55], 5) == 165, 'Test Case 7 Failed'
assert add_elements([10, 20, 30, 40, 50], 4) == 100, 'Test Case 9 Failed'
assert add_elements([11, 22, 33, 44, 55], 4) == 110, "Test case 3 failed"
assert add_elements([10, 20, 30, 40, 50], 5) == 150, "Test case 3 failed"
assert add_elements([10, 20, 30, 40, 50], 1) == 10, "Test case 4 failed"
assert add_elements([11, 22, 33, 44, 55], 2) == 33
assert add_elements([10, 20, 30, 40, 50], 5) == 150, "Test case 5 failed"
assert add_elements([1, 2, 3, 4, 5], 0) == 0
assert add_elements([10, 20, 30, 40, 50], 3) == 60, "Error: Test Case 5"
assert add_elements([11, 22, 33, 44, 55], 2) == 33, "Test case 3 failed"
assert add_elements([99, 88, 77, 66, 55], 1) == 99, "Test case 5 failed"
assert add_elements([10, 20, 30, 40, 50], 0) == 0
assert add_elements([11, 22, 33, 44, 55], 2) == 33, 'Test Case 3 Failed'
assert add_elements([11, 22, 33, 44, 55], 1) == 11
assert add_elements([11, 22, 33, 44, 55], 0) == 0
