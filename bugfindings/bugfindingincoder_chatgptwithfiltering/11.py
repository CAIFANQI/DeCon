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
assert string_xor("11", "01") == "10"
assert string_xor('000', '100') == '100'
assert string_xor('000', '110') == '110'
assert string_xor('110', '000') == '110'
assert string_xor('100', '000') == '100'
assert string_xor('00', '10') == '10'
assert string_xor("0", "0") == "0"
assert string_xor("0", "1") == "1"
assert string_xor("1", "0") == "1"
assert string_xor("10", "01") == "11"
assert string_xor("00", "10") == "10"
assert string_xor('1', '1') == '0'
assert string_xor('10', '00') == '10'
assert string_xor('01', '11') == '10'
assert string_xor("000", "111") == "111"
assert string_xor("0000", "1101") == "1101"
assert string_xor("1", "1") == "0"
assert string_xor('0000', '1001') == '1001'
assert string_xor("11111", "01110") == "10001"
assert string_xor("000", "100") == "100"
