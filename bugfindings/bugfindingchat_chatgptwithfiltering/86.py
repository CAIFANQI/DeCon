
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
assert anti_shuffle("hello world") == "ehllo dlorw"
assert anti_shuffle("hello") == "ehllo"
assert anti_shuffle("") == ""
assert anti_shuffle("python is awesome") == "hnopty is aeemosw"
assert anti_shuffle("programming is fun") == "aggimmnoprr is fnu"
assert anti_shuffle("this is a test") == "hist is a estt"
assert anti_shuffle("abc def ghi") == "abc def ghi"
assert anti_shuffle("123 456 789") == "123 456 789"
assert anti_shuffle("a b c d e f") == "a b c d e f"
assert anti_shuffle("cba fed ihg") == "abc def ghi"
assert anti_shuffle("aaa bbb ccc") == "aaa bbb ccc"
assert anti_shuffle("aaa bbb ccc ddd") == "aaa bbb ccc ddd"
assert anti_shuffle("aaa bbb ccc ddd eee") == "aaa bbb ccc ddd eee"
assert anti_shuffle("aaa bbb ccc ddd eee fff") == "aaa bbb ccc ddd eee fff"
assert anti_shuffle("aaa bbb ccc ddd eee fff ggg") == "aaa bbb ccc ddd eee fff ggg"
assert anti_shuffle("aaa bbb ccc ddd eee fff ggg hhh") == "aaa bbb ccc ddd eee fff ggg hhh"
assert anti_shuffle("aaa bbb ccc ddd eee fff ggg hhh iii") == "aaa bbb ccc ddd eee fff ggg hhh iii"
assert anti_shuffle("aaa bbb ccc ddd eee fff ggg hhh iii jjj") == "aaa bbb ccc ddd eee fff ggg hhh iii jjj"
assert anti_shuffle("aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk") == "aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk"
assert anti_shuffle("aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll") == "aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll"
assert anti_shuffle("aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm") == "aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm"
assert anti_shuffle("aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm nnn") == "aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm nnn"
assert anti_shuffle("aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm nnn ooo") == "aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm nnn ooo"
assert anti_shuffle("aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm nnn ooo ppp") == "aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm nnn ooo ppp"
assert anti_shuffle("aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm nnn ooo ppp qqq") == "aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm nnn ooo ppp qqq"
assert anti_shuffle("aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm nnn ooo ppp qqq rrr") == "aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm nnn ooo ppp qqq rrr"
assert anti_shuffle("aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm nnn ooo ppp qqq rrr sss") == "aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm nnn ooo ppp qqq rrr sss"
assert anti_shuffle("aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm nnn ooo ppp qqq rrr sss ttt") == "aaa bbb ccc ddd eee fff ggg hhh iii jjj kkk lll mmm nnn ooo ppp qqq rrr sss ttt"
assert anti_shuffle("a b c d e f g") == "a b c d e f g"
assert anti_shuffle("abc def ghi jkl") == "abc def ghi jkl"
assert anti_shuffle("a b c d e f g h i j k l m n o p q r s t u v w x y z") == "a b c d e f g h i j k l m n o p q r s t u v w x y z"
assert anti_shuffle("python is fun") == "hnopty is fnu"
assert anti_shuffle("a b c d e") == "a b c d e"
assert anti_shuffle("a b c") == "a b c"
assert anti_shuffle("abc") == "abc"
assert anti_shuffle("world") == "dlorw"
assert anti_shuffle("hello     world") == "ehllo     dlorw"
assert anti_shuffle('abc def ghi') == 'abc def ghi'
assert anti_shuffle('hello') == 'ehllo'
assert anti_shuffle('') == ''
assert anti_shuffle('a') == 'a'
assert anti_shuffle("python is great") == "hnopty is aegrt"
assert anti_shuffle("the quick brown fox") == "eht cikqu bnorw fox"
assert anti_shuffle("goodbye") == "bdegooy"
assert anti_shuffle("a b c d e f g h i") == "a b c d e f g h i"
assert anti_shuffle("a") == "a"
assert anti_shuffle("ab") == "ab"
assert anti_shuffle("cba") == "abc"
assert anti_shuffle("dcba") == "abcd"
assert anti_shuffle("123") == "123"
assert anti_shuffle("xyz") == "xyz"
assert anti_shuffle("keep it up") == "eekp it pu"
assert anti_shuffle("zyx wvu tsr") == "xyz uvw rst"
assert anti_shuffle("I am a cat") == "I am a act"
assert anti_shuffle("alphabet soup") == "aabehlpt opsu"
assert anti_shuffle("123 abcd") == "123 abcd"
assert anti_shuffle("h e l l o") == "h e l l o"
assert anti_shuffle("hello   world") == "ehllo   dlorw"
assert anti_shuffle("a b c d e f g h i j") == "a b c d e f g h i j"
assert anti_shuffle("a b c d") == "a b c d"
assert anti_shuffle("racecar") == "aaccerr"
assert anti_shuffle("hello 123") == "ehllo 123"
assert anti_shuffle("good morning") == "dgoo gimnnor"
assert anti_shuffle("abc xyz") == "abc xyz"
assert anti_shuffle("1234567890") == "0123456789"
assert anti_shuffle("test case") == "estt aces"
assert anti_shuffle("h") == "h"
assert anti_shuffle("hello world hello") == "ehllo dlorw ehllo"
assert anti_shuffle("12345") == "12345"
