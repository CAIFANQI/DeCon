

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
assert remove_vowels("hello") == "hll"
assert remove_vowels("world") == "wrld"
assert remove_vowels("python") == "pythn"
assert remove_vowels("aeiou") == ""
assert remove_vowels("") == ""
assert remove_vowels("abcdefghijklmnopqrstuvwxyz") == "bcdfghjklmnpqrstvwxyz"
assert remove_vowels("Python is a great programming language") == "Pythn s  grt prgrmmng lngg"
assert remove_vowels("1234567890") == "1234567890"
assert remove_vowels("apple") == "ppl"
assert remove_vowels("banana") == "bnn"
assert remove_vowels("cherry") == "chrry"
assert remove_vowels("orange") == "rng"
assert remove_vowels("h") == "h"
assert remove_vowels("abcde") == "bcd"
assert remove_vowels("AeIoU") == ""
assert remove_vowels("Python") == "Pythn"
assert remove_vowels("programming") == "prgrmmng"
assert remove_vowels("aardvark") == "rdvrk"
assert remove_vowels("algorithm") == "lgrthm"
assert remove_vowels('world') == 'wrld'
assert remove_vowels('Python') == 'Pythn'
assert remove_vowels('aeiou') == ''
assert remove_vowels('') == ''
assert remove_vowels("a") == ""
assert remove_vowels("Python is a great language") == "Pythn s  grt lngg"
assert remove_vowels("This is a test") == "Ths s  tst"
assert remove_vowels("Python Programming") == "Pythn Prgrmmng"
assert remove_vowels("hello world") == "hll wrld"
assert remove_vowels("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "BCDFGHJKLMNPQRSTVWXYZ"
assert remove_vowels("12345") == "12345"
assert remove_vowels("Python is awesome") == "Pythn s wsm"
assert remove_vowels("This is a test.") == "Ths s  tst."
assert remove_vowels("AEIOU") == ""
