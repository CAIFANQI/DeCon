from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    result = []

    for i in range(len(string)-1):
        result.append(string[:i+1])
    return result
assert 	all_prefixes("abcd") == ["a", "ab", "abc", "abcd"]
assert 	all_prefixes("a") == ["a"]
assert 	all_prefixes('') == []
assert 	all_prefixes('a') == ['a']
assert 	all_prefixes('ab') == ['a', 'ab']
assert 	all_prefixes('abx') == ['a', 'ab', 'abx']
assert 	all_prefixes('xyz') == ['x', 'xy', 'xyz']
assert 	all_prefixes('abc') == ['a', 'ab', 'abc']
assert 	all_prefixes('abcd') == ['a', 'ab', 'abc', 'abcd']
assert 	all_prefixes('abcdec') == ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdec']
assert 	all_prefixes("abcde") == ["a", "ab", "abc", "abcd", "abcde"]
assert 	all_prefixes("ab") == ["a", "ab"]
assert 	all_prefixes("") == []
assert all_prefixes('') == []
assert all_prefixes('a') == ['a']
assert all_prefixes('abc') == ['a', 'ab', 'abc']
assert all_prefixes("aab") == ["a", "aa", "aab"]
