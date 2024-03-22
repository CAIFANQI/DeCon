

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
assert 	str(change_base(1234, 10)) == "1234"
assert change_base(10, 2) == '1010'
assert change_base(10, 10) == '10'
assert change_base(42, 2) == '101010'
assert change_base(4, 7) == '4'
assert change_base(2, 7) == '2'
assert change_base(3, 2) == '11'
assert change_base(3, 7) == '3'
assert change_base(5, 2) == '101'
assert change_base(5, 3) == '12'
assert change_base(5, 7) == '5'
assert change_base(6, 2) == '110'
assert change_base(6, 7) == '6'
assert change_base(7, 2) == '111'
assert change_base(16, 10) == '16'
assert 	(change_base(10, 10) == "10")
assert 	change_base(100, 2) == '1100100'
