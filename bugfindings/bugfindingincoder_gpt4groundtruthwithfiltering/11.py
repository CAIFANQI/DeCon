from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i, j):
        if i == j:
            return '1'
        else:
            return '0'

    return ''.join(xor(x, y) for x, y in zip(a, b))
assert string_xor("1000", "0000") == "1000"
assert string_xor("1001", "0000") == "1001"
assert string_xor('0000', '1111') == '1111'
assert string_xor('0', '0') == '0'
assert string_xor('0', '1') == '1'
assert string_xor("11", "10") == "01"
assert string_xor("11", "01") == "10"
assert string_xor("10", "11") == "01"
assert string_xor('10', '11') == '01'
assert string_xor('01', '01') == '00'
assert string_xor('000', '000') == '000'
assert string_xor('001', '011') == '010'
assert string_xor('000', '100') == '100'
assert string_xor('000', '001') == '001'
assert string_xor('001', '000') == '001'
assert string_xor('000', '110') == '110'
assert string_xor('110', '000') == '110'
assert string_xor('100', '000') == '100'
assert string_xor('000', '010') == '010'
assert string_xor('010', '000') == '010'
assert string_xor('11', '10') == '01'
assert string_xor('10', '10') == '00'
assert string_xor('00', '10') == '10'
assert string_xor('00', '00') == '00'
assert string_xor("0", "0") == "0"
assert string_xor("0", "1") == "1"
assert string_xor("1", "0") == "1"
assert string_xor("01", "01") == "00"
assert string_xor("10", "01") == "11"
assert string_xor('010', '010') == '000'
assert string_xor("00", "10") == "10"
assert string_xor("010", "010") == "000"
assert string_xor('','') == ''
assert string_xor('1', '1') == '0'
assert string_xor('', 'aa') == ''
assert string_xor('10', '00') == '10'
assert string_xor('01', '11') == '10'
assert string_xor("000", "111") == "111"
assert string_xor("0000", "1101") == "1101"
assert string_xor("0000", "0010") == "0010"
assert string_xor("0010", "0000") == "0010"
assert string_xor("0000", "0000") == "0000"
assert string_xor('0000', '11111') == '1111'
assert string_xor('', 'a') == '', 'Empty strings XOR to non-empty strings should be non-empty strings'
assert string_xor("1", "1") == "0"
assert string_xor('11', '11') == '00'
assert string_xor('0000', '1001') == '1001'
assert string_xor("000000", "000000") == "000000"
assert string_xor("11111", "01110") == "10001"
assert string_xor("0100", "0100") == "0000"
assert string_xor("000", "100") == "100"
assert string_xor("10", "000") == "10"
assert string_xor("1011", "1110") == "0101"
assert string_xor("000", "000") == "000"
