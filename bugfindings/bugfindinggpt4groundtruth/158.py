
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    return sorted(words)[0]
assert 	find_max(['one', 'two', 'one']) == 'one'
assert 	find_max(['one', 'two', 'two', 'three']) == 'three'
assert 	find_max(['abb', 'abb', 'abb', 'abb']) == 'abb'
assert 	find_max(['abc', 'a', 'b', 'c']) == 'abc'
assert 	(find_max(['abc', 'a', 'b']) == 'abc'), 'error2'
assert 	(find_max(['abcd', 'abc', 'ab', 'a']) == 'abcd'), 'error3'
assert 	find_max(['abc', 'def', 'abc', 'ghi']) == 'abc'
assert 	find_max(['abc', 'def', 'abc', 'ghi', 'jkl']) == 'abc'
assert 	find_max(['abc', 'def', 'abc', 'ghi', 'jkl', 'abc']) == 'abc'
assert 	find_max(['abc', 'def', 'abc', 'ghi', 'jkl','mno']) == 'abc'
assert 	find_max(["a", "a", "a", "b", "c"]) == "a"
assert find_max(["c", "c++", "java", "python", "python", "python", "python"]) == "python"
assert 	find_max(['a', 'b', 'c', 'a', 'b', 'c', 'a']) == 'a'
assert 	find_max(['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'f']) == 'a'
