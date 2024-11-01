
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    return ''.join([''.join(sorted(list(i))) for i in s.split(' ')])
assert anti_shuffle("") == ""
assert anti_shuffle("abc") == "abc"
assert anti_shuffle('') == ''
assert anti_shuffle('a') == 'a'
assert anti_shuffle("a") == "a"
assert anti_shuffle("ab") == "ab"
assert anti_shuffle("123") == "123"
assert anti_shuffle("xyz") == "xyz"
assert anti_shuffle("h") == "h"
assert anti_shuffle("12345") == "12345"
