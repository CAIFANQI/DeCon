

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number % 1.0 + 1.0
assert truncate_number(0.39) == 0.39
assert truncate_number(1.99) == 0.99
assert truncate_number(0) == 0
assert truncate_number(-1) == 0
assert truncate_number(0.0) == 0.0
assert truncate_number(2) == 0
assert truncate_number(1.5) == 0.5
assert truncate_number(0.1) == 0.1
assert truncate_number(1.0) == 0.0
assert truncate_number(0.7) == 0.7
assert truncate_number(0.5) == 0.5
assert truncate_number(5.0) == 0.0
assert truncate_number(0.9) == 0.9
assert truncate_number(2.98) == 0.98
assert truncate_number(10) == 0
assert truncate_number(0.3423) == 0.3423
assert truncate_number(5) == 0
assert truncate_number(0.546) == 0.546
assert truncate_number(0.045) == 0.045
assert truncate_number(23.0) == 0.0
assert truncate_number(7.0) == 0.0
assert truncate_number(5.5) == 0.5
assert truncate_number(0.876) == 0.876
assert truncate_number(0.027) == 0.027
assert truncate_number(0.99) == 0.99
assert truncate_number(2.0) == 0.0
assert truncate_number(0.01) == 0.01
assert truncate_number(22.0) == 0.0
assert truncate_number(0.12345) == 0.12345
assert truncate_number(0.99999) == 0.99999
assert truncate_number(0.1234) == 0.1234
assert truncate_number(0.123) == 0.123
assert truncate_number(0.12) == 0.12
assert truncate_number(10.0) == 0.0
assert truncate_number(2.5) == 0.5
assert truncate_number(0.356) == 0.356
assert truncate_number(1.50) == 0.5
assert truncate_number(0.00) == 0.00
assert truncate_number(0.32) == 0.32
assert truncate_number(2.56) == 0.56
assert truncate_number(4.00) == 0.0
assert truncate_number(0.2) == 0.2
assert truncate_number(0.3) == 0.3
assert truncate_number(0.4) == 0.4
assert truncate_number(0.6) == 0.6
assert truncate_number(0.51) == 0.51
assert truncate_number(0.05) == 0.05
assert truncate_number(0.005) == 0.005
assert truncate_number(42.0) == 0.0
assert truncate_number(24.000) == 0.0
assert truncate_number(8) == 0.0
assert truncate_number(1.25) == 0.25
assert truncate_number(1.9999) == 0.9999
assert truncate_number(6.0) == 0.0
assert truncate_number(23) == 0
assert truncate_number(10.) == 0
assert truncate_number(0.111) == 0.111
assert truncate_number(4.0) == 0.0
assert truncate_number(0.123456789) == 0.123456789
assert truncate_number(6.987654321) == 0.987654321
assert truncate_number(0.056) == 0.056
assert truncate_number(4) == 0.0
assert truncate_number(10.5) == 0.5
assert truncate_number(11.5) == 0.5
assert truncate_number(12.5) == 0.5
assert truncate_number(23.5) == 0.5
assert truncate_number(34.5) == 0.5
assert truncate_number(0.98) == 0.98
assert truncate_number(4) == 0
assert truncate_number(0.75) == 0.75
assert truncate_number(4.25) == 0.25
assert truncate_number(4.75) == 0.75
assert truncate_number(5.75) == 0.75
assert truncate_number(0.25) == 0.25
assert truncate_number(1) == 0
assert (truncate_number(90.0) == 0.0)
assert (truncate_number(15.25) == 0.25)
assert (truncate_number(0.0078) == 0.0078)
assert truncate_number(1000000.000000) == 0.0
assert truncate_number(-1.0) == 0.0
assert truncate_number(100.5) == 0.5
assert truncate_number(0.999) == 0.999
assert truncate_number(35.) == 0.
assert truncate_number(0.) == 0.
assert truncate_number(19.0) == 0.0
assert truncate_number(8.00) == 0.0
assert truncate_number(1.00) == 0.0
assert truncate_number(20.0) == 0.0
assert truncate_number(6) == 0.0
assert truncate_number(3.0) == 0.0
assert truncate_number(30.0) == 0.0
assert truncate_number(100.0) == 0.0
assert truncate_number(300.0) == 0.0
assert truncate_number(1000.0) == 0.0
assert truncate_number(3000.0) == 0.0
assert truncate_number(10000.0) == 0.0
assert truncate_number(28.0) == 0.0
assert truncate_number(0.234) == 0.234
assert truncate_number(1.97) == 0.97
assert truncate_number(99.0) == 0.0
assert truncate_number(5.0) == 0
assert truncate_number(4.5) == 0.5
assert truncate_number(1.99) == .99
assert truncate_number(1.9999) == .9999
assert truncate_number(0.3) == .3
assert truncate_number(0.9999) == .9999
assert truncate_number(0.99999) == .99999
assert truncate_number(0.999999) == .999999
assert truncate_number(0.9999999) == .9999999
assert truncate_number(0.99999999) == .99999999
assert truncate_number(0.999999999) == .999999999
assert truncate_number(1.00) == 0.00
assert truncate_number(0.45) == 0.45
