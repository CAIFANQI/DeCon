from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) > maxlen:
            return s
assert longest(['', '']) == ''
assert longest(['a', 'aa', 'aaa', 'aaaa']) == 'aaaa'
assert longest(['', 'a', '']) == 'a'
assert longest(['', '', '']) == ''
assert longest([]) is None
assert longest(["asdf", "asdf"]) == "asdf"
assert longest(["asdf"]) == "asdf"
assert longest(["", "asdf", "sdfasdf"]) == "sdfasdf"
assert longest(["", ""]) == ""
assert longest(["", "a", "a"]) == "a"
assert longest(["", "", "", ""]) == ""
assert longest(["a", "abc", "abdc", "abcde"]) == "abcde"
assert longest(["abc", "abdc", "abce", "abcdef"]) == "abcdef"
assert longest(["abc", "abdc", "abcde", "abcdef"]) == "abcdef"
assert longest(["abc", "abdc", "abcdef", "abcd"]) == "abcdef"
assert longest(['a', 'aa', 'aaa', 'aaaa', 'aaaaa']) == 'aaaaa'
assert longest(['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa']) == 'aaaaaa'
assert longest(['abcde', 'abc', 'ab']) == 'abcde'
assert longest(['a', 'ab', 'abc', 'd', 'cd', 'bcd', 'abcd', 'abcde', 'abcdef']) == 'abcdef'
assert longest(["c", "a", "b", "a"]) == "c"
assert longest(["hi", "hell", "he", "hello"]) == "hello"
assert longest(["hi", "hell", "hello"]) == "hello"
assert longest(["hi", "hello"]) == "hello"
assert longest(["hello", "hi", "he", "hell", "hello"]) == "hello"
assert longest(["hello", "hello"]) == "hello"
assert longest([]) == None
assert longest(["hi", "hi"]) == "hi"
assert longest(['a']) == 'a'
assert longest(['abcd', 'abcdefghijklmnopqrstuvwxyz']) == 'abcdefghijklmnopqrstuvwxyz'
assert 	longest(["asdf", "as", "asdf"]) == "asdf"
assert 	longest(["asdf", "as", "df", "asdf"]) == "asdf"
assert 	longest(["asdf", "as", "df", "asdf", "as"]) == "asdf"
assert 	longest(["asdf", "as", "df", "asdf", "as", "asdf"]) == "asdf"
assert 	longest(["asdf", "as", "df", "asdf", "as", "asdf", "asdf"]) == "asdf"
assert 	longest(["asdf", "as", "df", "asdf", "as", "asdf", "asdf", "asdf", "asdf", "asdf"]) == "asdf"
assert longest(['abc', 'abc']) == 'abc'
assert longest(['abc', 'ab']) == 'abc'
assert longest(['a', 'abc', 'ab', 'd', '', '1', 'a', 'xz', 'bc', '', '']) == 'abc'
assert longest(['', '', 'ab', '', '']) == 'ab'
assert longest(['', '', '', 'ab']) == 'ab'
assert longest(['', '', '', 'ab', '', 'ab']) == 'ab'
assert longest(['', '', '', '', 'ab', '', 'ab']) == 'ab'
assert longest(['', '', '', '', '', 'ab', '', 'ab']) == 'ab'
assert longest(['', '', '', '', '', '', 'ab', '', 'ab']) == 'ab'
assert longest(['', '', '', '', '', '', '', 'ab', '', 'ab']) == 'ab'
assert longest(["", "hello", "hey", "world"]) == "hello"
assert longest(["aa", "aa"]) == "aa"
assert longest(["b", "c"]) == "b"
assert longest(["a", "bbbbb", "c"]) == "bbbbb"
assert longest(["a", "aaa", "bbbbb"]) == "bbbbb"
assert longest(["a", "aaa", "bbbbb", "c"]) == "bbbbb"
assert longest(["a", "b", "c"]) == "a"
assert longest(["a"]) == "a"
assert longest(["d", "a", "bc", "d", "qwertqw"]) == "qwertqw"
assert longest(["d", "a", "bc", "d", "qwertqw", "a", "abcdef"]) == "qwertqw"
assert longest(["world", "hello", "hi"]) == "world"
assert longest(["world", "hello", "world"]) == "world"
assert longest(["hello", "hi", "world"]) == "hello"
assert 	longest(["a", "test", "apple", "seattle", "banana"]) == "seattle"
assert 	longest([]) == None
assert longest(['1234', '12', '1', '12', '123']) == '1234'
assert longest(['123', '12', '1', '12', '123']) == '123'
assert longest(['123', '12', '1', '12', '1']) == '123'
assert longest(['1', '12', '12', '123', '1234', '12345', '123456']) == '123456'
assert longest(['1', '12', '12', '12']) == '12'
assert longest(['abcd', 'abc', 'ab']) == 'abcd'
assert longest(['ab', 'a']) == 'ab'
assert longest(['a', 'b']) == 'a'
assert 	longest(["a", "b", "ccc"]) == "ccc"
assert 	longest(["c", ""]) == "c"
assert 	longest(["a", "a", "a", "a", "a", "a"]) == "a"
