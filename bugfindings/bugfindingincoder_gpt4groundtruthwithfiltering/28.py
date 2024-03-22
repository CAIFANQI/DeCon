from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ' '.join(strings)
assert concatenate(["a", "b"]) == "ab"
assert concatenate(["a", "b", "c"]) == "abc"
assert concatenate(["a", "b", "c", "d"]) == "abcd"
assert concatenate(["a"]) == "a"
assert concatenate(["", "", ""]) == ""
assert concatenate(["", ""]) == ""
assert concatenate(["", "", "abc"]) == "abc"
assert concatenate(["", "", "abc", "def"]) == "abcdef"
assert concatenate(["", "", "abc", "def", "ghi"]) == "abcdefghi"
assert concatenate(["", "", "", "abc", "def", "ghi"]) == "abcdefghi"
assert concatenate(["", "a"]) == "a"
assert concatenate(["", "a", "b"]) == "ab"
assert concatenate(["", "a", "b", "c"]) == "abc"
assert concatenate("foo") == "foo"
assert concatenate(["", "c"]) == "c"
assert concatenate(["a", ""]) == "a"
assert concatenate(["a", "b", ""]) == "ab"
assert concatenate(["a", "b", "", "c"]) == "abc"
assert concatenate(["", "hello", "", "world"]) == "helloworld"
assert concatenate(["", "hello", "world"]) == "helloworld"
assert concatenate([""]) == ""
assert concatenate(["", "hi", "world"]) == "hiworld"
assert concatenate(["", "", "world"]) == "world"
assert concatenate(["", "", "world", ""]) == "world"
assert concatenate(["", "", "world", "hi"]) == "worldhi"
assert concatenate(["", "", "", ""]) == ""
assert concatenate(["", "", "", "", ""]) == ""
assert concatenate(["", "", "", "", "", ""]) == ""
assert concatenate(["", "hello", "world", "!"]) == "helloworld!"
assert concatenate(["hello", "", "world"]) == "helloworld"
assert concatenate(["hello", ""]) == "hello"
assert concatenate(["world"]) == "world"
assert concatenate([]) == ""
assert concatenate(["", "hi"]) == "hi"
assert concatenate(["", "hi", ""]) == "hi"
assert concatenate(["", "", "hi"]) == "hi"
assert concatenate(["", "a", "b", "", "c"]) == "abc"
assert concatenate(["", "a", "b", "", "c", "", "d", ""]) == "abcd"
assert concatenate(["", "a", "b", ""]) == "ab"
assert concatenate("Hello") == "".join(["H", "e", "l", "l", "o"])
assert concatenate(["abc", "", "def"]) == "abcdef"
assert concatenate(["abc", "def", "ghi"]) == "abcdefghi"
assert concatenate(["", "abc", "", "def", "ghi"]) == "abcdefghi"
assert concatenate(["", "test", "abc"]) == "testabc", ""
assert concatenate(["", "test", "abc", "def"]) == "testabcdef", ""
assert concatenate(["", "test", "abc", "def", "ghi"]) == "testabcdefghi", ""
assert concatenate(["", "a", "", "bb"]) == "a" + "bb"
assert concatenate(["", "a", "", "bb", "cc"]) == "a" + "bb" + "cc"
assert concatenate(['a']) == 'a'
assert concatenate(["a", "b", "c"]) == ("a" + "b" + "c")
assert concatenate(["", "abc", "", ""]) == "abc"
assert concatenate(["", " "]) == " "
assert concatenate(["", "1"]) == "1"
assert concatenate(["", "", "orange"]) == "orange"
assert concatenate(["", "hi", "there"]) == "hithere"
assert concatenate("abc") == "abc"
assert concatenate(["", "a", "b", "c", "", "d", "e", "f"]) == "abcdef"
assert concatenate(["", "", "", "", "", "", ""]) == ""
assert concatenate(["", "hi", "", "there", "", ""]) == "hithere"
assert concatenate(["1", "2"]) == "12"
assert concatenate('Hello world') == 'Hello world'
