

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
assert make_palindrome("abcd") == "abcdcba"
assert make_palindrome("race") == "racecar"
assert make_palindrome("abcba") == "abcba"
assert make_palindrome("aba") == "aba"
assert make_palindrome("a") == "a"
assert make_palindrome("") == ""
assert make_palindrome("level") == "level"
assert make_palindrome("abc") == "abcba"
assert make_palindrome('level') == 'level'
assert make_palindrome('python') == 'pythonohtyp'
assert make_palindrome('') == ''
assert make_palindrome("abba") == "abba"
assert make_palindrome("madam") == "madam"
assert make_palindrome('ababa') == 'ababa'
assert make_palindrome("ababa") == "ababa"
assert make_palindrome("ab") == "aba"
assert make_palindrome("world") == "worldlrow"
assert make_palindrome("radar") == "radar"
assert make_palindrome('abba') == 'abba'
assert make_palindrome('race') == 'racecar'
assert make_palindrome("python") == "pythonohtyp"
assert make_palindrome('abcba') == 'abcba'
assert make_palindrome('a') == 'a'
assert make_palindrome("abb") == "abba"
assert make_palindrome("hello") == "hellolleh"
assert make_palindrome('abb') == 'abba'
assert make_palindrome('abcd') == 'abcdcba'
assert make_palindrome('abccba') == 'abccba'
assert make_palindrome('ab') == 'aba'
assert make_palindrome('abc') == 'abcba'
assert make_palindrome('madam') == 'madam'
assert make_palindrome('aaaaa') == 'aaaaa'
assert make_palindrome("noon") == "noon"
assert make_palindrome("aaa") == "aaa"
assert make_palindrome("12321") == "12321"
assert make_palindrome("abab") == "ababa"
assert make_palindrome("abccba") == "abccba"
assert make_palindrome("abcb") == "abcba"
assert make_palindrome("aabb") == "aabbaa"
assert make_palindrome("abcde") == "abcdedcba"
assert make_palindrome("abcdef") == "abcdefedcba"
assert make_palindrome('noon') == 'noon'
assert make_palindrome("abbabb") == "abbabba"
assert make_palindrome("aabbaa") == "aabbaa"
assert make_palindrome('aaa') == 'aaa'
assert make_palindrome('radar') == 'radar'
assert make_palindrome("abcdeff") == "abcdeffedcba"
