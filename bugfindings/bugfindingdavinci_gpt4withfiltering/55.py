

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
assert fib(5) == 5
assert fib(6) == 8
assert fib(7) == 13
assert fib(10) == 55
assert fib(20) == 6765
assert fib(15) == 610
assert fib(8) == 21
assert fib(9) == 34
assert fib(11) == 89
assert fib(12) == 144
assert fib(13) == 233
assert fib(14) == 377
assert fib(16) == 987
assert fib(25) == 75025
assert fib(23) == 28657
assert fib(30) == 832040
assert fib(35) == 9227465
assert fib(10) == 55  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
assert fib(20) == 6765  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765
assert fib(1) == 1, 'Wrong result for n=1'
assert fib(10) == 55, 'Wrong result for n=10'
assert fib(36) == 14930352
