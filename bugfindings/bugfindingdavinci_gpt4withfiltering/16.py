

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    return len(set(string))
assert count_distinct_characters("") == 0
assert count_distinct_characters("A") == 1
assert count_distinct_characters("Abc") == 3
assert count_distinct_characters("AbcA") == 3
assert count_distinct_characters("abcd") == 4
assert count_distinct_characters('AbAB') == 2
assert count_distinct_characters("Hello") == 4
assert count_distinct_characters("a") == 1
assert count_distinct_characters("ab") == 2
assert count_distinct_characters("aB") == 2
assert count_distinct_characters("abcabc") == 3
assert count_distinct_characters("abcabd") == 4
assert count_distinct_characters('Abc') == 3
assert count_distinct_characters('0') == 1
assert count_distinct_characters('aaaaa') == 1
assert count_distinct_characters('  ') == 1
assert count_distinct_characters("Aa") == 1
assert count_distinct_characters("abcdefghijklmnopqrstuvwxyz") == 26
assert count_distinct_characters("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 26
assert count_distinct_characters("aBcDeFgHiJkLmNoPqRsTuVwXyZ") == 26
assert count_distinct_characters("0123456789") == 10
assert count_distinct_characters("AbA") == 2
assert count_distinct_characters("ABC") == 3
assert count_distinct_characters("aBc") == 3
assert count_distinct_characters("AbC") == 3
assert count_distinct_characters("ABCabc") == 3
assert count_distinct_characters("aAA") == 1
assert count_distinct_characters("abcc") == 3
assert count_distinct_characters("123") == 3
assert count_distinct_characters("aaaa") == 1
assert count_distinct_characters("bbbb") == 1
assert count_distinct_characters("aabb") == 2
assert count_distinct_characters("aABb") == 2
assert count_distinct_characters("abcdef") == 6
assert count_distinct_characters("\n\t") == 2
assert count_distinct_characters("aabbcc") == 3
assert count_distinct_characters("ADfA") == 3
assert count_distinct_characters("aabbccdDdeFF") == 6
assert count_distinct_characters("ab1a") == 3, "function count_distinct_characters is incorrect"
assert count_distinct_characters("") == 0, "function count_distinct_characters is incorrect"
assert count_distinct_characters("aaa") == 1
assert count_distinct_characters("ababa") == 2
assert count_distinct_characters('AbCDEa') == 5
assert count_distinct_characters("abcde") == 5
assert count_distinct_characters("abcDA") == 4
assert count_distinct_characters("XyZ") == 3
assert count_distinct_characters('peter piper picked a peck of pickled peppers') == 14
assert count_distinct_characters("abcabcabc") == 3
assert count_distinct_characters("Hi") == 2
assert count_distinct_characters("i h a t e y o u.") == 10
assert count_distinct_characters('') == 0
assert count_distinct_characters('aaaaaaaaaaaaaaaa') == 1
assert count_distinct_characters("zzzZZZZZzzzz") == 1
assert count_distinct_characters("123123") == 3
assert count_distinct_characters("Go") == 2
assert count_distinct_characters("abcaef") == 5
assert count_distinct_characters('Manohar') == 6
assert count_distinct_characters('a') == 1
assert count_distinct_characters("abcabcabcabc") == 3
assert count_distinct_characters("qwertyuiop") == 10
assert count_distinct_characters("banana") == 3
assert count_distinct_characters("Banana") == 3
assert count_distinct_characters("abc") == 3
assert count_distinct_characters("abracadabra") == 5
assert count_distinct_characters('The quick brown fox jumps over the lazy dog') == 27
assert count_distinct_characters("aabbb") == 2
assert count_distinct_characters("aabbbccc") == 3
assert count_distinct_characters("ABCABC") == 3
assert count_distinct_characters("AaBbCc") == 3
assert count_distinct_characters("AaBbCcAaBbCc") == 3
assert count_distinct_characters("ABCabcABCabc") == 3
assert count_distinct_characters("ABCabcABCabcABCabc") == 3
assert count_distinct_characters('AaAaBbbbC') == 3
assert count_distinct_characters("ABab") == 2
assert count_distinct_characters("AaaaaaBbb") == 2
assert count_distinct_characters("abcdefgh") == 8
assert count_distinct_characters("   ") == 1
assert count_distinct_characters("string") == 6
assert count_distinct_characters("Zebra") == 5
assert count_distinct_characters('AbcABCa') == 3
assert count_distinct_characters('xyz') == 3
assert count_distinct_characters('XYZ') == 3
assert count_distinct_characters('aBcabcabc') == 3
assert count_distinct_characters('abc') == 3
assert count_distinct_characters('aaa') == 1
assert count_distinct_characters('Aa') == 1
assert count_distinct_characters('aaaAa') == 1
assert count_distinct_characters('ab') == 2
assert count_distinct_characters('abAB') == 2
assert count_distinct_characters('abAa') == 2
assert count_distinct_characters('abcdabcdabcd') == 4
assert count_distinct_characters('abcdefghijklmnopqrstuvwxyz') == 26
assert count_distinct_characters('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 26
assert count_distinct_characters("  ") == 1
assert count_distinct_characters('abcABC') == 3
assert count_distinct_characters('abcdABCD') == 4
assert count_distinct_characters('HELLO') == 4
assert count_distinct_characters('HELLo') == 4
assert count_distinct_characters('123') == 3
assert count_distinct_characters('123aBc') == 6
assert count_distinct_characters('123abc') == 6
assert count_distinct_characters('     ') == 1
assert count_distinct_characters('   ') == 1
assert count_distinct_characters('aBcAaBb') == 3
assert count_distinct_characters("abcdE") == 5
assert count_distinct_characters("1 1 1 1 1") == 2
assert count_distinct_characters("aAaBbCcC") == 3
assert count_distinct_characters("aAAAAbbbb") == 2
assert count_distinct_characters("a\ta\na") == 3  # '\t' and '\n' are treated as different characters
assert count_distinct_characters('aabc') == 3
assert count_distinct_characters('aba') == 2
assert count_distinct_characters("asdfAAA") == 4
assert count_distinct_characters("asdfAAAaaa") == 4
assert count_distinct_characters("asd") == 3
assert count_distinct_characters(" ") == 1
assert count_distinct_characters("AaBb") == 2
assert count_distinct_characters("aabBc") == 3
assert count_distinct_characters("abcdefabcdef") == 6
assert count_distinct_characters("abcdefABCDEF") == 6
assert count_distinct_characters("The quick brown fox jumped over the lazy dog") == 26
assert count_distinct_characters("The quick brown fox jumped over the lazy dog.") == 27
assert count_distinct_characters("ABCD") == 4, 'expected 4'
assert count_distinct_characters("") == 0, 'expected 0'
assert count_distinct_characters("a") == 1, 'expected 1'
assert count_distinct_characters("ab") == 2, 'expected 2'
assert count_distinct_characters("aB") == 2, 'expected 2'
assert count_distinct_characters("aaaaa") == 1
assert count_distinct_characters("bbbbb") == 1
assert count_distinct_characters("ababab") == 2
assert count_distinct_characters("aabbaa") == 2
assert count_distinct_characters("AbCdEfGhIjKlMnOpQrStUvWxYz") == 26
assert count_distinct_characters("1234567890") == 10
assert count_distinct_characters("abcdeFghijklmnopqrstuvwxyz") == 26
assert count_distinct_characters("ABCdeFGHIJKLMNOPQRSTUVWXYZ") == 26
assert count_distinct_characters('abcdAbcd') == 4
assert count_distinct_characters('aaaa') == 1
assert count_distinct_characters('oooo') == 1
assert count_distinct_characters('abcDabcd') == 4
assert count_distinct_characters("abcdeabcde") == 5
assert count_distinct_characters("abcabcabcABC") == 3
assert count_distinct_characters("abcABCABCabc") == 3
assert count_distinct_characters("')]") == 3
assert count_distinct_characters('abcdefabcdefabc') == 6, 'test 4'
assert count_distinct_characters("abcABC") == 3
assert count_distinct_characters("1112233") == 3
assert count_distinct_characters("aba") == 2
assert count_distinct_characters("AaAaBbBbCcCc") == 3
assert count_distinct_characters('abcabcabcabcabc') == 3
assert count_distinct_characters('abcABCabcABCabcABC') == 3
assert count_distinct_characters('aaaaaaaa') == 1
assert count_distinct_characters('aaaaaaaaaab') == 2
assert count_distinct_characters('abcABCabcABCabcABCabcde') == 5
assert count_distinct_characters('123456') == 6
assert count_distinct_characters("beep") == 3
assert count_distinct_characters("AaA") == 1
assert count_distinct_characters("hello world") == 8
assert count_distinct_characters("Hello, world!") == 10
assert count_distinct_characters("aabbbcccc") == 3
assert count_distinct_characters("aaaaaaaaaa") == 1
assert count_distinct_characters('aa') == 1
assert count_distinct_characters('ABCdef') == 6
assert count_distinct_characters("Python") == 6
assert count_distinct_characters("pYtHoN") == 6
assert count_distinct_characters('123123123') == 3
assert count_distinct_characters('123123123123123') == 3
assert count_distinct_characters('ABCABCABCABCABC') == 3
assert count_distinct_characters('abcdabcdabcdabcd') == 4
assert count_distinct_characters("1234") == 4
assert count_distinct_characters("aA") == 1
assert count_distinct_characters("aAa") == 1
assert count_distinct_characters("aAab") == 2
assert count_distinct_characters("abbbb") == 2
assert count_distinct_characters("AAaaBBbbCCccDDdd") == 4
assert count_distinct_characters("abcABCabc") == 3
assert count_distinct_characters("abcABCabcDEF") == 6
assert count_distinct_characters("asdf") == 4
assert count_distinct_characters("asdfa") == 4
assert count_distinct_characters("asdfASDF") == 4
assert count_distinct_characters("asdfASDf") == 4
assert count_distinct_characters("Aaa") == 1
assert count_distinct_characters("abcdefa") == 6
assert count_distinct_characters("!@#$!@#$!@#$") == 4
assert count_distinct_characters("ABCDdabcdE") == 5
assert count_distinct_characters("Hello World") == 8
assert count_distinct_characters("!@#$%^&*()") == 10
assert count_distinct_characters("qwertyuiopasdfghjklzxcvbnm") == 26
assert count_distinct_characters("QWERTYUIOPASDFGHJKLZXCVBNM") == 26
assert count_distinct_characters('banana') == 3
assert count_distinct_characters("AbCabCabC") == 3
assert count_distinct_characters("aBbCcDdEe") == 5
assert count_distinct_characters("aBbCcdEe") == 5
assert count_distinct_characters("12345678") == 8
assert count_distinct_characters("zzZzz") == 1
assert count_distinct_characters("aaaBBB") == 2
assert count_distinct_characters("aBaBc") == 3
assert count_distinct_characters("abcaabca") == 3
assert count_distinct_characters("AaAaBbBbCcCcDdDdEeEeFfFfGgGgHhHhIiIiJjJjKkKkLlLlMmMmNnNnOoOoPpPpQqQqRrRrSsSsTtTtUuUuVvVvWwWwXxXxYyYyZzZz") == 26
assert count_distinct_characters('aaaaaaaaaaaaaaaaaa') == 1
assert count_distinct_characters("AbcABC") == 3
assert count_distinct_characters("aBcABC") == 3
assert count_distinct_characters("aBcABCabc") == 3
assert count_distinct_characters("aaaaaa") == 1
assert count_distinct_characters("abca") == 3
assert count_distinct_characters("aaadddd") == 2, "Wrong answer"
assert count_distinct_characters("AaA") == 1, "Wrong answer"
assert count_distinct_characters("") == 0, "Wrong answer"
assert count_distinct_characters("aaaaaaaaaaaaaaaaa") == 1, "Slow solution"
assert count_distinct_characters("aaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 2, "Slow solution"
assert count_distinct_characters("aAaAa") == 1
assert count_distinct_characters("a1a2A1A2") == 3
