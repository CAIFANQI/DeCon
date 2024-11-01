
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    new_lst = []
    for word in sentence.split():
        flg = 0
        for i in range(2, len(word)):
            if len(word)%i == 0:
                flg = 1
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)
assert words_in_sentence(' ') == ''
assert words_in_sentence("abc def ghijk") == "abc def ghijk"
assert words_in_sentence("abc def ghijklm") == "abc def ghijklm"
assert words_in_sentence("abc defghijklmnop") == "abc defghijklmnop"
assert words_in_sentence("How") == "How"
assert words_in_sentence("How are you?") == "How are"
assert words_in_sentence('this is a test') == 'is'
assert words_in_sentence('this test is good') == 'is'
assert words_in_sentence('this is good') == 'is'
assert words_in_sentence('') == ''
assert words_in_sentence('abc def ghijklm nopqrstuvwxyz') == 'abc def ghijklm nopqrstuvwxyz'
assert words_in_sentence('abc def ghijklm nopqrstuvwxyz abc') == 'abc def ghijklm nopqrstuvwxyz abc'
assert words_in_sentence('abc def ghijklm nopqrstuvwxyz abc def ghijklm nopqrstuvwxyz') == 'abc def ghijklm nopqrstuvwxyz abc def ghijklm nopqrstuvwxyz'
assert words_in_sentence('  ab ') == 'ab'
assert words_in_sentence('aa') == 'aa'
assert words_in_sentence('ab') == 'ab'
assert words_in_sentence('abc') == 'abc'
assert words_in_sentence('abc abd') == 'abc abd'
assert words_in_sentence('abc def ghi') == 'abc def ghi'
assert words_in_sentence('abc def ghi j') == 'abc def ghi'
assert words_in_sentence('abc def ghi j k') == 'abc def ghi'
assert words_in_sentence('abc def ghi j k l') == 'abc def ghi'
assert words_in_sentence('abc def ghi j k l m') == 'abc def ghi'
assert words_in_sentence('abc def ghi j k l m n p') == 'abc def ghi'
assert words_in_sentence('abc def ghi j k l m n p q r') == 'abc def ghi'
assert words_in_sentence("loveyouguys") == "loveyouguys", "The function does not produce the right output!"
assert words_in_sentence("loveyou") == "loveyou", "The function does not produce the right output!"
assert words_in_sentence('abc ') == 'abc'
assert words_in_sentence('abc def') == 'abc def'
assert words_in_sentence("hello") == "hello"
assert words_in_sentence('abcdefghijklmnopqrstuvwxyz') == ''
assert words_in_sentence('abcdefghijklmnopqrstuvwxyz ') == ''
assert words_in_sentence("   123   ") == "123"
assert words_in_sentence("   123   456   ") == "123 456"
assert words_in_sentence("1 2 3 4 5") == ""
assert words_in_sentence("1 2 3 4 5 6") == ""
assert words_in_sentence("   1 2 3 4 5 6   ") == ""
assert words_in_sentence("   1 2 3 4 5 ") == ""
assert words_in_sentence("1 2 3 4 5 6 7 8") == ""
assert words_in_sentence("1 2 3 4 5 6 7 8 9") == ""
assert words_in_sentence("Hello ") == "Hello"
assert words_in_sentence("aa A") == "aa"
assert words_in_sentence("Aa A") == "Aa"
assert words_in_sentence("Aaa A") == "Aaa"
assert words_in_sentence("abcdefghijklmnopqrstuvwxyz") == ""
assert words_in_sentence("a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z") == ""
assert words_in_sentence('I am a student.') == 'am'
assert words_in_sentence('Hello') == 'Hello'
assert words_in_sentence("a b c d e f g") == ""
assert words_in_sentence("a b c d e f g h") == ""
assert words_in_sentence("!!!!!") == "!!!!!"
assert words_in_sentence("Hello World!") == "Hello"
