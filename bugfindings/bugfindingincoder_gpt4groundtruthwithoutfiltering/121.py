
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    return sum([x for idx, x in enumerate(lst) if idx%2==1 and x%2==1])
assert solution([1]) == 1
assert solution([3]) == 3
assert solution([1,3,5]) == 6, "OddSum"
assert solution([]) == 0
assert solution([2]) == 0
assert solution([3, 5]) == 3
assert solution([3, 1, 2, 3, 1]) == 4
assert solution([1, 3, 5]) == 6
assert solution([1, 2, 3, 4, 5]) == 9
assert solution([1, 1]) == 1
assert solution([0, 0, 0, 0]) == 0
assert solution([0,1,2,3]) == 0
assert solution([1,2,3,4]) == 4
assert solution([2,2,2,2,2,2]) == 0
assert solution([2,3,5]) == 5
assert solution([2,3,4]) == 0
assert solution([5, 1, 5]) == 10
assert solution([1, 1, 2, 0]) == 1
assert solution([]) == 0, "Empty list is expected"
assert solution([0, 0, 0, 0]) == 0, "Empty list is expected"
assert solution([-10, -20, -30, -40, -50]) == 0
assert solution([1,2,3,4,5,6,7,8,9,10]) == 25
assert solution([0, 5]) == 0
assert solution([0, 0, 0]) == 0
assert solution([-3]) == -3
assert solution([0,2,3,3]) == 3
assert solution([0,0,0,0]) == 0
assert solution([-1]) == -1
assert solution([5, 5, 5, 5]) == 10
assert solution([0, 2, 2]) == 0
