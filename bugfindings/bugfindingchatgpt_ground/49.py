

def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    ret = 0
    for i in range(n):
        ret = (2 * ret) % p
    return ret
assert modp(0, 5) == 1
assert modp(1, 5) == 2
assert modp(2, 5) == 4
assert modp(3, 5) == 3
assert modp(4, 5) == 1
assert modp(100, 17) == 16
assert modp(1000, 17) == 1
assert modp(1, 3) == 2
assert modp(10, 17) == 4
assert modp(5, 5) == 2
assert modp(6, 5) == 4
assert modp(7, 5) == 3
assert modp(8, 5) == 1
assert modp(100, 7) == 2
assert modp(10, 1000000007) == 1024
assert modp(100, 1000000007) == 976371285
assert modp(1, 7) == 2
assert modp(2, 7) == 4
assert modp(3, 7) == 1
assert modp(4, 7) == 2
assert modp(5, 7) == 4
assert modp(6, 7) == 1
assert modp(7, 7) == 2
assert modp(8, 7) == 4
assert modp(9, 7) == 1
assert modp(9, 5) == 2
assert modp(10, 5) == 4
assert modp(1000000, 3) == 1
assert modp(1000001, 3) == 2
assert modp(1, 17) == 2
assert modp(2, 17) == 4
assert modp(3, 17) == 8
assert modp(4, 17) == 16
assert modp(5, 17) == 15
assert modp(6, 17) == 13
assert modp(7, 17) == 9
assert modp(8, 17) == 1
assert modp(9, 17) == 2
assert modp(11, 17) == 8
assert modp(12, 17) == 16
assert modp(13, 17) == 15
assert modp(14, 17) == 13
assert modp(15, 17) == 9
assert modp(16, 17) == 1
assert modp(10, 7) == 2
assert modp(0, 17) == 1
assert modp(6, 3) == 1
assert modp(7, 3) == 2
assert modp(10, 3) == 1
assert modp(20, 3) == 1
assert modp(30, 3) == 1
assert modp(40, 3) == 1
assert modp(20, 17) == 16
assert modp(11, 5) == 3
assert modp(0, 7) == 1
assert modp(0, 11) == 1
assert modp(1, 11) == 2
assert modp(2, 11) == 4
assert modp(3, 11) == 8
assert modp(4, 11) == 5
assert modp(5, 11) == 10
assert modp(6, 11) == 9
assert modp(7, 11) == 7
assert modp(8, 11) == 3
assert modp(9, 11) == 6
assert modp(10, 11) == 1
assert modp(11, 7) == 4
assert modp(1, 1) == 0
assert modp(2, 1) == 0
assert modp(3, 1) == 0
assert modp(0, 2) == 1
assert modp(2, 2) == 0
assert modp(0, 3) == 1
assert modp(3, 2) == 0
assert modp(3, 3) == 2
assert modp(4, 1) == 0
assert modp(4, 2) == 0
assert modp(4, 3) == 1
assert modp(4, 4) == 0
assert modp(5, 1) == 0
assert modp(5, 3) == 2
assert modp(6, 1) == 0
assert modp(6, 2) == 0
assert modp(6, 4) == 0
assert modp(7, 1) == 0
assert modp(8, 1) == 0
assert modp(8, 2) == 0
assert modp(8, 4) == 0
assert modp(8, 8) == 0
assert modp(9, 1) == 0
assert modp(10, 1) == 0
assert modp(10, 2) == 0
assert modp(10, 6) == 4
assert modp(20, 13) == 9
assert modp(40, 13) == 3
assert modp(60, 13) == 1
assert modp(0, -3) == 1
assert modp(100, 13) == 3
assert modp(100, 11) == 1
assert modp(1000, 11) == 1
assert modp(10000, 100) == 76
assert modp(100000, 1000) == 376
assert modp(1000000, 10000) == 9376
assert modp(1, 1000000007) == 2
assert modp(2, 1000000007) == 4
assert modp(3, 1000000007) == 8
assert modp(4, 1000000007) == 16
assert modp(5, 1000000007) == 32
assert modp(6, 1000000007) == 64
assert modp(7, 1000000007) == 128
assert modp(8, 1000000007) == 256
assert modp(9, 1000000007) == 512
assert modp(10000, 7) == 2
assert modp(1000, 13) == 3
assert modp(40, 17) == 1
assert modp(10000, 17) == 1
