
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
assert vowels_count('aba') == 2
assert vowels_count('x') is 0
assert vowels_count('xyx') is 0
assert vowels_count('xyyx') is 0
assert vowels_count('xyyxyxyx') is 0
assert vowels_count(' ') == 0
assert vowels_count('a') == 1
assert vowels_count('ab ') == 1
assert vowels_count('ab') == 1, 'test3'
assert vowels_count('abf') == 1, 'test4'
assert vowels_count('abg') == 1, 'test5'
assert vowels_count('abj') == 1, 'test7'
assert vowels_count('abl') == 1, 'test9'
assert vowels_count('abl') == 1, 'test10'
assert vowels_count('abp') == 1, 'test13'
assert vowels_count('abq') == 1, 'test14'
assert vowels_count('abr') == 1, 'test15'
assert vowels_count('abs') == 1, 'test16'
assert vowels_count('abt') == 1, 'test17'
assert vowels_count('abu') == 2, 'test18'
assert vowels_count('abv') == 1, 'test19'
assert vowels_count('abw') == 1, 'test20'
assert vowels_count('abx') == 1, 'test21'
assert vowels_count('acb') == 1, 'test24'
assert vowels_count('acc') == 1, 'test25'
assert vowels_count('abbba') == 2
assert vowels_count('aaab') == 3
assert vowels_count('bb') == 0
assert vowels_count('bbb') == 0
assert vowels_count("abby") == 2, "Testcase 2 failed on \"abby\""
assert vowels_count("abbyyz") == 1, "Testcase 7 failed on \"abbyyz\""
assert vowels_count("abbycz") == 1, "Testcase 8 failed on \"abbycz\""
assert vowels_count("elephant") == 3
assert vowels_count("orange") == 3
assert vowels_count("a") == 1
assert vowels_count("y") == 1
assert vowels_count("A") == 1
assert vowels_count('aa') == 2
assert vowels_count('abb') == 1
assert vowels_count("a bcd ee") == 3
assert vowels_count("aby") == 2
assert vowels_count('abye') == 2
assert vowels_count('abyez') == 2
assert vowels_count('abyezy') == 3
assert vowels_count('abyesz') == 2
assert vowels_count('abyeszy') == 3
assert vowels_count('abyeszyz') == 2
assert vowels_count('aby') == 2
assert vowels_count('cat') == 1, 'Check the correctness of vowels_count'
assert vowels_count("ae") is 2
assert vowels_count("oi") is 2
assert vowels_count('ae') == 2
assert vowels_count('ai') == 2
assert vowels_count('yu') == 1
assert vowels_count('e') == 1
assert vowels_count("eiuvxy") == 4
assert vowels_count("hey") == 2
assert vowels_count("ya") == 1
assert vowels_count("i") == 1
assert vowels_count("o") == 1
assert vowels_count("u") == 1
assert vowels_count("hey") == 2, "vowels_count should return 2 when given 'hey'"
assert vowels_count("hallo") == 2, "vowels_count should return 2 when given 'hallo'"
assert vowels_count("aapp") == 2, "aapp"
assert vowels_count("aappppleee") == 5, "aappppleee"
assert vowels_count('ai') == 2, 'ai counts 2'
assert vowels_count('abaass') == 3
assert vowels_count('bbaaa') == 3
assert vowels_count('abbaaa') == 4
assert vowels_count("heeeehi") == 5
assert vowels_count("ehihe") == 3
assert vowels_count("ehihihi") == 4
assert vowels_count("e") == 1
assert vowels_count("ii") == 2
assert vowels_count("oo") == 2
assert vowels_count("iy") == 2
assert vowels_count("eyy") == 2, "vowels_count function should return 2"
assert vowels_count('yes') == 1, 'yes should be counted as 1'
assert vowels_count('yess') == 1, 'yesss count should be 1'
assert vowels_count('z') == 0, 'z should not be counted as 0'
assert vowels_count('goodbye') == 3
assert vowels_count("aabccca") == 3
assert vowels_count("abbbcccabbba") == 3
assert vowels_count("abbbbbbaabb") == 3
assert vowels_count('aeiou') == 5
assert vowels_count('halo') == 2
assert vowels_count('halohalo') == 4
assert vowels_count('halohaloo') == 5
assert vowels_count('hello') == 2
assert vowels_count('x') == 0
assert vowels_count("x") == 0
assert vowels_count("hi hi") == 2, "hi hi"
assert vowels_count("abyzae") == 3
assert vowels_count('cats') is 1
assert vowels_count('cat') is 1
assert vowels_count("a") in (1, 0)
assert vowels_count("ba") in (1, 2)
assert vowels_count('abaadaba') == 5
assert vowels_count("aeiou") == 5
assert vowels_count('a') == 1 #not a vowel!
assert vowels_count('h') == 0
assert vowels_count('uo') == 2 #different vowels
assert vowels_count('ab') == 1
assert vowels_count('ba') == 1
assert vowels_count('cae') == 2
assert vowels_count('lOOW') == 2, 'test fails'
assert vowels_count('xyz') == 0
assert vowels_count('abracadabraz') == 5
assert vowels_count("abacaba") == 4
assert vowels_count('anana') == 3
assert vowels_count('ananas') == 3
assert vowels_count('ananass') == 3
assert vowels_count('aoeu') == 4
assert vowels_count('u') == 1
assert vowels_count('yss') == 0
assert vowels_count("w") == 0
assert vowels_count("ew") == 1
assert vowels_count("aba") == 2
assert vowels_count('pale') == 2
assert vowels_count('elephant') == 3
assert vowels_count('eyes') == 2
