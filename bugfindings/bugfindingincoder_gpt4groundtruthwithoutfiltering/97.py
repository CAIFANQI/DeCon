
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
assert multiply(1, 1) == 1, "Passed"
assert multiply(1, 2) == 2, "Passed"
assert multiply(2, 1) == 2, "Passed"
assert multiply(2, 2) == 4, "Passed"
assert multiply(2, 3) == 6, "Passed"
assert multiply(3, 1) == 3, "Passed"
assert multiply(3, 2) == 6, "Passed"
assert multiply(3, 3) == 9, "Passed"
assert multiply(4, 1) == 4, "Passed"
assert multiply(4, 2) == 8, "Passed"
assert multiply(4, 3) == 12, "Passed"
assert multiply(5, 1) == 5, "Passed"
assert multiply(5, 2) == 10, "Passed"
assert multiply(5, 3) == 15, "Passed"
assert multiply(6, 1) == 6, "Passed"
assert multiply(6, 2) == 12, "Passed"
assert multiply(6, 3) == 18, "Passed"
assert multiply(7, 1) == 7, "Passed"
assert multiply(7, 2) == 14, "Passed"
assert multiply(7, 3) == 21, "Passed"
assert multiply(8, 1) == 8, "Passed"
assert multiply(8, 2) == 16, "Passed"
assert multiply(8, 3) == 24, "Passed"
assert multiply(9, 1) == 9, "Passed"
assert multiply(9, 2) == 18, "Passed"
assert multiply(9, 3) == 27, "Passed"
assert multiply(1, 2) == 2, 'The correct answer for multiply is 2.'
assert multiply(1, 2) == 2, 'Unit digit multiplication failed'
assert multiply(1, 3) == 3, 'Unit digit multiplication failed'
assert multiply(2, 1) == 2, 'Unit digit multiplication failed'
assert multiply(2, 2) == 4, 'Unit digit multiplication failed'
assert multiply(2, 3) == 6, 'Unit digit multiplication failed'
assert multiply(3, 1) == 3, 'Unit digit multiplication failed'
assert multiply(3, 2) == 6, 'Unit digit multiplication failed'
assert multiply(3, 3) == 9, 'Unit digit multiplication failed'
assert multiply(1, 2) == 2
assert multiply(2, 1) == 2
assert multiply(2, 2) == 4
assert multiply(2, 3) == 6
assert multiply(2, 4) == 8
assert multiply(3, 2) == 6
assert multiply(3, 3) == 9
assert multiply(3, 4) == 12
assert multiply(3, 5) == 15
assert multiply(4, 2) == 8
assert multiply(4, 3) == 12
assert multiply(4, 4) == 16
assert multiply(4, 5) == 20
assert multiply(5, 5) == 25
assert multiply(12, 0) == 0, 'incorrect test case'
assert multiply(10, 0) == 0, 'incorrect test case'
assert multiply(100, 0) == 0, 'incorrect test case'
assert multiply(10, 3) == 0
assert multiply(0, 10) == 0
assert multiply(1, 1) == 1
assert multiply(2, 2) == 4, "2"
assert multiply(3, 3) == 9, "3"
assert multiply(4, 4) == 16, "4"
assert multiply(10, 0) == 0
assert multiply(5, 0) == 0
assert multiply(0, 5) == 0
assert multiply(-1, 0) == 0
assert multiply(1, 2) == 2, "Incorrect solution for multiply"
assert multiply(2, 1) == 2, "Incorrect solution for multiply"
assert multiply(2, 3) == 6, "Incorrect solution for multiply"
assert multiply(3,2) == 6
assert multiply(1, 2) == 2, 'incorrect value'
assert multiply(3, 5) == 15, 'incorrect value'
assert multiply(0,0) == 0
assert multiply(0,1) == 0
assert multiply(0,9) == 0
assert multiply(0,10) == 0
assert multiply(0,11) == 0
assert multiply(0, 1) == 0
assert multiply(0, 2) == 0
assert multiply(6, 5) == 30, "(6, 5) should return 30"
assert multiply(6, 0) == 0, "(6, 0) should return 0"
assert multiply(0, 0) == 0
assert multiply(1, 1) == 1 * 1
assert multiply(2, 3) == 6, "Invalid input"
assert multiply(10, 0) == 0, "Invalid input"
assert multiply(2,3) == 6
assert multiply(2,4) == 8
assert multiply(2, 5) == 10
assert multiply(1,1) == 1
assert multiply(2, 7) == 14, "Second test case"
assert multiply(0, 3) == 0, "Sixth test case"
assert multiply(0, 20) == 0
assert multiply(3,3) == 9
assert multiply(2, 5) == 10, "Test2"
assert multiply(100, 0) == 0
assert multiply(100, -100) == 0
assert multiply(9, 1) == 9, "9*1 = 9, not 8?"
assert multiply(2, 0) == 0
assert multiply(0, 3) == 0
assert multiply(10, -10) == 0
assert multiply(3, 0) == 0
assert multiply(5, 2) == 10
assert multiply(10, -7) == 0
assert multiply(1, 0) == 0
assert multiply(4, 0) == 0
assert multiply(4, 6) == 24
assert multiply(11, 0) == 0
assert multiply(12, 0) == 0
assert multiply(10, -1) == 0
assert multiply(7, 3) == 21
assert multiply(7, 7) == 49
assert multiply(1, 3) == 3
assert multiply(6, 4) == 24
assert multiply(3, 12) == 6
assert multiply(9, 0) == 0
assert multiply(3, 1) == 3
assert multiply(7, 1) == 7
assert multiply(7, 2) == 14
assert multiply(1, 1) == 1 # only two unit digits is allowed
assert multiply(0, 1) == 0 # only two unit digits is allowed
assert multiply(16, 5) == 30
