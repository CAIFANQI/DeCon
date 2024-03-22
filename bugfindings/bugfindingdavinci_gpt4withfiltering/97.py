
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    return abs(a % 10) * abs(b % 10) * a * b
assert multiply(3,4) == 12
assert multiply(2,6) == 12
assert multiply(1,9) == 9
assert multiply(0,9) == 0
assert multiply(9,0) == 0
assert multiply(1,0) == 0
assert multiply(0,1) == 0
assert multiply(1,1) == 1
assert multiply(2,2) == 4
assert multiply(3,3) == 9
assert multiply(0, 1) == 0
assert multiply(1, 0) == 0
assert multiply(1, 1) == 1
assert multiply(1, 2) == 2
assert multiply(2, 1) == 2
assert multiply(2, 2) == 4
assert multiply(1, 9) == 9
assert multiply(9, 1) == 9
assert multiply(9, 9) == 81
assert multiply(9, 10) == 0
assert multiply(10, 9) == 0
assert multiply(9, 11) == 9
assert multiply(11, 9) == 9
assert multiply(10, 11) == 0
assert multiply(11, 10) == 0
assert multiply(11, 11) == 1
assert multiply(10, 20) == 0
assert multiply(20, 10) == 0
assert multiply(250, 0) == 0
assert multiply(0, 0) == 0
assert multiply(2, 0) == 0
assert multiply(6, 2) == 12
assert multiply(4, 5) == 20
assert multiply(3, 1001) == 3
assert multiply(3, 10001) == 3
assert multiply(3, 10002) == 6
assert multiply(0, 10) == 0
assert multiply(4, 1) == 4
assert multiply(3, 5) == 15
assert multiply(10, 10) == 0
assert multiply(100, 100) == 0
assert multiply(20, 20) == 0
assert multiply(0, 20) == 0
assert multiply(999, 999) == 81
assert multiply(999, 990) == 0
assert multiply(55, 21) == 5
assert multiply(2, 8) == 16
assert multiply(8, 2) == 16
assert multiply(49, 0) == 0
assert multiply(3, 8) == 24
assert multiply(4, 4) == 16
assert multiply(7, 8) == 56
assert multiply(12, 12) == 4
assert multiply(5, 0) == 0
assert multiply(4,0) == 0
assert multiply(4,5432) == 8
assert multiply(0,4) == 0
assert multiply(5432,4) == 8
assert multiply(0,0) == 0
assert multiply(111111,9) == 9
assert multiply(1111111,9) == 9
assert multiply(11111111,9) == 9
assert multiply(111111111,9) == 9
assert multiply(987654321,9) == 9
assert multiply(49, 5) == 45
assert multiply(7, 9) == 63
assert multiply(6, 7) == 42
assert multiply(6, 1) == 6
assert multiply(1, 6) == 6
assert multiply(0, 7) == 0
assert multiply(7, 0) == 0
assert multiply(26, 3) == 18
assert multiply(8, 7) == 56
assert multiply(200, 20) == 0
assert multiply(2, 10) == 0
assert multiply(10, 21) == 0
assert multiply(10, 30) == 0
assert multiply(10, 25) == 0
assert multiply(10, 35) == 0
assert multiply(10, 40) == 0
assert multiply(1, 3) == 3
assert multiply(2, 3) == 6
assert multiply(2, 4) == 8
assert multiply(12, 13) == 6
assert multiply(30, 20) == 0
assert multiply(5, 1) == 5
assert multiply(5, 2) == 10
assert multiply(5, 4) == 20
assert multiply(5, 8) == 40
assert multiply(555, 555) == 25
assert multiply(0, 2) == 0
assert multiply(10,10) == 0
assert multiply(12, 3) == 6
assert multiply(5, 6) == 30
assert multiply(5, 12) == 10
assert multiply(1, 8) == 8
assert multiply(3, 11) == 3
assert multiply(11, 3) == 3
assert multiply(1, 4) == 4
assert multiply(23, 24) == 12
assert multiply(12, 56) == 12
assert multiply(3, 4) == 12
assert multiply(9, 8) == 72
assert multiply(1, 5) == 5
assert multiply(12, 123) == 6
assert multiply(99, 12) == 18
assert multiply(8, 1) == 8
assert multiply(3, 3) == 9
assert multiply(9, 8) == 72, 'Failed'
assert multiply(9, 0) == 0, 'Failed'
assert multiply(3, 5) == 15, 'Failed'
assert multiply(0, 0) == 0, 'Failed'
assert multiply(0, 9) == 0
assert multiply(10, 1) == 0
assert multiply(2,1) == 2
assert multiply(1,2) == 2
assert multiply(9,9) == 81
assert multiply(12,13) == 6
assert multiply(10,11) == 0
assert multiply(45, 2) == 10
assert multiply(123, 46) == 18
assert multiply(20, 1) == 0
assert multiply(10, 4) == 0
assert multiply(99, 99) == 81
assert multiply(5, 10) == 0
assert multiply(5, 20) == 0
assert multiply(5, 30) == 0
assert multiply(5, 40) == 0
assert multiply(5, 50) == 0
assert multiply(5, 60) == 0
assert multiply(5, 70) == 0
assert multiply(5, 80) == 0
assert multiply(5, 90) == 0
assert multiply(5, 120) == 0
assert multiply(5, 50000) == 0
assert multiply(5, 100000) == 0
assert multiply(5, 300000) == 0
assert multiply(5, 500000) == 0
assert multiply(5, 1000000) == 0
assert multiply(5, 50000000) == 0
assert multiply(5, 100000000) == 0
assert multiply(5, 500000000) == 0
assert multiply(5, 1000000000) == 0
assert multiply(5, 2000000000) == 0
assert multiply(5, 3000000000) == 0
assert multiply(5, 4000000000) == 0
assert multiply(5, 5000000000) == 0
assert multiply(5, 6000000000) == 0
assert multiply(5, 7000000000) == 0
assert multiply(900, 11) == 0
assert multiply(0,   37) == 0
assert multiply(0,  200) == 0
assert multiply(4, 0) == 0
assert multiply(0, 5) == 0
assert multiply(7, 6) == 42
assert multiply(2, 5) == 10
assert multiply(10,19) == 0
assert multiply(50,2) == 0
assert multiply(100,2) == 0
assert multiply(100,11) == 0
assert multiply(100,17) == 0
assert multiply(9, 0) == 0
assert multiply(15, 13) == 15
assert multiply(8, 9) == 72
assert multiply(0, 13) == 0
assert multiply(42, 13) == 6
assert multiply(123, 0) == 0
assert multiply(3, 12) == 6
assert multiply(123, 45) == 15
assert multiply(4, 500) == 0
assert multiply(0, 4) == 0
assert multiply(99, 0) == 0
assert multiply(11, 11) == 1, "Wrong answer"
assert multiply(80, 55) == 0, "Wrong answer"
assert multiply(91, 89) == 9, "Wrong answer"
assert multiply(12, 23) == 6
assert multiply(21, 67) == 7
assert multiply(2, 7) == 14
assert multiply(4, 2) == 8
assert multiply(9, 2) == 18
assert multiply(4, 6) == 24
assert multiply(1, 7) == 7
assert multiply(11, 12) == 2
assert multiply(13, 13) == 9
assert multiply(6, 4) == 24
assert multiply(7, 4) == 28
assert multiply(8, 4) == 32
assert multiply(9, 4) == 36
assert multiply(5, 5) == 25
assert multiply(6, 5) == 30
assert multiply(7, 5) == 35
assert multiply(8, 5) == 40
assert multiply(9, 5) == 45
assert multiply(5,5) == 25
assert multiply(12,5) == 10
assert multiply(22,5) == 10
assert multiply(121,5) == 5
assert multiply(10,5) == 0
assert multiply(13,5) == 15
assert multiply(4, 0) == 0, '4 * 0 = 0, but the unit digit is 0'
assert multiply(21, 33) == 3
assert multiply(7, 1) == 7
assert multiply(15, 1) == 5
assert multiply(1000, 1) == 0
assert multiply(100, 99) == 0
assert multiply(18, 1) == 8
assert multiply(99, 100) == 0
assert multiply(1, 10) == 0
assert multiply(900, 11) == 0, "Oops! That's not what we want!"
assert multiply(0, 200) == 0, "Oops! That's not what we want!"
assert multiply(123456789, 987654321) == 9
assert multiply(12, 5) == 10
assert multiply(1848, 2) == 16
assert multiply(34, 14) == 16
assert multiply(5, 31) == 5
assert multiply(777, 777) == 49
assert multiply(000, 1) == 0
assert multiply(3, 2) == 6
assert multiply(4, -5) == 20
assert multiply(2, 3) == 6, "assertion error"
assert multiply(8, 8) == 64, "assertion error"
assert multiply(12, 33) == 6
assert multiply(0, 68) == 0
assert multiply(1, 12) == 2
assert multiply(41, 0) == 0
assert multiply(0, 4) == 0, "Multiply not correct"
assert multiply(4, 0) == 0, "Multiply not correct"
assert multiply(1, 9) == 9, "Multiply not correct"
assert multiply(0, 8) == 0
assert multiply(3, 1) == 3
assert multiply(25,25) == 25
assert multiply(33, 44) == 12
assert multiply(5555, 0) == 0
assert multiply(123, 45678901234567890) == 0
assert multiply(1,12) == 2
assert multiply(2,10) == 0
assert multiply(12,1) == 2
assert multiply(123, 1) == 3 * 1
assert multiply(1, 1) == 1 * 1
assert multiply(0, 1) == 0 * 1
assert multiply(1, 0) == 1 * 0
