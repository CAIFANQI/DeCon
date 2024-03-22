
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
assert intersection((1, 5), (2, 4)) == "YES"
assert intersection((1, 7), (8, 10)) == "NO"
assert intersection((3, 7), (5, 9)) == "YES"
assert intersection((1, 2), (3, 4)) == "NO"
assert intersection((1, 10), (5, 15)) == "YES"
assert intersection((1, 10), (11, 15)) == "NO"
assert intersection((1, 5), (6, 10)) == "NO"
assert intersection((1, 5), (3, 7)) == "YES"
assert intersection((2, 4), (5, 7)) == "NO"
assert intersection((1, 3), (4, 6)) == "NO"
assert intersection((1, 3), (3, 5)) == "NO"
assert intersection((1, 5), (6, 7)) == "NO"
assert intersection((1, 7), (8, 12)) == "NO"
assert intersection((1, 3), (4, 5)) == "NO"
assert intersection((1, 4), (2, 4)) == "YES"
assert intersection((3, 7), (2, 5)) == "YES"
assert intersection((1, 5), (6, 8)) == "NO"
assert intersection((2, 5), (6, 9)) == "NO"
assert intersection((2, 5), (6, 10)) == "NO"
assert intersection((10, 15), (12, 20)) == "YES"
assert intersection((1, 10), (11, 20)) == "NO"
assert intersection((1, 5), (5, 10)) == "NO"
assert intersection((1, 2), (2, 4)) == "NO"
assert intersection((1, 10), (5, 8)) == "YES"
assert intersection((1, 7), (3, 5)) == "YES"
assert intersection((1, 7), (5, 10)) == "YES"
assert intersection((1, 10), (2, 4)) == "YES"
assert intersection((1, 4), (5, 7)) == "NO"
assert intersection((1, 10), (15, 20)) == "NO"
assert intersection((1, 7), (8, 9)) == "NO"
assert intersection((1, 10), (12, 15)) == "NO"
assert intersection((1, 6), (7, 10)) == "NO"
assert intersection((1, 6), (4, 8)) == "YES"
assert intersection((1, 5), (3, 8)) == "YES"
assert intersection((1, 7), (5, 9)) == "YES"
assert intersection((1, 3), (1, 3)) == "YES"
assert intersection((1, 3), (0, 1)) == "NO"
assert intersection((1, 3), (0, 4)) == "YES"
assert intersection((1, 10), (10, 20)) == "NO"
assert intersection((1, 13), (2, 4)) == "YES"
assert intersection((1, 19), (2, 4)) == "YES"
assert intersection((1, 10), (5, 7)) == "YES"
assert intersection((1,5),(3,7)) == "YES"
assert intersection((1,10),(10,15)) == "NO"
assert intersection((2, 4), (1, 3)) == "NO"
assert intersection((3, 7), (1, 5)) == "YES"
assert intersection((4, 6), (1, 3)) == "NO"
assert intersection((6, 10), (1, 5)) == "NO"
assert intersection((1, 10), (0, 0)) == "NO"
assert intersection((1, 13), (6, 8)) == "YES"
assert intersection((1, 13), (14, 18)) == "NO"
assert intersection((1, 13), (14, 15)) == "NO"
assert intersection((1, 13), (14, 16)) == "NO"
assert intersection((1, 13), (0, 0)) == "NO"
assert intersection((1, 13), (14, 14)) == "NO"
assert intersection((1, 13), (15, 15)) == "NO"
assert intersection((1, 13), (15, 16)) == "NO"
assert intersection((1, 13), (0, 18)) == "NO"
assert intersection((1, 13), (0, 22)) == "NO"
assert intersection((1, 13), (0, 24)) == "NO"
assert intersection((1, 13), (0, 26)) == "NO"
assert intersection((1, 13), (0, 27)) == "NO"
assert intersection((1, 13), (0, 28)) == "NO"
assert intersection((1, 13), (0, 30)) == "NO"
assert intersection((1, 13), (0, 32)) == "NO"
assert intersection((1, 13), (0, 33)) == "NO"
assert intersection((1, 13), (0, 34)) == "NO"
assert intersection((1, 13), (0, 36)) == "NO"
assert intersection((1, 13), (0, 38)) == "NO"
assert intersection((1, 13), (0, 40)) == "NO"
assert intersection((1, 13), (0, 42)) == "NO"
assert intersection((1, 13), (0, 44)) == "NO"
assert intersection((1, 13), (0, 45)) == "NO"
assert intersection((1, 13), (0, 46)) == "NO"
assert intersection((1, 13), (0, 48)) == "NO"
assert intersection((1, 13), (0, 49)) == "NO"
assert intersection((1, 7), (4, 8)) == "YES"
assert intersection((10, 20), (15, 25)) == "YES"
assert intersection((10, 20), (25, 30)) == "NO"
assert intersection((10, 20), (30, 40)) == "NO"
assert intersection((1, 5), (5, 7)) == "NO"
assert intersection((1, 10), (2, 9)) == "YES"
assert intersection((1, 3), (3, 4)) == "NO"
assert intersection((1, 7), (2, 4)) == "YES"
assert intersection((1, 3), (2, 2)) == "NO"
assert intersection((1, 5), (5, 5)) == "NO"
assert intersection((1, 7), (7, 7)) == "NO"
assert intersection((1, 3), (3, 3)) == "NO"
assert intersection((2, 4), (1, 5)) == "YES"
assert intersection((1, 10), (10, 15)) == "NO"
assert intersection((1, 5), (2, 8)) == "YES"
assert intersection((1, 10), (4, 7)) == "YES"
assert intersection((1,5),(2,4)) == "YES"
assert intersection((1, 4), (2, 5)) == "YES"
assert intersection((3, 5), (1, 3)) == "NO"
assert intersection((6, 8), (1, 5)) == "NO"
assert intersection((1, 7), (5, 8)) == "YES"
assert intersection((1, 5), (5, 6)) == "NO"
assert intersection((5, 6), (1, 5)) == "NO"
assert intersection((6, 7), (1, 5)) == "NO"
assert intersection((5, 8), (1, 10)) == "YES"
assert intersection((1, 7), (2, 10)) == "YES"
assert intersection((1, 7), (3, 6)) == "YES"
assert intersection((1, 10), (5, 10)) == "YES"
assert intersection((1, 10), (10, 10)) == "NO"
assert intersection((1, 10), (10, 11)) == "NO"
assert intersection((1, 10), (11, 11)) == "NO"
assert intersection((1, 10), (10, 12)) == "NO"
assert intersection((1, 7), (2, 9)) == "YES"
assert intersection((1, 2), (3, 3)) == "NO"
