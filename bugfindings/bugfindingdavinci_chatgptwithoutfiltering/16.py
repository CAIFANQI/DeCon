

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
assert count_distinct_characters("abcd") == 4
assert count_distinct_characters("a") == 1
assert count_distinct_characters("ab") == 2
assert count_distinct_characters("abcabc") == 3
assert count_distinct_characters("abcabd") == 4
assert count_distinct_characters('aaaaa') == 1
assert count_distinct_characters("abcdefghijklmnopqrstuvwxyz") == 26
assert count_distinct_characters("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 26
assert count_distinct_characters("ABC") == 3
assert count_distinct_characters("abcc") == 3
assert count_distinct_characters("aaaa") == 1
assert count_distinct_characters("bbbb") == 1
assert count_distinct_characters("aabb") == 2
assert count_distinct_characters("abcdef") == 6
assert count_distinct_characters("aabbcc") == 3
assert count_distinct_characters("") == 0, "function count_distinct_characters is incorrect"
assert count_distinct_characters("aaa") == 1
assert count_distinct_characters("ababa") == 2
assert count_distinct_characters("abcde") == 5
assert count_distinct_characters("abcabcabc") == 3
assert count_distinct_characters('') == 0
assert count_distinct_characters('aaaaaaaaaaaaaaaa') == 1
assert count_distinct_characters("abcaef") == 5
assert count_distinct_characters('a') == 1
assert count_distinct_characters("abcabcabcabc") == 3
assert count_distinct_characters("qwertyuiop") == 10
assert count_distinct_characters("banana") == 3
assert count_distinct_characters("abc") == 3
assert count_distinct_characters("abracadabra") == 5
assert count_distinct_characters("aabbb") == 2
assert count_distinct_characters("aabbbccc") == 3
assert count_distinct_characters("ABCABC") == 3
assert count_distinct_characters("abcdefgh") == 8
assert count_distinct_characters("string") == 6
assert count_distinct_characters('xyz') == 3
assert count_distinct_characters('XYZ') == 3
assert count_distinct_characters('abc') == 3
assert count_distinct_characters('aaa') == 1
assert count_distinct_characters('ab') == 2
assert count_distinct_characters('abcdabcdabcd') == 4
assert count_distinct_characters('abcdefghijklmnopqrstuvwxyz') == 26
assert count_distinct_characters('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 26
assert count_distinct_characters('HELLO') == 4
assert count_distinct_characters('aabc') == 3
assert count_distinct_characters('aba') == 2
assert count_distinct_characters("asd") == 3
assert count_distinct_characters("abcdefabcdef") == 6
assert count_distinct_characters("ABCD") == 4, 'expected 4'
assert count_distinct_characters("") == 0, 'expected 0'
assert count_distinct_characters("a") == 1, 'expected 1'
assert count_distinct_characters("ab") == 2, 'expected 2'
assert count_distinct_characters("aaaaa") == 1
assert count_distinct_characters("bbbbb") == 1
assert count_distinct_characters("ababab") == 2
assert count_distinct_characters("aabbaa") == 2
assert count_distinct_characters('aaaa') == 1
assert count_distinct_characters('oooo') == 1
assert count_distinct_characters("abcdeabcde") == 5
assert count_distinct_characters('abcdefabcdefabc') == 6, 'test 4'
assert count_distinct_characters("aba") == 2
assert count_distinct_characters('abcabcabcabcabc') == 3
assert count_distinct_characters('aaaaaaaa') == 1
assert count_distinct_characters('aaaaaaaaaab') == 2
assert count_distinct_characters("beep") == 3
assert count_distinct_characters("aabbbcccc") == 3
assert count_distinct_characters("aaaaaaaaaa") == 1
assert count_distinct_characters('aa') == 1
assert count_distinct_characters('ABCABCABCABCABC') == 3
assert count_distinct_characters('abcdabcdabcdabcd') == 4
assert count_distinct_characters("abbbb") == 2
assert count_distinct_characters("asdf") == 4
assert count_distinct_characters("asdfa") == 4
assert count_distinct_characters("abcdefa") == 6
assert count_distinct_characters("qwertyuiopasdfghjklzxcvbnm") == 26
assert count_distinct_characters("QWERTYUIOPASDFGHJKLZXCVBNM") == 26
assert count_distinct_characters('banana') == 3
assert count_distinct_characters("abcaabca") == 3
assert count_distinct_characters('aaaaaaaaaaaaaaaaaa') == 1
assert count_distinct_characters("aaaaaa") == 1
assert count_distinct_characters("abca") == 3
assert count_distinct_characters("aaadddd") == 2, "Wrong answer"
assert count_distinct_characters("") == 0, "Wrong answer"
assert count_distinct_characters("aaaaaaaaaaaaaaaaa") == 1, "Slow solution"
assert count_distinct_characters("aaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 2, "Slow solution"
