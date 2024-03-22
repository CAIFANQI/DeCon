

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    import math

    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, min(int(math.sqrt(p)), p)):
            if p % k == 0:
                return False
        return True
    f = [0, 1]
    while True:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            n -= 1
        if n == 0:
            return f[-1]
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
assert prime_fib(4) == 13, "Wrong implementation of prime_fib"
assert prime_fib(2) == 3, 'second'
assert prime_fib(3) == 5, 'third'
assert prime_fib(4) == 13, 'fourth'
assert prime_fib(5) == 89, 'fifth'
assert prime_fib(5) == 89, "Nope, that's not right"
assert prime_fib(5) == 89, 'prime_fib is not correct'
assert prime_fib(2) == 3, 'error2'
assert prime_fib(1) == 2, 'The 1-th Fibonacci prime should be 2.'
