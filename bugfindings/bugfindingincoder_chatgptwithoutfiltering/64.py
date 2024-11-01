
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = "aeiouyAEIOUY"
    n_vowels = sum(c in vowels for c in s)
    return n_vowels
assert vowels_count('a') == 1
assert vowels_count("a") == 1
assert vowels_count("A") == 1
assert vowels_count('aa') == 2
assert vowels_count("ae") is 2
assert vowels_count("oi") is 2
assert vowels_count('ae') == 2
assert vowels_count('ai') == 2
assert vowels_count('e') == 1
assert vowels_count("i") == 1
assert vowels_count("o") == 1
assert vowels_count("u") == 1
assert vowels_count('ai') == 2, 'ai counts 2'
assert vowels_count("e") == 1
assert vowels_count("ii") == 2
assert vowels_count("oo") == 2
assert vowels_count("iy") == 2
assert vowels_count('aeiou') == 5
assert vowels_count("a") in (1, 0)
assert vowels_count("aeiou") == 5
assert vowels_count('a') == 1 #not a vowel!
assert vowels_count('uo') == 2 #different vowels
assert vowels_count('aoeu') == 4
assert vowels_count('u') == 1
