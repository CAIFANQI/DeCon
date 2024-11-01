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
assert string_xor('0000', '1111') == '1111'
assert string_xor('0', '1') == '1'
assert string_xor("0", "1") == "1"
assert string_xor("1", "0") == "1"
assert string_xor("10", "01") == "11"
assert string_xor("000", "111") == "111"
