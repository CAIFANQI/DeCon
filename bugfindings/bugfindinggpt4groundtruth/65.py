
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
assert '12345' == circular_shift('12345', 0)
assert '12345' == circular_shift('12345', -5)
assert circular_shift(0, 1) == '0'
assert 	circular_shift("123", 2) == "231"
assert 	circular_shift("123", 0) == "123"
assert 	circular_shift("1234", 0) == "1234"
assert 	'4321' == circular_shift('1234', 6)
assert 	circular_shift(4523, -100) == '4523'
assert circular_shift("1234", 4) == "1234"
assert 	"421234" == circular_shift(421234, 0)
assert circular_shift(0, 1) == "0"
assert 	circular_shift(10, 0) 	== '10'
assert 	circular_shift(0, 2) 	== '0'
assert 	(circular_shift(515, 5) == '515'), "Error"
assert circular_shift(123, 2) == "231"
assert circular_shift(123, 4) == "321"
assert circular_shift(123, 0) == "123"
assert circular_shift(0, 0) == "0"
assert circular_shift(12345, 0) == "12345"
