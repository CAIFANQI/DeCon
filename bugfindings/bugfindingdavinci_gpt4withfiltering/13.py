

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return b
assert greatest_common_divisor(12, 18) == 6, "Should be 6"
assert greatest_common_divisor(7, 14) == 7, "Should be 7"
assert greatest_common_divisor(47, 90) == 1, "Should be 1"
assert greatest_common_divisor(2, 3) == 1, "Should be 1"
assert greatest_common_divisor(4, 5) == 1, "Should be 1"
assert greatest_common_divisor(3, 3) == 3, "Should be 3"
assert greatest_common_divisor(6, 3) == 3, "Should be 3"
assert greatest_common_divisor(5, 7) == 1, "Should be 1"
assert greatest_common_divisor(9, 5) == 1, "Should be 1"
assert greatest_common_divisor(23, 11) == 1, "Should be 1"
assert greatest_common_divisor(2, 2) == 2, "Should be 2"
assert greatest_common_divisor(1, 1) == 1, "Should be 1"
assert greatest_common_divisor(1, 2) == 1, "Should be 1"
assert greatest_common_divisor(2, 1) == 1
assert greatest_common_divisor(6, 9) == 3
assert greatest_common_divisor(1, 5) == 1
assert greatest_common_divisor(10, 15) == 5
assert greatest_common_divisor(10, 20) == 10
assert greatest_common_divisor(30, 20) == 10
assert greatest_common_divisor(2, 6) == 2
assert greatest_common_divisor(12, 8) == 4
assert greatest_common_divisor(20, 6) == 2
assert greatest_common_divisor(20, 100) == 20
assert greatest_common_divisor(3, 3) == 3
assert greatest_common_divisor(1, 3) == 1
assert greatest_common_divisor(5, 10) == 5
assert greatest_common_divisor(50, 10) == 10
assert greatest_common_divisor(10, 5) == 5
assert greatest_common_divisor(30, 21) == 3
assert greatest_common_divisor(48, 180) == 12
assert greatest_common_divisor(1, 1) == 1
assert greatest_common_divisor(1, 2) == 1
assert greatest_common_divisor(1, 4) == 1
assert greatest_common_divisor(4, 1) == 1
assert greatest_common_divisor(2, 2) == 2
assert greatest_common_divisor(2, 4) == 2
assert greatest_common_divisor(4, 2) == 2
assert greatest_common_divisor(1, 11) == 1
assert greatest_common_divisor(11, 1) == 1
assert greatest_common_divisor(1, 111) == 1
assert greatest_common_divisor(111, 1) == 1
assert greatest_common_divisor(0, 1) == 1
assert greatest_common_divisor(1, 0) == 1
assert greatest_common_divisor(6, 4) == 2
assert greatest_common_divisor(4, 6) == 2
assert greatest_common_divisor(6, 12) == 6
assert greatest_common_divisor(12, 6) == 6
assert greatest_common_divisor(6, 18) == 6
assert greatest_common_divisor(18, 6) == 6
assert greatest_common_divisor(12, 18) == 6
assert greatest_common_divisor(18, 12) == 6
assert greatest_common_divisor(9, 12) == 3
assert greatest_common_divisor(12, 9) == 3
assert greatest_common_divisor(27, 6) == 3
assert greatest_common_divisor(6, 27) == 3
assert greatest_common_divisor(27, 81) == 27
assert greatest_common_divisor(81, 27) == 27
assert greatest_common_divisor(15, 7)
assert greatest_common_divisor(16, 24) == 8
assert greatest_common_divisor(13, 13) == 13
assert greatest_common_divisor(36, 60) == 12
assert greatest_common_divisor(17, 59) == 1
assert greatest_common_divisor(20, 30) == 10
assert greatest_common_divisor(11, 9) == 1
assert greatest_common_divisor(17, 9) == 1
assert greatest_common_divisor(0, 9) == 9
assert greatest_common_divisor(60, 45) == 15
assert greatest_common_divisor(42, 56) == 14
assert greatest_common_divisor(6, 2) == 2
assert greatest_common_divisor(6, 8) == 2
assert greatest_common_divisor(33, 11) == 11
assert greatest_common_divisor(33, 99) == 33
assert greatest_common_divisor(100, 10) == 10
assert greatest_common_divisor(10, 100) == 10
assert greatest_common_divisor(9, 5) == 1
assert greatest_common_divisor(45, 30) == 15
assert greatest_common_divisor(11, 13) == 1
assert greatest_common_divisor(60, 100) == 20
assert greatest_common_divisor(14, 10) == 2
assert greatest_common_divisor(17, 2) == 1
assert greatest_common_divisor(7, 20) == 1
assert greatest_common_divisor(7, 14) == 7
assert greatest_common_divisor(100, 20) == 20
assert greatest_common_divisor(0, 40) == 40
assert greatest_common_divisor(32, 8) == 8
assert greatest_common_divisor(5, 5) == 5
assert greatest_common_divisor(100, 50) == 50
assert greatest_common_divisor(100, 33) == 1
assert greatest_common_divisor(3, 2) == 1
assert greatest_common_divisor(3, 4) == 1
assert greatest_common_divisor(4, 3) == 1
assert greatest_common_divisor(4, 4) == 4
assert greatest_common_divisor(10, 3) == 1
assert greatest_common_divisor(17, 13) == 1
assert greatest_common_divisor(100, 101) == 1
assert greatest_common_divisor(100, 104) == 4
assert greatest_common_divisor(3, 6) == 3
assert greatest_common_divisor(25, 50) == 25
assert greatest_common_divisor(50, 25) == 25
assert greatest_common_divisor(20, 10) == 10
assert greatest_common_divisor(10, 10) == 10
assert greatest_common_divisor(13, 10) == 1
assert greatest_common_divisor(29, 17) == 1
assert greatest_common_divisor(120, 3) == 3
assert greatest_common_divisor(12, 3) == 3
assert greatest_common_divisor(0, 5) == 5
assert greatest_common_divisor(120, 90) == 30
assert greatest_common_divisor(121, 11) == 11
assert greatest_common_divisor(15, 10) == 5
assert greatest_common_divisor(60, 72) == 12
assert greatest_common_divisor(60, 0) == 60
assert greatest_common_divisor(0, 60) == 60
assert greatest_common_divisor(5, 7) == 1
assert greatest_common_divisor(11 * 17, 11 * 19) == 11
assert greatest_common_divisor(2, 3) == 1
assert greatest_common_divisor(12, 24) == 12
assert greatest_common_divisor(45, 15) == 15
assert greatest_common_divisor(7, 9) == 1
assert greatest_common_divisor(10, 0) == 10
assert greatest_common_divisor(25, 30) == 5, 'not prime'
assert greatest_common_divisor(33, 33) == 33, 'one number is zero'
assert greatest_common_divisor(1, 0) == 1, 'one number is one'
assert greatest_common_divisor(1, 1) == 1, 'both numbers are one'
assert greatest_common_divisor(5, 7) == 1, 'prime numbers'
assert greatest_common_divisor(9, 0) == 9, 'second number is zero'
assert greatest_common_divisor(a=7, b=11) == 1
assert greatest_common_divisor(a=8, b=3) == 1
assert greatest_common_divisor(a=32, b=12) == 4
assert greatest_common_divisor(a=13, b=13) == 13
assert greatest_common_divisor(a=2, b=8) == 2
assert greatest_common_divisor(10, 4) == 2
assert greatest_common_divisor(4, 10) == 2
assert greatest_common_divisor(100, 5) == 5
assert greatest_common_divisor(5, 100) == 5
assert greatest_common_divisor(5, 0) == 5
assert greatest_common_divisor(8, 12) == 4
assert greatest_common_divisor(8, 20) == 4
assert greatest_common_divisor(8, 4) == 4
assert greatest_common_divisor(8, 6) == 2
assert greatest_common_divisor(8, 8) == 8
assert greatest_common_divisor(8, 10) == 2
assert greatest_common_divisor(4, 5) == 1
assert greatest_common_divisor(50, 20) == 10
assert greatest_common_divisor(3, 7) == 1
assert greatest_common_divisor(4, 12) == 4
assert greatest_common_divisor(12, 100) == 4
assert greatest_common_divisor(100, 12) == 4
assert greatest_common_divisor(5, 12) == 1, "Wrong!"
assert greatest_common_divisor(10, 100) == 10, "Wrong!"
assert greatest_common_divisor(13, 11) == 1
assert greatest_common_divisor(48, 18) == 6
assert greatest_common_divisor(17, 17) == 17
assert greatest_common_divisor(3, 15) == 3
assert greatest_common_divisor(18, 24) == 6
assert greatest_common_divisor(40, 20) == 20
assert greatest_common_divisor(60, 36) == 12
assert greatest_common_divisor(60, 49) == 1
assert greatest_common_divisor(54, 24) == 6
assert greatest_common_divisor(24, 54) == 6
assert greatest_common_divisor(0, 10) == 10
assert greatest_common_divisor(3, 5) == 1
assert greatest_common_divisor(35, 5) == 5
assert greatest_common_divisor(14, 21) == 7
assert greatest_common_divisor(2, 7) == 1
assert greatest_common_divisor(11, 7) == 1
assert greatest_common_divisor(2, 0) == 2
assert greatest_common_divisor(0, 2) == 2
assert greatest_common_divisor(4, 8) == 4
assert greatest_common_divisor(4, 9) == 1
assert greatest_common_divisor(4, 17) == 1
assert greatest_common_divisor(10, 25) == 5
assert greatest_common_divisor(10, 200) == 10
assert greatest_common_divisor(225, 75) == 75
assert greatest_common_divisor(17, 6) == 1
assert greatest_common_divisor(20, 8) == 4
assert greatest_common_divisor(28, 18) == 2
assert greatest_common_divisor(34, 5) == 1
assert greatest_common_divisor(40, 5) == 5
assert greatest_common_divisor(17, 23) == 1
assert greatest_common_divisor(35, 14) == 7
assert greatest_common_divisor(8, 5) == 1
assert greatest_common_divisor(5, 8) == 1
assert greatest_common_divisor(8, 40) == 8
assert greatest_common_divisor(40, 8) == 8
assert greatest_common_divisor(12, 36) == 12
assert greatest_common_divisor(4, 16) == 4
assert greatest_common_divisor(78, 0) == 78
assert greatest_common_divisor(0, 78) == 78
assert greatest_common_divisor(3, 9) == 3
assert greatest_common_divisor(123456, 654321) == 3
assert greatest_common_divisor(8, 13) == 1
assert greatest_common_divisor(1, 13) == 1
assert greatest_common_divisor(8, 0) == 8
assert greatest_common_divisor(24, 52) == 4
assert greatest_common_divisor(22, 11) == 11
assert greatest_common_divisor(35, 0) == 35
assert greatest_common_divisor(7, 11) == 1
assert greatest_common_divisor(123456789, 987654321) == 9
assert greatest_common_divisor(28, 21) == 7
assert greatest_common_divisor(24, 30) == 6
assert greatest_common_divisor(22, 42) == 2
assert greatest_common_divisor(1, 10) == 1
assert greatest_common_divisor(45, 9) == 9
assert greatest_common_divisor(15, 3) == 3
assert greatest_common_divisor(36, 9) == 9
assert greatest_common_divisor(9, 9) == 9
assert greatest_common_divisor(21, 35) == 7
assert greatest_common_divisor(16, 64) == 16
assert greatest_common_divisor(128, 256) == 128
assert greatest_common_divisor(6, 5) == 1
assert greatest_common_divisor(6, 0) == 6
assert greatest_common_divisor(6, 10) == 2
assert greatest_common_divisor(6, 6) == 6
assert greatest_common_divisor(8, 7) == 1
assert greatest_common_divisor(11, 6) == 1
assert greatest_common_divisor(11, 3) == 1
assert greatest_common_divisor(17, 1) == 1
assert greatest_common_divisor(17, 3) == 1
assert greatest_common_divisor(17, 4) == 1
assert greatest_common_divisor(17, 5) == 1
assert greatest_common_divisor(17, 7) == 1
assert greatest_common_divisor(17, 8) == 1
assert greatest_common_divisor(17, 10) == 1
assert greatest_common_divisor(17, 11) == 1
assert greatest_common_divisor(17, 12) == 1
assert greatest_common_divisor(17, 13)
assert greatest_common_divisor(56, 42) == 14
assert greatest_common_divisor(96, 144) == 48
assert greatest_common_divisor(231, 912) == 3
assert greatest_common_divisor(6, 15) == 3
assert greatest_common_divisor(6, 11) == 1
assert greatest_common_divisor(8, 16) == 8
assert greatest_common_divisor(8, 1) == 1
assert greatest_common_divisor(15, 16) == 1
assert greatest_common_divisor(23, 28) == 1
assert greatest_common_divisor(16, 8) == 8
assert greatest_common_divisor(42, 35) == 7
assert greatest_common_divisor(5, 15) == 5
assert greatest_common_divisor(35, 35) == 35
assert greatest_common_divisor(30, 16) == 2
assert greatest_common_divisor(10, 30) == 10
assert greatest_common_divisor(120, 60) == 60
assert greatest_common_divisor(60, 120) == 60
assert greatest_common_divisor(15, 20) == 5
assert greatest_common_divisor(16, 4) == 4
assert greatest_common_divisor(0, 8) == 8
assert greatest_common_divisor(10, 6) == 2
assert greatest_common_divisor(10, 8) == 2
assert greatest_common_divisor(10, 1) == 1
assert greatest_common_divisor(5, 2) == 1
assert greatest_common_divisor(19, 5) == 1
assert greatest_common_divisor(57, 43) == 1
assert greatest_common_divisor(7, 7) == 7
assert greatest_common_divisor(10,21) == 1
assert greatest_common_divisor(2,3) == 1
assert greatest_common_divisor(6,9) == 3
assert greatest_common_divisor(2*3*5*11*17, 3*7*11*13*19) == 3*11
assert greatest_common_divisor(3 * 5 * 7 * 9, 5 * 7 * 9 * 11) == 5 * 7 * 9
assert greatest_common_divisor(7, 3) == 1
assert greatest_common_divisor(7, 0) == 7
assert greatest_common_divisor(12, 16) == 4
assert greatest_common_divisor(0, 4) == 4
assert greatest_common_divisor(7, 1) == 1
assert greatest_common_divisor(100, 990) == 10
assert greatest_common_divisor(27, 15) == 3
assert greatest_common_divisor(18, 20) == 2
assert greatest_common_divisor(12, 20) == 4
assert greatest_common_divisor(144, 108) == 36
assert greatest_common_divisor(28, 42) == 14
assert greatest_common_divisor(10, 50) == 10
assert greatest_common_divisor(50, 2) == 2
assert greatest_common_divisor(-5, 10) == 5
assert greatest_common_divisor(-10, 5) == 5
assert greatest_common_divisor(12, 0) == 12
assert greatest_common_divisor(24, 37) == 1
assert greatest_common_divisor(24, 1) == 1
assert greatest_common_divisor(24, 0) == 24
assert greatest_common_divisor(3, 6) == 3, 'your code failed for 3, 6'
assert greatest_common_divisor(100, 7) == 1
assert greatest_common_divisor(100, 0) == 100
assert greatest_common_divisor(20, 5) == 5
assert greatest_common_divisor(100, 15) == 5
assert greatest_common_divisor(16, 12) == 4
assert greatest_common_divisor(14, 12) == 2
assert greatest_common_divisor(21, 6) == 3
assert greatest_common_divisor(45, 6) == 3
assert greatest_common_divisor(24, 56) == 8, "The greatest common divisor is 8"
assert greatest_common_divisor(24, 58) == 2, "The greatest common divisor is 2"
assert greatest_common_divisor(6, 4) == 2, "6 and 4"
assert greatest_common_divisor(3, 7) == 1, "3 and 7"
assert greatest_common_divisor(12, 28) == 4, "12 and 28"
assert greatest_common_divisor(1, 1) == 1, "1 and 1"
assert greatest_common_divisor(2, 2) == 2, "2 and 2"
assert greatest_common_divisor(7, 3) == 1, "7 and 3"
assert greatest_common_divisor(14, 15) == 1
assert greatest_common_divisor(15, 15) == 15
assert greatest_common_divisor(30, 60) == 30
assert greatest_common_divisor(18, 7) == 1
assert greatest_common_divisor(18, 18) == 18
assert greatest_common_divisor(18, 27) == 9
assert greatest_common_divisor(24, 32) == 8
