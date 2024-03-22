
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
assert words_string(",") == []
assert words_string(',') == []
assert words_string("1 2") == ["1", "2"], "1 2"
assert words_string("word") == ["word"]
assert words_string("word1 word2") == ["word1", "word2"]
assert words_string("dog cat fish eggs bird") == ['dog', 'cat', 'fish', 'eggs', 'bird']
assert words_string("dog cat fish eggs bird horse") == ['dog', 'cat', 'fish', 'eggs', 'bird', 'horse']
assert words_string("dog cat fish eggs bird horse run") == ['dog', 'cat', 'fish', 'eggs', 'bird', 'horse', 'run']
assert words_string("dog cat fish eggs bird horse run about") == ['dog', 'cat', 'fish', 'eggs', 'bird', 'horse', 'run', 'about']
assert words_string("one two") == ["one", "two"]
assert words_string("one two three") == ['one', 'two', 'three']
assert words_string('') == []
assert words_string("dog cat fox horse bear") == ["dog", "cat", "fox", "horse", "bear"]
assert words_string("dog cat") == ["dog", "cat"]
assert words_string("dog cat and mouse") == ["dog", "cat", "and", "mouse"]
assert words_string("cat and rat") == ["cat", "and", "rat"]
assert words_string("a b c") == ['a', 'b', 'c']
assert words_string("") == []
assert words_string("hello world") == ["hello", "world"]
assert words_string("hello world,") == ["hello", "world"]
assert words_string("hello") == ["hello"]
assert words_string(",,") == []
assert words_string(",,,") == []
assert words_string(",,,,") == []
assert words_string('apple banana cherry apple') == ['apple', 'banana', 'cherry', 'apple']
assert words_string("apple banana cherry") == ["apple", "banana", "cherry"]
assert words_string("Hello") == ["Hello"]
assert words_string('a b c') == ['a', 'b', 'c']
assert words_string('a b c d') == ['a', 'b', 'c', 'd']
assert words_string('i love apples and oranges') == ['i', 'love', 'apples', 'and', 'oranges']
assert words_string('goodbye') == ['goodbye']
assert words_string(" ".join(['this', 'is', 'an', 'example']))==['this', 'is', 'an', 'example']
assert words_string('this an example')==['this', 'an', 'example']
assert words_string('foo') == ['foo']
assert words_string('foo bar') == ['foo', 'bar']
assert words_string('foobar bat') == ['foobar', 'bat']
assert words_string('Hello') == ['Hello']
assert words_string("a b c d e") == ['a', 'b', 'c', 'd', 'e']
assert words_string("hi") == ['hi']
assert words_string("foo")        == ["foo"]
assert words_string("")           == []
assert words_string("hello")==["hello"]
assert words_string("Hi there")==["Hi","there"]
assert words_string("Hi there Hi there")==["Hi", "there", "Hi", "there"]
assert words_string('hello world') == ['hello', 'world']
assert words_string('hello') == ['hello']
assert words_string('Hello,') == ['Hello']
assert words_string("a b c") == ["a","b","c"]
assert words_string('abc def') == ['abc', 'def']
assert words_string(' '.join(['a', 'b', 'c'])) ==  ['a', 'b', 'c']
assert words_string('') == [], ''
assert words_string('a c d') == ['a', 'c', 'd']
assert words_string(',a,')== ['a']
