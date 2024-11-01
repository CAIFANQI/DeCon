
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[:len(s) - shift] + s[len(s) - shift:]
assert circular_shift(10, 0) == '10'
assert circular_shift(1234, 4) == '1234'
assert circular_shift(1234, 6) == '4321'
assert circular_shift(1234, 10) == '4321'
assert circular_shift(1234, 14) == '4321'
assert circular_shift(1234, 18) == '4321'
assert circular_shift(1234, 22) == '4321'
assert circular_shift(2, 0) == '2', '2 is a circular shift'
assert circular_shift(3, 0) == '3', '3 is a circular shift'
assert circular_shift(4, 0) == '4', '4 is a circular shift'
assert circular_shift(5, 0) == '5', '5 is a circular shift'
assert circular_shift(6, 0) == '6', '6 is a circular shift'
assert circular_shift(7, 0) == '7', '7 is a circular shift'
assert circular_shift(8, 0) == '8', '8 is a circular shift'
assert circular_shift(9, 0) == '9', '9 is a circular shift'
assert circular_shift(10, 0) == '10', '10 is a circular shift'
assert circular_shift(11, 0) == '11', '11 is a circular shift'
assert circular_shift(12, 0) == '12', '12 is a circular shift'
assert circular_shift(13, 0) == '13', '13 is a circular shift'
assert circular_shift(14, 0) == '14', '14 is a circular shift'
assert circular_shift(15, 0) == '15', '15 is a circular shift'
assert circular_shift(16, 0) == '16', '16 is a circular shift'
assert circular_shift(17, 0) == '17', '17 is a circular shift'
assert circular_shift(18, 0) == '18', '18 is a circular shift'
assert circular_shift(19, 0) == '19', '19 is a circular shift'
assert circular_shift(20, 0) == '20', '20 is a circular shift'
assert circular_shift(10, 0) == "10"
assert circular_shift(10000000000000, 0) == '10000000000000'
assert circular_shift(100000000000000, 0) == '100000000000000'
assert circular_shift(1032, 0) == '1032'
assert circular_shift(123, 0) == '123'
assert circular_shift(1, -16) == '1'
assert circular_shift(1, -20) == '1'
assert circular_shift(1, 1) == '1'
assert circular_shift(1, 0) == '1'
assert circular_shift(0, -1) == '0'
assert circular_shift(2, 1) == "2"
assert circular_shift(123, 0)=="123"
assert circular_shift(1234, 0)=="1234"
assert circular_shift(8, 0) == '8'
assert circular_shift(8, 1) == '8'
assert circular_shift(1, -1) == '1'
assert circular_shift(0, 1) == '0'
assert circular_shift(0, 0) == '0'
assert circular_shift(-1, 0) == '-1'
assert circular_shift(101, 4) == '101'
assert circular_shift(42, -2) == '42'
assert circular_shift(42, 0) == '42'
assert circular_shift(0, 2) == '0'
assert circular_shift(1234, 0) == '1234'
assert circular_shift(12345, 0) == '12345'
assert circular_shift(123456000, 0) == '123456000'
assert circular_shift(10, -10) == '10'
assert circular_shift(10, 2) == '10'
assert circular_shift(0, -2) == '0'
assert circular_shift(10, 0) == "10", "10"
assert circular_shift(1, 2) == "1"
assert circular_shift(10, 2) == "10"
assert circular_shift(3, 1) == '3'
assert circular_shift(0, 5) == '0'
