
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
assert 	add_elements([0, 0, 0, 0], 4) == 0
assert 	add_elements([1, 2, 3, 4, 5], 0) == 0
assert 	add_elements([1, 1, 1, 1, 1, 1], 0) == 0
assert 	(add_elements([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 10) == 0)
assert 	(add_elements([], 10) == 0)
assert 	add_elements([0, 0, 0, 0], 1) == 0
assert 	add_elements([0, 0, 0, 0], 2) == 0
assert 	add_elements([0, 0, 0, 0, 0, 0], 5) == 0
assert 	add_elements([1, 0, 0], 3) == 1
assert 	add_elements([0, 0, 0], 4) == 0
assert 	add_elements([1, 2, 3, 4, 5], 5) == 15
assert 	add_elements([0, 0, 0, 0], 0) == 0
assert 	add_elements([0, 0], 1) == 0
assert 	add_elements([4, 3, 2, 1], 2) == 7
assert 	add_elements([4, 3, 2, 1], 3) == 9
assert 	add_elements([7, 9, 2, 3, 4], 4) == 21, 'error!'
assert 	add_elements([1,2,3,4,5,6,7,8,9,10], 3) == 3 + 1 + 2
assert 	add_elements([5,8,3,2,1], 4) == 3 + 2 + 5 + 8
assert 	add_elements([1, 2, 3, 4], 0) == 0
assert 	add_elements([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 2) == 0
assert 	add_elements([0,0,0,0,0,0,0,0,0,0], 10) == 0
assert 	add_elements([0,0,0,0,0,0,0,0,0,0], 11) == 0
assert 	add_elements([9, 9, 9], 2) == 18
assert 	add_elements([9, 9, 9], 3) == 27
assert 	(add_elements([9], 2) == 9)
assert 	(add_elements([9], 1) == 9)
