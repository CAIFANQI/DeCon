

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
assert decode_cyclic(encode_cyclic("A")).upper() == "A"
assert decode_cyclic(encode_cyclic("AB")).upper() == "AB"
assert decode_cyclic(encode_cyclic("ABC")).upper() == "ABC"
assert decode_cyclic(encode_cyclic("ABCD")).upper() == "ABCD"
assert decode_cyclic(encode_cyclic("ABCDE")).upper() == "ABCDE"
assert decode_cyclic(encode_cyclic("ABCDEF")).upper() == "ABCDEF"
assert decode_cyclic(encode_cyclic("ABCDEFG")).upper() == "ABCDEFG"
assert decode_cyclic(encode_cyclic("ABCDEFGH")).upper() == "ABCDEFGH"
assert decode_cyclic(encode_cyclic("ABCDEFGHI")).upper() == "ABCDEFGHI"
assert decode_cyclic(encode_cyclic("ABCDEFGHIJ")).upper() == "ABCDEFGHIJ"
assert decode_cyclic(encode_cyclic("ABCDEFGHIJKL")).upper() == "ABCDEFGHIJKL"
assert decode_cyclic(encode_cyclic("ABCDEFGHIJKLM")).upper() == "ABCDEFGHIJKLM"
assert decode_cyclic(encode_cyclic("ABCDEFGHIJKLMN")).upper() == "ABCDEFGHIJKLMN"
assert decode_cyclic(encode_cyclic("abc")) == "abc"
assert decode_cyclic(encode_cyclic("abcd")) == "abcd"
assert decode_cyclic(encode_cyclic("abcde")) == "abcde"
assert decode_cyclic(encode_cyclic("abcdef")) == "abcdef"
assert decode_cyclic(encode_cyclic("abcdefg")) == "abcdefg"
assert decode_cyclic(encode_cyclic("abcdefgh")) == "abcdefgh"
assert decode_cyclic(encode_cyclic("abcdefghi")) == "abcdefghi"
assert decode_cyclic(encode_cyclic("abcdefghij")) == "abcdefghij"
assert decode_cyclic(encode_cyclic("abcdefghijk")) == "abcdefghijk"
assert decode_cyclic(encode_cyclic("abcdefghijkl")) == "abcdefghijkl"
assert decode_cyclic(encode_cyclic("abcdefghijklm")) == "abcdefghijklm"
assert decode_cyclic(encode_cyclic("abcdefghijklmno")) == "abcdefghijklmno"
assert decode_cyclic("gg") == encode_cyclic("gg")
assert decode_cyclic("ggg") == encode_cyclic("ggg")
assert decode_cyclic("gggg") == encode_cyclic("gggg")
assert decode_cyclic("ggggg") == encode_cyclic("ggggg")
assert decode_cyclic("gggggg") == encode_cyclic("gggggg")
assert decode_cyclic("ggggggg") == encode_cyclic("ggggggg")
assert decode_cyclic("gggggggg") == encode_cyclic("gggggggg")
assert decode_cyclic("ggggggggg") == encode_cyclic("ggggggggg")
assert decode_cyclic("gggggggggg") == encode_cyclic("gggggggggg")
assert decode_cyclic("ggggggggggg") == encode_cyclic("ggggggggggg")
assert decode_cyclic("gggggggggggg") == encode_cyclic("gggggggggggg")
assert decode_cyclic("ggggggggggggg") == encode_cyclic("ggggggggggggg")
assert decode_cyclic(encode_cyclic("AA")) == "AA"
assert decode_cyclic(encode_cyclic("AAA")) == "AAA"
assert decode_cyclic(encode_cyclic("AAAAA")) == "AAAAA"
assert decode_cyclic(encode_cyclic("BBBBBB")) == "BBBBBB"
assert decode_cyclic(encode_cyclic("CCCCCC")) == "CCCCCC"
assert decode_cyclic(encode_cyclic("DDDDDD")) == "DDDDDD"
assert decode_cyclic(encode_cyclic("EEEEEE")) == "EEEEEE"
assert decode_cyclic(encode_cyclic("FFFFFFFF")) == "FFFFFFFF"
assert decode_cyclic(encode_cyclic("GGGGGGGG")) == "GGGGGGGG"
assert decode_cyclic(encode_cyclic("HHHHHHHH")) == "HHHHHHHH"
assert decode_cyclic(encode_cyclic("IIIIIIII")) == "IIIIIIII"
assert decode_cyclic(encode_cyclic("JJJJJJJJ")) == "JJJJJJJJ"
assert decode_cyclic(encode_cyclic("KKKKKKKK")) == "KKKKKKKK"
assert decode_cyclic(encode_cyclic("LLLLLLLLLL")) == "LLLLLLLLLL"
assert decode_cyclic("ab") == "ab"
assert decode_cyclic(encode_cyclic("abd")) == "abd"
assert decode_cyclic(encode_cyclic("abcdefghijklmnop")) == "abcdefghijklmnop"
assert decode_cyclic(encode_cyclic("abcdefghijklmnopq")) == "abcdefghijklmnopq"
assert decode_cyclic(encode_cyclic("abcdefghijklmnopqrst")) == "abcdefghijklmnopqrst"
assert decode_cyclic(encode_cyclic("abcdefghijklmnopqrstu")) == "abcdefghijklmnopqrstu"
assert decode_cyclic(encode_cyclic("abcdefghijklmnopqrstuv")) == "abcdefghijklmnopqrstuv"
assert decode_cyclic(encode_cyclic("azzz")) == "azzz"
assert decode_cyclic(encode_cyclic("zza")) == "zza"
assert decode_cyclic(encode_cyclic("zzzzzzzzzz")) == "zzzzzzzzzz"
assert decode_cyclic(encode_cyclic("zzzzzzzzzzzzzzzzzzzz")) == "zzzzzzzzzzzzzzzzzzzz"
assert decode_cyclic("aB") == "aB"
assert decode_cyclic("aaabbbb") == encode_cyclic("aaabbbb")
assert decode_cyclic("aaabbb") == encode_cyclic("aaabbb")
assert decode_cyclic("a") == encode_cyclic("a")
assert decode_cyclic("aa") == encode_cyclic("aa")
assert decode_cyclic("ab") == encode_cyclic("ab")
assert decode_cyclic("aaabb") == encode_cyclic("aaabb")
assert decode_cyclic("aaab") == encode_cyclic("aaab")
assert decode_cyclic("") == ""
assert decode_cyclic("A") == "A"
assert decode_cyclic("BB") == "BB"
assert decode_cyclic("CC") == "CC"
assert decode_cyclic("DD") == "DD"
assert decode_cyclic(encode_cyclic("AB")) == "AB"
assert decode_cyclic(encode_cyclic("ABC")) == "ABC"
assert decode_cyclic(encode_cyclic("ABCABCABCABC")) == "ABCABCABCABC"
assert decode_cyclic(encode_cyclic("bbbbb")) == "bbbbb"
assert decode_cyclic(encode_cyclic("bbbbbbb")) == "bbbbbbb"
assert decode_cyclic(encode_cyclic("bbbbbbbbb")) == "bbbbbbbbb"
assert decode_cyclic(encode_cyclic("bbbbbbbbbbb")) == "bbbbbbbbbbb"
assert decode_cyclic(encode_cyclic("bbbbbbbbbbbbb")) == "bbbbbbbbbbbbb"
assert decode_cyclic(encode_cyclic("bbbbbbbbbbbbbbb")) == "bbbbbbbbbbbbbbb"
assert encode_cyclic("a") == decode_cyclic("a")
assert encode_cyclic("aa") == decode_cyclic("aa")
assert encode_cyclic("aaa") == decode_cyclic("aaa")
assert encode_cyclic("aaaa") == decode_cyclic("aaaa")
assert encode_cyclic("aaaaa") == decode_cyclic("aaaaa")
assert encode_cyclic("bbbbb") == decode_cyclic("bbbbb")
assert encode_cyclic("bbbbbb") == decode_cyclic("bbbbbb")
assert encode_cyclic("bbbbbbb") == decode_cyclic("bbbbbbb")
assert encode_cyclic("bbbbbbbb") == decode_cyclic("bbbbbbbb")
assert encode_cyclic("cccccccc") == decode_cyclic("cccccccc")
assert encode_cyclic("zzzzzzzz") == decode_cyclic("zzzzzzzz")
assert decode_cyclic(encode_cyclic('abc')) == 'abc'
assert decode_cyclic(encode_cyclic('abbb')) == 'abbb'
assert decode_cyclic(encode_cyclic('abbcb')) == 'abbcb'
assert decode_cyclic(encode_cyclic('abbbbbbb')) == 'abbbbbbb'
assert decode_cyclic(encode_cyclic('ababababa')) == 'ababababa'
assert decode_cyclic(encode_cyclic('abababbba')) == 'abababbba'
assert decode_cyclic(encode_cyclic('abababbbbba')) == 'abababbbbba'
assert decode_cyclic(encode_cyclic('abbbaaaba')) == 'abbbaaaba'
assert decode_cyclic(encode_cyclic('abbbbbabb')) == 'abbbbbabb'
assert decode_cyclic(encode_cyclic('abbbbbabbc')) == 'abbbbbabbc'
assert decode_cyclic(encode_cyclic('abbbbbabc')) == 'abbbbbabc'
assert decode_cyclic(encode_cyclic('abbbbbabbbbb')) == 'abbbbbabbbbb'
assert decode_cyclic(encode_cyclic('abbbbbabbbbbc')) == 'abbbbbabbbbbc'
assert decode_cyclic(encode_cyclic("CD")) == "CD"
assert decode_cyclic(encode_cyclic("ACD")) == "ACD"
assert decode_cyclic(encode_cyclic("BCD")) == "BCD"
assert decode_cyclic(encode_cyclic("BC")) == "BC"
assert decode_cyclic(encode_cyclic("DC")) == "DC"
assert decode_cyclic(encode_cyclic("DCBA")) == "DCBA"
assert decode_cyclic(encode_cyclic("ABBA")) == "ABBA"
assert decode_cyclic(encode_cyclic("ABCDD")) == "ABCDD"
assert decode_cyclic(encode_cyclic("ABACD")) == "ABACD"
assert decode_cyclic(encode_cyclic("ACBCD")) == "ACBCD"
assert decode_cyclic(encode_cyclic("ACDCBA")) == "ACDCBA"
assert decode_cyclic(encode_cyclic("ABDBA")) == "ABDBA"
assert decode_cyclic(encode_cyclic("AACB")) == "AACB"
assert decode_cyclic(encode_cyclic("AADB")) == "AADB"
assert decode_cyclic('aaaa') == 'aaaa'
assert decode_cyclic("abb") == "bab"
assert decode_cyclic("BBB") == encode_cyclic("BBB")
assert decode_cyclic(encode_cyclic("aaaaa")) == "aaaaa"
assert decode_cyclic(encode_cyclic("abca")) == "abca"
assert decode_cyclic(encode_cyclic("zabca")) == "zabca"
assert decode_cyclic(encode_cyclic("abcaz")) == "abcaz"
assert decode_cyclic(encode_cyclic("zabcaz")) == "zabcaz"
assert decode_cyclic(encode_cyclic("ababab")) == "ababab"
assert decode_cyclic(encode_cyclic("baababa")) == "baababa"
assert decode_cyclic(encode_cyclic("baababab")) == "baababab"
assert decode_cyclic(encode_cyclic("bbaabaab")) == "bbaabaab"
assert decode_cyclic(encode_cyclic("baabbaba")) == "baabbaba"
assert decode_cyclic(encode_cyclic("aaabbaaa")) == "aaabbaaa"
assert decode_cyclic(encode_cyclic("aabbababa")) == "aabbababa"
assert decode_cyclic(encode_cyclic("aaaaaa")) == "aaaaaa"
assert decode_cyclic("aaaa") == encode_cyclic("aaaa")
assert decode_cyclic(encode_cyclic("abbbbccdde")) == "abbbbccdde"
assert decode_cyclic(encode_cyclic("abbbbbcccddde")) == "abbbbbcccddde"
assert decode_cyclic(encode_cyclic("abbcc")) == "abbcc"
assert decode_cyclic(encode_cyclic("abcdabcd")) == "abcdabcd"
assert decode_cyclic(encode_cyclic("bbbb")) == "bbbb"
assert decode_cyclic(encode_cyclic("bbbbbb")) == "bbbbbb"
assert decode_cyclic(encode_cyclic("abbbab")) == "abbbab"
assert decode_cyclic('ab') == 'ab'
assert decode_cyclic('aaaaa') == 'aaaaa'
assert decode_cyclic('c') == encode_cyclic('c')
assert decode_cyclic("aaaa") == "a" * 4
