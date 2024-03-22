
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
assert 	anti_shuffle("") == ""
assert 	anti_shuffle("aaaaaaaaaaaaaaa") == "aaaaaaaaaaaaaaa"
assert 	anti_shuffle("A B C D E F G H I J") == "A B C D E F G H I J"
assert 	anti_shuffle("Z Y X W V U T S R Q P O N M L K J I H G F E D C B A") == "Z Y X W V U T S R Q P O N M L K J I H G F E D C B A"
assert 	anti_shuffle('a b c d') == 'a b c d'
assert anti_shuffle('A') == 'A'
assert anti_shuffle('12345') == '12345'
assert anti_shuffle('!') == '!'
