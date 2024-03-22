

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
assert fizz_buzz(13) == 0
assert fizz_buzz(1) == 0
assert fizz_buzz(20) == 0, "test failed"
assert fizz_buzz(11) == 0
assert fizz_buzz(30) == 0
assert fizz_buzz(47) == 0
assert fizz_buzz(2) == 0
assert fizz_buzz(3) == 0
assert fizz_buzz(4) == 0
assert fizz_buzz(5) == 0
assert fizz_buzz(6) == 0
assert fizz_buzz(7) == 0
assert fizz_buzz(8) == 0
assert fizz_buzz(9) == 0
assert fizz_buzz(10) == 0
assert fizz_buzz(12) == 0
assert fizz_buzz(14) == 0
assert fizz_buzz(15) == 0
assert fizz_buzz(16) == 0
assert fizz_buzz(20) == 0
assert fizz_buzz(21) == 0
assert fizz_buzz(22) == 0
assert fizz_buzz(25) == 0
assert fizz_buzz(24) == 0
assert fizz_buzz(27) == 0
assert fizz_buzz(28) == 0
assert fizz_buzz(32) == 0
assert fizz_buzz(33) == 0
assert fizz_buzz(35) == 0
assert fizz_buzz(36) == 0
assert fizz_buzz(38) == 0
assert fizz_buzz(40) == 0
assert fizz_buzz(42) == 0
assert fizz_buzz(0) == 0
assert fizz_buzz(17) == 0
assert fizz_buzz(18) == 0
assert fizz_buzz(19) == 0
assert fizz_buzz(77) == 0
assert fizz_buzz(111) == 3
assert fizz_buzz(100) == 3
assert fizz_buzz(101) == 3
assert fizz_buzz(20) == 0  # 20 is not divisible by 7
assert fizz_buzz(40) == 0  # no numbers between 31 and 39 are divisible by 7
assert fizz_buzz(34) == 0
assert fizz_buzz(72) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(23) == 0
assert fizz_buzz(70) == 0
assert fizz_buzz(80) == 3
assert fizz_buzz(143) == 4
assert fizz_buzz(1) == 0, "Error in fizz_buzz"
assert fizz_buzz(55) == 0
assert fizz_buzz(150) == 4
assert fizz_buzz(45) == 0
