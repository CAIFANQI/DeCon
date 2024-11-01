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
assert string_xor('1', '0') == '1'
assert string_xor('0', '1') == '1'
assert string_xor('10101010', '01010101') == '11111111'
assert string_xor('000', '111') == '111'
assert string_xor('01', '10') == '11'
assert string_xor('010', '101') == '111'
assert string_xor('111', '000') == '111'
assert string_xor('101', '010') == '111'
assert string_xor('1111', '0000') == '1111'
assert string_xor('10', '01') == '11'
assert string_xor('00', '11') == '11'
assert string_xor('001', '110') == '111'
assert string_xor('111111', '000000') == '111111'
assert string_xor('000000', '111111') == '111111'
assert string_xor('0000', '1111') == '1111'
assert string_xor('11111111', '00000000') == '11111111'
assert string_xor('11', '00') == '11'
assert string_xor('011', '100') == '111'
assert string_xor('100', '011') == '111'
assert string_xor('110', '001') == '111'
assert string_xor('1010', '0101') == '1111'
assert string_xor('0101', '1010') == '1111'
