

def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    for i in range(len(text)):
        if text[i] != text[len(text) - i]:
            return False
    return True
assert is_palindrome('') == True
assert is_palindrome('a') == True
assert is_palindrome('abc') == False
assert is_palindrome('aba') == True
assert is_palindrome('racecar') == True
assert is_palindrome("racecar") == True
assert is_palindrome("madam") == True
assert is_palindrome("level") == True
assert is_palindrome("python") == False
assert is_palindrome("hello") == False
assert is_palindrome("noon") == True
assert is_palindrome("") == True
assert is_palindrome("a") == True
assert is_palindrome("ab") == False
assert is_palindrome("12321") == True
assert is_palindrome("12345") == False
assert is_palindrome("racecar") == True, "Test case 2 failed"
assert is_palindrome("12321") == True, "Test case 3 failed"
assert is_palindrome("python") == False, "Test case 4 failed"
assert is_palindrome('hello') == False
assert is_palindrome('12321') == True
assert is_palindrome('12345') == False
assert is_palindrome(" ") == True
assert is_palindrome('level') == True
assert is_palindrome('ab') == False
assert is_palindrome('abcba') == True
assert is_palindrome('abcdcba') == True
assert is_palindrome("abcba") == True
assert is_palindrome("hello") == False, "Test case 2 failed"
assert is_palindrome('madam') == True
assert is_palindrome('python') == False
assert is_palindrome("deed") == True
assert is_palindrome("level") == True, "Test case 2 failed"
assert is_palindrome("hello") == False, "Test case 3 failed"
assert is_palindrome("racecar") == True, "Test case 4 failed"
assert is_palindrome("python") == False, "Test case 5 failed"
assert is_palindrome('abcdba') == False
assert is_palindrome("world") == False
assert is_palindrome('abba') == True
assert is_palindrome('abcd') == False
assert is_palindrome('aa') == True
assert is_palindrome('abccba') == True
assert is_palindrome("radar") == True
assert is_palindrome("") == True, "Test case 3 failed"
assert is_palindrome("a") == True, "Test case 4 failed"
assert is_palindrome("level") == True, "Test case 5 failed"
assert is_palindrome("abcde") == False
assert is_palindrome('noon') == True
