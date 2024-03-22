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
assert "foo" == longest(["foo", "bar", "foo"])
assert "foo" == longest(["foo"])
assert longest(["a", "b", "ab", "c"]) == "ab"
assert longest(["a", "ab"]) == "ab"
assert longest(["ab", "b"]) == "ab"
assert longest(["a", "ab", "b"]) == "ab"
assert longest([]) is None
assert longest(["foo"]) == "foo"
assert longest(["bar", "baz"]) == "bar"
assert longest(["foo", "foo", "foo"]) == "foo"
assert longest(["foo", "foo", "bar"]) == "foo"
assert longest(["foo", "foo", "foo", "foo"]) == "foo"
assert longest(["foo", "foo", "foo", "bar", "bar", "bar", "bar"]) == "foo"
assert longest(["foo", "foo", "foo", "foo", "bar", "bar", "bar", "bar", "bar"]) == "foo"
assert longest(["foo", "foo", "foo", "foo", "bar", "bar", "bar", "bar", "bar", "bar"]) == "foo"
assert "ABC" == longest(["ABC", "ABC", "ABC"])
assert "ABC" == longest(["ABC", "ABC"])
assert "ABC" == longest(["ABC", "ABC", "ABC", "ABC"])
assert longest(["hey"]) == "hey"
assert longest(["hi"]) == "hi"
assert longest(["hi", "hi", "hi"]) == "hi"
assert longest(["hi", "hi", "hi", "bye"]) == "bye"
assert longest(["hi", "hi", "hi", "bye", "bye", "bye"]) == "bye"
assert longest(["abc"]) == "abc"
assert longest(["a", "bc", "c"]) == "bc"
assert longest(["abcdefghijklmnopqrstuvwxyz"]) == "abcdefghijklmnopqrstuvwxyz"
assert longest(["a"]) == "a"
assert longest(["a", "a", "b"]) == "a"
assert longest(["a", "b", "a", "b"]) == "a"
assert longest(['ab']) == 'ab'
assert longest(['aaaaaa', 'aaaaaaa']) == 'aaaaaaa'
assert longest(['aaaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaa']) == 'aaaaaaa'
assert longest(['a', 'aaaa', 'aaaaa', 'aaaaaaa', 'aaaaaa']) == 'aaaaaaa'
assert longest(['a', 'ab', 'abc', 'abcd', 'abcde']) == 'abcde'
assert longest(['a', 'ab', 'abd', 'abc', 'abcd']) == 'abcd'
assert longest(["1"]) == "1"
assert 'Hello World' == longest(['Hello World'])
assert None == longest([])
assert 'a' == longest(['a'])
assert longest(["a", "a"]) == "a"
assert longest(["a", "b"]) == "a"
assert longest(["a", "b", "c"]) == "a"
assert longest(["abc", "de", "ghi"]) == "abc"
assert longest(['abc']) == 'abc'
assert longest(['ab', 'c', 'de', 'hij', 'klmnopqrstuvwxyz']) == 'klmnopqrstuvwxyz'
assert longest(["aba"]) == "aba"
assert longest(["aba", "aba", "aba", "aba"]) == "aba"
assert longest(["aba", "aba", "aba", "aba", "aba"]) == "aba"
assert longest(["aba", "aba", "aba", "aba", "aba", "aba"]) == "aba"
assert longest(["abc", "abcd"]) == "abcd"
assert longest(["aaaaa", "aa"]) == "aaaaa"
assert longest(["aaaaa", "a"]) == "aaaaa"
assert longest(["ab", "aba"]) == "aba"
assert longest(["ab", "a"]) == "ab"
assert longest(["ab", "b", "aba", "bb"]) == "aba"
assert longest(["ab", "ab", "aba"]) == "aba"
assert longest(["ab", "ab", "a"]) == "ab"
assert longest(["ab", "ab"]) == "ab"
assert longest(["abc", "a", "b"]) == "abc"
assert longest(["abc", "a", "b", "c"]) == "abc"
assert longest(["abc", "abc", "abc"]) == "abc"
assert longest(["abc", "abc", "abc", "abc"]) == "abc"
assert longest(["abc", "abc", "abc", "abc", "", "abc"]) == "abc"
assert longest(["cat", "a", "dog", "cat"]) == "cat"
assert longest(['']) == ''
assert longest(['hi']) == 'hi'
assert longest(["test", "tester"]) == "tester"
assert longest(["test", "testers", "testers"]) == "testers"
assert longest(['ab', 'aaa']) == 'aaa'
assert longest(['aaa', 'aa', 'aaa', 'aaaaaaa', 'aaaaaa']) == 'aaaaaaa'
assert longest(['ab', 'ab', 'ab']) == 'ab'
assert longest(["ab"]) == "ab"
assert longest(["a", "b", "a"]) == "a"
assert longest(["ab", "ac"]) == "ab"
assert longest(["a", "c", "a", "b", "a"]) == "a"
assert longest(["aaa", "aaa"]) == "aaa"
assert longest(["aaaaaaa", "aaa"]) == "aaaaaaa"
assert longest(["aaaaaaa"]) == "aaaaaaa"
assert longest(['', 'bc']) == 'bc'
assert longest(["ab", "ab", "ab"]) == "ab"
assert longest(["a", "bb", "c"]) == "bb"
assert longest(["a", "aa", "bb", "ccc"]) == "ccc"
assert longest(['this', 'is', 'a','string']) =='string'
assert longest(['this', 'is', 'a','string', 'an']) =='string'
assert longest(['this', 'is', 'a','string', 'an','string','string']) =='string'
assert longest(['hello', 'and', 'hello', 'world']) == 'hello', 'it should return "hello"'
assert longest(['', 'hello', 'world']) == 'hello', 'it should return "hello"'
assert "abcbc" == longest(["abc", "abcbc", "abc", "abc"])
assert longest(["bb", "ccc", "dddd", "eee"]) == "dddd"
assert longest(["a", "b", "ccc", "dddd", "eee", "ffff"]) == "dddd"
assert longest(['ab', 'bc']) == 'ab'
assert longest(["test string"]) == "test string"
assert 'a' == longest(['a', 'b'])
assert longest(["abc", "abc", "abc", "aef"]) == "abc"
assert longest(["abcdef"]) == "abcdef"
assert longest(["hello"]) == "hello"
assert longest(['abc', 'abbb']) == 'abbb'
assert longest(["ab", "ab", "abc"]) == "abc"
assert "abcdef" == longest(["abcdef"])
assert longest(["abc", "ac", "ab"]) == "abc"
assert longest(["a1", "a2", "a3"]) == "a1"
assert longest(["aa", "aa", "aa"]) == "aa"
assert longest(['aaaa', 'bbbb', 'abcde']) == 'abcde'
