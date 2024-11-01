

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
assert 	fizz_buzz(13) == 0
assert 	fizz_buzz(10) == 0
assert 	fizz_buzz(15) == 0
assert 	fizz_buzz(7) == 0
assert 	fizz_buzz(28) == 0
assert 	fizz_buzz(29) == 0
assert 	fizz_buzz(30) == 0
assert 	fizz_buzz(32) == 0
assert 	fizz_buzz(33) == 0
assert 	fizz_buzz(34) == 0
assert 	fizz_buzz(35) == 0
assert 	fizz_buzz(36) == 0
assert 	fizz_buzz(38) == 0
assert 	fizz_buzz(39) == 0
