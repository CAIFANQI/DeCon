

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    return len(set(string))
assert 	count_distinct_characters("abc") == 3, "abc"
assert 	count_distinct_characters("abcabcc") == 3, "abcabcc"
assert 	count_distinct_characters("") == 0, "Empty string"
assert count_distinct_characters('abcde') == 5
assert count_distinct_characters('abcdeab') == 5
assert count_distinct_characters('ABCDE') == 5
assert count_distinct_characters("abcde") == 5
assert count_distinct_characters("") == 0
assert 	count_distinct_characters('a') == 1
assert 	count_distinct_characters('ab') == 2
assert 	count_distinct_characters('abc') == 3
assert count_distinct_characters('') == 0
assert count_distinct_characters('a') == 1
assert count_distinct_characters('abc') == 3
assert count_distinct_characters('ABC') == 3
