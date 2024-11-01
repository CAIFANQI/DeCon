
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
assert 	vowels_count("abracadabra") == 5
assert 	vowels_count("acacacagtacatac") == 7
assert 	vowels_count("tattarrattat") == 4
assert 	vowels_count("a") == 1
assert 	vowels_count("xyz") == 0
assert 	vowels_count("yarn") == 1
assert 	vowels_count("u") == 1
assert 	vowels_count("e") == 1
assert 	vowels_count('a') == 1
assert 	vowels_count('a') == 1, 'error in case of one vowel'
assert 	vowels_count('yay') == 2, 'error in case of two vowels at end'
assert 	vowels_count('yAY') == 2, 'error in case of two vowels at end'
assert 	vowels_count('a') == 1, 'One vowel'
assert 	vowels_count('i') == 1, 'One vowel'
assert 	vowels_count('ai') == 2, 'Two vowels'
assert 	vowels_count('aiu') == 3, 'Three vowels'
assert 	vowels_count('yay') == 2, 'Two vowels'
assert 	vowels_count("a") == 1, "vowels_count of a string with only one vowel should be 1"
assert 	vowels_count("xyz") == 0, "vowels_count of a string with only consonants should be 0"
assert 	vowels_count('yippee') == 3
assert 	vowels_count('yoyo') == 2
assert 	vowels_count("yawn") == 1
assert 	vowels_count("yest") == 1
assert 	vowels_count("yes") == 1
assert 	vowels_count("yet") == 1
assert 	vowels_count('foo') == 2
assert 	vowels_count('xyz') == 0
assert 	vowels_count('aeiou') == 5
assert 	vowels_count("a") 	== 1
assert 	vowels_count("i") 	== 1
assert 	vowels_count("ai") 	== 2
assert 	vowels_count("aai") 	== 3
assert 	vowels_count("aaa") 	== 3
assert 	vowels_count("aaii") 	== 4
assert 	vowels_count("aaiii") 	== 5
assert 	vowels_count('yooly') == 3, "Case: yooly"
assert 	vowels_count('yooo') == 3, "Case: yooo"
assert 	vowels_count('hoo') == 2, "Case: hoo"
assert 	vowels_count('y') == 1, "Case: y"
assert 	vowels_count('hoohoo') == 4, "Case: hoohoo"
assert 	vowels_count('a') == 1, "Case: a"
assert 	vowels_count('silly') == 2
assert vowels_count("a") == 1, "input 'a' should return 1"
assert 	vowels_count('hello') == 2
assert 	vowels_count('y') == 1
assert 	vowels_count("yacoma") == 3
assert 	vowels_count("mathematics") == 4
assert 	vowels_count("ae") == 2
assert 	vowels_count("aeiou") == 5
assert 	vowels_count("aeiouyxyz") == 5
assert 	vowels_count('aeiou') 	==	5
assert 	vowels_count('yay') 	==	2
assert 	vowels_count('yoo') 	==	2
assert 	vowels_count("b") == 0
assert 	vowels_count("c") == 0
assert 	vowels_count("sarah") == 2
assert 	vowels_count("sarah123") == 2
assert 	vowels_count("sarah1234") == 2
assert 	vowels_count("yayy") == 2
assert 	vowels_count("yayyyyay") == 3
assert 	vowels_count('pie') 	== 2, 	"wrong result for 'pie'"
assert vowels_count('a') == 1
assert vowels_count('xyz') == 0
assert vowels_count('y') == 1
assert vowels_count('o') == 1
assert 	vowels_count('yayay') == 3
assert 	vowels_count('a') == 1, 'Wrong result for string with one vowel'
assert 	vowels_count('foo') == 2, 'Wrong result for string with two vowels'
assert 	vowels_count('xyz') == 0, 'Wrong result for string with no vowels'
assert 	vowels_count('foobar') == 3, 'Wrong result for string with three vowels'
assert 	vowels_count('foobaz') == 3, 'Wrong result for string with three vowels'
assert 	vowels_count("aeiou") == 5, "error"
assert 	vowels_count("y") == 1, "Wrong answer for 'y'"
assert 	vowels_count('yayyyy') == 2
assert 	vowels_count("honey") == 3
assert 	vowels_count("sky") == 1
assert 	vowels_count("year") == 2
assert 	vowels_count("y") == 1
assert 	vowels_count('a') 	== 1
assert 	vowels_count("abracadabra") == 5, "5 vowels"
assert 	vowels_count("grgrgrg") == 0, "No vowels"
assert 	vowels_count("abcdeyy") == 3, "3 vowels, 'y' at the end"
assert 	vowels_count("accuu") == 3
assert 	vowels_count("yyyyyyy") == 1
