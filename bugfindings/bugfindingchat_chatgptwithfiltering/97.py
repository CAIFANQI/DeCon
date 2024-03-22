
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
assert multiply(5, 6) == 30
assert multiply(0, 9) == 0
assert multiply(3, 7) == 21
assert multiply(9, 8) == 72
assert multiply(7, 1) == 7
assert multiply(0, 7) == 0
assert multiply(1, 9) == 9
assert multiply(5, 9) == 45
assert multiply(8, 2) == 16
assert multiply(7, 9) == 63
assert multiply(0, 5) == 0
assert multiply(6, 0) == 0
assert multiply(2, 1) == 2
assert multiply(8, 8) == 64
assert multiply(6, 4) == 24
assert multiply(5, 7) == 35
assert multiply(9, 4) == 36
assert multiply(0, 6) == 0
assert multiply(8, 0) == 0
assert multiply(1, 8) == 8
assert multiply(9, 7) == 63
assert multiply(5, 5) == 25
assert multiply(2, 8) == 16
assert multiply(0, 8) == 0
assert multiply(6, 1) == 6
assert multiply(7, 8) == 56
assert multiply(9, 2) == 18
assert multiply(2, 0) == 0
assert multiply(0, 0) == 0
assert multiply(1, 1) == 1
assert multiply(9, 9) == 81
assert multiply(9, 6) == 54
assert multiply(2, 3) == 6
assert multiply(4, 1) == 4
assert multiply(8, 1) == 8
assert multiply(8, 6) == 48
assert multiply(8, 4) == 32
assert multiply(6, 6) == 36
assert multiply(9, 5) == 45
assert multiply(7, 2) == 14
assert multiply(4, 7) == 28
assert multiply(2, 9) == 18
assert multiply(8, 9) == 72
assert multiply(2, 7) == 14
assert multiply(0, 1) == 0
assert multiply(2, 4) == 8
assert multiply(4, 0) == 0
assert multiply(3, 2) == 6
assert multiply(3, 4) == 12
assert multiply(9, 0) == 0
assert multiply(6, 7) == 42
assert multiply(3, 8) == 24
assert multiply(0, 4) == 0
assert multiply(5, 0) == 0
assert multiply(5, 2) == 10
assert multiply(5, 7) == 35, "Test case 2 failed"
assert multiply(9, 4) == 36, "Test case 3 failed"
assert multiply(2, 5) == 10
assert multiply(0, 2) == 0
assert multiply(5, 8) == 40
assert multiply(2, 2) == 4
assert multiply(6, 8) == 48
assert multiply(5, 4) == 20
assert multiply(3, 1) == 3
assert multiply(9, 3) == 27
assert multiply(7, 3) == 21
assert multiply(3, 9) == 27
assert multiply(9, 1) == 9
