

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fib(n - 1) + fib(n - 2)
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5
assert fib(6) == 8
assert fib(7) == 13
assert fib(8) == 21
assert fib(9) == 34
assert fib(10) == 55
assert fib(11) == 89
assert fib(12) == 144
assert fib(13) == 233
assert fib(14) == 377
assert fib(15) == 610
assert fib(16) == 987
assert fib(17) == 1597
assert fib(18) == 2584
assert fib(19) == 4181
assert fib(20) == 6765
assert fib(21) == 10946
assert fib(22) == 17711
assert fib(23) == 28657
assert fib(24) == 46368
assert fib(25) == 75025
assert fib(26) == 121393
assert fib(27) == 196418
assert fib(28) == 317811
assert fib(29) == 514229
assert fib(30) == 832040
assert fib(31) == 1346269
assert fib(32) == 2178309
assert fib(33) == 3524578
assert fib(34) == 5702887
assert fib(35) == 9227465
assert fib(36) == 14930352
assert fib(37) == 24157817
assert fib(2) == 1, "2 should be the second Fibonacci number"
assert fib(0) == 0
