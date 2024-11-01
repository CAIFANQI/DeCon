
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    return sum([x for idx, x in enumerate(lst) if idx%2==1 and x%2==1])
assert solution(list(range(1, 1001))) == 250000
assert solution([]) == 0
assert solution([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert solution([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
assert solution([-3, -4, -5, -6, -7, -8, -9, -10]) == -3 + -5 + -7 + -9
assert solution([5, 5, 5, 5, 5, 5, 5, 5]) == 5 + 5 + 5 + 5
assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50
assert solution([0, 2, 4, 6, 8, 10, 12, 14, 16, 18]) == 0
assert solution([9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9 + 7 + 5 + 3 + 1
assert solution([0, 0, 1, 1, 2, 2, 3, 3, 4, 4]) == 1 + 3
assert solution([-9, -8, -7, -6, -5, -4, -3, -2, -1, 0]) == -9 + -7 + -5 + -3 + -1
assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 25
assert solution([]) == 0, 'wrong solution'
assert solution([2, 4, 6, 8, 10]) == 0
assert solution([1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 9, "Wrong answer"
assert solution([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
assert solution([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert solution([1]) == 1
assert (solution([4, 6, 8, 10])) == 0
assert (solution([10, 12, 14, 16])) == 0
assert solution([3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 15
assert solution([0, -1, -5]) == -5
assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 1 + 3 + 5 + 7 + 9 + 11
assert solution([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0, 'Wrong Answer'
assert solution([2]) == 0
assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
assert solution([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 45
assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19
assert solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
assert solution([2,2,4,4,6,6,8,8]) == 0
assert solution([4,4,4,4,4,4,4,4,4,4]) == 0
assert solution([2,2,2,2,2,2,2,2,2,2]) == 0
assert solution([42]) == 0
assert solution([12, 12, 12, 12, 12, 12, 12, 12, 12, 12]) == 0
assert solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
assert solution([0, 2, 4, 6, 8, 10]) == 0
assert solution([1, 0, 1, 1, 0, 1, 1, 1]) == 3
assert solution([2, 4, 6, 8, 10, 12, 14, 16]) == 0
