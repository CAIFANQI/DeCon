

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
assert modp(10, 2) == 0
assert modp(20, 2) == 0
assert modp(30, 2) == 0
assert modp(2, 1) == 0,'modp 2 1'
assert modp(10, 13) == 10
assert modp(10, 26) == 10
assert modp(5, 7) == 4
assert modp(5, 9) == 5
assert modp(5, 27) == 5
assert modp(3, 5) == 3
assert modp(2, 1) == 0
assert modp(2,3) == 1
assert modp(4, 4) == 0, "Your function modp is broken"
assert modp(4, 8) == 0, "Your function modp is broken"
assert modp(10, 2) == 0, "Your function modp is broken"
assert modp(11, 2) == 0, "Your function modp is broken"
assert modp(12, 2) == 0, "Your function modp is broken"
assert modp(13, 2) == 0, "Your function modp is broken"
assert modp(14, 2) == 0, "Your function modp is broken"
assert modp(15, 2) == 0, "Your function modp is broken"
assert modp(16, 2) == 0, "Your function modp is broken"
assert modp(17, 2) == 0, "Your function modp is broken"
assert modp(18, 2) == 0, "Your function modp is broken"
assert modp(19, 2) == 0, "Your function modp is broken"
assert modp(20, 2) == 0, "Your function modp is broken"
assert modp(6, 2) == 0
assert modp(7, 2) == 0
assert modp(14, 2) == 0
assert modp(16, 2) == 0
assert modp(17, 2) == 0
assert modp(17, 4) == 0
assert modp(31, 2) == 0
assert modp(31, 4) == 0
assert modp(31, 7) == 2
assert modp(31, 16) == 0
assert modp(31, 22) == 2
assert modp(42, -1) == 0
assert modp(42, 4) == 0
assert modp(42, -2) == 0
assert modp(42, 2) == 0
assert modp(42, 1) == 0
assert modp(5, 5) == 2
assert modp(8, 11) == 3
assert modp(5, 8) == 0
assert modp(11, 10) == 8
assert modp(100, 5) == 1
assert modp(100, 3) == 1
assert modp(9, 7) == 1
assert modp(3, 2) == 0
assert modp(5, 3) == 2, '5^3 mod 3'
assert modp(8, 3) == 1
assert modp(5000000, 3) == 1
assert modp(42, 3) == 1
assert modp(2**8+2**6, 2**8+2**6) == 2**8
assert modp(13, 3) == 2
assert modp(15, 3) == 2
assert modp(5, 2) == 0
assert modp(6, 3) == 1
assert modp(10, 3) == 1
assert modp(3,4) == 0
assert modp(4,7) == 2
assert modp(3,3) == 2
assert modp(3,5) == 3
assert modp(2, 3) == 1
assert modp(3, 7) == 1
assert modp(4, 4) == 0
assert modp(9, 4) == 0
assert modp(0, 3) == 1
assert modp(4, 3) == 1
assert modp(5, 4) == 0
assert modp(4, 7) == 2
assert modp(3, 11) == 8
assert modp(3, 9) == 8
assert modp(24, 5) == 1
assert modp(7, 6) == 2, '7 should be 2 mod 6'
assert modp(3, 4) == 0
assert modp(10, 11) == 1
