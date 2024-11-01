

def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord(ch)) for ch in s])
assert decode_shift("fghij") == "abcde"
assert decode_shift("klmno") == "fghij"
assert decode_shift("pqrst") == "klmno"
assert decode_shift("uvwxy") == "pqrst"
assert decode_shift("zabcd") == "uvwxy"
assert decode_shift("xyz") == "stu"
assert decode_shift("vwxyz") == "qrstu"
assert decode_shift("abcde") == "vwxyz"
