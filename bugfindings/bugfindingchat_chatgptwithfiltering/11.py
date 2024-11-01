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
assert string_xor("0000", "1111") == "1111"
assert string_xor("0101", "1010") == "1111"
assert string_xor("101010", "010101") == "111111"
assert string_xor("000", "111") == "111"
assert string_xor("1010101010", "0101010101") == "1111111111"
assert string_xor("111000", "000111") == "111111"
assert string_xor("000000", "111111") == "111111"
assert string_xor("111111", "000000") == "111111"
assert string_xor('1111', '0000') == '1111'
assert string_xor('010101', '101010') == '111111'
assert string_xor("1111", "0000") == "1111"
assert string_xor("1100", "0011") == "1111"
assert string_xor("01010101", "10101010") == "11111111"
assert string_xor("11111111", "00000000") == "11111111"
assert string_xor("00000000", "11111111") == "11111111"
assert string_xor('101010', '010101') == '111111'
assert string_xor('1', '0') == '1'
assert string_xor('0', '1') == '1'
assert string_xor("10101010", "01010101") == "11111111"
assert string_xor("11110000", "00001111") == "11111111"
assert string_xor('10101010', '01010101') == '11111111'
assert string_xor('11111111', '00000000') == '11111111'
assert string_xor('101010101010', '010101010101') == '111111111111'
assert string_xor('1010101010101010', '0101010101010101') == '1111111111111111'
assert string_xor('10101010101010101010', '01010101010101010101') == '11111111111111111111'
assert string_xor('101010101010101010101010', '010101010101010101010101') == '111111111111111111111111'
assert string_xor('1010101010101010101010101010', '0101010101010101010101010101') == '1111111111111111111111111111'
assert string_xor('10101010101010101010101010101010', '01010101010101010101010101010101') == '11111111111111111111111111111111'
assert string_xor('1010101010101010101010101010101010', '0101010101010101010101010101010101') == '1111111111111111111111111111111111'
assert string_xor("0", "0") == "0"
assert string_xor("1", "1") == "0"
assert string_xor("101010101", "010101010") == "111111111"
assert string_xor('0101', '1010') == '1111'
assert string_xor('00000000', '11111111') == '11111111'
assert string_xor('0000000000000000', '1111111111111111') == '1111111111111111'
assert string_xor("111000", "001100") == "110100"
assert string_xor("010101", "101010") == "111111"
assert string_xor('11110000', '00001111') == '11111111'
assert string_xor('1010', '0101') == '1111'
assert string_xor('0011', '1100') == '1111'
assert string_xor('1001', '0110') == '1111'
assert string_xor('0101', '1111') == '1010'
assert string_xor("0", "1") == "1"
assert string_xor("1", "0") == "1"
assert string_xor("100", "001") == "101"
assert string_xor("0000000000", "1111111111") == "1111111111"
assert string_xor('000000', '111111') == '111111'
assert string_xor('0110', '1001') == '1111'
assert string_xor('0000', '1111') == '1111'
assert string_xor("110011", "001100") == "111111"
assert string_xor("1001", "0110") == "1111"
assert string_xor("111", "000") == "111"
assert string_xor('1100', '0011') == '1111'
assert string_xor('111111', '000000') == '111111'
assert string_xor('1010101010', '0101010101') == '1111111111'
assert string_xor('0000000000', '1111111111') == '1111111111'
assert string_xor('1111111111', '0000000000') == '1111111111'
assert string_xor('1010', '0000') == '1010'
assert string_xor('0000', '1010') == '1010'
assert string_xor('0000', '1000') == '1000'
assert string_xor('0001', '1000') == '1001'
assert string_xor('0010', '1000') == '1010'
assert string_xor('0100', '1000') == '1100'
assert string_xor('101', '010') == '111'
assert string_xor('0', '0') == '0'
assert string_xor('1', '1') == '0'
assert string_xor("001", "100") == "101"
assert string_xor("1010", "0101") == "1111"
assert string_xor("11001100", "00110011") == "11111111"
assert string_xor("10", "01") == "11"
assert string_xor("101", "010") == "111"
assert string_xor("10101", "01010") == "11111"
assert string_xor("1010101", "0101010") == "1111111"
assert string_xor("0110", "1001") == "1111"
assert string_xor("0101", "1111") == "1010"
assert string_xor("1111", "0001") == "1110"
assert string_xor("101010101010", "010101010101") == "111111111111"
assert string_xor("000000000000", "111111111111") == "111111111111"
assert string_xor("10101010101010", "01010101010101") == "11111111111111"
assert string_xor("00000000000000", "11111111111111") == "11111111111111"
assert string_xor("00001111", "11110000") == "11111111"
assert string_xor('00001111', '11110000') == '11111111'
