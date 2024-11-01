
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
assert words_in_sentence('dolor sit amet') == 'dolor sit'
assert words_in_sentence('integer ut placerat velit') == 'integer ut velit'
assert words_in_sentence("") == ""
assert words_in_sentence("123 12345 123456") == "123 12345"
assert words_in_sentence('lorem ipsum') == 'lorem ipsum'
assert words_in_sentence("Pythons are very strong") == "Pythons are"
assert words_in_sentence("Hello World") == "Hello World"
assert words_in_sentence("one two") == "one two"
assert words_in_sentence("madam i'm adam") == "madam i'm"
assert words_in_sentence("the") == "the"
assert words_in_sentence("I know nothing") == "nothing"
assert words_in_sentence('1234567890abcdef') == ''
assert "" == words_in_sentence("")
assert words_in_sentence("prime") == "prime"
assert words_in_sentence("my prize is primes") == "my prize is"
assert words_in_sentence('Hello') == 'Hello'
assert words_in_sentence('hello world') == 'hello world'
assert words_in_sentence('hello') == 'hello'
assert words_in_sentence("you are my friend") == "you are my"
assert words_in_sentence("One") == "One"
assert words_in_sentence(" ") == ""
assert words_in_sentence("            ") == ""
assert words_in_sentence("a bc def ghi jkl mno pqr stu vwx yz") == "bc def ghi jkl mno pqr stu vwx yz"
assert words_in_sentence("a bc def ghi jkl mno pqr stu vwx yz 123456789") == "bc def ghi jkl mno pqr stu vwx yz"
assert words_in_sentence("a bc def ghi jkl mno pqr stu vwx yz 123456789 abcdefghijklmnopqrstuvwxyz") == "bc def ghi jkl mno pqr stu vwx yz"
assert words_in_sentence('the the the') == 'the the the'
assert words_in_sentence('the the') == 'the the'
assert words_in_sentence('the') == 'the'
assert words_in_sentence('the quick brown fox jumps over the lazy dog') == 'the quick brown fox jumps the dog'
assert words_in_sentence('Well, you are very good') == 'Well, you are'
assert words_in_sentence('You are the best') == 'You are the'
assert words_in_sentence('or') == 'or'
assert words_in_sentence('Hello Hello Hello Hello Hello') == 'Hello Hello Hello Hello Hello'
assert 'you are awesome' == words_in_sentence('you are awesome')
assert 'are you awesome' == words_in_sentence('are you awesome')
assert 'are you' == words_in_sentence('are you')
assert 'you are are are' == words_in_sentence('you are are are')
assert 'and and why' == words_in_sentence('and and why')
assert 'you are' == words_in_sentence('you are')
assert words_in_sentence("Hello World!") == "Hello"
assert words_in_sentence("apple pear") == "apple"
assert words_in_sentence("hey") == "hey"
