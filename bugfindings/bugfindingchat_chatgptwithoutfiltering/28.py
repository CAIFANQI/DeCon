from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ' '.join(strings)
assert concatenate(["hello", "world"]) == "helloworld"
assert concatenate(["hello", " ", "world"]) == "hello world"
assert concatenate([""]) == ""
assert concatenate(["hello"]) == "hello"
assert concatenate(['hello', ' ', 'world']) == 'hello world'
assert concatenate(['hello', 'world', '!']) == 'helloworld!'
assert concatenate(['foo', 'bar', 'baz']) == 'foobarbaz'
assert concatenate(['', '']) == ''
assert concatenate([]) == ''
assert concatenate(["one", "two", "three"]) == "onetwothree"
assert concatenate(["this", "is", "a", "test"]) == "thisisatest"
assert concatenate(['hello']) == 'hello'
assert concatenate(["a", "b", "c"]) == "abc"
assert concatenate(["", "x", "y"]) == "xy"
assert concatenate(['hello', ' ', 'world', '!']) == 'hello world!'
assert concatenate(["I", "am", "a", "programmer"]) == "Iamaprogrammer"
assert concatenate([]) == ""
assert concatenate(['abc', 'def', 'ghi']) == 'abcdefghi'
assert concatenate(['']) == ''
assert concatenate(['python', 'is', 'awesome']) == 'pythonisawesome'
assert concatenate(['this', 'is', 'a', 'test']) == 'thisisatest'
assert concatenate(["good", "morning"]) == "goodmorning"
assert concatenate(["python", "is", "fun"]) == "pythonisfun"
assert concatenate(["foo", "bar"]) == "foobar"
assert concatenate(["abc", "def", "ghi"]) == "abcdefghi"
assert concatenate(['Hello', ' ', 'World']) == 'Hello World'
assert concatenate(['Hello', '', 'World']) == 'HelloWorld'
assert concatenate(['abc', 'def', 'ghi', 'jkl']) == 'abcdefghijkl'
assert concatenate(["This", " ", "is", " ", "a", " ", "test"]) == "This is a test"
assert concatenate(['good', 'morning']) == 'goodmorning'
assert concatenate(['how', 'are', 'you']) == 'howareyou'
assert concatenate(['a', 'b', 'c']) == 'abc'
assert concatenate(['', '', '']) == ''
assert concatenate(['a', 'b', 'c', 'd', 'e']) == 'abcde'
assert concatenate(['hello', '', 'world']) == 'helloworld'
assert concatenate(["foo", "bar", "baz"]) == "foobarbaz"
assert concatenate(["baz"]) == "baz"
assert concatenate(['a', 'b', 'c', 'd']) == 'abcd'
assert concatenate(["", ""]) == ""
assert concatenate(["hello", "", "world"]) == "helloworld"
assert concatenate(['1', '2', '3']) == '123'
assert concatenate(['cat', 'dog', 'mouse']) == 'catdogmouse'
assert concatenate(['apple', 'banana', 'orange']) == 'applebananaorange'
assert concatenate(['foo', 'bar']) == 'foobar'
assert concatenate(["hello", " ", "world", "!"]) == "hello world!"
assert concatenate(['123', '456', '789']) == '123456789'
assert concatenate(["python", "is", "awesome"]) == "pythonisawesome"
assert concatenate(['one', 'two', 'three']) == 'onetwothree'
assert concatenate(["I", "am", "learning", "Python"]) == "IamlearningPython"
assert concatenate(["This", "is", "a", "test"]) == "Thisisatest"
assert concatenate(["1", "2", "3"]) == "123"
assert concatenate(['hello', 'world', '!', '']) == 'helloworld!'
assert concatenate(['', 'hello', 'world']) == 'helloworld'
assert concatenate(['one']) == 'one'
assert concatenate(["1", "2", "3", "4"]) == "1234"
assert concatenate(['python', 'is', 'great']) == 'pythonisgreat'
assert concatenate(['I', 'love', 'coding']) == 'Ilovecoding'
assert concatenate(["", "hello", "world"]) == "helloworld"
