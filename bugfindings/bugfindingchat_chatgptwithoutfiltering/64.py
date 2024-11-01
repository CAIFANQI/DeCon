
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
assert vowels_count("aeiou") == 5
assert vowels_count("aeiou") == 5, "Test case 3 failed"
assert vowels_count("a") == 1, "Test case 7 failed"
assert vowels_count("aeiou") == 5, "Error: Test Case 5"
assert vowels_count('aeiou') == 5
assert vowels_count("e") == 1, "Test case 8 failed"
assert vowels_count("i") == 1, "Test case 9 failed"
assert vowels_count("o") == 1, "Test case 10 failed"
assert vowels_count("u") == 1, "Test case 11 failed"
assert vowels_count("a") == 1, "Test case 9 failed"
assert vowels_count("a") == 1, 'Test Case 6 Failed'
assert vowels_count("e") == 1, 'Test Case 7 Failed'
assert vowels_count("i") == 1, 'Test Case 8 Failed'
assert vowels_count("o") == 1, 'Test Case 9 Failed'
assert vowels_count("u") == 1, 'Test Case 10 Failed'
assert vowels_count("ay") == 2, 'Test Case 12 Failed'
assert vowels_count("ey") == 2, 'Test Case 13 Failed'
assert vowels_count("iy") == 2, 'Test Case 14 Failed'
assert vowels_count("oy") == 2, 'Test Case 15 Failed'
assert vowels_count("uy") == 2, 'Test Case 16 Failed'
assert vowels_count('aeiou') == 5, 'Test Case 3 Failed'
assert vowels_count("aeiou") == 5, "Test case 5 failed"
assert vowels_count('a') == 1
assert vowels_count("aeiou") == 5, "Test case 2 failed"
assert vowels_count("aeiouy") == 6, 'Test Case 7 Failed'
assert vowels_count("AEIOUaeiou") == 10, "Test case 6 failed"
assert vowels_count('a') == 1, "Test case 7 failed"
assert vowels_count('e') == 1, "Test case 8 failed"
assert vowels_count('i') == 1, "Test case 9 failed"
assert vowels_count('o') == 1, "Test case 10 failed"
assert vowels_count('u') == 1, "Test case 11 failed"
assert vowels_count('aeiou') == 5, "Test case 14 failed"
assert vowels_count('aeiouy') == 6, "Test case 15 failed"
