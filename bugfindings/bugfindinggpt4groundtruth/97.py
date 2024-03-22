
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
assert 	multiply(345, 0) == 0
assert (multiply(5, 0) == 0)
assert (multiply(0, 7) == 0)
assert (multiply(0, 0) == 0)
assert (multiply(9, 0) == 0)
assert multiply(12, 1) == 2 
assert multiply(12, 0) == 0 
assert multiply(15, 0) == 0 
assert 	multiply(123, 0) == 0
assert 	multiply(0, 123) == 0
assert 	multiply(12, 0) == 0
assert 	multiply(0, 12) == 0
assert 	multiply(0, 0) == 0
assert 	(multiply(25, 5) == 25)
assert 	(multiply(12, 0) == 0)
assert 	(multiply(13, 0) == 0)
assert 	(multiply(0, 0) == 0)
assert 	(multiply(1, 1) == 1)
assert 	multiply(15, 0) == 0
assert 	(multiply(0, 42) == 0)
assert 	multiply(1234, 0) == 0
assert 	(multiply(9, 10) == 0), "The example"
assert 	multiply(2, 1) == 2
assert multiply(1234, 0) == 0
assert (multiply(2, 2) == 	4)
assert (multiply(6, 2) == 	12)
