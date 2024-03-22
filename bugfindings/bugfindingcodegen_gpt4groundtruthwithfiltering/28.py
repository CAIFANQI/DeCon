from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ' '.join(strings)
assert 	concatenate(['a', 'b', 'c']) == 'abc'
assert 	concatenate(['a', 'b', 'c', 'd', 'e']) == 'abcde'
assert 	concatenate(['a', 'b', 'c', 'd', 'e', 'f']) == 'abcdef'
assert 	concatenate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == 'abcdefghij'
assert 	concatenate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']) == 'abcdefghijkl'
assert 	concatenate(['abc', 'def']) == 'abcdef'
assert 	concatenate(['abc', 'def', 'ghi']) == 'abcdefghi'
assert 	concatenate(['abc', 'def', 'ghi', 'jkl']) == 'abcdefghijkl'
assert 	concatenate(['abc', 'def', 'ghi', 'jkl','mno']) == 'abcdefghijklmno'
assert 	concatenate(["abc", "def", "ghi"]) == "abcdefghi"
assert 	concatenate(["abc", "def", "ghi", ""]) == "abcdefghi"
assert 	concatenate([]) == ""
assert 	concatenate([""]) == ""
assert 	concatenate([" "]) == " "
assert 	concatenate(["a ", "b "]) == "a b "
assert 	concatenate(["a ", "b ", "c "]) == "a b c "
assert 	concatenate(["a ", "b ", "c ", "d "]) == "a b c d "
assert 	concatenate(["a ", "b ", "c ", "d ", ""]) == "a b c d "
assert 	concatenate(["a ", "b ", "c ", "d ", "e "]) == "a b c d e "
assert 	concatenate(["a ", "b ", "c ", "d ", "e ", ""]) == "a b c d e "
assert 	concatenate(["this", "is", "a", "list"]) == "thisisalist"
assert 	concatenate(["a", "b"]) == "ab"
assert 	concatenate(["a", ""]) == "a"
assert 	concatenate(["a"]) == "a"
assert 	concatenate(["", ""]) == ""
assert 	concatenate(["a", "b", "c", "d"]) == "abcd"
assert 	concatenate(["ab", "cd"]) == "abcd"
assert 	concatenate(["ab", "cd", ""]) == "abcd"
assert 	concatenate(["ab", "cd", "ef", ""]) == "abcdef"
assert 	concatenate(["ab", "cd", "ef", "g", ""]) == "abcdefg"
assert 	concatenate(["ab", "cd", "ef", "g", "hi", ""]) == "abcdefghi"
assert 	concatenate(['abc', '123', 'def']) == 'abc123def', "Wrong result for ['abc', '123', 'def']"
assert 	concatenate(['abc']) == 'abc', "Wrong result for ['abc']"
assert 	concatenate(["", ""]) == "", "Wrong result"
assert 	concatenate(["1", "2", "3", "4"]) == "1234", "Wrong result"
assert 	concatenate(["four", "five", "six"]) == "fourfivesix"
assert 	concatenate(["seven", "eight", "nine"]) == "seveneightnine"
assert 	concatenate(["ten", "eleven", "twelve"]) == "teneleventwelve"
assert 	concatenate(["thirteen", "fourteen", "fifteen"]) == "thirteenfourteenfifteen"
assert 	concatenate(["sixteen", "seventeen", "eighteen"]) == "sixteenseventeeneighteen"
assert concatenate(["!", "!", "!"]) == "!!!"
assert 	concatenate(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]) == "abcdefghij"
assert 	concatenate(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]) == "abcdefghijklmnop"
assert 	concatenate(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]) == "abcdefghijklmnopqrstuvwxyz"
assert concatenate([]) == ""
assert concatenate(["", "", "", "", "", "", "", ""]) == ""
assert concatenate(["", "a", "", "", "", "", "", "", "b", ""]) == "ab"
assert concatenate(["", "", "", "", "", "", "", "", "", ""]) == ""
assert concatenate(["", "ab", "", "", "", "", "", "", "", ""]) == "ab"
assert concatenate(["", "", "ab", "", "", "", "", "", "", "", ""]) == "ab"
assert concatenate(["", "", "", "ab", "", "", "", "", "", "", ""]) == "ab"
assert concatenate(["", "", "", "", "ab", "", "", "", "", "", ""]) == "ab"
assert concatenate(["", "", "", "", "", "ab", "", "", "", "", ""]) == "ab"
assert concatenate(["", "", "", "", "", "", "ab", "", "", "", ""]) == "ab"
assert 	concatenate(["w", "o", "r", "l", "d"]) == "world", "ERROR"
assert 	concatenate(["d", "o", "y"]) == "doy", "ERROR"
assert 	concatenate(["a"]) == "a", "error"
assert 	concatenate([]) == "", "error"
assert 	concatenate(["a","b"]) == "ab", "error"
assert 	concatenate(["", "world", ""]) == "world"
assert 	concatenate(["Hello"]) == "Hello"
assert 	concatenate(["Hello", ""]) == "Hello"
assert 	concatenate(["hello", ""]) == "hello"
assert 	concatenate(["", "world"]) == "world"
assert 	concatenate(["a"]) 	== "a", "a"
assert 	concatenate([""]) 	== "", "empty"
assert 	concatenate(["Hello", ",", "world", "!"]) == "Hello,world!", "should be Hello,world!"
assert 	concatenate(['foo', 'bar', 'baz']) == 'foobarbaz'
assert 	concatenate(["foo", "bar", "baz"]) == "foobarbaz"
assert 	concatenate(["foo", "bar", "baz", "quux"]) == "foobarbazquux"
assert 	concatenate(["Hello ", "world"]) == "Hello world"
assert 	concatenate(["1", "2", "3", "4"]) == "1234"
assert 	concatenate(["5", "6"]) == "56"
assert 	concatenate([" ", "a", ""]) == " a"
