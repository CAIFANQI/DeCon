
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
assert anti_shuffle('abcd ef') == 'abcd ef'
assert anti_shuffle('abcd ef abcd') == 'abcd ef abcd'
assert anti_shuffle('a b c d') == 'a b c d'
assert anti_shuffle("abc def ghi xyz") == "abc def ghi xyz"
assert anti_shuffle("") == ""
assert anti_shuffle("a") == "a"
assert anti_shuffle("1") == "1"
assert anti_shuffle("2 2") == "2 2"
assert anti_shuffle('abc def ghi jkl') == 'abc def ghi jkl'
assert anti_shuffle('abc 1 def 2 ghi 3 jkl') == 'abc 1 def 2 ghi 3 jkl'
assert anti_shuffle("abcd") == "abcd"
assert anti_shuffle("a b c d e") == "a b c d e"
assert anti_shuffle("a b c de") == "a b c de"
assert anti_shuffle("a b cd e") == "a b cd e"
assert anti_shuffle("abc de f") == "abc de f"
assert anti_shuffle("abc def") == "abc def"
assert anti_shuffle("a b c d e f") == "a b c d e f"
assert anti_shuffle("a b c d ef") == "a b c d ef"
assert anti_shuffle("a b c de f") == "a b c de f"
assert anti_shuffle("a b cd e f") == "a b cd e f"
assert anti_shuffle("a bc d e f") == "a bc d e f"
assert anti_shuffle("ab cd e f") == "ab cd e f"
assert anti_shuffle("abc d e f") == "abc d e f"
assert anti_shuffle('a1b c2d') == '1ab 2cd'
assert anti_shuffle("hello world") == "ehllo dlorw"
assert anti_shuffle("Zzzz Zzzz Zzzz") == "Zzzz Zzzz Zzzz"
assert anti_shuffle("python") == "hnopty"
assert anti_shuffle("a b c d e f g h i j k l m n o p q r s t u v w x y z") == "a b c d e f g h i j k l m n o p q r s t u v w x y z"
assert anti_shuffle("t") == "t"
assert anti_shuffle("I") == "I"
assert 'aaa bcd' == anti_shuffle('aaa cbd')
assert anti_shuffle("ba") == "ab"
assert anti_shuffle("a b") == "a b"
assert anti_shuffle("ab ba") == "ab ab"
assert anti_shuffle("a b c d") == "a b c d"
assert anti_shuffle("HELLO world") == "EHLLO dlorw"
assert anti_shuffle("HELLO WORLD") == "EHLLO DLORW"
assert anti_shuffle("a b c") == "a b c"
assert anti_shuffle('goodbye world') == 'bdegooy dlorw'
assert anti_shuffle('hello') == 'ehllo'
assert anti_shuffle('a') == 'a'
assert anti_shuffle('') == ''
assert anti_shuffle("aabbcc") == "aabbcc"
assert anti_shuffle("1234 5678") == "1234 5678"
assert anti_shuffle("hello") == "ehllo"
assert anti_shuffle("a aa") == "a aa"
assert anti_shuffle("a aa b bb") == "a aa b bb"
assert anti_shuffle("a aa b bb c cc") == "a aa b bb c cc"
assert anti_shuffle("AB CD EF ab cd ef") == "AB CD EF ab cd ef"
assert anti_shuffle("h") == "h"
assert anti_shuffle("this is a test") == "hist is a estt"
assert anti_shuffle('hello world') == 'ehllo dlorw'
assert anti_shuffle("I am a boy") == "I am a boy"
assert '123456' == anti_shuffle('213456')
assert 'Bbdehoott' == anti_shuffle('Bbdehoott')
assert 'Aaa' == anti_shuffle('Aaa')
assert '' == anti_shuffle('')
assert (anti_shuffle("a bb cc") == "a bb cc")
assert anti_shuffle("test") == "estt"
assert anti_shuffle("testing!") == "!eginstt"
assert anti_shuffle("hi") == "hi"
assert "a bcd" == anti_shuffle("a cbd")
assert "" == anti_shuffle("")
assert anti_shuffle("aaA bbB !zzz") == "Aaa Bbb !zzz"
assert anti_shuffle("A B !zzz") == "A B !zzz"
assert anti_shuffle("abc") == "abc"
assert anti_shuffle("1a2b3c") == "123abc"
assert anti_shuffle("cde") == "cde"
assert anti_shuffle("1bc defg") == "1bc defg"
