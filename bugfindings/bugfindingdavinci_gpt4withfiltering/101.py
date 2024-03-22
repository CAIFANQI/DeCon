
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
assert words_string("hi, i'm kevin") == ["hi", "i'm", "kevin"]
assert words_string("") == []
assert words_string("12, 24, 456, 24") == ["12", "24", "456", "24"]
assert words_string("Hello world") == ["Hello", "world"]
assert words_string("Viktor, Marko, Ana") == ["Viktor", "Marko", "Ana"]
assert words_string("Python, Ruby, C#, JavaScript") == ["Python", "Ruby", "C#", "JavaScript"]
assert words_string("spam, eggs, ham") == ['spam', 'eggs', 'ham']
assert words_string("a, b, c") == ["a", "b", "c"]
assert words_string("a, b, c, d, e") == ["a", "b", "c", "d", "e"]
assert words_string("this is a string") == ["this", "is", "a", "string"]
assert words_string("a piece of code") == ["a", "piece", "of", "code"]
assert words_string("Hi, there!") == ["Hi", "there!"]
assert words_string("This is an awesome test") == ["This", "is", "an", "awesome", "test"]
assert words_string("four five six") == ["four", "five", "six"]
assert words_string("this is a test") == ["this", "is", "a", "test"]
assert words_string("now is the time") == ["now", "is", "the", "time"]
assert words_string("now is the time for all good men to come to the aid of their country") == ["now", "is", "the", "time", "for", "all", "good", "men", "to", "come", "to", "the", "aid", "of", "their", "country"]
assert words_string("of course, not all exercises are fun") == ["of", "course", "not", "all", "exercises", "are", "fun"]
assert words_string("hello my name is max") == ["hello", "my", "name", "is", "max"]
assert words_string("hi") == ["hi"]
assert words_string("these are words") == ["these", "are", "words"]
assert words_string("are these, words") == ["are", "these", "words"]
assert words_string("these, are words") == ["these", "are", "words"]
assert words_string("Now is the time, the time is now") == ["Now", "is", "the", "time", "the", "time", "is", "now"]
assert words_string("Vampires suck blood") == ["Vampires", "suck", "blood"]
assert words_string("Hello") == ["Hello"]
assert words_string("Hello, how are you") == ["Hello", "how", "are", "you"]
assert words_string("nospaces") == ["nospaces"]
assert words_string("a") == ["a"]
assert words_string("a b") == ["a", "b"]
assert words_string("a b c") == ["a", "b", "c"]
assert words_string("one two") == ["one", "two"]
assert words_string("foo-bar") == ["foo-bar"]
assert words_string("foo-bar bar") == ["foo-bar", "bar"]
assert words_string(",") == []
assert words_string("Hello World!") == ["Hello", "World!"]
assert words_string("This, is, a, test") == ["This", "is", "a", "test"]
assert words_string("This is a string") == ["This", "is", "a", "string"]
assert words_string("Hello ,world") == ["Hello", "world"]
assert words_string("This is a, test") == ["This", "is", "a", "test"]
assert words_string("This is a test, isn't it") == ["This", "is", "a", "test", "isn't", "it"]
assert words_string("How are you?") == ["How", "are", "you?"]
assert words_string("abc def") == ["abc", "def"]
assert words_string("abc-def") == ["abc-def"]
assert words_string("1_2_3") == ["1_2_3"]
assert words_string("hello world") == ["hello", "world"]
assert words_string("word1 word2 word3") == ["word1", "word2", "word3"]
assert words_string("word1 word2 word3, word4") == ["word1", "word2", "word3", "word4"]
assert words_string("word1, word2, word3, word4, word5") == ["word1", "word2", "word3", "word4", "word5"]
assert words_string("dog, cat") == ["dog", "cat"]
assert words_string("dog, cat, fish") == ["dog", "cat", "fish"]
assert words_string("one two three") == ["one", "two", "three"]
assert words_string("Lorem ipsum dolor sit amet") == ["Lorem", "ipsum", "dolor", "sit", "amet"]
assert words_string("Hello, world!") == ["Hello", "world!"]
assert words_string("This is a test") == ["This", "is", "a", "test"]
assert words_string("hey") == ["hey"], "Single word returns wrong value"
assert words_string("hey, buddy") == ["hey", "buddy"], "Two words separated by comma returns wrong value"
assert words_string("How are you? We're good!") == ['How', 'are', 'you?', "We're", 'good!']
assert words_string("1 2 3") == ["1", "2", "3"]
assert words_string("This, is, a, string, of, words") == ["This", "is", "a", "string", "of", "words"]
assert words_string("This is a string, of words") == ["This", "is", "a", "string", "of", "words"]
assert words_string("This") == ["This"]
assert words_string("This is a string of words") == ["This", "is", "a", "string", "of", "words"]
assert words_string("One Two Three") == ["One", "Two", "Three"]
assert words_string("Four Five Six") == ["Four", "Five", "Six"]
assert words_string("Seven Eight Nine") == ["Seven", "Eight", "Nine"]
assert words_string("Hello, world, how, are, you?") == ["Hello", "world", "how", "are", "you?"]
assert words_string("ab cd ef") == ["ab", "cd", "ef"]
assert words_string("ab") == ["ab"]
assert words_string("test test test") == ["test", "test", "test"]
assert words_string("This is a sentence") == ["This", "is", "a", "sentence"]
assert words_string("1 2 3 4 5") == ["1", "2", "3", "4", "5"]
assert words_string("The fox jumped over the dog") == ["The", "fox", "jumped", "over", "the", "dog"]
assert words_string("The") == ["The"]
assert words_string("stressed dessert") == ["stressed", "dessert"]
assert words_string("stressed") == ["stressed"]
assert words_string("Hello, world") == ["Hello", "world"]
assert words_string("hello, world, it, is, me") == ["hello", "world", "it", "is", "me"]
assert words_string("I am a string of words") == ["I", "am", "a", "string", "of", "words"]
assert words_string("Test1 test2 test3") == ["Test1", "test2", "test3"]
assert words_string("Test1") == ["Test1"]
assert words_string("this is a sentence") == ["this", "is", "a", "sentence"]
assert words_string("This is an example!") == ["This", "is", "an", "example!"]
assert words_string("What's the matter with Kansas.") == ["What's", "the", "matter", "with", "Kansas."]
assert words_string("I think the best thing you can do is to forget the past and start over.") == ['I', 'think', 'the', 'best', 'thing', 'you', 'can', 'do', 'is', 'to', 'forget', 'the', 'past', 'and', 'start', 'over.']
assert words_string("Find a thing you love and go after it.") == ['Find', 'a', 'thing', 'you', 'love', 'and', 'go', 'after', 'it.']
assert words_string("hello how are you?") == ["hello", "how", "are", "you?"]
assert words_string("Pete likes to read") == ["Pete", "likes", "to", "read"]
assert words_string("A B, C") == ["A", "B", "C"]
assert ["I", "love", "to", "code"] == words_string("I love to code")
assert ["Here", "is", "an", "example", "of", "text", "justification."] == words_string("Here is an example of text justification.")
assert ["a", "b", "c", "d"] == words_string("a b c d")
assert ["ab", "c", "d"] == words_string("ab c d")
assert words_string("a, b") == ["a", "b"]
assert words_string("a, b, c, d") == ["a", "b", "c", "d"]
assert words_string("one, two, three") == ["one", "two", "three"]
assert words_string("Hello World") == ["Hello", "World"]
assert words_string("hello, world, another") == ["hello", "world", "another"]
assert words_string("hello, world, another test") == ["hello", "world", "another", "test"]
assert words_string("abc") == ["abc"]
assert words_string("Hello, my name is") == ["Hello", "my", "name", "is"]
assert words_string("Hello, World") == ["Hello", "World"]
assert words_string("Hello ,World") == ["Hello", "World"]
assert words_string("A test") == ["A", "test"]
assert words_string("This is a test too") == ["This", "is", "a", "test", "too"]
assert words_string("Hello World, It's me") == ["Hello", "World", "It's", "me"]
assert words_string("my name is muzo") == ["my", "name", "is", "muzo"]
assert words_string("Hello") == ['Hello']
assert words_string("one, two, three, four, five") == ['one', 'two', 'three', 'four', 'five']
assert words_string("one two three four five") == ['one', 'two', 'three', 'four', 'five']
assert words_string("Wow that is sooooo cool") == ["Wow", "that", "is", "sooooo", "cool"]
assert words_string("Oh my god that is amazeballs") == ["Oh", "my", "god", "that", "is", "amazeballs"]
assert words_string("I like cats") == ["I", "like", "cats"]
assert ['hello', 'world'] == words_string('hello world')
assert ['a', 'coder', 'is', 'a', 'programmer'] == words_string('a coder is a programmer')
assert words_string("i, love, programing") == ["i", "love", "programing"]
assert words_string("i_love_programing") == ["i_love_programing"]
assert words_string("Hm...") == ["Hm..."]
assert words_string("a b c d e") == ["a", "b", "c", "d", "e"]
assert words_string("a") == ["a"], "Test 3 Failed"
assert words_string("a, b, c, d, e") == ["a", "b", "c", "d", "e"], "Test 8 Failed"
