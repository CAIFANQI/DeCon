

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
assert make_palindrome('abc') == 'abcba'
assert make_palindrome('a') == 'a'
assert make_palindrome("aba") == "aba"
assert make_palindrome("aa") == "aa"
assert make_palindrome("") == ""
assert make_palindrome("a") == "a"
assert make_palindrome('abba') == 'abba'
assert make_palindrome('abb') == 'abba'
assert make_palindrome('abbb') == 'abbba'
assert make_palindrome('ab') == 'aba'
assert make_palindrome('') == ''
assert make_palindrome('abcd') == 'abcdcba'
assert make_palindrome('abcde') == 'abcdedcba'
assert make_palindrome("aaaaa") == "aaaaa"
assert make_palindrome('AN') == 'ANA'
assert make_palindrome('A') == 'A'
assert make_palindrome("abba") == "abba"
assert make_palindrome('abacaba') == 'abacaba'
assert make_palindrome('abcdfgfdcba') == 'abcdfgfdcba'
assert make_palindrome('abcdefgfedcba') == 'abcdefgfedcba'
assert make_palindrome('abcdefggfedcba') == 'abcdefggfedcba'
assert make_palindrome("aaabbb") == "aaabbbaaa"
assert make_palindrome("abcdedcba") == "abcdedcba"
assert make_palindrome("abcdeedcba") == "abcdeedcba"
assert make_palindrome("zzzz") == "zzzz"
assert make_palindrome("zzz") == "zzz"
assert make_palindrome('aba') == 'aba'
assert make_palindrome('aa') == 'aa'
assert make_palindrome('aaa') == 'aaa'
assert make_palindrome('aabaa') == 'aabaa'
assert make_palindrome('aabccbaa') == 'aabccbaa'
assert make_palindrome('aabcbaa') == 'aabcbaa'
assert make_palindrome("ABCD") == "ABCDCBA"
assert make_palindrome("ABCDED") == "ABCDEDCBA"
assert make_palindrome('gomez') == 'gomezemog'
assert make_palindrome('aaaa') == 'aaaa'
assert make_palindrome("aaaa") == "aaaa"
assert make_palindrome("aaa") == "aaa"
assert make_palindrome("abc") == "abcba"
assert make_palindrome("abcd") == "abcdcba"
assert make_palindrome("abcde") == "abcdedcba"
assert make_palindrome("abcdef") == "abcdefedcba"
assert make_palindrome("abcdefghi") == "abcdefghihgfedcba"
assert make_palindrome("abcdefghij") == "abcdefghijihgfedcba"
assert make_palindrome("abcdefghijk") == "abcdefghijkjihgfedcba"
assert make_palindrome("abcdefghijkl") == "abcdefghijklkjihgfedcba"
assert make_palindrome('abccba') == 'abccba'
assert make_palindrome("abab") == "ababa"
assert make_palindrome("aabaa") == "aabaa"
assert make_palindrome('cab') == 'cabac'
assert make_palindrome('redder') == 'redder'
assert make_palindrome('racecar') == 'racecar'
assert make_palindrome('abaaba') == 'abaaba'
assert make_palindrome('abbacabba') == 'abbacabba'
assert make_palindrome('abcdefgfed') == 'abcdefgfedcba'
assert make_palindrome('12321') == '12321'
assert make_palindrome('abcdd') == 'abcddcba'
assert make_palindrome("abacaba") == "abacaba"
assert make_palindrome("ababab") == "abababa"
assert make_palindrome('abcba') == 'abcba'
assert make_palindrome("racecar") == "racecar"
assert make_palindrome("ab") == "aba"
assert make_palindrome('bba') == 'bbabb'
assert make_palindrome('abcdef') == 'abcdefedcba'
assert make_palindrome('abcdefg') == 'abcdefgfedcba'
assert make_palindrome('helloolleh') == 'helloolleh'
assert make_palindrome('abac') == 'abacaba'
assert make_palindrome('abacab') == 'abacaba'
assert make_palindrome('abacababac') == 'abacababacaba'
assert make_palindrome("aaabcbaaa") == "aaabcbaaa"
assert make_palindrome("baaabcbaaa") == "baaabcbaaab"
assert make_palindrome("abacab") == "abacaba"
assert make_palindrome('abcdcba') == 'abcdcba'
assert make_palindrome("abcba") == "abcba"
assert make_palindrome("abababa") == "abababa"
assert make_palindrome("level") == "level"
assert make_palindrome("wasitacaroracatisaw") == "wasitacaroracatisaw"
assert make_palindrome("tattarrattat") == "tattarrattat"
assert make_palindrome("deed") == "deed"
assert make_palindrome("acaba") == "acabaca"
assert (make_palindrome("ab") == "aba")
assert (make_palindrome("bab") == "bab")
assert make_palindrome("abcdcba") == "abcdcba"
assert make_palindrome('abcddcba') == 'abcddcba'
assert make_palindrome('abababa') == 'abababa'
assert make_palindrome('madam') == 'madam'
assert make_palindrome('applppa') == 'applppa'
