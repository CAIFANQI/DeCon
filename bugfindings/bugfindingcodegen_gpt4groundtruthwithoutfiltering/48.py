

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
assert is_palindrome("") == True
assert is_palindrome("aa") == True
assert is_palindrome("123454321") == True
assert is_palindrome("abc") == False
assert is_palindrome("abcba") == True
assert is_palindrome("abcbbba") == False
assert is_palindrome("abcbbbbaa") == False
assert is_palindrome("abcbbbbaaA") == False
assert 	is_palindrome("abba") == True
assert 	is_palindrome("abababa") == True
assert 	is_palindrome("abababababa") == True
assert 	is_palindrome("abc") == False
assert 	is_palindrome("a") == True
assert 	is_palindrome("aa") == True
assert 	is_palindrome("aaa") == True
assert 	is_palindrome("aaaa") == True
assert 	is_palindrome("") == True
assert 	is_palindrome("a" * 1000 + "b" * 9000 + "a" * 1000) == True
assert 	is_palindrome('abba') == True
assert 	is_palindrome('abacaba') == True
assert 	is_palindrome('a') == True
assert 	is_palindrome('ab') == False
assert 	is_palindrome('') == True
assert 	is_palindrome(' ') == True
assert 	is_palindrome('1a') == False
assert 	is_palindrome('a1') == False
assert 	is_palindrome('aa1') == False
assert 	is_palindrome('aa1a') == False
assert 	is_palindrome('1a1a') == False
assert 	is_palindrome("kajak") == True
assert 	is_palindrome("race a car") == False
assert 	is_palindrome("hello") == False
assert is_palindrome('') == True, 'Empty string'
assert is_palindrome('abccba') == True, 'Odd length'
assert is_palindrome('a') == True, 'One char'
assert is_palindrome('aa') == True, 'Even length'
assert is_palindrome('aba') == True, 'Even length, first and last chars are different'
assert is_palindrome('abcba') == True, 'Even length, first and last chars are different'
assert is_palindrome('a c') == False, 'Even length, first and last chars are different'
assert is_palindrome('abacaba') == True, 'Even length, multiple occurences of the same character'
assert is_palindrome('abb') == False, 'Even length, multiple occurences of the same character'
assert is_palindrome('abc') == False, 'Even length, multiple occurences of the same character'
assert is_palindrome('ab') == False, 'Odd length, first and last chars are the same'
assert is_palindrome('') == True,'should be True'
assert is_palindrome('a') == True,'should be True'
assert is_palindrome('aa') == True,'should be True'
assert is_palindrome('aba') == True,'should be True'
assert is_palindrome('abba') == True,'should be True'
assert is_palindrome('amanaplanacanalpanama') == True,'should be True'
assert is_palindrome('abcdefgh') == False,'should be False'
assert is_palindrome('123454321') == True,'should be True'
assert is_palindrome('123454322') == False,'should be False'
assert is_palindrome('11112222') == False,'should be False'
