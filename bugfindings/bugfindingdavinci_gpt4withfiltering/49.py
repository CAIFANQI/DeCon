

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
assert 1 == modp(4,3)
assert 2 == modp(5,3)
assert 1 == modp(6,3)
assert 1 == modp(10,3)
assert 2 == modp(11,3)
assert 1 == modp(12,3)
assert 1 == modp(16,3)
assert 2 == modp(17,3)
assert 1 == modp(18,3)
assert 1 == modp(22,3)
assert 2 == modp(23,3)
assert 1 == modp(24,3)
assert modp(3, 5) == 3
assert modp(3, 13) == 8
assert modp(1, 5) == 2
assert modp(2, 5) == 4
assert modp(4, 5) == 1
assert modp(5, 5) == 2
assert modp(6, 5) == 4
assert modp(999999, 19) == 18
assert modp(0, 10) == 1
assert modp(2,13) == 4
assert modp(3,13) == 8
assert modp(4,13) == 3
assert modp(5,13) == 6
assert modp(6,13) == 12
assert modp(7,13) == 11
assert modp(8,13) == 9
assert modp(9,13) == 5
assert modp(10,13) == 10
assert modp(11,13) == 7
assert modp(12,13) == 1
assert modp(13,13) == 2
assert modp(14,13) == 4
assert modp(15,13) == 8
assert modp(16,13) == 3
assert modp(17,13) == 6
assert modp(18,13) == 12
assert modp(19,13) == 11
assert modp(20,13) == 9
assert modp(21,13) == 5
assert modp(22,13) == 10
assert modp(23,13) == 7
assert modp(24,13) == 1
assert modp(25,13) == 2
assert modp(26,13) == 4
assert modp(27,13) == 8
assert modp(5, 13) == 6
assert modp(2, 3) == 1
assert modp(1000, 1) == 0
assert modp(1, 10) == 2
assert modp(2, 2) == 0
assert modp(0, 5) == 1
assert modp(1, 7) == 2
assert modp(2, 7) == 4
assert modp(3, 7) == 1
assert modp(4, 7) == 2
assert modp(1, 3) == 2
assert modp(3, 3) == 2
assert modp(4, 3) == 1
assert modp(5, 3) == 2
assert modp(6, 3) == 1
assert modp(7, 3) == 2
assert modp(8, 3) == 1
assert modp(0, 3) == 1
assert modp(5, 11) == 10
assert modp(10, 7) == 2
assert modp(5, 7) == 4
assert modp(6, 7) == 1
assert modp(10, 10 ** 9 + 7) == 1024
assert modp(8, 5) == 1
assert modp(3, 10) == 8
assert modp(10, 10) == 4
assert modp(4, 10) == 16 % 10
assert modp(10, 1000) == 1024 % 1000
assert modp(100, 1000) == 1267650600228229401496703205376 % 1000
assert modp(4, 17) == (2 ** 4) % 17
assert modp(4, 17) == 16
assert modp(1, 4) == 2
assert modp(1, 11) == 2
assert modp(2, 11) == 4
assert modp(3, 11) == 8
assert modp(10, 11) == 1024 % 11
assert 64 == modp(6,65)
assert 2 == modp(10,7)
assert 65536 == modp(16,65537)
assert 1 == modp(0,13)
assert modp(2, 11) == 4 % 11
assert modp(3, 11) == 8 % 11
assert modp(4, 11) == 16 % 11
assert modp(5, 11) == 32 % 11
assert modp(6, 11) == 64 % 11
assert modp(7, 11) == 128 % 11
assert modp(8, 11) == 256 % 11
assert modp(9, 11) == 512 % 11
assert modp(11, 11) == 2048 % 11
assert modp(12, 11) == 4096 % 11
assert modp(13, 11) == 8192 % 11
assert modp(14, 11) == 16384 % 11
assert modp(15, 11) == 32768 % 11
assert modp(16, 11) == 65536 % 11
assert modp(17, 11) == 131072 % 11
assert modp(18, 11) == 262144 % 11
assert modp(19, 11) == 524288 % 11
assert modp(20, 11) == 1048576 % 11
assert modp(21, 11) == 2097152 % 11
assert modp(22, 11) == 4194304 % 11
assert modp(7, 5) == 3
assert modp(9, 5) == 2
assert modp(4, 2) == 0
assert modp(6, 1024) == 64
assert modp(3, 16) == 8
assert modp(0, 7) == 1
assert modp(4, 29) == 16
assert modp(1, 13) == 2
assert modp(2, 13) == 4
assert modp(4, 13) == 3
assert modp(12, 13) == 1
assert modp(100, 2) == 0
assert modp(2, 10) == 4
assert modp(4, 10) == 6
assert modp(5, 10) == 2
assert modp(6, 10) == 4
assert modp(7, 10) == 8
assert modp(1, 97) == 2
assert modp(2, 97) == 4
assert modp(3, 97) == 8
assert modp(4, 97) == 16
assert modp(5, 97) == 32
assert modp(6, 97) == 64
assert modp(10, 5) == 4
assert modp(14, 5) == 4
assert modp(18, 5) == 4
assert modp(1234, 5) == 4
assert modp(123456, 7) == 1
assert modp(11, 5) == 3
assert modp(15, 7) == 1
assert modp(10, 3) == 1024 % 3
assert modp(10, 13) == 1024 % 13
assert modp(10, 101) == 1024 % 101
assert modp(1, 1009) == 2
assert modp(1, 19) == 2
assert modp(1, 10**10) == 2
assert modp(2, 3) == 4 % 3
assert modp(3, 3) == 8 % 3
assert modp(4, 3) == 16 % 3
assert modp(5, 3) == 32 % 3
assert modp(100, 3) == 1267650600228229401496703205376 % 3
assert modp(100, 101) == 1
assert modp(1, 6) == 2
assert modp(0, 13) == 1
assert modp(120, 13) == 1
assert modp(10, 13) == 10
assert modp(10, 2) == 0
assert modp(10, 3) == 1
assert modp(10, 4) == 0
assert modp(10, 6) == 4
assert modp(8, 10) == 6
assert modp(9, 10) == 2
assert modp(500, 10) == 6
assert modp(0, 101) == 1
assert modp(1, 101) == 2
assert modp(2, 101) == 4
assert modp(3, 101) == 8
assert modp(4, 101) == 16
