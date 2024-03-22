

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    return len(set(string))
assert count_distinct_characters('ABC') == 3
assert count_distinct_characters('abcdefghijklmnopqrstuvwxyz') == 26
assert count_distinct_characters("abCBA") == 3
assert count_distinct_characters("abc") == 3
assert count_distinct_characters("abcd") == 4
assert count_distinct_characters("abcde") == 5
assert count_distinct_characters("HALlo") == 4
assert count_distinct_characters("HaLlO") == 4
assert count_distinct_characters("a") == 1
assert count_distinct_characters("aba") == 2
assert count_distinct_characters("abba") == 2
assert count_distinct_characters("ABC") == 3
assert count_distinct_characters("abaBc") == 3
assert count_distinct_characters("ab") == 2
assert count_distinct_characters("abaBcDe") == 5
assert count_distinct_characters('abC') == 3, 'The function should return 3 for letters a, b, c, and C'
assert count_distinct_characters('AB') == 2, 'The function should return 2 for letters A and B'
assert count_distinct_characters('ABC') == 3, 'The function should return 3 for letters A, B, C, and C'
assert count_distinct_characters('ABCD') == 4, 'The function should return 4 for letters A, B, C, and D'
assert count_distinct_characters('ABCDE') == 5, 'The function should return 5 for letters A, B, C, D, and E'
assert count_distinct_characters('ABCDEF') == 6, 'The function should return 6 for letters A, B, C, D, E, and F'
assert count_distinct_characters('ABCDEFG') == 7, 'The function should return 7 for letters A, B, C, D, E, and F, and G'
assert count_distinct_characters('ABCDEFGH') == 8
assert count_distinct_characters("abA") == 2
assert count_distinct_characters('abc') == 3
assert count_distinct_characters("") == 0
assert count_distinct_characters("abCA") == 3
assert count_distinct_characters("hELLOooo") == 4
assert count_distinct_characters("abCab") == 3
assert count_distinct_characters("hELLOabaa") == 6
assert count_distinct_characters('abC') == 3
assert count_distinct_characters('aAbC') == 3
assert count_distinct_characters('') == 0
assert count_distinct_characters("abaabc") == 3
assert count_distinct_characters('XabA') == 3
assert count_distinct_characters('abX') == 3
assert count_distinct_characters('abx') == 3
assert count_distinct_characters("abcde") is 5
assert count_distinct_characters("ABCDE") is 5
assert count_distinct_characters("") is 0
assert count_distinct_characters("aBcDe") == 5
assert count_distinct_characters('') == 0, 'There are 0 distinct characters: '
assert count_distinct_characters("Aa") == 1
assert count_distinct_characters("aabc") == 3
assert count_distinct_characters("abcc") == 3
assert count_distinct_characters("aBc") == 3
assert count_distinct_characters("Abc") == 3
assert count_distinct_characters("ABc") == 3
assert count_distinct_characters("aaaaaa") == 1
assert count_distinct_characters("abAab") == 2
assert count_distinct_characters("abBbA") == 2
assert count_distinct_characters("a") is 1
assert count_distinct_characters("A") is 1
assert count_distinct_characters("aa") is 1
assert count_distinct_characters('AabBcC') == 3
assert count_distinct_characters('A') == 1
assert count_distinct_characters('a') == 1
assert count_distinct_characters('ab') == 2
assert count_distinct_characters('aABBcCD') == 4
assert count_distinct_characters('aAabcCd') == 4
assert count_distinct_characters('abc') == 3, 'the result is incorrect'
assert count_distinct_characters('abbb') == 2, 'the result is incorrect'
assert count_distinct_characters('') == 0, 'the result is incorrect'
assert count_distinct_characters('dog') == 3
assert count_distinct_characters('DoG') == 3
assert count_distinct_characters('abbc') == 3
assert count_distinct_characters('abbcc') == 3
assert count_distinct_characters('abbccc') == 3
assert count_distinct_characters('ab') == 2, 'ab should consist of 2 distinct characters'
assert count_distinct_characters('abaB') == 2
assert count_distinct_characters('ababa') == 2
assert count_distinct_characters('abaAa') == 2
assert count_distinct_characters('aBb') is 2
assert count_distinct_characters('aaa') is 1
assert count_distinct_characters('aaaaa') is 1
assert count_distinct_characters("abC") == 3
assert count_distinct_characters('') == 0, 'The result should be 0'
assert count_distinct_characters('abc') == 3, 'The result should be 3'
assert count_distinct_characters('abcabc') == 3, 'The result should be 3'
assert count_distinct_characters("abcA") == 3
assert count_distinct_characters('a') ==  1
assert count_distinct_characters('') ==  0
assert count_distinct_characters('abc') ==  3
assert count_distinct_characters('aBcAb') is 3
assert count_distinct_characters('AB') == 2
assert count_distinct_characters('abcd') == 4
assert count_distinct_characters('abbbc') == 3
assert count_distinct_characters('abBcD') == 4
assert count_distinct_characters("abBcD") == 4
assert count_distinct_characters("c") == 1
assert count_distinct_characters("abd") == 3
assert count_distinct_characters("abccde") == 5
assert count_distinct_characters("abacab") == 3
