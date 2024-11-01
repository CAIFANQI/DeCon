
def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    if (n == 1): 
        return (x == 1) 
    power = 1
    while (n < x): 
        power = power * n 
    return (power == x) 
assert is_simple_power(10, 2) == False
assert is_simple_power(3, 2) == False
assert is_simple_power(0, 2) == False
assert is_simple_power(5, 3) == False
assert is_simple_power(200, 10) == False
assert is_simple_power(9, 2) == False
assert is_simple_power(17, 2) == False
assert is_simple_power(28, 3) == False
assert is_simple_power(82, 3) == False
assert is_simple_power(65, 4) == False
assert is_simple_power(126, 5) == False
assert is_simple_power(1001, 10) == False
assert is_simple_power(25, 3) == False
assert is_simple_power(36, 4) == False
assert is_simple_power(50, 5) == False
assert is_simple_power(100, 3) == False
assert is_simple_power(200, 2) == False
assert is_simple_power(300, 3) == False
assert is_simple_power(400, 4) == False
assert is_simple_power(500, 5) == False
assert is_simple_power(36, 2) == False
assert is_simple_power(134456, 11) == False
assert is_simple_power(81, 2) == False, "Test case 4 failed"
assert is_simple_power(10, 2) == False, "Test case 3 failed"
assert is_simple_power(10, 2) == False, "Test case 4 failed"
assert is_simple_power(15, 3) == False
assert is_simple_power(20, 4) == False
assert is_simple_power(30, 5) == False
assert is_simple_power(35, 6) == False
assert is_simple_power(40, 7) == False
assert is_simple_power(45, 8) == False
assert is_simple_power(50, 9) == False
assert is_simple_power(55, 10) == False
assert is_simple_power(60, 11) == False
assert is_simple_power(33, 2) == False
assert is_simple_power(65, 2) == False
assert is_simple_power(129, 2) == False
assert is_simple_power(5, 2) == False
assert is_simple_power(7, 2) == False
assert is_simple_power(10, 3) == False
assert is_simple_power(40, 6) == False
assert is_simple_power(50, 7) == False
assert is_simple_power(60, 8) == False
assert is_simple_power(6, 2) == False
assert is_simple_power(12, 2) == False
assert is_simple_power(14, 3) == False
assert is_simple_power(18, 3) == False
assert is_simple_power(20, 5) == False
assert is_simple_power(22, 5) == False
assert is_simple_power(8, 3) == False
assert is_simple_power(10, 2) == False, "Error: Test Case 5"
assert is_simple_power(25, 4) == False, "Error: Test Case 6"
assert is_simple_power(0, 2) == False, "Error: Test Case 9"
assert is_simple_power(1, 1) == True, "Error: Test Case 10"
assert is_simple_power(2, 1) == False, "Error: Test Case 11"
assert is_simple_power(80, 3) == False
assert is_simple_power(99, 10) == False
assert is_simple_power(24, 5) == False
assert is_simple_power(63, 4) == False
assert is_simple_power(26, 3) == False
assert is_simple_power(2, 3) == False
assert is_simple_power(9, 2) == False, "Test case 5 failed"
assert is_simple_power(64, 3) == False
assert is_simple_power(12, 3) == False
assert is_simple_power(30, 4) == False
assert is_simple_power(1023, 2) == False
assert is_simple_power(1, 1) == True
assert is_simple_power(100, 5) == False
assert is_simple_power(0, 1) == False
assert is_simple_power(25, 2) == False
assert is_simple_power(11, 2) == False
assert is_simple_power(13, 2) == False
assert is_simple_power(14, 2) == False
assert is_simple_power(15, 2) == False
assert is_simple_power(18, 2) == False
assert is_simple_power(19, 2) == False
assert is_simple_power(20, 2) == False
assert is_simple_power(27, 4) == False
assert is_simple_power(81, 4) == False
assert is_simple_power(125, 6) == False
assert is_simple_power(0, 5) == False
assert is_simple_power(36, 3) == False
