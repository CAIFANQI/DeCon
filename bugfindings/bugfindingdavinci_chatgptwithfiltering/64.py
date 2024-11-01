
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
assert vowels_count("a") == 1
assert vowels_count("e") == 1
assert vowels_count("i") == 1
assert vowels_count("o") == 1
assert vowels_count("u") == 1
assert vowels_count("ay") == 2
assert vowels_count("aeiouy") == 6
assert vowels_count("aeiou") == 5
assert vowels_count('oy') == 2
assert vowels_count('aeiouy') == 6
assert vowels_count('aei') == 3
assert vowels_count('aeiouaeiouaeiou') == 15
assert vowels_count("aei") == 3
assert vowels_count("aeiouaeiouaeiou") == 15
assert vowels_count("aaa") == 3
assert vowels_count('a') == 1
assert vowels_count('aeiou') == 5
assert vowels_count('I') == 1
assert vowels_count('aeioy') == 5
assert vowels_count('aeio') == 4
assert vowels_count('ae') == 2
assert vowels_count('u') == 1
assert vowels_count("aEiOu") == 5
assert vowels_count("AEIOU") == 5
assert vowels_count("AeiOu") == 5
assert vowels_count("AEIOUY") == 6
assert vowels_count("aa") == 2
assert vowels_count("AaAaAa") == 6
assert vowels_count("EeEeEe") == 6
assert vowels_count("IiIiIi") == 6
assert vowels_count("OoOoOo") == 6
assert vowels_count("UuUuUu") == 6
assert vowels_count('ey') == 2
assert vowels_count('aa') == 2
assert vowels_count("aeio") == 4
assert vowels_count("aeiouu") == 6
assert vowels_count("aeiooo") == 6
assert vowels_count("aeioou") == 6
assert vowels_count("ie") == 2
assert vowels_count("oy") == 2
assert vowels_count("eee") == 3
assert vowels_count("ooo") == 3
assert vowels_count("ioi") == 3
assert vowels_count("ou") == 2
assert 3 == vowels_count("iou")
assert vowels_count("ae") == 2
assert vowels_count("AiA") == 3
assert vowels_count("AEA") == 3
assert vowels_count("AeA") == 3
assert vowels_count("aaeeoo") == 6
assert vowels_count("io") == 2
assert vowels_count("aaaaeiou") == 8
assert vowels_count("aeioy") == 5
assert vowels_count("iii") == 3
assert vowels_count('AEIOU') == 5
assert vowels_count('aEiOu') == 5
assert vowels_count('aeiOU') == 5
assert vowels_count('AaEeIiOoUu') == 10
assert vowels_count('aEiO') == 4
assert vowels_count("aaaeee") == 6
assert vowels_count("aaaeeeiii") == 9
assert vowels_count("aaeiuio") == 7
assert vowels_count('aaaaa') == 5
assert vowels_count("ee") == 2
assert vowels_count("eeee") == 4
assert vowels_count('e') == 1
assert vowels_count('i') == 1
assert vowels_count('o') == 1
