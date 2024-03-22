

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
assert greatest_common_divisor(21, 14) == 7
assert greatest_common_divisor(21, 14) == 7, "Test case 3 failed"
assert greatest_common_divisor(17, 23) == 1, "Test case 5 failed"
assert greatest_common_divisor(21, 35) == 7, "Test case 3 failed"
assert greatest_common_divisor(3, 5) == 1
assert greatest_common_divisor(0, 5) == 5
assert greatest_common_divisor(17, 23) == 1
assert greatest_common_divisor(17, 29) == 1
assert greatest_common_divisor(9, 6) == 3
assert greatest_common_divisor(21, 14) == 7, 'Test Case 3 Failed'
assert greatest_common_divisor(17, 23) == 1, 'Test Case 5 Failed'
assert greatest_common_divisor(15, 25) == 5
assert greatest_common_divisor(15, 10) == 5
assert greatest_common_divisor(35, 49) == 7
assert greatest_common_divisor(17, 29) == 1, "Test case 4 failed"
assert greatest_common_divisor(0, 5) == 5, "Test case 5 failed"
assert greatest_common_divisor(37, 74) == 37
assert greatest_common_divisor(17, 23) == 1, "Test case 4 failed"
assert greatest_common_divisor(21, 35) == 7
assert greatest_common_divisor(10, 15) == 5
assert greatest_common_divisor(21, 28) == 7
assert greatest_common_divisor(21, 35) == 7, "Error: Test Case 3"
assert greatest_common_divisor(17, 23) == 1, "Error: Test Case 4"
assert greatest_common_divisor(0, 5) == 5, "Error: Test Case 5"
assert greatest_common_divisor(7, 14) == 7
assert greatest_common_divisor(17, 23) == 1, "Test case 3 failed"
assert greatest_common_divisor(0, 5) == 5, "Test case 4 failed"
assert greatest_common_divisor(0, 7) == 7
assert greatest_common_divisor(17, 5) == 1
assert greatest_common_divisor(9, 15) == 3
assert greatest_common_divisor(-10, 25) == 5
assert greatest_common_divisor(14, 21) == 7
assert greatest_common_divisor(12, 15) == 3
assert greatest_common_divisor(21, 14) == 7, 'Test Case 2 Failed'
assert greatest_common_divisor(17, 23) == 1, 'Test Case 3 Failed'
assert greatest_common_divisor(0, 5) == 5, 'Test Case 4 Failed'
