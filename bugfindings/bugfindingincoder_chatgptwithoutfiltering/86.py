
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
assert anti_shuffle('abc') == 'abc'
assert anti_shuffle(' ') ==' '
assert anti_shuffle('') == ''
assert anti_shuffle('a') == 'a'
assert anti_shuffle('ab') == 'ab'
assert anti_shuffle("abc")==  "abc"
assert anti_shuffle('abcdef') == 'abcdef'
assert anti_shuffle('a' * 99) == 'a' * 99
assert anti_shuffle('a' * 100) == 'a' * 100
assert anti_shuffle('a' * 1000) == 'a' * 1000
assert anti_shuffle('a' * 10000) == 'a' * 10000
assert anti_shuffle(' ') == " "
assert anti_shuffle("   ") =='   '
