
def intersection(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """
    def is_prime(num):
        if num == 1 or num == 0:
            return False
        if num == 2:
            return True
        for i in range(2, num):
            if num%i == 0:
                return False
        return True

    l = max(interval1[0], interval2[0])
    r = min(interval1[1], interval2[1])
    length = r - l
    if length > 0:
        return "YES"
    return "NO"
assert intersection((1, 3), (2, 4)) == "NO"
assert intersection((4, 7), (4, 6)) == "YES"
assert intersection((1, 4), (6, 10)) == "NO"
assert intersection((6, 10), (3, 5)) == "NO"
assert intersection((1, 3), (1, 4)) == "YES"
assert intersection((1, 3), (4, 6)) == "NO"
assert intersection((1, 5), (7, 9)) == "NO"
assert intersection((1, 9), (7, 11)) == "YES"
assert intersection((1, 9), (11, 14)) == "NO"
assert intersection((8, 9), (10, 10)) == "NO"
assert intersection((1,3), (3,5)) == "NO"
assert intersection((1, 3), (3, 4)) == "NO"
assert intersection((2, 4), (3, 5)) == "NO"
assert intersection((1, 6), (2, 4)) == "YES"
assert intersection((2, 5), (3, 7)) == "YES"
assert intersection((1, 6), (7, 9)) == "NO"
assert intersection((1, 4), (7, 9)) == "NO"
assert intersection((1, 10), (11, 12)) == "NO"
assert intersection((1, 12), (11, 12)) == "NO"
assert intersection((2, 3), (5, 7)) == "NO"
assert intersection((1, 10), (3, 5)) == "YES"
assert intersection((1, 10), (2, 5)) == 'YES'
assert intersection((1, 10), (12, 15)) == 'NO'
assert intersection((1, 4), (1, 2)) == 'NO'
assert intersection((1, 2), (1, 4)) == 'NO'
assert intersection((2, 3), (4, 5)) == 'NO'
assert intersection((1, 2), (3, 4)) == 'NO'
assert intersection((1, 5), (0, 4)) == 'YES'
assert intersection((0, 5), (2, 3)) == 'NO'
assert intersection((1, 2), (2, 3)) == 'NO'
assert intersection((4, 9), (1, 5)) == 'NO'
assert intersection((1, 10), (6, 7)) == 'NO'
assert intersection((5, 8), (5, 8)) == 'YES'
assert intersection((5, 6), (7, 8)) == 'NO'
assert intersection((0, 3), (2, 6)) == 'NO'
assert intersection((0, 3), (2, 5)) == 'NO'
assert intersection((0, 3), (2, 4)) == 'NO'
assert intersection((0, 3), (3, 6)) == 'NO'
assert intersection((0, 3), (3, 4)) == 'NO'
assert intersection((0, 1), (2, 3)) == "NO"
assert intersection((1, 2), (2, 3)) == "NO"
assert intersection((5, 8), (3, 7)) == "YES"
assert intersection((1, 5), (3, 7)) == "YES"
assert intersection((1, 9), (5, 7)) == "YES"
assert intersection((2, 4), (1, 5)) == "YES"
assert intersection([2, 3], [4, 5]) == "NO"
assert intersection([1, 8], [6, 8]) == "YES"
assert intersection([1, 8], [8, 9]) == "NO"
assert intersection([2, 3], [4, 7]) == "NO"
assert intersection([1, 8], [2, 5]) == "YES"
assert intersection([1, 8], [5, 8]) == "YES"
assert intersection((1, 10), (10, 12)) == "NO"
assert intersection((1, 10), (2, 5)) == "YES"
assert intersection((5, 15), (10, 20)) == "YES"
assert intersection((10, 20), (15, 20)) == "YES"
assert intersection((10, 20), (15, 25)) == "YES"
assert intersection((15, 20), (15, 25)) == "YES"
assert intersection((15, 25), (10, 20)) == "YES"
assert intersection((15, 25), (15, 20)) == "YES"
assert intersection((5, 5), (15, 15)) == "NO"
assert intersection((15, 15), (5, 5)) == "NO"
assert intersection((1,6), (2,4)) == "YES"
assert intersection((1,2), (2,4)) == "NO"
assert intersection((1, 2), (3, 4)) == "NO"
assert intersection((2, 3), (1, 6)) == "NO"
assert intersection((1, 100), (1, 30)) == "YES"
assert intersection((1, 2), (1, 1)) == "NO"
assert intersection((1, 1), (2, 3)) == "NO"
assert intersection((1,100), (2,100)) == "NO"
assert intersection((1,100), (200,300)) == "NO"
assert intersection((1, 3), (1, 3)) == "YES"
assert intersection((0, 0), (4, 5)) == "NO"
assert intersection((1, 2), (4, 5)) == "NO"
assert intersection((1, 2), (3, 3)) == "NO"
assert intersection((1, 5), (2, 7)) == "YES"
assert intersection((2, 3), (3, 4)) == "NO"
assert intersection((1, 4), (5, 6)) == "NO"
assert intersection((6, 8), (2, 4)) == "NO"
assert intersection((9, 14), (3, 5)) == "NO"
assert intersection((9, 17), (15, 23)) == "YES"
assert intersection((3, 5), (2, 3)) == "NO"
assert intersection((6, 8), (7, 12)) == "NO"
assert intersection((9, 17), (11, 13)) == "YES"
assert intersection((4, 7), (8, 10)) == "NO"
assert intersection((1, 8), (8, 11)) == "NO"
assert intersection((1, 3), (2, 4)) == 'NO'
assert intersection((-1, 1), (1, 1)) == 'NO'
assert intersection((-3, -2), (1, 4)) == 'NO'
assert intersection((5, 8), (4, 7)) == 'YES'
assert intersection((-5, -4), (1, 4)) == 'NO'
assert intersection((-6, -5), (1, 4)) == 'NO'
assert intersection((-6, -5), (0, 4)) == 'NO'
assert intersection((1, 1), (0, 1)) == 'NO'
assert intersection((-1, -1), (0, -1)) == 'NO'
assert intersection((0, 2), (0, 2)) == 'YES'
assert intersection((1, 3), (1, 3)) == 'YES'
assert intersection((1, 3), (3, 5)) == "NO"
assert intersection((1, 3), (0, 1)) == "NO"
assert intersection((1, 3), (1, 1)) == "NO"
assert intersection((1, 3), (3, 3)) == "NO"
assert intersection((2, 5), (4, 7)) == 'NO'
assert intersection((6, 11), (9, 12)) == 'YES'
assert intersection((10, 20), (0, 10)) == 'NO'
assert intersection((1, 7), (4, 10)) == 'YES'
assert intersection((4, 10), (1, 7)) == 'YES'
assert intersection((1, 4), (4, 10)) == 'NO'
assert intersection((4, 10), (1, 4)) == 'NO'
assert intersection((0, 3), (2, 10)) == 'NO'
assert intersection((2, 10), (0, 3)) == 'NO'
assert intersection((1, 2), (4, 10)) == 'NO'
assert intersection((4, 10), (1, 2)) == 'NO'
assert intersection((2, 4), (1, 3)) == 'NO'
assert intersection((0, 2), (2, 4)) == 'NO'
assert intersection((2, 4), (0, 2)) == 'NO'
assert intersection((4, 5), (4, 10)) == 'NO'
assert intersection([0, 0], [5, 5]) == "NO"
assert intersection([0, 1], [4, 5]) == "NO"
assert intersection([3, 7], [1, 2]) == "NO"
assert intersection([0, 2], [3, 5]) == "NO"
assert intersection([0, 5], [1, 3]) == "YES"
assert intersection([4, 5], [0, 2]) == "NO"
assert intersection([5, 6], [0, 2]) == "NO"
assert intersection([0, 1], [5, 6]) == "NO"
assert intersection([5, 6], [0, 1]) == "NO"
assert intersection([2, 3], [3, 4]) == 'NO'
assert intersection([1, 3], [1, 3]) == 'YES'
assert intersection([1, 3], [1, 4]) == 'YES'
assert intersection([1, 7], [4, 8]) == 'YES'
assert intersection([2, 5], [3, 7]) == 'YES'
assert intersection([1, 2], [3, 4]) == 'NO'
assert intersection([1, 5], [6, 8]) == 'NO'
assert intersection([2, 3], [4, 5]) == 'NO'
assert intersection([3, 4], [1, 2]) == 'NO'
assert intersection([5, 6], [1, 2]) == 'NO'
assert intersection([1, 2], [5, 6]) == 'NO'
assert intersection([5, 6], [3, 4]) == 'NO'
assert intersection([7, 8], [1, 2]) == 'NO'
assert intersection((1, 10), (7, 15)) == "YES"
assert intersection((1, 10), (11, 20)) == "NO"
assert intersection((1, 10), (5, 15)) == "YES"
assert intersection((1, 10), (15, 20)) == "NO"
assert intersection((1, 10), (20, 30)) == "NO"
assert intersection((1, 10), (1, 8)) == "YES"
assert intersection((1, 10), (1, 3)) == "YES"
assert intersection((1, 3), (4, 7)) == "NO"
assert intersection((4, 5), (6, 7)) == "NO"
assert intersection((3, 4), (7, 9)) == "NO"
assert intersection((1,3), (3,4)) == "NO"
assert intersection((1,3), (4,8)) == "NO"
assert intersection((1,3), (1,8)) == "YES"
assert intersection((1,1), (2,2)) == "NO"
assert intersection((0, 10), (3, 8)) == "YES"
assert intersection((3, 8), (0, 10)) == "YES"
assert intersection((0, 10), (5, 15)) == "YES"
assert intersection((5, 15), (0, 10)) == "YES"
assert intersection((0, 10), (12, 15)) == "NO"
assert intersection((12, 15), (0, 10)) == "NO"
assert intersection((2, 3), (3, 6)) == 'NO'
assert intersection((1, 5), (2, 3)) == 'NO'
assert intersection((1, 5), (6, 7)) == 'NO'
assert intersection([5, 5], [1, 4]) == "NO"
assert intersection([1, 4], [4, 5]) == "NO"
assert intersection([4, 5], [1, 4]) == "NO"
assert intersection([1, 3], [2, 4]) == "NO"
assert intersection([2, 4], [1, 3]) == "NO"
assert intersection((5,11), (11,17)) == "NO"
assert intersection((5,11), (13,17)) == "NO"
assert intersection((1,5), (2,6)) == "YES"
assert intersection((1,9), (2,3)) == "NO"
assert intersection((1,9), (2,6)) == "NO"
assert intersection((1,9), (2,8)) == "NO"
assert intersection((1,9), (3,4)) == "NO"
assert intersection([1, 7], [2, 3]) == "NO"
assert intersection([1, 7], [3, 5]) == "YES"
assert intersection([1, 7], [8, 9]) == "NO"
assert intersection([1, 7], [0, 6]) == "YES"
assert intersection([3, 7], [1, 5]) == "YES"
assert intersection([1, 7], [0, 1]) == "NO"
assert intersection([1, 7], [0, 2]) == "NO"
assert intersection([1, 7], [1, 1]) == "NO"
assert intersection([1, 7], [2, 2]) == "NO"
assert intersection([1, 6], [2, 4]) == "YES"
assert intersection([1, 4], [3, 6]) == "NO"
assert intersection([1, 6], [7, 10]) == "NO"
assert intersection([10, 12], [6, 12]) == "YES"
assert intersection([3, 6], [8, 10]) == "NO"
assert intersection([3, 6], [4, 9]) == "YES"
assert intersection([10, 12], [2, 3]) == "NO"
assert intersection([1, 2], [3, 4]) == "NO"
assert intersection((1, 4), (2, 5)) == "YES"
assert intersection((3, 7), (5, 7)) == "YES"
assert intersection((5, 7), (3, 7)) == "YES"
assert intersection((4, 7), (4, 8)) == "YES"
assert intersection((4, 8), (4, 7)) == "YES"
assert intersection((4, 6), (5, 7)) == "NO"
assert intersection((5, 7), (4, 6)) == "NO"
assert intersection((4, 7), (7, 10)) == "NO"
assert intersection((7, 10), (4, 7)) == "NO"
assert intersection((1, 5), (6, 10)) == "NO"
assert intersection((6, 10), (1, 5)) == "NO"
assert intersection((2, 3), (1, 3)) == "NO"
assert intersection((1, 3), (4, 5)) == "NO"
assert intersection((2,4), (4,5)) == "NO"
assert intersection((1,10), (3,6)) == "YES"
assert intersection((1,100), (101, 200)) == "NO"
assert intersection((1,2), (2,3)) == "NO"
assert intersection((1,10), (10,20)) == "NO"
assert intersection([2, 3], [3, 4]) == "NO"
assert intersection([1, 4], [6, 7]) == "NO"
assert intersection([1, 4], [5, 7]) == "NO"
assert intersection([5, 5], [2, 3]) == "NO"
assert intersection([4, 5], [2, 3]) == "NO"
assert intersection([0, 0], [1, 2]) == "NO"
assert intersection([-10, -1], [-3, -1]) == "YES"
assert intersection([1, 2], [4, 5]) == "NO"
assert intersection([1, 5], [4, 7]) == "NO"
assert intersection([8, 9], [1, 5]) == "NO"
assert intersection([1, 5], [2, 6]) == "YES"
assert intersection([5, 10], [2, 3]) == "NO"
assert intersection([1, 5], [3, 7]) == "YES"
assert intersection([1, 4], [3, 7]) == "NO"
assert intersection([1, 1], [2, 2]) == "NO"
assert intersection([1, 9], [1, 10]) == "NO"
assert intersection([1, 10], [1, 9]) == "NO"
assert intersection([1, 5], [5, 10]) == "NO"
assert intersection([5, 10], [1, 5]) == "NO"
assert intersection([1, 10], [11, 20]) == "NO"
assert intersection([11, 20], [1, 10]) == "NO"
assert intersection([1, 10], [3, 5]) == "YES"
assert intersection((1, 5), (2, 3)) == "NO"
assert intersection([4, 6], [4, 6]) == 'YES'
assert intersection([4, 6], [4, 9]) == 'YES'
assert intersection((2, 5), (3, 5)) == "YES"
assert intersection((1, 4), (6, 8)) == "NO"
assert intersection((2, 4), (1, 3)) == "NO"
assert intersection((5, 5), (6, 6)) == "NO"
assert intersection((3, 4), (2, 3)) == "NO"
assert intersection((2, 2), (3, 3)) == "NO"
assert intersection((2, 3), (4, 5)) == "NO"
assert intersection((1, 7), (5, 8)) == "YES"
assert intersection([1, 3], [5, 6]) == "NO"
assert intersection([1, 2], [2, 3]) == "NO"
assert intersection([1, 5], [6, 7]) == "NO"
assert intersection([1, 5], [7, 8]) == "NO"
assert intersection((2, 5), (1, 3)) == "NO"
assert intersection((1, 7), (5, 6)) == "NO"
assert intersection((1, 7), (6, 6)) == "NO"
assert intersection((3, 8), (4, 7)) == "YES"
assert intersection((1, 4), (7, 10)) == "NO"
assert intersection((2, 9), (1, 5)) == "YES"
assert intersection((1, 10), (5, 7)) == "YES"
assert intersection((1, 4), (1, 4)) == "YES"
assert intersection([1, 3], [3, 4]) == 'NO'
assert intersection([1, 3], [5, 5]) == 'NO'
assert intersection([1, 3], [4, 5]) == 'NO'
assert intersection([1, 3], [0, 0]) == 'NO'
assert intersection((1, 6), (3, 8)) == "YES"
assert intersection((0, 4), (2, 6)) == "YES"
assert intersection((3, 5), (2, 4)) == "NO"
assert intersection((1, 2), (0, 0)) == "NO"
assert intersection((1, 12), (5, 18)) == "YES"
assert intersection((1, 8), (2, 4)) == "YES"
assert intersection((1, 5), (1, 4)) == "YES"
assert intersection((1, 3), (0, 5)) == "YES"
assert intersection((2, 3), (1, 1)) == "NO"
assert intersection((3, 3), (1, 1)) == "NO"
assert intersection([1, 5], [2, 4]) == "YES"
assert intersection([1, 5], [3, 4]) == "NO"
assert intersection([1, 5], [3, 5]) == "YES"
assert intersection([1, 5], [6, 10]) == "NO"
assert intersection([1, 2], [2, 3]) == 'NO'
assert intersection([1, 3], [4, 7]) == 'NO'
assert intersection((1, 6), (3, 7)) == "YES"
assert intersection((1, 9), (7, 9)) == "YES"
assert intersection((1, 2), (4, 5)) == 'NO'
assert intersection((1, 3), (3, 5)) == 'NO'
assert intersection((1, 3), (4, 5)) == 'NO'
assert intersection((1, 5), (3, 5)) == 'YES'
assert intersection((1, 5), (2, 4)) == 'YES'
assert intersection((1, 5), (2, 5)) == 'YES'
assert intersection((1, 6), (2, 5)) == 'YES'
assert intersection((1, 7), (3, 5)) == 'YES'
assert intersection((1, 8), (3, 5)) == 'YES'
assert intersection((1, 10), (1, 6)) == "YES"
assert intersection((10, 20), (21, 22)) == "NO"
assert intersection((10, 20), (10, 15)) == "YES"
assert intersection((10, 20), (5, 15)) == "YES"
assert intersection((1, 2), (3, 5)) == "NO"
assert intersection([1, 3], [3, 4]) == "NO"
assert intersection([1, 3], [4, 5]) == "NO"
assert intersection([1, 3], [4, 6]) == "NO"
assert intersection([1, 3], [4, 7]) == "NO"
assert intersection([1, 4], [2, 5]) == "YES"
assert intersection([1, 4], [2, 4]) == "YES"
assert intersection([1, 4], [5, 6]) == "NO"
assert intersection((100, 200), (150, 300)) == "NO"
assert intersection((-5, -1), (-1, 5)) == "NO"
assert intersection((-15, -5), (-10, -5)) == "YES"
assert intersection((-5, 0), (1, 3)) == "NO"
assert intersection((-15, -10), (-5, -1)) == "NO"
assert intersection((-15, -10), (-15, -10)) == "YES"
assert intersection((8, 12), (10, 14)) == 'YES'
assert intersection((10, 12), (10, 12)) == 'YES'
assert intersection((1, 13), (10, 14)) == 'YES'
assert intersection((1, 13), (2, 14)) == 'YES'
assert intersection((1, 13), (2, 13)) == 'YES'
assert intersection((7, 10), (6, 8)) == "NO"
assert intersection((1, 7), (1, 5)) == "NO"
assert intersection((1, 8), (1, 7)) == "NO"
assert intersection((10, 13), (8, 12)) == 'YES'
assert intersection((10, 13), (8, 11)) == 'NO'
assert intersection((10, 13), (11, 13)) == 'YES'
assert intersection((11, 13), (10, 13)) == 'YES'
assert intersection((11, 13), (1, 1)) == 'NO'
assert intersection((100, 99), (11, 13)) == 'NO'
assert intersection((1, 10), (10, 13)) == "NO"
assert intersection((1, 100), (60, 70)) == "NO"
assert intersection((1, 100), (10, 99)) == "YES"
assert intersection((1, 100), (11, 99)) == "NO"
assert intersection((0, 5), (2, 3)) == "NO"
assert intersection((1, 2), (5, 6)) == 'NO'
assert intersection((5, 6), (1, 2)) == 'NO'
assert intersection((1, 2), (1, 3)) == 'NO'
assert intersection((1, 3), (1, 2)) == 'NO'
assert intersection((1, 4), (1, 4)) == 'YES'
assert intersection((3, 5), (3, 5)) == 'YES'
assert intersection((1, 6), (1, 6)) == 'YES'
assert intersection((1, 5), (6, 8)) == "NO"
assert intersection((11, 13), (11, 19)) == "YES"
assert intersection((2, 3), (1, 2)) == "NO"
assert intersection((11, 20), (1, 10)) == "NO"
assert intersection((5, 10), (11, 20)) == "NO"
assert intersection((11, 20), (5, 10)) == "NO"
assert intersection((4, 6), (7, 12)) == "NO"
assert intersection((10, 15), (20, 25)) == "NO"
assert intersection((0, 2), (1, 3)) == "NO"
assert intersection((3, 4), (0, 2)) == "NO"
assert intersection((0, 6), (1, 3)) == "YES"
assert intersection((7, 9), (1, 3)) == "NO"
assert intersection((1, 10), (2, 3)) == "NO"
assert intersection((1, 6), (3, 5)) == "YES"
assert intersection((1, 8), (3, 5)) == "YES"
assert intersection((1, 5), (2, 6)) == "YES"
assert intersection((2, 5), (1, 4)) == "YES"
assert intersection((1, 3), (1, 5)) == 'YES'
assert intersection((3, 5), (3, 6)) == 'YES'
assert intersection((1, 5), (3, 5)) == "YES"
assert intersection((1, 5), (3, 6)) == "YES"
assert intersection((1, 100), (3, 50)) == "YES"
assert intersection((1, 4), (5, 7)) == "NO"
assert intersection((1, 9), (10, 12)) == "NO"
assert intersection((3, 4), (4, 5)) == "NO"
assert intersection((1, 4), (3, 5)) == "NO"
assert intersection((1, 6), (6, 10)) == "NO"
assert intersection((6, 10), (10, 15)) == "NO"
assert intersection((10, 20), (15, 25)) == 'YES'
assert intersection((10, 20), (40, 50)) == 'NO'
assert intersection((10, 20), (21, 30)) == 'NO'
assert intersection((1, 10), (10, 20)) == "NO"
assert intersection((1,1), (2,4)) == "NO"
assert intersection((1,3), (1,3)) == "YES"
assert intersection((1,3), (4,5)) == "NO"
assert intersection((2,4), (1,1)) == "NO"
assert intersection((1,5), (1,1)) == "NO"
assert intersection((1, 5), (2, 4)) == "YES"
assert intersection((1, 8), (2, 5)) == "YES"
assert intersection([1, 2], [5, 6]) == "NO"
assert intersection([1, 5], [3, 6]) == "YES"
assert intersection((10, 12), (20, 30)) == "NO"
assert intersection((6, 8), (9, 10)) == "NO"
assert intersection((2, 5), (1, 7)) == "YES"
assert intersection((10, 15), (20, 40)) == "NO"
assert intersection((1, 1), (2, 2)) == "NO"
assert intersection((3, 4), (5, 6)) == "NO"
assert intersection((11, 18), (12, 17)) == "YES"
assert intersection((9, 11), (5, 10)) == "NO"
assert intersection([3, 5], [7, 9]) == "NO"
assert intersection([3, 5], [5, 6]) == "NO"
assert intersection((1, 4), (2, 4)) == "YES"
assert intersection((2, 3), (3, 5)) == "NO"
assert intersection((0, 100), (1, 2)) == "NO"
assert intersection((1, 2), (0, 100)) == "NO"
assert intersection((0, 1), (1, 2)) == "NO"
assert intersection((0, 0), (0, 0)) == "NO"
assert intersection((0, 2), (2, 5)) == "NO"
assert intersection((1, 4), (4, 5)) == "NO"
assert intersection((4, 5), (1, 3)) == "NO"
assert intersection((0, 5), (1, 3)) == "YES"
assert intersection((0, 10), (20, 30)) == 'NO'
assert intersection((0, 10), (5, 15)) == 'YES'
assert intersection((7, 13), (13, 8)) == "NO"
assert intersection((1, 9), (2, 6)) == "NO"
assert intersection((1, 8), (5, 6)) == "NO"
assert intersection((1, 10), (1, 9)) == "NO"
assert intersection((1, 10), (4, 4)) == "NO"
assert intersection((1, 10), (6, 10)) == "NO"
assert intersection((1, 10), (9, 10)) == "NO"
assert intersection((1, 1000000), (1000001, 2000000)) == "NO"
assert intersection((1, 5), (5, 10)) == "NO"
assert intersection((1, 10), (1, 2)) == "NO"
assert intersection((1, 10), (0, 12)) == "NO"
assert intersection((1, 3), (2, 5)) == 'NO'
assert intersection((1, 1), (4, 5)) == 'NO'
assert intersection((1, 4), (4, 7)) == 'NO'
assert intersection((1, 4), (5, 8)) == 'NO'
assert intersection((1, 4), (2, 8)) == 'YES'
assert intersection((1, 3), (1, 4)) == 'YES'
assert intersection((5, 7), (3, 4)) == "NO"
assert intersection((7, 9), (5, 6)) == "NO"
assert intersection((1, 2), (1, 3)) == "NO"
assert intersection((4, 6), (7, 9)) == "NO"
assert intersection((1, 5), (6, 9)) == "NO"
assert intersection((5, 6), (1, 4)) == "NO"
assert intersection((1, 3), (5, 8)) == "NO"
assert intersection((5, 8), (1, 3)) == "NO"
assert intersection((1, 10), (5, 10)) == "YES"
assert intersection((1, 6), (2, 10)) == "NO"
assert intersection((1, 2), (2, 5)) == "NO"
assert intersection((1, 5), (7, 15)) == "NO"
assert intersection((3, 10), (5, 7)) == "YES"
assert intersection((5, 12), (7, 13)) == "YES"
assert intersection((5, 10), (8, 10)) == "YES"
assert intersection((3, 5), (4, 10)) == "NO"
assert intersection((2, 3), (1, 4)) == "NO"
assert intersection((1, 2), (5, 6)) == "NO"
assert intersection((5, 6), (2, 3)) == "NO"
assert intersection((2, 4), (1, 6)) == "YES"
assert intersection((1, 10), (2, 6)) == "NO"
assert intersection((11, 15), (2, 6)) == "NO"
assert intersection((0, 4), (2, 5)) == "YES"
assert intersection((0, 10), (10, 20)) == "NO"
assert intersection((0, 12), (14, 25)) == "NO"
assert intersection((0, 2), (10, 20)) == "NO"
assert intersection((1, 3), (3, 7)) == "NO"
assert intersection((4, 6), (3, 5)) == "NO"
assert intersection((1, 7), (4, 10)) == "YES"
assert intersection((4, 10), (4, 8)) == "NO"
assert intersection((4, 14), (4, 8)) == "NO"
assert intersection((2, 4), (1, 4)) == "YES"
assert intersection((1, 3), (1, 2)) == "NO"
assert intersection([1, 6], [8, 9]) == "NO"
assert intersection([-1, -1], [1, 1]) == "NO"
assert intersection([-6, -2], [-4, -2]) == "YES"
assert intersection([1, 4], [1, 3]) == "YES"
assert intersection([1, 4], [1, 5]) == "YES"
assert intersection([1, 4], [0, 4]) == "YES"
assert intersection([1, 4], [0, 3]) == "YES"
