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
assert all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]
assert all_prefixes("12345") == ["1", "12", "123", "1234", "12345"]
assert all_prefixes("a") == ["a"]
assert all_prefixes("") == []
assert all_prefixes("python") == ["p", "py", "pyt", "pyth", "pytho", "python"]
assert all_prefixes("python") == ['p', 'py', 'pyt', 'pyth', 'pytho', 'python']
assert all_prefixes("a") == ['a']
assert all_prefixes("code") == ["c", "co", "cod", "code"]
assert all_prefixes('a') == ['a']
assert all_prefixes('abc') == ['a', 'ab', 'abc']
assert all_prefixes('hello') == ['h', 'he', 'hel', 'hell', 'hello']
assert all_prefixes("abc") == ["a", "ab", "abc"]
assert all_prefixes('') == []
assert all_prefixes("hello") == ['h', 'he', 'hel', 'hell', 'hello']
assert all_prefixes("programming") == ['p', 'pr', 'pro', 'prog', 'progr', 'progra', 'program', 'programm', 'programmi', 'programmin', 'programming']
assert all_prefixes("prefix") == ["p", "pr", "pre", "pref", "prefi", "prefix"]
assert all_prefixes("abcde") == ["a", "ab", "abc", "abcd", "abcde"]
assert all_prefixes("programming") == ["p", "pr", "pro", "prog", "progr", "progra", "program", "programm", "programmi", "programmin", "programming"]
assert all_prefixes("abcdefg") == ["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg"]
assert all_prefixes("ab") == ["a", "ab"]
assert all_prefixes("abcd") == ["a", "ab", "abc", "abcd"]
assert all_prefixes("world") == ["w", "wo", "wor", "worl", "world"]
