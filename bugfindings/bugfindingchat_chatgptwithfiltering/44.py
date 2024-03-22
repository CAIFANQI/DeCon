

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
assert change_base(10, 2) == "1010"
assert change_base(10, 8) == "12"
assert change_base(15, 2) == "1111"
assert change_base(15, 8) == "17"
assert change_base(100, 2) == "1100100"
assert change_base(100, 8) == "144"
assert change_base(100, 16) == "64"
assert change_base(20, 2) == "10100"
assert change_base(20, 16) == "14"
assert change_base(255, 2) == "11111111"
assert change_base(16, 2) == "10000"
assert change_base(16, 8) == "20"
assert change_base(16, 10) == "16"
assert change_base(100, 5) == "400"
assert change_base(7, 3) == "21"
assert change_base(15, 4) == "33"
assert change_base(10, 8) == '12'
assert change_base(15, 2) == '1111'
assert change_base(15, 8) == '17'
assert change_base(100, 2) == '1100100'
assert change_base(100, 8) == '144'
assert change_base(100, 16) == '64'
assert change_base(16, 16) == "10"
assert change_base(100, 10) == "100"
assert change_base(8, 3) == "22"
assert change_base(10, 3) == "101"
assert change_base(10, 4) == "22"
assert change_base(10, 5) == "20"
assert change_base(10, 6) == "14"
assert change_base(10, 7) == "13"
assert change_base(10, 9) == "11"
assert change_base(10, 10) == "10"
assert change_base(1, 2) == "1"
assert change_base(1, 8) == "1"
assert change_base(1, 16) == "1"
assert change_base(9, 2) == "1001"
assert change_base(9, 8) == "11"
assert change_base(9, 16) == "9"
assert change_base(20, 8) == "24"
assert change_base(1000, 10) == "1000"
assert change_base(7, 2) == "111"
assert change_base(7, 8) == "7"
assert change_base(7, 16) == "7"
assert change_base(255, 8) == "377"
assert change_base(8, 2) == '1000'
assert change_base(8, 16) == '8'
assert change_base(110, 2) == '1101110'
assert change_base(110, 8) == '156'
assert change_base(1, 2) == '1'
assert change_base(1, 8) == '1'
assert change_base(1, 16) == '1'
assert change_base(2, 2) == '10'
assert change_base(2, 8) == '2'
assert change_base(2, 16) == '2'
assert change_base(25, 2) == "11001"
assert change_base(25, 8) == "31"
assert change_base(25, 16) == "19"
assert change_base(123, 2) == "1111011"
assert change_base(123, 8) == "173"
assert change_base(16, 8) == '20'
assert change_base(15, 3) == '120'
assert change_base(100, 5) == '400'
assert change_base(7, 4) == '13'
assert change_base(10, 3) == '101'
assert change_base(10, 4) == '22'
assert change_base(10, 5) == '20'
assert change_base(10, 6) == '14'
assert change_base(10, 7) == '13'
assert change_base(10, 9) == '11'
assert change_base(10, 10) == '10'
assert change_base(15, 4) == '33'
assert change_base(15, 5) == '30'
assert change_base(15, 6) == '23'
assert change_base(15, 7) == '21'
assert change_base(15, 9) == '16'
assert change_base(15, 10) == '15'
assert change_base(123, 10) == "123"
assert change_base(255, 2) == '11111111'
assert change_base(255, 8) == '377'
assert change_base(13, 5) == '23'
assert change_base(123, 4) == '1323'
assert change_base(20, 16) == '14'
assert change_base(7, 2) == '111'
assert change_base(7, 3) == '21'
assert change_base(7, 8) == '7'
assert change_base(7, 16) == '7'
assert change_base(7, 5) == "12"
assert change_base(15, 3) == "120"
assert change_base(15, 5) == "30"
assert change_base(15, 6) == "23"
assert change_base(15, 7) == "21"
assert change_base(15, 10) == "15"
assert change_base(25, 3) == "221"
assert change_base(25, 4) == "121"
assert change_base(25, 6) == "41"
assert change_base(25, 7) == "34"
assert change_base(25, 10) == "25"
assert change_base(20, 5) == "40"
assert change_base(8, 2) == "1000"
assert change_base(8, 10) == "8"
assert change_base(8, 16) == "8"
assert change_base(123, 4) == "1323"
assert change_base(456, 8) == "710"
assert change_base(7, 10) == "7"
