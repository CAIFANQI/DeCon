

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
assert same_chars("abc", "cba") == True
assert same_chars("abc", "def") == False
assert same_chars("abc", "abcd") == False
assert same_chars("abc", "ab") == False
assert same_chars("", "") == True
assert same_chars('abc', 'def') == False
assert same_chars('abc', 'ab') == False
assert same_chars('abc', 'abcd') == False
assert same_chars("abc", "def") == False, "Test case 2 failed"
assert same_chars("abc", "ab") == False, "Test case 3 failed"
assert same_chars("abc", "abcd") == False, "Test case 4 failed"
assert same_chars("", "") == True, "Test case 5 failed"
assert same_chars("a", "a") == True, "Test case 6 failed"
assert same_chars("abc", "cab") == True, "Test case 7 failed"
assert same_chars("abc", "abccba") == True
assert same_chars("abcd", "abc") == False
assert same_chars("abc", "cab") == True
assert same_chars('abc', 'def') == False, "Test Case 2 Failed"
assert same_chars('abc', 'ab') == False, "Test Case 3 Failed"
assert same_chars('abc', 'abcd') == False, "Test Case 4 Failed"
assert same_chars('abc', 'abccba') == True, "Test Case 5 Failed"
assert same_chars("abc", "") == False
assert same_chars("", "abc") == False
assert same_chars("abcd", "abcd") == True
assert same_chars("abcd", "abdc") == True
assert same_chars("abcd", "abcde") == False
assert same_chars("abcd", "abcc") == False
assert same_chars('abc', 'def') == False, "Test case 2 failed"
assert same_chars('abc', 'ab') == False, "Test case 3 failed"
assert same_chars('abc', 'abcd') == False, "Test case 4 failed"
assert same_chars("abc", "abc") == True, "Test case 6 failed"
assert same_chars('abc', 'def') == False, 'Test Case 2 Failed'
assert same_chars('abc', 'ab') == False, 'Test Case 3 Failed'
assert same_chars('abc', 'abcd') == False, 'Test Case 4 Failed'
assert same_chars('', '') == True, 'Test Case 5 Failed'
assert same_chars("abc", "cbaabc") == True
assert same_chars("abc", "cba") == True, "Test case 2 failed"
assert same_chars("abc", "def") == False, "Test case 3 failed"
assert same_chars("", "") == True, "Test case 4 failed"
assert same_chars("abc", "abcd") == False, "Test case 5 failed"
assert same_chars('aaa', 'aaa') == True, "Test case 3 failed"
assert same_chars('abc', 'abcd') == False, "Test case 5 failed"
assert same_chars('abc', 'abccba') == True, 'Test Case 4 Failed'
assert same_chars("hello", "hlelo") == True, "Test case 2 failed"
assert same_chars("hello", "hello") == True, "Test case 3 failed"
assert same_chars("hello", "helloworld") == False, "Test case 5 failed"
assert same_chars("a", "a") == True
assert same_chars("abc", "abccba") == True, "Test case 3 failed"
assert same_chars("abc", "abcd") == False, "Test case 3 failed"
assert same_chars("abc", "ab") == False, "Test case 4 failed"
assert same_chars("abc", "acb") == True, "Test case 5 failed"
assert same_chars("ab", "abc") == False
assert same_chars("abc", "abc") == True
assert same_chars("abc", "abc") == True, "Test case 5 failed"
assert same_chars("abc", "abccba") == True, "Test case 4 failed"
assert same_chars("abcd", "dcba") == True
assert same_chars("abcd", "dcb") == False
assert same_chars("abc", "abca") == True
assert same_chars("abc", "a") == False
assert same_chars('abcd', 'abc') == False
assert same_chars('abcd', 'dcba') == True
assert same_chars("hello", "olleh") == True
assert same_chars("hello", "hello") == True
assert same_chars("hello", "olle") == False
assert same_chars("hello", "hell") == False
assert same_chars("hello", "he") == False
assert same_chars('abc', 'abcd') == False, "Test case 3 failed"
assert same_chars('abc', 'ab') == False, "Test case 4 failed"
assert same_chars('', '') == True, "Test case 5 failed"
assert same_chars('abc', 'abccba') == True
assert same_chars('abc', 'aabbcc') == True
assert same_chars("hello", "world") == False
assert same_chars("123", "321") == True
assert same_chars("123", "456") == False
assert same_chars("abc", "def") == False, 'Test Case 2 Failed'
assert same_chars("abc", "abcd") == False, 'Test Case 4 Failed'
