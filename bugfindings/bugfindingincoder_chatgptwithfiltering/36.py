

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    ns = []
    for i in range(n):
        if i % 11 == 0 and i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == '7')
    return ans
assert fizz_buzz(2) == 0,'should return 0, given 2 as input'
assert fizz_buzz(3) == 0,'should return 0, given 3 as input'
assert fizz_buzz(4) == 0,'should return 0, given 4 as input'
assert fizz_buzz(5) == 0,'should return 0, given 5 as input'
assert fizz_buzz(7) == 0,'should return 0, given 7 as input'
assert fizz_buzz(8) == 0,'should return 0, given 8 as input'
assert fizz_buzz(9) == 0,'should return 0, given 9 as input'
assert fizz_buzz(10) == 0,'should return 0, given 10 as input'
assert fizz_buzz(11) == 0,'should return 0, given 11 as input'
assert fizz_buzz(13) == 0,'should return 0, given 13 as input'
assert fizz_buzz(14) == 0,'should return 0, given 14 as input'
assert fizz_buzz(15) == 0,'should return 0, given 15 as input'
assert fizz_buzz(101) == 3
assert fizz_buzz(102) == 3
assert fizz_buzz(103) == 3
assert fizz_buzz(80) == 3
assert fizz_buzz(100) == 3
assert fizz_buzz(7) == 0
assert fizz_buzz(7) == 0, "7 should equal 0"
assert fizz_buzz(10) == 0, "10 should equal 0"
assert fizz_buzz(14) == 0, "14 should equal 0"
assert fizz_buzz(11) == 0, "Incorrect fizz_buzz output."
assert fizz_buzz(13) == 0, "Incorrect fizz_buzz output."
assert fizz_buzz(25) == 0, "Incorrect fizz_buzz output."
assert fizz_buzz(3) == 0, "Incorrect fizz_buzz output."
assert fizz_buzz(7) == 0, "Incorrect fizz_buzz output."
assert fizz_buzz(12) == 0, "Incorrect fizz_buzz output."
assert fizz_buzz(2) == 0, "Incorrect fizz_buzz output."
assert fizz_buzz(7) == 0, "fizz buzz fails for 7"
assert fizz_buzz(5) == 0, "fizz buzz fails for 5"
assert fizz_buzz(9) == 0, "fizz buzz fails for 9"
assert fizz_buzz(10) == 0, "fizz buzz fails for 10"
assert fizz_buzz(1) == 0
assert fizz_buzz(0) == 0
assert fizz_buzz(10) == 0
assert fizz_buzz(11) == 0
assert fizz_buzz(12) == 0
assert fizz_buzz(13) == 0
assert fizz_buzz(300) == 10
assert fizz_buzz(99) == 3
assert fizz_buzz(125) == 4
assert fizz_buzz(130) == 4
assert fizz_buzz(139) == 4
assert fizz_buzz(253) == 7
assert fizz_buzz(2) == 0
assert fizz_buzz(14) == 0, "14 is not divisible by 11 or 13, so '0' should be returned."
assert fizz_buzz(25) == 0, "25 is not divisible by 11 or 13, so '0' should be returned."
assert fizz_buzz(122) == 4
assert fizz_buzz(131) == 4
assert fizz_buzz(138) == 4
assert fizz_buzz(143) == 4
assert fizz_buzz(3) == 0
assert fizz_buzz(15) == 0
assert fizz_buzz(6) == 0
assert fizz_buzz(9) == 0
assert fizz_buzz(27) == 0
assert fizz_buzz(17) == 0
