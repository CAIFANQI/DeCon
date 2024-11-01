
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
assert 	(words_string('Hello, my name is John') == ['Hello','my', 'name', 'is', 'John']), "should return ['Hello','my', 'name', 'is', 'John']"
assert 	words_string("") == []
assert words_string("Double, double toil and trouble") == ['Double', 'double', 'toil', 'and', 'trouble']
assert 	words_string("abc def, ghi") == ["abc", "def", "ghi"]
assert 	words_string("abc, def, ghi") == ["abc", "def", "ghi"]
assert words_string("Hello, my name is Simon") == ['Hello','my', 'name', 'is', 'Simon']
assert words_string("") == []
assert words_string("Hello, my name is Simon, and this is a test") == ['Hello','my', 'name', 'is', 'Simon', 'and', 'this', 'is', 'a', 'test']
assert 	words_string('one, two, three, four') == ['one', 'two', 'three', 'four'],'string test failed'
assert 	words_string('abc def ghi jkl') == ['abc', 'def', 'ghi', 'jkl'], 'incorrect, expected abc,def,ghi,jkl'
assert 	words_string("One, two, three") == 	["One", "two", "three"]
assert 	words_string("double, space") == 	["double", "space"]
assert 	words_string("") == 	[]
assert 	words_string("Hello, My name is Peter, I am 26 years old") == ['Hello', 'My', 'name', 'is', 'Peter', 'I', 'am', '26', 'years', 'old']
assert 	words_string("Hello, my name is Peter, I am 26 years old") == ['Hello','my', 'name', 'is', 'Peter', 'I', 'am', '26', 'years', 'old']
assert 	words_string("Hello, my name is Peter, I am 26 years old.") == ['Hello','my', 'name', 'is', 'Peter', 'I', 'am', '26', 'years', 'old.']
assert 	words_string("1, 2, 3, 4") == ["1", "2", "3", "4"]
assert 	words_string('a b c') == 	['a', 'b', 'c']
assert 	words_string('Hello World') == ['Hello', 'World']
assert 	words_string('Hello, World, How, are, you') == ['Hello', 'World', 'How', 'are', 'you']
assert 	words_string('Hello, World, How, Are, You') == ['Hello', 'World', 'How', 'Are', 'You']
assert words_string("") == 	[]
assert 	words_string('hello') == ['hello']
assert 	words_string('hello, world') == ['hello', 'world']
assert 	words_string('hello, world, this, is, me') == ['hello', 'world', 'this', 'is','me']
