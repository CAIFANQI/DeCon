from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [x for x in strings if x in substring]
assert 	filter_by_substring(['Hello', 'Hello', 'World'], 'Hello') == ['Hello', 'Hello']
assert filter_by_substring(["hello", "world", "this", "is", "me"], "wor") == ["world"]
assert filter_by_substring(["hello", "world", "this", "is", "me"], "") == ["hello", "world", "this", "is", "me"]
assert filter_by_substring(["hello", "world", "this", "is", "me"], "qwerty") == []
assert 	filter_by_substring(['hello', 'goodbye', 'hello again'], 'hello') == ['hello', 'hello again']
assert 	filter_by_substring(['cobra', 'caesar', 'viper','sidewinder', 'viper'], 'caesar') == ['caesar']
assert 	filter_by_substring(['cobra', 'caesar', 'viper','sidewinder', 'viper'], 'viper') == ['viper', 'viper']
assert 	filter_by_substring(['cobra', 'caesar', 'viper','sidewinder', 'viper'], 'cobra') == ['cobra']
assert 	filter_by_substring(['cobra', 'caesar', 'viper','sidewinder', 'viper'],'sidewinder') == ['sidewinder']
assert 	filter_by_substring(['cobra', 'caesar', 'viper','sidewinder', 'viper'],'sida') == []
assert 	filter_by_substring(["foo", "bar", "foobar"], "baz") == []
assert 	filter_by_substring(["foo", "bar", "foobar"], "foobar") == ["foobar"]
assert 	filter_by_substring(["foo", "bar", "foobar"], "foobarbaz") == []
assert 	filter_by_substring(["foo", "bar", "foobar"], "foobaz") == []
assert filter_by_substring(["abc", "", "a", "1234", "a", "z", "", "abcd"], "1234") == ["1234"]
assert filter_by_substring(["abcd", "1234", "a", "z", "", "abcd"], "1234") == ["1234"]
assert 	filter_by_substring(["Python", "Ruby", "JavaScript", "Ruby"], "Java") == ["JavaScript"]
assert filter_by_substring(['abc', 'xyz', 'acd', 'acdf'], 'cd') == ['acd', 'acdf']
assert filter_by_substring(['abc', 'xyz', 'acd', 'acdf'], 'abz') == []
assert filter_by_substring(['abc', 'xyz', 'acd', 'acdf'], 'cdx') == []
assert filter_by_substring(['abc', 'xyz', 'acd', 'acdf'], 'acdf') == ['acdf']
assert filter_by_substring(["I am a teacher", "I am a student at ABC", "I am a student at DEF"], "student") == ["I am a student at ABC", "I am a student at DEF"]
assert filter_by_substring(["I am a teacher", "I am a student at ABC", "I am a student at DEF"], "teacher") == ["I am a teacher"]
assert filter_by_substring(["I am a teacher", "I am a student at ABC", "I am a student at DEF"], "") == ["I am a teacher", "I am a student at ABC", "I am a student at DEF"]
assert filter_by_substring(["I am a teacher", "I am a student at ABC", "I am a student at DEF"], "I am a") == ["I am a teacher", "I am a student at ABC", "I am a student at DEF"]
assert filter_by_substring(["hello", "word", "world"], "hello") == ["hello"]
assert filter_by_substring(["hello", "word", "world"], "zoo") == []
assert filter_by_substring(['h', 'a', 'b','s', 'w', 'a'], 'c') == []
assert filter_by_substring(['h', 'a', 'b','s', 'w', 'a'], '') == ['h', 'a', 'b','s', 'w', 'a']
assert filter_by_substring(['h', 'a', 'b','s', 'w', 'a'], 'q') == []
assert filter_by_substring(['h', 'a', 'b','s', 'w', 'a'], 'h') == ['h']
