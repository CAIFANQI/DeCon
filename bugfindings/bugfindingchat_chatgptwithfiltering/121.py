
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    return sum([x for idx, x in enumerate(lst) if idx%2==1 and x%2==1])
assert solution([2, 4, 6, 8, 10]) == 0, "Test case 2 failed"
assert solution([2, 4, 6, 8, 10]) == 0
assert solution([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
assert solution([2, 4, 6, 8]) == 0
assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
assert solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
assert solution([2, 4, 6, 8, 10]) == 0, "Test case 4 failed"
assert solution([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0, "Test case 5 failed"
assert solution([2, 4, 6, 8, 10]) == 0, 'Test Case 4 Failed'
assert solution([2, 4, 6, 8, 10]) == 0, 'Test Case 2 Failed'
assert solution([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0, 'Test Case 5 Failed'
assert solution([2, 4, 6, 8, 10]) == 0, 'Test Case 3 Failed'
assert solution([2, 2, 2, 2, 2]) == 0, 'Test Case 4 Failed'
assert solution([2, 2, 2, 2, 2]) == 0
assert solution([]) == 0
assert solution([2]) == 0
assert solution([4]) == 0
assert solution([5]) == 5
assert solution([1, 3, 5, 7, 9]) == 15
assert solution([10, 20, 30, 40, 50]) == 0
assert solution([2, 4, 6, 8, 10, 12]) == 0
assert solution([1] * 10**6) == 1 * (10**6 // 2)
assert solution([2] * 10**6) == 0
assert solution([2, 3, 4, 5, 6]) == 0, "Test case 2 failed"
assert solution([2, 4, 6, 8, 10]) == 0, "Test case 5 failed"
assert solution([2, 4, 6, 8, 10]) == 0, "Error: Test Case 2"
