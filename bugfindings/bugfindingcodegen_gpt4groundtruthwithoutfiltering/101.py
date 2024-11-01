
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    if not s:
        return []

    s_list = []

    for letter in s:
        if letter == ',':
            s_list.append(',')
        else:
            s_list.append(letter)

    s_list = "".join(s_list)
    return s_list.split()
assert 	(words_string('Hello') == ['Hello']), "should return ['Hello']"
assert 	words_string("") == []
assert words_string("") == []
assert 	words_string('abc def ghi jkl') == ['abc', 'def', 'ghi', 'jkl'], 'incorrect, expected abc,def,ghi,jkl'
assert 	words_string("") == 	[]
assert 	words_string('a b c') == 	['a', 'b', 'c']
assert 	words_string('Hello World') == ['Hello', 'World']
assert words_string("") == 	[]
assert 	words_string('hello') == ['hello']
