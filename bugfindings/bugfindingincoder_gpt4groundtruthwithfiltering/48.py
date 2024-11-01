

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
assert is_palindrome('aba') == True
assert is_palindrome('abba') == True
assert is_palindrome(' ') == True
assert is_palindrome('abbba') == True
assert is_palindrome('abbbba') == True
assert is_palindrome(' ') is True
assert is_palindrome('abba') is True
assert is_palindrome('abbaa') is False
assert is_palindrome('abbbb') is False
assert is_palindrome("abca") == False
assert is_palindrome('A man, a plan, a canal: Panama A man, a plan, a canal: Panama') == False
assert is_palindrome('racecar ') == False
assert is_palindrome('abca') is False
assert is_palindrome('abcb') is False
assert is_palindrome('acab') is False
assert is_palindrome("Racecar") == False
assert is_palindrome("Aracecar") == False
assert is_palindrome('abbca') == False
assert is_palindrome('abca') == False
assert is_palindrome('abcd') == False
assert is_palindrome('bcda') == False
assert is_palindrome('dab') == False
assert is_palindrome('abcdd') == False
assert is_palindrome('abcdba') == False
assert is_palindrome('abaab') == False
assert is_palindrome("AA AB AC AD AB AC AD") == False
assert is_palindrome("AA AB AC AD AB AC AB") == False
assert is_palindrome("AA AB AC AD AB AC AB AC") == False
assert is_palindrome("AA AB AC AD AB AC AB AC AB") == False
assert is_palindrome("AA AB AC AD AB AC AB AC AB AC") == False
assert is_palindrome("AA AB AC AD AB AC AB AC AB AC AB") == False
assert is_palindrome("AA AB AC AD AB AC AB AC AB AC AB AC") == False
assert is_palindrome("AA AB AC AD AB AC AB AC AB AC AB AC AB") == False
assert is_palindrome('abaA') == False
assert is_palindrome("aba ba") == False
assert is_palindrome("ABBAbc") == False
assert is_palindrome("abba") == True
assert is_palindrome('ab') is False
assert is_palindrome('abbb') is False
assert is_palindrome('abbabba') is True
assert is_palindrome('abbaabba') is True
assert is_palindrome('aba')
assert not is_palindrome('abb')
assert not is_palindrome('abbaa')
assert not is_palindrome('ab')
assert not is_palindrome('abbaab')
assert not is_palindrome('abbaaba')
assert not is_palindrome('abbaabaa')
assert not is_palindrome('abbaabaac')
assert not is_palindrome('abbaabaabc')
assert not is_palindrome('abbaabaabcde')
assert not is_palindrome('abbaabaabcdea')
assert not is_palindrome('abbaabaabcdeaa')
assert not is_palindrome('abbaabaabcdeaaa')
assert is_palindrome('racecar') == True
assert is_palindrome('nomnom') == False
assert is_palindrome('race') == False
assert is_palindrome('nom') == False
assert is_palindrome('abbb') == False
assert is_palindrome('abbbbba') == True
assert is_palindrome("racecar")
assert not is_palindrome("racecars")
assert not is_palindrome("A man, a plan, a canal: Panama!!")
assert not is_palindrome("A man, a plan, a canal: Panama")
assert not is_palindrome("racecar  ")
assert is_palindrome("A man, a plan, a canal: Panama") == False
assert is_palindrome('race car') == False
assert is_palindrome((1, 2)) == False
assert is_palindrome('aa') == True
assert is_palindrome('aaa') == True
assert is_palindrome('abaAaba') == True
assert not is_palindrome("A man, a plan, a canal: Panama.")
assert not is_palindrome("A man, a plan, a canal: Panama!?!")
assert not is_palindrome("race a car!")
assert not is_palindrome("A man, a plan, a canal: Panama!!?!? ")
assert is_palindrome("A man, a plan, a canal: Panama!") is False
assert is_palindrome("A man, a plan, a canal: Panama ") is False
assert is_palindrome("A man, a plan, a canal: Panama!!") is False
assert is_palindrome("abbaa") == False
assert is_palindrome("abbaaa"[::-1]) == False
assert is_palindrome("abbaaa") == False
assert is_palindrome('abcccba') == True
assert not is_palindrome("Aaba!")
assert not is_palindrome("A man, a plan, a canal: Panama!")
assert not is_palindrome("A man, a plan, a canal: Panama ma amarnata")
assert not is_palindrome("A man, a plan, a canal: Panama  ma amarnata")
assert not is_palindrome("racecarp")
assert not is_palindrome("racecarcars")
assert not is_palindrome("racecarcarp")
assert not is_palindrome("racecarpp")
assert not is_palindrome("racecarcarpp")
assert not is_palindrome("abc")
assert not is_palindrome("A man a plan a canal Panama")
assert not is_palindrome("The quick brown fox jumps over the lazy dog")
assert is_palindrome("A man, a plan, a canal: Panama!") == False
assert is_palindrome("racecar") == True
assert is_palindrome("racecar!") == False
assert is_palindrome("racecar  ") == False
assert not is_palindrome("dog")
assert not is_palindrome('A man, a plan, a canal: Panama!')
assert not is_palindrome('abc')
assert is_palindrome("abbaabb") == False
assert is_palindrome("a b") == False
assert is_palindrome("abbaabbb") == False
assert not is_palindrome('race a car')
assert not is_palindrome(' '.join(['hello', 'hello']))
assert not is_palindrome(' hello ')
assert not is_palindrome('a man, a plan, a canal: Panama!')
assert is_palindrome("abba") is True
assert is_palindrome("racer") is False
assert is_palindrome('abac') == False
assert is_palindrome('racecar') is True
assert is_palindrome('race car') is False
assert is_palindrome('aba') is True
assert is_palindrome('abcabc') is False
assert is_palindrome('abccba') is True
assert is_palindrome('dog') == False
assert is_palindrome("racecAR") is False
assert is_palindrome("racecars") is False
assert is_palindrome("race car") is False
assert is_palindrome("abbaab") == False
assert not is_palindrome('abcd')
assert not is_palindrome('abcbac')
assert not is_palindrome('abcb')
assert is_palindrome("abbaaab") == False, "Palindrome test!"
assert is_palindrome('kayak')
assert is_palindrome('kayak kayak')
assert not is_palindrome('abbak')
assert is_palindrome('racecarc') is False
assert is_palindrome('racecarc') == False
assert is_palindrome('bab') is True
assert is_palindrome('kayak') == True
assert is_palindrome('abc') is False
assert is_palindrome('abcbcbc') is False
assert is_palindrome('abbcc') is False
assert is_palindrome("abc") == False
assert is_palindrome("abcd") == False
assert is_palindrome('racecars') == False
assert is_palindrome("racecarc") == False
assert is_palindrome('abad') == False
assert is_palindrome('abcbad') == False
assert is_palindrome('abbcad') == False
assert is_palindrome('abbbc') == False
assert is_palindrome('abbab') == False
assert is_palindrome("abbaa") is False
assert is_palindrome("raba") is False
assert not is_palindrome('hellO')
assert not is_palindrome('heello')
assert not is_palindrome("abbaa")
assert not is_palindrome("aabba")
assert is_palindrome('racecar  ') == False
assert is_palindrome('dented') == False
assert is_palindrome('racecarracecar') == True
assert is_palindrome('race car race') == False
assert is_palindrome('abc dabc abc') == False
assert is_palindrome('racecar')
assert not is_palindrome('na')
assert not is_palindrome('  n')
assert is_palindrome("abba" * 100) == True
assert is_palindrome("a" * 1000) == True
assert is_palindrome('') is True
assert is_palindrome('noonrace') == False
assert is_palindrome("race car") == False
assert is_palindrome("A man racecar a mãe") == False
assert is_palindrome("A man racecar") == False
assert not is_palindrome("abaac")
assert not is_palindrome("ab")
assert not is_palindrome("abbaab")
assert is_palindrome('abcde dcba ') == False
assert is_palindrome('ab ca ') == False
assert is_palindrome('abcbaa') is False
