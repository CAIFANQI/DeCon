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
assert all_prefixes("a") == ["a"]
assert all_prefixes('a') == ["a"]
assert all_prefixes('a') == ['a']
assert all_prefixes('') == []
assert all_prefixes('x') == ['x']
assert all_prefixes('abc') == ['a', 'ab', 'abc']
assert all_prefixes('aaaa') == ['a', 'aa', 'aaa', 'aaaa']
assert all_prefixes("A") == ["A"]
assert all_prefixes("B") == ["B"]
assert all_prefixes("C") == ["C"]
assert all_prefixes("D") == ["D"]
assert sorted(all_prefixes('abcd')) == sorted(['a', 'ab', 'abc', 'abcd'])
assert sorted(all_prefixes('abbb')) == sorted(['a', 'ab', 'abb', 'abbb'])
assert all_prefixes("ACA") == ["A", "AC", "ACA"]
assert all_prefixes('abcd') == ['a', 'ab', 'abc', 'abcd']
assert all_prefixes("a") == ['a']
assert all_prefixes("aaa") == ['a', 'aa', 'aaa']
assert all_prefixes("") == []
assert all_prefixes("a") ==  ["a"]
assert all_prefixes("aaaa") == ["a", "aa", "aaa", "aaaa"]
assert all_prefixes("abcd") == ["a", "ab", "abc", "abcd"]
assert all_prefixes("cd") == ["c", "cd"]
