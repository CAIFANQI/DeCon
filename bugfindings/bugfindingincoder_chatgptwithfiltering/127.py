
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
assert intersection((1,4), (1,5)) == "YES", "check the correctness of intersection"
assert intersection((1,5), (2,5)) == "YES", "check the correctness of intersection"
assert intersection((1,4), (3,5)) == "NO", "check the correctness of intersection"
assert intersection((4,5), (1,4)) == "NO", "check the correctness of intersection"
assert intersection((1,4), (5,5)) == "NO", "check the correctness of intersection"
assert intersection((5,5), (1,6)) == "NO", "check the correctness of intersection"
assert intersection((5,6), (1,5)) == "NO", "check the correctness of intersection"
assert intersection((3,5), (3,4)) == "NO"
assert intersection((3,5), (5,7)) == "NO"
assert intersection((1,3), (1,3)) == "YES"
assert intersection((1,3), (2,4)) == "NO"
assert intersection((1,3), (2,5)) == "NO"
assert intersection((1,5), (1,10)) == "NO"
assert intersection((1,5), (1,11)) == "NO"
assert intersection((2,4), (1,9)) == "YES"
assert intersection((2,4), (1,11)) == "YES"
assert intersection((2,5), (1,3)) == "NO"
assert intersection((2,5), (1,10)) == "YES"
assert intersection((2,5), (1,11)) == "YES"
assert intersection((1, 3), (2, 4)) == "NO"
assert intersection((2, 3), (5, 8)) == "NO"
assert intersection((2, 5), (3, 5)) == "YES"
assert intersection((3, 5), (5, 5)) == "NO"
assert intersection((3, 5), (3, 7)) == "YES"
assert intersection((3, 5), (5, 9)) == "NO"
assert intersection((3, 7), (5, 6)) == "NO"
assert intersection((3, 7), (3, 7)) == "NO"
assert intersection((3, 7), (3, 10)) == "NO"
assert intersection((3, 10), (1, 5)) == "YES"
assert intersection((3, 10), (1, 7)) == "NO"
assert intersection((3, 10), (1, 3)) == "NO"
assert intersection((3, 10), (1, 2)) == "NO"
assert intersection((1, 3), (5, 8)) == "NO"
assert intersection((2, 3), (3, 5)) == "NO"
assert intersection((1,3), (4, 5)) == "NO", "the length of intersection should be 2"
assert intersection((1,4), (2, 3)) == "NO", "the length of intersection should be 2"
assert intersection((1,5), (2, 3)) == "NO", "the length of intersection should be 2"
assert intersection((4,5), (6,7)) == "NO", "the length of intersection should be 2"
assert intersection((3, 5), (4, 7)) == "NO"
assert intersection((3, 5), (4, 5)) == "NO"
assert intersection((3, 7), (4, 7)) == "YES"
assert intersection((3, 7), (4, 11)) == "YES"
assert intersection((3, 7), (3, 11)) == "NO"
assert intersection((1, 3), (3, 4)) == "NO"
assert intersection((1, 1), (3, 4)) == "NO"
assert intersection((1,5),(2,7)) == "YES"
assert intersection((1,5),(3,7)) == "YES"
assert intersection((1,5),(2,3)) == "NO"
assert intersection((3,5),(1,7)) == "YES"
assert intersection((1, 3), (3, 4)) == "NO", "incorrect result"
assert intersection((3, 4), (1, 2)) == "NO", "incorrect result"
assert intersection((10, 50), (50, 60)) == 'NO'
assert intersection((10, 20), (10, 20)) == 'NO'
assert intersection((10, 20), (10, 30)) == 'NO'
assert intersection((10, 20), (20, 40)) == 'NO'
assert intersection((1, 3), (1, 2)) == "NO"
assert intersection((3, 5), (5, 6)) == "NO"
assert intersection((3, 5), (6, 6)) == "NO"
assert intersection((1, 4), (4, 5)) == "NO"
assert intersection((7, 8), (8, 10)) == "NO"
assert intersection((7, 8), (7, 11)) == "NO"
assert intersection((0, 0), (2, 5)) == 'NO'
assert intersection((1, 1), (2, 2)) == 'NO'
assert intersection((1, 3), (2, 5)) == 'NO'
assert intersection((1, 3), (2, 7)) == "NO"
assert intersection((2, 4), (4, 5)) == "NO"
assert intersection((3, 4), (1, 5)) == "NO"
assert intersection((1,3), (2, 5)) == "NO"
assert intersection((1,3), (3, 6)) == "NO"
assert intersection((3,5), (5, 6)) == "NO"
assert intersection((2,9), (5, 9)) == "NO"
assert intersection((2, 3), (1, 3)) == "NO"
assert intersection((9, 10), (7, 8)) == "NO"
assert intersection((2, 4), (5, 7)) == "NO"
assert intersection((3, 7), (3, 8)) == "NO"
assert intersection((1, 3), (3, 6)) == "NO"
assert intersection((1, 3), (5, 6)) == "NO"
assert intersection((3, 4), (3, 5)) == "NO"
assert intersection((4, 6), (5, 6)) == 'NO'
assert intersection((3, 5), (5, 10)) == 'NO'
assert intersection((3, 5), (6, 10)) == 'NO'
assert intersection((10, 11), (11, 20)) == 'NO'
assert intersection((1,5), (2,4)) == "YES"
assert intersection((1, 3), (2, 5)) == "NO"
assert intersection((0, 10), (2, 3)) == "NO"
