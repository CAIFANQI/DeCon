

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
assert decode_shift(encode_shift("hello")) == "hello"
assert decode_shift(encode_shift("world")) == "world"
assert decode_shift(encode_shift("abcdefghijklmnopqrstuvwxyz")) == "abcdefghijklmnopqrstuvwxyz"
assert decode_shift("fghij") == "abcde"
assert decode_shift(encode_shift("abcxyz")) == "abcxyz"
assert decode_shift(encode_shift("abcde")) == "abcde"
assert decode_shift(encode_shift("xyzab")) == "xyzab"
assert decode_shift("klmno") == "fghij"
assert decode_shift("pqrst") == "klmno"
assert decode_shift("uvwxy") == "pqrst"
assert decode_shift("zabcd") == "uvwxy"
assert decode_shift(encode_shift("")) == ""
assert decode_shift(encode_shift("python")) == "python"
assert decode_shift(encode_shift("xyz")) == "xyz"
assert decode_shift(encode_shift("abc")) == "abc"
assert decode_shift("xyz") == "stu"
assert decode_shift(encode_shift("zoo")) == "zoo"
assert encode_shift(decode_shift("hello")) == "hello"
assert encode_shift(decode_shift("abcde")) == "abcde"
assert encode_shift(decode_shift("xyz")) == "xyz"
assert encode_shift(decode_shift("abcdefghijklmnopqrstuvwxyz")) == "abcdefghijklmnopqrstuvwxyz"
assert decode_shift(encode_shift("zxcvb")) == "zxcvb"
assert encode_shift(decode_shift("world")) == "world"
assert decode_shift("vwxyz") == "qrstu"
assert decode_shift(encode_shift("defabc")) == "defabc"
assert decode_shift(encode_shift("xyzabc")) == "xyzabc"
assert decode_shift(encode_shift("programming")) == "programming"
assert decode_shift(encode_shift("code")) == "code"
assert decode_shift("abcde") == "vwxyz"
