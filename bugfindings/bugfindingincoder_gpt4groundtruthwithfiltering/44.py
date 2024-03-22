

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x -= base
    return ret
assert change_base(16, 10) == '16'
assert change_base(8, 10) == '8'
assert change_base(9, 16) == '9'
assert change_base(10, 10) == '10'
assert change_base(1, 4) == '1', "base numbers are less than 10."
assert change_base(2, 16) == '2'
assert change_base(1, 2) == "1"
assert change_base(2, 2) == "10"
assert change_base(3, 2) == "11"
assert change_base(4, 2) == "100"
assert change_base(255, 10) == '255'
assert change_base(100, 10) == "100", "The base is wrong"
assert change_base(2000, 10) == "2000", "The base is wrong"
assert change_base(10, 10) == "10", "The base is wrong"
assert change_base(104, 10) == '104'
assert change_base(15, 2) == "1111"
assert change_base(5, 2) == "101"
assert change_base(1, 10) == "1"
assert change_base(16, 4) == '100'
assert change_base(123, 10) == "123", "123 is not a multiple of 10"
assert change_base(123, 10) == "123"
assert change_base(170, 10) == '170'
assert change_base(2, 5) == '2'
assert change_base(1, 36) == "1".upper()
assert change_base(7, 8) == "7"
assert change_base(123, 10) == '123'
assert change_base(925, 10) == '925'
assert change_base(9251, 10) == '9251'
assert change_base(2, 2) == '10'
