
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
assert circular_shift(123456789, 10) == '987654321'
assert circular_shift(123, 4) == '321'
assert circular_shift(123, 1234) == '321'
assert circular_shift(123, 11) == '321'
assert circular_shift(123, 100) == '321'
assert circular_shift(123, 8) == '321'
assert circular_shift(1234, 5) == '4321'
assert circular_shift(1234, 9) == '4321'
assert circular_shift(1234, 13) == '4321'
assert circular_shift(1234, 17) == '4321'
assert circular_shift(0, 2) == '0'
assert circular_shift(0, 10) == '0'
assert circular_shift(123456789, 20) == '987654321'
assert circular_shift(1, 2) == '1'
assert circular_shift(1, 1000) == '1'
assert circular_shift(123, 1000) == '321'
assert circular_shift(531, 9) == '135'
assert circular_shift(10, 1) == '01'
assert circular_shift(12, 1) == '21'
assert circular_shift(123456789, 11) == '987654321'
assert circular_shift(1234, 10) == '4321'
assert circular_shift(1729, 15) == '9271'
assert circular_shift(12345, 6) == '54321'
assert circular_shift(12345, 10) == '54321'
assert circular_shift(1234567, 10) == '7654321'
assert circular_shift(12, 3) == '21'
assert circular_shift(91, 1) == '19'
assert circular_shift(2009, 5) == '9002'
assert circular_shift(2009, 100) == '9002'
assert circular_shift(123, 10) == '321'
assert "4321" == circular_shift(1234, 5)
assert circular_shift(11, 3) == '11'
assert circular_shift(11, 4) == '11'
assert circular_shift(11, 5) == '11'
assert circular_shift(1234, 8) == '4321'
assert '321' == circular_shift(123, 10)
assert circular_shift(4321, 5) == '1234'
assert circular_shift(12345, 8) == '54321'
assert circular_shift(22, 3) == '22'
assert circular_shift(987, 5) == '789'
assert circular_shift(1, 5) == '1'
assert circular_shift(1, 6) == '1'
assert "4321" == circular_shift(1234, 7)
assert circular_shift(0, 5) == "0"
assert circular_shift(12345, 12) == '54321'
assert circular_shift(7, 2) == '7'
assert circular_shift(7, 3) == '7'
assert circular_shift(12345, 15) == '54321'
assert circular_shift(98765, 15) == '56789'
assert circular_shift(123, 7) == '321'
assert "21" == circular_shift(12, 1)
assert circular_shift(5, 2) == '5'
assert circular_shift(5, 3) == '5'
assert circular_shift(5, 5) == '5'
assert circular_shift(5, 100) == '5'
assert circular_shift(5, 1000) == '5'
assert circular_shift(5, 123456789) == '5'
assert circular_shift(123456789, 12) == '987654321'
assert circular_shift(12345, 7) == '54321'
assert circular_shift(123, 9) == '321'
assert circular_shift(12345, 6777) == '54321'
assert circular_shift(54321, 6) == '12345'
assert '555555555' == circular_shift(555555555, 100)
assert '19' == circular_shift(91, 1)
assert "3" == circular_shift(3, 4)
assert "8" == circular_shift(8, 4)
assert "31" == circular_shift(13, 4)
assert "8" == circular_shift(8, 5)
assert "8" == circular_shift(8, 8)
assert "8" == circular_shift(8, 9)
assert '24' == circular_shift(42, 1)
assert circular_shift(123, 6) == '321'
