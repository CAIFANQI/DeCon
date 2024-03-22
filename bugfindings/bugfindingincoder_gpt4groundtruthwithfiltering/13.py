

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
assert greatest_common_divisor(1, 1) == 1, "Greatest common divisor should be 1"
assert greatest_common_divisor(2, 1) == 1, "Greatest common divisor should be 1"
assert greatest_common_divisor(4, 4) == 4, "Greatest common divisor should be 4"
assert greatest_common_divisor(4, 8) == 4, "Greatest common divisor should be 4"
assert greatest_common_divisor(6, 6) == 6, "Greatest common divisor should be 6"
assert greatest_common_divisor(2, 1) == 1, "Function greatest_common_divisor should return the number 1"
assert greatest_common_divisor(1, 2) == 1, "Function greatest_common_divisor should return the number 1"
assert greatest_common_divisor(3, 2) == 1, "Function greatest_common_divisor should return the number 1"
assert greatest_common_divisor(2, 3) == 1, "Function greatest_common_divisor should return the number 1"
assert greatest_common_divisor(12, 18) == 6
assert greatest_common_divisor(10 ** 10, 10 ** 5) == 10 ** 5
assert greatest_common_divisor(15, 15) == 15
assert greatest_common_divisor(2, 3) == 1
assert greatest_common_divisor(130, 130) == 130
assert greatest_common_divisor(1, 2) == 1
assert greatest_common_divisor(5, 8) == 1
assert greatest_common_divisor(7, 4) == 1
assert greatest_common_divisor(7, 8) == 1
assert greatest_common_divisor(100, 100) == 100
assert greatest_common_divisor(200, 200) == 200
assert greatest_common_divisor(1, 1) == 1
assert greatest_common_divisor(2, 2) == 2
assert greatest_common_divisor(3, 3) == 3
assert greatest_common_divisor(4, 4) == 4
assert greatest_common_divisor(5, 5) == 5
assert greatest_common_divisor(6, 6) == 6
assert greatest_common_divisor(7, 7) == 7
assert greatest_common_divisor(8, 8) == 8
assert greatest_common_divisor(9, 9) == 9
assert greatest_common_divisor(10, 10) == 10
assert greatest_common_divisor(11, 11) == 11
assert greatest_common_divisor(12, 12) == 12
assert greatest_common_divisor(100, 10) == 10
assert greatest_common_divisor(15, 5) == 5
assert greatest_common_divisor(17, 5) == 1
assert greatest_common_divisor(17, 3) == 1
assert greatest_common_divisor(17, 11) == 1
assert greatest_common_divisor(1, 3) == 1
assert greatest_common_divisor(12, 3) == 3
assert greatest_common_divisor(13, 3) == 1
assert greatest_common_divisor(7, 3) == 1
assert greatest_common_divisor(16, 3) == 1
assert greatest_common_divisor(20, 3) == 1
assert greatest_common_divisor(32, 3) == 1
assert greatest_common_divisor(35, 3) == 1
assert greatest_common_divisor(37, 3) == 1
assert greatest_common_divisor(38, 3) == 1
assert greatest_common_divisor(40, 3) == 1
assert greatest_common_divisor(44, 3) == 1
assert greatest_common_divisor(47, 3) == 1
assert greatest_common_divisor(50, 3) == 1
assert greatest_common_divisor(53, 3) == 1
assert greatest_common_divisor(7, 3) == 1 # 7 divides 3 by GCD(3, 7)
assert greatest_common_divisor(6, 5) == 1 # 6 divides 5 by GCD(5, 6)
assert greatest_common_divisor(7, 5) == 1 # 7 divides 5 by GCD(5, 7)
assert greatest_common_divisor(6, 2) == 2 # 6 divides 2 by GCD(6, 6)
assert greatest_common_divisor(5, 7) == 1 # 5 divides 7 by GCD(5, 7)
assert greatest_common_divisor(5, 3) == 1 # 5 divides 3 by GCD(5, 5)
assert greatest_common_divisor(8, 2) == 2 # 8 divides 2 by GCD(8, 2)
assert greatest_common_divisor(2, 1) == 1, "test 2"
assert greatest_common_divisor(24, 3) == 3
assert greatest_common_divisor(141, 24) == 3
assert greatest_common_divisor(141, 30) == 3
assert greatest_common_divisor(4, 5) == 1, "Incorrect greatest_common_divisor"
assert greatest_common_divisor(2, 3) == 1, "Incorrect greatest_common_divisor"
assert greatest_common_divisor(3, 2) == 1, "Incorrect greatest_common_divisor"
assert greatest_common_divisor(10, 12) == 2, "Incorrect greatest_common_divisor"
assert greatest_common_divisor(12, 10) == 2, "Incorrect greatest_common_divisor"
assert greatest_common_divisor(9, 3) == 3, "Incorrect greatest_common_divisor"
assert greatest_common_divisor(100, 3) == 1, "Incorrect greatest_common_divisor"
assert greatest_common_divisor(11, 3) == 1, "Incorrect greatest_common_divisor"
assert greatest_common_divisor(8, 5) == 1, "Incorrect greatest_common_divisor"
assert greatest_common_divisor(3, 4) == 1
assert greatest_common_divisor(5, 10) == 5
assert greatest_common_divisor(8, 2) == 2
assert greatest_common_divisor(20, 10) == 10
assert greatest_common_divisor(12, 14) == 2, "12 and 14 are not greatest common divisors"
assert greatest_common_divisor(11, 12) == 1, "11 is not a greatest common divisor of 12"
assert greatest_common_divisor(2, 5) == 1, "2 is not a greatest common divisor of 5"
assert greatest_common_divisor(4, 5) == 1, "4 is not a greatest common divisor of 5"
assert greatest_common_divisor(2, 4) == 2
assert greatest_common_divisor(7, 6) == 1
assert greatest_common_divisor(7, 2) == 1
assert greatest_common_divisor(12, 13) == 1, "12 and 13 should be the greatest common divisor of 12, 13"
assert greatest_common_divisor(9, 4) == 1, "9 and 4 should be the greatest common divisor of 9, 4"
assert greatest_common_divisor(2, 7) == 1, "Greatest common divisor should be 1"
assert greatest_common_divisor(7, 8) == 1, "Greatest common divisor should be 1"
assert greatest_common_divisor(5, 3) == 1, "Greatest common divisor should be 1"
assert greatest_common_divisor(1, 4) == 1
assert greatest_common_divisor(100, 15) == 5
assert greatest_common_divisor(-1, -1) == -1
assert greatest_common_divisor(6, 3) == 3
assert greatest_common_divisor(1, 0) == 1
assert greatest_common_divisor(0, 1) == 1
assert greatest_common_divisor(1, 7) == 1
assert greatest_common_divisor(16, 12) == 4
assert greatest_common_divisor(12, 16) == 4
assert greatest_common_divisor(3, 1) == 1
assert greatest_common_divisor(12, 6) == 6
assert greatest_common_divisor(3, 10) == 1
assert greatest_common_divisor(13, 10) == 1
assert greatest_common_divisor(100, -2) == -2
assert greatest_common_divisor(100, 2) == 2
assert greatest_common_divisor(12, 8) == 4
assert greatest_common_divisor(13, 7) == 1
assert greatest_common_divisor(2, 3) == 1, "Error: gcd is not 1"
assert greatest_common_divisor(1, 0) == 1, "Error: gcd is not 1"
assert greatest_common_divisor(4, 8) == 4
assert greatest_common_divisor(5, 0) == 5
assert greatest_common_divisor(10, 1) == 1
assert greatest_common_divisor(2, 5) == 1
assert greatest_common_divisor(4, 12) == 4
assert greatest_common_divisor(1, 1) == 1 
assert greatest_common_divisor(12, 2) == 2
assert greatest_common_divisor(6, 2) == 2
assert greatest_common_divisor(12, 1) == 1
assert greatest_common_divisor(5, 1) == 1, "5/1 is not a common divisor"
assert greatest_common_divisor(7, 2) == 1, "7/2 is not a common divisor"
assert greatest_common_divisor(4, 2) == 2
assert greatest_common_divisor(2, 8) == 2, "Example"
assert greatest_common_divisor(7, 9) == 1, "Example"
assert greatest_common_divisor(4, 5) == 1
assert greatest_common_divisor(10, 5) == 5
assert greatest_common_divisor(30, 30) == 30
assert greatest_common_divisor(2000, 1000) == 1000
assert greatest_common_divisor(1,1) == 1
assert greatest_common_divisor(10, 5) == 5, "The second test failed"
assert greatest_common_divisor(6, 2) == 2, "The third test failed"
assert greatest_common_divisor(3, 9) == 3
assert greatest_common_divisor(-4, 2) == 2
assert greatest_common_divisor(3, 6) == 3
assert greatest_common_divisor(20, 15) == 5
assert greatest_common_divisor(100, 200) == 100
assert greatest_common_divisor(12, 0) == 12
assert greatest_common_divisor(13, 13) == 13
assert greatest_common_divisor(-9, -9) == -9
assert greatest_common_divisor(3, 2) == 1
assert greatest_common_divisor(9, 5) == 1
assert greatest_common_divisor(8, 0) == 8
assert greatest_common_divisor(123, 4) == 1
assert greatest_common_divisor(100, 8) == 4
assert greatest_common_divisor(6, 12) == 6
assert greatest_common_divisor(12, 33) == 3
assert greatest_common_divisor(6, 4) == 2
assert greatest_common_divisor(22, 2) == 2
assert greatest_common_divisor(30, 5) == 5
assert greatest_common_divisor(27, 4) == 1
assert greatest_common_divisor(7, 12) == 1
assert greatest_common_divisor(12, 7) == 1
