
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
assert 	vowels_count("a") == 1
assert 	vowels_count("u") == 1
assert 	vowels_count("e") == 1
assert 	vowels_count('a') == 1
assert 	vowels_count('a') == 1, 'error in case of one vowel'
assert 	vowels_count('a') == 1, 'One vowel'
assert 	vowels_count('i') == 1, 'One vowel'
assert 	vowels_count('ai') == 2, 'Two vowels'
assert 	vowels_count('aiu') == 3, 'Three vowels'
assert 	vowels_count("a") == 1, "vowels_count of a string with only one vowel should be 1"
assert 	vowels_count('aeiou') == 5
assert 	vowels_count("a") 	== 1
assert 	vowels_count("i") 	== 1
assert 	vowels_count("ai") 	== 2
assert 	vowels_count("aai") 	== 3
assert 	vowels_count("aaa") 	== 3
assert 	vowels_count("aaii") 	== 4
assert 	vowels_count("aaiii") 	== 5
assert 	vowels_count('a') == 1, "Case: a"
assert vowels_count("a") == 1, "input 'a' should return 1"
assert 	vowels_count("ae") == 2
assert 	vowels_count("aeiou") == 5
assert 	vowels_count('aeiou') 	==	5
assert vowels_count('a') == 1
assert vowels_count('o') == 1
assert 	vowels_count('a') == 1, 'Wrong result for string with one vowel'
assert 	vowels_count("aeiou") == 5, "error"
assert 	vowels_count('a') 	== 1
