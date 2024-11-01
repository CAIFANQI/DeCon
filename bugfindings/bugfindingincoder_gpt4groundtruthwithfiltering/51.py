

def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u", "w", "y"]])
assert remove_vowels("") == ""
assert remove_vowels('') == ''
assert remove_vowels("a") == ""
assert remove_vowels("WTF?!") == "WTF?!"
assert remove_vowels("WTF!") == "WTF!"
assert remove_vowels('h') == 'h'
assert remove_vowels('c') == 'c'
assert remove_vowels('bb') == 'bb'
assert remove_vowels('cc') == 'cc'
assert remove_vowels("aaaa") == ""
assert remove_vowels("z") == "z", "Sixth test failed"
assert remove_vowels("ab") is "b"
assert remove_vowels('abc') == 'bc'
assert remove_vowels("h")=="h"
assert remove_vowels("c#") == "c#"
assert remove_vowels("C++") == "C++"
assert remove_vowels('') == '' 
assert remove_vowels('cat') == 'ct'
