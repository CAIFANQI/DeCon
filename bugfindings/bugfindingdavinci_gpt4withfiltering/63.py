

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
assert fibfib(3) == 1
assert fibfib(4) == 2
assert fibfib(5) == 4
assert fibfib(6) == 7
assert fibfib(7) == 13
assert fibfib(8) == 24
assert fibfib(9) == 44
assert fibfib(10) == 81
assert fibfib(11) == 149
assert fibfib(12) == 274
assert fibfib(13) == 504
assert fibfib(14) == 927
assert fibfib(15) == 1705
assert fibfib(16) == 3136
assert fibfib(17) == 5768
assert fibfib(18) == 10609
assert fibfib(19) == 19513
assert fibfib(20) == 35890
assert fibfib(21) == 66012
assert fibfib(22) == 121415
assert fibfib(23) == 223317
assert fibfib(24) == 410744
assert fibfib(25) == 755476
assert fibfib(26) == 1389537
assert fibfib(27) == 2555757
