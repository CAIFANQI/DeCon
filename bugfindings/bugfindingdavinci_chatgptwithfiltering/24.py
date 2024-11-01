

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in reversed(range(n)):
        if n - i == 0:
            return i
assert largest_divisor(10) == 5
assert largest_divisor(20) == 10
assert largest_divisor(55) == 11
assert largest_divisor(5) == 1
assert largest_divisor(11) == 1
assert largest_divisor(28) == 14
assert largest_divisor(33) == 11
assert largest_divisor(9) == 3
assert largest_divisor(25) == 5
assert largest_divisor(26) == 13
assert largest_divisor(3) == 1
assert largest_divisor(12) == 6
assert largest_divisor(101) == 1
assert largest_divisor(80) == 40
assert largest_divisor(17) == 1
assert largest_divisor(13) == 1
assert largest_divisor(365) == 73
assert largest_divisor(4) == 2
assert largest_divisor(27) == 9
assert largest_divisor(24) == 12
assert largest_divisor(7) == 1
assert largest_divisor(18) == 9
assert largest_divisor(40) == 20
assert largest_divisor(15) == 5
assert largest_divisor(100) == 50
assert largest_divisor(2) == 1
assert largest_divisor(50) == 25
assert largest_divisor(37) == 1
assert largest_divisor(128) == 64
assert largest_divisor(n=1024) == 512
assert largest_divisor(n=7) == 1
assert largest_divisor(n=19) == 1
assert largest_divisor(6) == 3
assert largest_divisor(14) == 7
assert largest_divisor(16) == 8
assert largest_divisor(39) == 13
assert largest_divisor(42) == 21
assert largest_divisor(145) == 29
assert largest_divisor(8) == 4
assert largest_divisor(99) == 33
assert largest_divisor(999) == 333
assert largest_divisor(30) == 15
assert largest_divisor(29) == 1
assert largest_divisor(64) == 32
assert largest_divisor(1024) == 512
assert largest_divisor(23) == 1
assert largest_divisor(2**16) == 2**15
assert largest_divisor(13) == 1, "Error, something went wrong with largest_divisor"
assert largest_divisor(32) == 16
assert largest_divisor(98) == 49
assert 1 == largest_divisor(7)
assert 5 == largest_divisor(15)
assert 1 == largest_divisor(17)
assert 1 == largest_divisor(23)
assert 1 == largest_divisor(29)
assert largest_divisor(21) == 7
assert largest_divisor(49) == 7
assert largest_divisor(220) == 110
assert largest_divisor(35) == 7
assert largest_divisor(4096) == 2048
assert largest_divisor(1000) == 500
assert largest_divisor(2048) == 1024
assert largest_divisor(135) == 45
assert largest_divisor(36) == 18
assert largest_divisor(19) == 1
assert largest_divisor(22) == 11
assert largest_divisor(123) == 41
assert largest_divisor(127) == 1
assert largest_divisor(103) == 1
assert 1 == largest_divisor(5)
assert 7 == largest_divisor(21)
assert largest_divisor(120) == 60
assert largest_divisor(111) == 37
