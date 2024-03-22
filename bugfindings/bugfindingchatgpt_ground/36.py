

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
assert fizz_buzz(20) == 0
assert fizz_buzz(80) == 3
assert fizz_buzz(30) == 0
assert fizz_buzz(40) == 0
assert fizz_buzz(50) == 0
assert fizz_buzz(60) == 0
assert fizz_buzz(90) == 3
assert fizz_buzz(100) == 3
assert fizz_buzz(20) == 0, "Test case 2 failed"
assert fizz_buzz(100) == 3, "Test case 10 failed"
assert fizz_buzz(20) == 0, "Error: Test Case 2"
assert fizz_buzz(30) == 0, "Error: Test Case 3"
assert fizz_buzz(40) == 0, "Error: Test Case 4"
assert fizz_buzz(50) == 0, "Error: Test Case 5"
assert fizz_buzz(60) == 0, "Error: Test Case 6"
assert fizz_buzz(7) == 0
assert fizz_buzz(11) == 0
assert fizz_buzz(13) == 0
