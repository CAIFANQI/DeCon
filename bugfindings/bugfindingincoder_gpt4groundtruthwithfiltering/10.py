

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return ''

    beginning_of_suffix = 0

    while not is_palindrome(string):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]
assert make_palindrome('') == ''
assert make_palindrome('aba') == 'aba'
assert make_palindrome('abba') == 'abba'
assert make_palindrome("aba") == "aba"
assert make_palindrome('') == ('')
assert make_palindrome("racecarracecar") == "racecarracecar"
assert make_palindrome("racecarracecarracecarracecar") == "racecarracecarracecarracecar"
assert make_palindrome("racecarracecarracecarracecarracecar") == "racecarracecarracecarracecarracecar"
assert make_palindrome("racecarracecarracecarracecarracecarracecar") == "racecarracecarracecarracecarracecarracecar"
assert make_palindrome("racecarracecarracecarracecarracecarracecarracecar") == "racecarracecarracecarracecarracecarracecarracecar"
assert make_palindrome("a") == "a"
assert make_palindrome("aaaaa") == "aaaaa"
assert make_palindrome("abba") == "abba"
assert make_palindrome('a') == 'a'
assert make_palindrome('racecar') =='racecar'
assert make_palindrome("racecar") == "racecar"
assert make_palindrome("racecar racecar") == "racecar racecar"
assert make_palindrome("aaaa") == "aaaa"
assert make_palindrome("abacaba") == "abacaba"
assert make_palindrome("aa") == "aa"
assert make_palindrome('ab') == 'aba'
assert make_palindrome("aba") == "aba" 
assert make_palindrome("abbaabba") == "abbaabba"
assert make_palindrome("aaa") == "aaa"
assert make_palindrome("abbba") == "abbba"
assert make_palindrome('abaaba') == 'abaaba'
assert make_palindrome('a' * 10) == 'a' * 10
assert make_palindrome('aba' * 10) == 'aba' * 10
assert make_palindrome('abbba') == 'abbba'
assert make_palindrome('abbbbba') == 'abbbbba'
assert make_palindrome('abbbbbba') == 'abbbbbba'
assert make_palindrome("aaaaaa") == "aaaaaa"
assert make_palindrome("abbbba") == "abbbba"
assert make_palindrome("") == ""
assert make_palindrome("A") == "A"
assert make_palindrome("z") == "z"
assert make_palindrome('aba') == "aba"
assert make_palindrome('abba') == "abba"
assert make_palindrome("abcba") == "abcba"
assert make_palindrome('1') == '1'
assert make_palindrome('12') == '121'
assert make_palindrome("bab") == "bab"
assert make_palindrome('aaa') == 'aaa'
assert make_palindrome("abbbbbba") == "abbbbbba"
assert make_palindrome('a' * 100) == 'a' * 100
assert make_palindrome("racecaracecar") == "racecaracecar"
assert make_palindrome("rotor") == "rotor"
assert make_palindrome("abaaba") == "abaaba"
assert make_palindrome('aaaa') == 'aaaa'
assert make_palindrome("a" * 100) == "a" * 100
assert make_palindrome('aaaaa') == 'aaaaa'
assert make_palindrome('aaa') == 'aaa' 
assert make_palindrome("a" * 100 + "a") == "a" * 100 + "a"
assert make_palindrome("aba") == "aba" # no such palindrome
assert make_palindrome("ABCBA") == "ABCBA"
