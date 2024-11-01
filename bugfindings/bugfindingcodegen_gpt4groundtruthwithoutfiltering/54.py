

def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    return s0 == s1
assert 	same_chars("apple", "app") == False, 'error2'
assert 	same_chars("aa", "aaaa") == True, 'error3'
assert 	same_chars("", "") == True, 'error4'
assert 	same_chars("a", "") == False, 'error5'
assert 	same_chars("aa", "") == False, 'error6'
assert 	same_chars("ab", "a") == False, 'error7'
assert 	same_chars("abb", "a") == False, 'error9'
assert 	same_chars("abb", "abb") == True, 'error10'
assert 	same_chars("abb", "b") == False, 'error11'
assert 	same_chars("abb", "a") == False, 'error12'
assert 	same_chars("abab", "aab") == True, 'error14'
assert same_chars('joseph', 'joseph') == True
assert same_chars('joseph', 'jo') == False
assert same_chars('joseph', 'Joseph') == False
