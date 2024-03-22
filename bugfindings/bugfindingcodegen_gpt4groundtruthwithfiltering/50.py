

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
assert 	decode_shift(encode_shift("abc")) == "abc"
assert 	decode_shift(encode_shift("xyz")) == "xyz"
assert 	decode_shift(encode_shift("def")) == "def"
assert 	decode_shift(encode_shift("ghi")) == "ghi"
assert 	decode_shift(encode_shift("jkl")) == "jkl"
assert 	decode_shift(encode_shift("mno")) == "mno"
assert 	decode_shift(encode_shift("pqrs")) == "pqrs"
assert 	decode_shift(encode_shift("tuv")) == "tuv"
assert 	decode_shift(encode_shift("wxy")) == "wxy"
assert 	decode_shift(encode_shift("z")) == "z"
assert encode_shift(decode_shift("zzz")) == "zzz"
assert decode_shift(encode_shift("zzz")) == "zzz"
assert decode_shift(encode_shift("apple")) == "apple"
