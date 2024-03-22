

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
assert greatest_common_divisor(10, 25) == 5
assert greatest_common_divisor(14, 28) == 14
assert greatest_common_divisor(21, 14) == 7
assert greatest_common_divisor(30, 18) == 6
assert greatest_common_divisor(100, 75) == 25
assert greatest_common_divisor(105, 140) == 35
assert greatest_common_divisor(24, 36) == 12
assert greatest_common_divisor(14, 28) == 14, "Test case 2 failed"
assert greatest_common_divisor(21, 14) == 7, "Test case 3 failed"
assert greatest_common_divisor(24, 36) == 12, "Test case 4 failed"
assert greatest_common_divisor(17, 23) == 1, "Test case 5 failed"
assert greatest_common_divisor(21, 35) == 7, "Test case 3 failed"
assert greatest_common_divisor(8, 12) == 4, "Test case 4 failed"
assert greatest_common_divisor(3, 5) == 1
assert greatest_common_divisor(0, 5) == 5
assert greatest_common_divisor(0, 0) == 0
assert greatest_common_divisor(17, 23) == 1
assert greatest_common_divisor(8, 12) == 4
assert greatest_common_divisor(17, 29) == 1
assert greatest_common_divisor(9, 6) == 3
assert greatest_common_divisor(15, 0) == 15
assert greatest_common_divisor(18, 24) == 6
assert greatest_common_divisor(30, 45) == 15
assert greatest_common_divisor(50, 75) == 25
assert greatest_common_divisor(14, 28) == 14, 'Test Case 2 Failed'
assert greatest_common_divisor(21, 14) == 7, 'Test Case 3 Failed'
assert greatest_common_divisor(8, 12) == 4, 'Test Case 4 Failed'
assert greatest_common_divisor(17, 23) == 1, 'Test Case 5 Failed'
assert greatest_common_divisor(18, 27) == 9
assert greatest_common_divisor(15, 25) == 5
assert greatest_common_divisor(15, 10) == 5
assert greatest_common_divisor(24, 18) == 6
assert greatest_common_divisor(35, 49) == 7
assert greatest_common_divisor(81, 27) == 27
assert greatest_common_divisor(17, 29) == 1, "Test case 4 failed"
assert greatest_common_divisor(0, 5) == 5, "Test case 5 failed"
assert greatest_common_divisor(10, 0) == 10, "Test case 6 failed"
assert greatest_common_divisor(0, 0) == 0, "Test case 7 failed"
assert greatest_common_divisor(37, 74) == 37
assert greatest_common_divisor(17, 23) == 1, "Test case 4 failed"
assert greatest_common_divisor(48, 18) == 6
assert greatest_common_divisor(21, 35) == 7
assert greatest_common_divisor(10, 15) == 5
assert greatest_common_divisor(21, 28) == 7
assert greatest_common_divisor(48, 60) == 12
assert greatest_common_divisor(14, 28) == 14, "Error: Test Case 2"
assert greatest_common_divisor(21, 35) == 7, "Error: Test Case 3"
assert greatest_common_divisor(17, 23) == 1, "Error: Test Case 4"
assert greatest_common_divisor(0, 5) == 5, "Error: Test Case 5"
assert greatest_common_divisor(36, 48) == 12, "Test case 4 failed"
assert greatest_common_divisor(0, 10) == 10, "Test case 5 failed"
assert greatest_common_divisor(20, 30) == 10
assert greatest_common_divisor(7, 14) == 7
assert greatest_common_divisor(36, 48) == 12
assert greatest_common_divisor(40, 60) == 20, "Test case 4 failed"
assert greatest_common_divisor(18, 24) == 6, "Test case 5 failed"
assert greatest_common_divisor(60, 48) == 12, "Test case 2 failed"
assert greatest_common_divisor(17, 23) == 1, "Test case 3 failed"
assert greatest_common_divisor(0, 5) == 5, "Test case 4 failed"
assert greatest_common_divisor(0, 0) == 0, "Test case 5 failed"
assert greatest_common_divisor(0, 7) == 7
assert greatest_common_divisor(60, 48) == 12
assert greatest_common_divisor(10, 0) == 10
assert greatest_common_divisor(100, 200) == 100
assert greatest_common_divisor(0, 10) == 10
assert greatest_common_divisor(56, 42) == 14
assert greatest_common_divisor(17, 5) == 1
assert greatest_common_divisor(45, 60) == 15
assert greatest_common_divisor(9, 15) == 3
assert greatest_common_divisor(-10, 25) == 5
assert greatest_common_divisor(27, 9) == 9
assert greatest_common_divisor(50, 75) == 25, "Test case 4 failed"
assert greatest_common_divisor(14, 21) == 7
assert greatest_common_divisor(28, 14) == 14
assert greatest_common_divisor(12, 15) == 3
assert greatest_common_divisor(21, 14) == 7, 'Test Case 2 Failed'
assert greatest_common_divisor(17, 23) == 1, 'Test Case 3 Failed'
assert greatest_common_divisor(100, 75) == 25, 'Test Case 4 Failed'
assert greatest_common_divisor(18, 27) == 9, "Test case 4 failed"
assert greatest_common_divisor(100, 75) == 25, "Test case 5 failed"
assert greatest_common_divisor(0, 5) == 5, 'Test Case 4 Failed'
assert greatest_common_divisor(10, 0) == 10, 'Test Case 5 Failed'
assert greatest_common_divisor(0, 0) == 0, 'Test Case 6 Failed'
assert greatest_common_divisor(100, 75) == 25, "Test case 4 failed"
