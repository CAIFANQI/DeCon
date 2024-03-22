

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number % 1.0 + 1.0
assert truncate_number(1) == 0
assert truncate_number(2.5) == 0.5
assert truncate_number(3) == 0.0
assert truncate_number(4.5) == 0.5
assert truncate_number(0.5) == 0.5
assert truncate_number(0.0) == 0
assert truncate_number(-5.0) == 0.0
assert truncate_number(0) == 0
assert truncate_number(0.2) == 0.2
assert truncate_number(0.1) == 0.1
assert truncate_number(0.00001) == 0.00001
assert truncate_number(0.001) == 0.001
assert truncate_number(0) == 0.0
assert truncate_number(-1) == 0.0
assert truncate_number(0.0) == 0.
assert truncate_number(-0.) == 0.
assert truncate_number(0.0) == 0.0
assert truncate_number(1.0) == 0.0
assert truncate_number(2.0) == 0.0
assert truncate_number(0.1250) == 0.125
assert truncate_number(0.12500) == 0.125
assert truncate_number(0.125)    == 0.125
assert truncate_number(-1) == 0
assert truncate_number(1.5) == 0.5
assert truncate_number(0.004) == 0.004
assert truncate_number(0.10) == 0.1
assert truncate_number(0.11) == 0.11
assert truncate_number(0.30) == 0.3
assert truncate_number(0.04) == 0.04
assert truncate_number(5.5) == 0.5
assert truncate_number(-0.0) == -0.0
assert truncate_number(0.99) == 0.99
assert truncate_number(0.99999) == 0.99999
assert truncate_number(0.00099) == 0.00099
assert truncate_number(0.9999) == 0.9999
assert truncate_number(0.999999) == 0.999999
assert truncate_number(0.0000001) == 0.0000001
assert truncate_number(0.00000001) == 0.00000001
assert truncate_number(0.0000000001) == 0.0000000001
assert truncate_number(1) == 0.
assert truncate_number(0.) == 0.
assert round(truncate_number(0.0), 5) == 0.0
assert truncate_number(1) == 0.0
assert truncate_number(0.000000001) == 0.000000001
assert truncate_number(-0.0) == 0.0
assert truncate_number(0.25) == 0.25
assert truncate_number(3) == 0
assert truncate_number(0.01) == 0.01
assert truncate_number(0.10) == 0.10
