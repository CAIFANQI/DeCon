
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
assert 	words_in_sentence("A test is not a test") == "is not", "A test is not a test"
assert 	words_in_sentence("1 2 3") == "", "1 2 3"
assert 	words_in_sentence("") == ""
assert 	words_in_sentence("Mary did not go to the store yesterday.") == 'did not go to the store', 'error'
assert 	words_in_sentence('the quick brown fox') == 'the quick brown fox'
assert 	words_in_sentence('the quick brown fox jumps') == 'the quick brown fox jumps'
assert 	words_in_sentence("I have a new car") == 'new car'
assert 	words_in_sentence("I have a new car with a person") == 'new car'
