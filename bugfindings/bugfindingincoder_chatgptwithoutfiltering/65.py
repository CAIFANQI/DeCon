
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
assert circular_shift(1234, 6) == '4321'
assert circular_shift(1234, 10) == '4321'
assert circular_shift(1234, 14) == '4321'
assert circular_shift(1234, 18) == '4321'
assert circular_shift(1234, 22) == '4321'
assert circular_shift(101, 4) == '101'
assert circular_shift(0, 2) == '0'
assert circular_shift(1, 2) == "1"
assert circular_shift(0, 5) == '0'
