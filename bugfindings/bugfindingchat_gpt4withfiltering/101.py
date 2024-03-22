
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
assert words_string("hello world") == ["hello", "world"]
assert words_string("hello, world") == ["hello", "world"]
assert words_string("hello, world,") == ["hello", "world"]
assert words_string("hello world!") == ["hello", "world!"]
assert words_string("hello, world!") == ["hello", "world!"]
assert words_string("one two three") == ["one", "two", "three"]
assert words_string("this is a test") == ["this", "is", "a", "test"]
assert words_string("apple, banana, orange") == ["apple", "banana", "orange"]
assert words_string("a b c d e") == ["a", "b", "c", "d", "e"]
assert words_string("hello world, hello") == ["hello", "world", "hello"]
assert words_string("hello") == ["hello"]
assert words_string("hello world") == ['hello', 'world']
assert words_string("hello, world") == ['hello', 'world']
assert words_string("hello world, how are you") == ['hello', 'world', 'how', 'are', 'you']
assert words_string("hello, world,") == ['hello', 'world']
assert words_string("hello world,") == ['hello', 'world']
assert words_string("hello, world, hello world") == ['hello', 'world', 'hello', 'world']
assert words_string("") == []
assert words_string("how are you") == ['how', 'are', 'you'], "Test case 2 failed"
assert words_string("this is a test") == ['this', 'is', 'a', 'test'], "Test case 4 failed"
assert words_string("hello world") == ['hello', 'world'], "Test case 5 failed"
assert words_string("hello world,") == ["hello", "world"]
assert words_string("hello world, how are you") == ["hello", "world", "how", "are", "you"]
assert words_string("good morning") == ["good", "morning"]
assert words_string("red green blue") == ["red", "green", "blue"]
assert words_string("hello world, how are you?") == ["hello", "world", "how", "are", "you?"]
assert words_string("hello ,world") == ["hello", "world"]
assert words_string("hello ,world,") == ["hello", "world"]
assert words_string("hello, world, how, are, you") == ["hello", "world", "how", "are", "you"]
assert words_string("hello world how are you") == ["hello", "world", "how", "are", "you"]
assert words_string("hello world, hello world") == ["hello", "world", "hello", "world"]
assert words_string("This is a test") == ["This", "is", "a", "test"]
assert words_string("Python, programming, language") == ["Python", "programming", "language"]
assert words_string("I love coding") == ["I", "love", "coding"]
assert words_string("Hello world") == ["Hello", "world"]
assert words_string("Hello") == ["Hello"]
assert words_string("hello,") == ["hello"]
assert words_string("python is awesome") == ['python', 'is', 'awesome']
assert words_string("one two three four five") == ['one', 'two', 'three', 'four', 'five']
assert words_string("One, two, three") == ["One", "two", "three"]
assert words_string("Python is awesome") == ["Python", "is", "awesome"]
assert words_string("One Two Three") == ["One", "Two", "Three"]
assert words_string("hello, world, how, are, you,") == ["hello", "world", "how", "are", "you"]
assert words_string("four five six") == ["four", "five", "six"]
assert words_string("hello world") == ["hello", "world"], "Test case 2 failed"
assert words_string("hello, world") == ["hello", "world"], "Test case 3 failed"
assert words_string("hello world, how are you") == ["hello", "world", "how", "are", "you"], "Test case 4 failed"
assert words_string('Hello world') == ['Hello', 'world']
assert words_string('Hello, world,') == ['Hello', 'world']
assert words_string("programming is fun") == ["programming", "is", "fun"]
assert words_string(",world") == ["world"]
assert words_string(",") == []
assert words_string('hello world') == ['hello', 'world']
assert words_string('hello, world') == ['hello', 'world']
assert words_string('hello, world,') == ['hello', 'world']
assert words_string("apple banana cherry") == ["apple", "banana", "cherry"]
assert words_string("cat dog mouse") == ["cat", "dog", "mouse"]
assert words_string("alpha beta gamma") == ["alpha", "beta", "gamma"]
assert words_string("one two three") == ["one", "two", "three"], "Test case 2 failed"
assert words_string("red blue green") == ["red", "blue", "green"], "Test case 5 failed"
