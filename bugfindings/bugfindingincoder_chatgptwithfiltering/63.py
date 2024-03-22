

def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)
assert fibfib(0) == 0
assert fibfib(1) == 0
assert fibfib(2) == 1
assert fibfib(7) == 13
assert fibfib(1) == 0 
assert fibfib(2) == 1 
assert fibfib(3) == 1
assert fibfib(4) == 2
assert fibfib(2)
assert fibfib(3)
assert fibfib(1) is 0
assert fibfib(2) is 1
assert fibfib(3) is 1
assert fibfib(0) == 0, "The fibfib of 0 is 0"
assert fibfib(2) == 1, "The fibfib of 2 is 1"
