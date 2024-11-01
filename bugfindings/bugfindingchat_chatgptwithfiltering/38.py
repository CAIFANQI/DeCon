

def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    return encode_cyclic(s)
assert decode_cyclic(encode_cyclic("abc")) == "abc"
assert decode_cyclic(encode_cyclic("abcdef")) == "abcdef"
assert decode_cyclic(encode_cyclic("abcdefghi")) == "abcdefghi"
assert decode_cyclic(encode_cyclic("abcdefghij")) == "abcdefghij"
assert decode_cyclic(encode_cyclic("abcdefghijklmnop")) == "abcdefghijklmnop"
assert decode_cyclic(encode_cyclic("a")) == "a"
assert decode_cyclic(encode_cyclic("ab")) == "ab"
assert decode_cyclic(encode_cyclic("abcd")) == "abcd"
assert decode_cyclic(encode_cyclic("abcde")) == "abcde"
assert decode_cyclic(encode_cyclic("abcdefg")) == "abcdefg"
assert decode_cyclic(encode_cyclic("abcdefgh")) == "abcdefgh"
assert decode_cyclic(encode_cyclic("abcdefghijklmnopqrstuvwxyz")) == "abcdefghijklmnopqrstuvwxyz"
assert decode_cyclic(encode_cyclic("abcdefghijk")) == "abcdefghijk"
assert decode_cyclic(encode_cyclic("abcdefghijkl")) == "abcdefghijkl"
assert decode_cyclic(encode_cyclic("abcdefghijklm")) == "abcdefghijklm"
assert decode_cyclic(encode_cyclic("abcdefghijklmn")) == "abcdefghijklmn"
assert decode_cyclic(encode_cyclic("abcdefghijklmno")) == "abcdefghijklmno"
assert decode_cyclic(encode_cyclic("abcdefghijklmnopq")) == "abcdefghijklmnopq"
assert decode_cyclic(encode_cyclic("abcdefghijklmnopqr")) == "abcdefghijklmnopqr"
assert decode_cyclic(encode_cyclic("abcdefghijklmnopqrs")) == "abcdefghijklmnopqrs"
assert decode_cyclic(encode_cyclic("abcdefghijklmnopqrst")) == "abcdefghijklmnopqrst"
assert decode_cyclic(encode_cyclic("abcdefghijklmnopqrstu")) == "abcdefghijklmnopqrstu"
assert decode_cyclic(encode_cyclic("abcdefghijklmnopqrstuv")) == "abcdefghijklmnopqrstuv"
assert decode_cyclic(encode_cyclic("abcdefghijklmnopqrstuvw")) == "abcdefghijklmnopqrstuvw"
assert decode_cyclic(encode_cyclic("abcdefghijklmnopqrstuvwx")) == "abcdefghijklmnopqrstuvwx"
assert decode_cyclic(encode_cyclic("abcdefghijklmnopqrstuvwxy")) == "abcdefghijklmnopqrstuvwxy"
assert decode_cyclic("aaa") == "aaa"
assert decode_cyclic(encode_cyclic('abcdef')) == 'abcdef'
assert decode_cyclic(encode_cyclic('abcdefghi')) == 'abcdefghi'
assert decode_cyclic(encode_cyclic('abcdefghij')) == 'abcdefghij'
assert decode_cyclic(encode_cyclic('abcdefghijklmnopqrstuvwxyz')) == 'abcdefghijklmnopqrstuvwxyz'
assert decode_cyclic(encode_cyclic("world")) == "world"
assert decode_cyclic(encode_cyclic("python")) == "python"
assert decode_cyclic(encode_cyclic("")) == ""
assert decode_cyclic('bcabca') == 'abcabc'
assert decode_cyclic(encode_cyclic('abc')) == 'abc'
assert decode_cyclic(encode_cyclic('abcd')) == 'abcd'
assert decode_cyclic(encode_cyclic('abcde')) == 'abcde'
assert decode_cyclic(encode_cyclic('abcdefg')) == 'abcdefg'
assert decode_cyclic(encode_cyclic('abcdefgh')) == 'abcdefgh'
assert decode_cyclic(encode_cyclic('abcdefghijk')) == 'abcdefghijk'
assert decode_cyclic(encode_cyclic('abcdefghijkl')) == 'abcdefghijkl'
assert decode_cyclic(encode_cyclic('abcdefghijklm')) == 'abcdefghijklm'
assert decode_cyclic(encode_cyclic('abcdefghijklmn')) == 'abcdefghijklmn'
assert decode_cyclic(encode_cyclic('abcdefghijklmno')) == 'abcdefghijklmno'
assert decode_cyclic(encode_cyclic('abcdefghijklmnop')) == 'abcdefghijklmnop'
assert decode_cyclic(encode_cyclic('abcdefghijklmnopq')) == 'abcdefghijklmnopq'
assert decode_cyclic(encode_cyclic('abcdefghijklmnopqr')) == 'abcdefghijklmnopqr'
assert decode_cyclic(encode_cyclic('abcdefghijklmnopqrs')) == 'abcdefghijklmnopqrs'
assert decode_cyclic(encode_cyclic('abcdefghijklmnopqrst')) == 'abcdefghijklmnopqrst'
assert decode_cyclic(encode_cyclic('abcdefghijklmnopqrstu')) == 'abcdefghijklmnopqrstu'
assert decode_cyclic(encode_cyclic('abcdefghijklmnopqrstuv')) == 'abcdefghijklmnopqrstuv'
assert decode_cyclic(encode_cyclic('abcdefghijklmnopqrstuvw')) == 'abcdefghijklmnopqrstuvw'
assert decode_cyclic(encode_cyclic('abcdefghijklmnopqrstuvwx')) == 'abcdefghijklmnopqrstuvwx'
assert decode_cyclic(encode_cyclic('abcdefghijklmnopqrstuvwxy')) == 'abcdefghijklmnopqrstuvwxy'
assert encode_cyclic(decode_cyclic('abc')) == 'abc'
assert encode_cyclic(decode_cyclic('abcd')) == 'abcd'
assert encode_cyclic(decode_cyclic('abcde')) == 'abcde'
assert decode_cyclic('kl') == 'kl'
assert decode_cyclic('lm') == 'lm'
assert decode_cyclic('mn') == 'mn'
assert decode_cyclic('no') == 'no'
assert decode_cyclic('op') == 'op'
assert decode_cyclic('pq') == 'pq'
assert decode_cyclic('qr') == 'qr'
assert decode_cyclic('rs') == 'rs'
assert decode_cyclic('st') == 'st'
assert decode_cyclic('tu') == 'tu'
assert decode_cyclic('uv') == 'uv'
assert decode_cyclic('vw') == 'vw'
assert decode_cyclic('wx') == 'wx'
assert decode_cyclic('xy') == 'xy'
assert decode_cyclic('yz') == 'yz'
assert decode_cyclic('za') == 'za'
assert decode_cyclic('ab') == 'ab'
assert decode_cyclic('bc') == 'bc'
assert decode_cyclic('cd') == 'cd'
assert decode_cyclic('de') == 'de'
assert decode_cyclic('ef') == 'ef'
assert decode_cyclic('fg') == 'fg'
assert decode_cyclic('gh') == 'gh'
assert decode_cyclic('hi') == 'hi'
assert decode_cyclic('ij') == 'ij'
assert decode_cyclic('jk') == 'jk'
assert encode_cyclic(decode_cyclic("abc")) == "abc"
assert encode_cyclic(decode_cyclic("abcdef")) == "abcdef"
assert encode_cyclic(decode_cyclic("abcdefghi")) == "abcdefghi"
assert encode_cyclic(decode_cyclic("abcdefghij")) == "abcdefghij"
assert encode_cyclic(decode_cyclic("abcdefghijklmnopqrstuvwxyz")) == "abcdefghijklmnopqrstuvwxyz"
assert decode_cyclic(encode_cyclic("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")) == "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
assert decode_cyclic('BCA') == 'ABC'
assert decode_cyclic('AB') == 'AB'
assert decode_cyclic('A') == 'A'
assert decode_cyclic(encode_cyclic("1234567890")) == "1234567890"
assert decode_cyclic(encode_cyclic("hello world")) == "hello world"
assert decode_cyclic(encode_cyclic("coding is fun")) == "coding is fun"
assert decode_cyclic(encode_cyclic("programming")) == "programming"
