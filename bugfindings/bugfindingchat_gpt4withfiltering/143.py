
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
assert words_in_sentence("") == ""
assert words_in_sentence("The quick brown fox") == "The quick brown fox"
assert words_in_sentence("Hello") == "Hello"
assert words_in_sentence("Hello world") == "Hello world"
assert words_in_sentence("The cat is black") == "The cat is black"
assert words_in_sentence("The cat in the hat") == "The cat in the hat"
assert words_in_sentence("This is a test") == "is"
assert words_in_sentence('') == ''
assert words_in_sentence("abc") == "abc"
assert words_in_sentence("abc def") == "abc def"
