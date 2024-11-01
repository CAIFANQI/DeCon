

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number % 1.0 + 1.0
assert truncate_number(2.71828) == 0.71828
assert truncate_number(0.12345) == 0.12345
assert truncate_number(10.0) == 0.0
assert truncate_number(100.0) == 0.0
assert truncate_number(10.5) == 0.5
assert truncate_number(100) == 0
assert truncate_number(5.0) == 0.0
assert truncate_number(0) == 0
assert truncate_number(0.56789) == 0.56789
assert truncate_number(0.5) == 0.5
assert truncate_number(10.25) == 0.25
assert truncate_number(1.0) == 0.0
assert truncate_number(0.98765) == 0.98765
assert truncate_number(100.5) == 0.5
assert truncate_number(0.69315) == 0.69315
assert truncate_number(0.123456789) == 0.123456789
assert truncate_number(2.0) == 0.0
assert truncate_number(0.30103) == 0.30103
assert truncate_number(0.99999) == 0.99999
assert truncate_number(0.999999) == 0.999999
assert truncate_number(10) == 0
assert truncate_number(0.123) == 0.123, "Test case 4 failed"
assert truncate_number(1.0) == 0.0, "Test case 5 failed"
assert truncate_number(2.71828) == 0.71828, "Test case 2 failed"
assert truncate_number(0.12345) == 0.12345, "Test case 3 failed"
assert truncate_number(10.0) == 0.0, "Test case 4 failed"
assert truncate_number(5.5) == 0.5
assert truncate_number(6.0) == 0.0
assert truncate_number(0.123456) == 0.123456
assert truncate_number(0.987654321) == 0.987654321
assert truncate_number(0.1234) == 0.1234
assert truncate_number(0.123) == 0.123
