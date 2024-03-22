
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    return sorted(words)[0]
assert find_max(["", ""]) == ""
assert find_max(["", "", ""]) == ""
assert find_max(["", "", "a"]) == "a"
assert find_max(["", "", "a", "a"]) == "a"
assert find_max(["", "", "a", "a", "a"]) == "a"
assert find_max(["", "", "a", "a", "a", "a"]) == "a"
assert find_max(["", "a"]) == "a"
assert find_max(["", "a", "a"]) == "a"
assert find_max(["", "a", "a", "a"]) == "a"
assert find_max(["", "a", "a", "a", "a"]) == "a"
assert find_max(["", "a", "a", "a", "a", "a"]) == "a"
assert find_max(["", "a", "a", "a", "a", "a", "a"]) == "a"
assert find_max(["", "a", "a", "a", "a", "a", "a", "a"]) == "a"
assert find_max(["", "a", "a", "a", "a", "a", "a", "a", "a"]) == "a"
assert find_max(["", "a", "a", "a", "a", "a", "a", "a", "a", "a"]) == "a"
assert find_max(["", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]) == "a"
assert find_max(["", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]) == "a"
assert find_max(["", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]) == "a"
assert find_max(["", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]) == "a"
assert find_max(['aaaa', 'aaaa', 'aaaa']) == 'aaaa'
assert find_max(['aaaa', 'aaaa', 'aaaa', 'aaaa']) == 'aaaa'
assert find_max(['aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa']) == 'aaaa'
assert find_max(['aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa']) == 'aaaa'
assert find_max(['aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa']) == 'aaaa'
assert find_max(['aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa', 'aaaa']) == 'aaaa'
assert find_max(['a']) == 'a'
assert find_max(['a', 'a']) == 'a'
assert find_max(["", "", "piglet", "piglet", "piglet"]) == "piglet"
assert find_max(["", "", "piglet", "doglet", "piglet", "doglet", "piglet", "doglet"]) == "doglet"
assert find_max(["", "", "piglet", "doglet", "piglet", "doglet", "doglet", "doglet", "piglet"]) == "doglet"
assert find_max(["", "", "piglet", "doglet", "piglet", "doglet", "doglet", "doglet", "piglet", "doglet", "doglet"]) == "doglet"
assert find_max(['helo', 'hello', 'hell', 'hel', 'helloo']) == 'hello'
assert find_max(['helo', 'hello', 'hell', 'hel', 'helloo', 'helloooo']) == 'hello'
assert find_max(["", "a", "b", "c", "d", "d", "e", "e", "c", "e", "f", "a"]) == "a"
assert find_max(["", "a", "b", "c", "d", "d", "e", "e", "c", "e", "f", "a", "d"]) == "a"
assert find_max(["", "a", "b", "c", "d", "d", "e", "e", "c", "e", "f", "a", "b", "d"]) == "a"
assert find_max(["", "a", "b", "c", "d", "d", "e", "e", "c", "e", "f", "a", "b", "c", "d"]) == "a"
assert find_max(["", "a", "b", "c", "d", "d", "e", "e", "c", "e", "f", "a", "b", "c", "d", "e"]) == "a"
assert find_max([ "apple", "app", "ppl", "apple", "lpl", "pl", "le" ])  ==  "apple"
assert find_max([ "apple", "app", "ppl", "apple", "lpl", "pl", "le", "al" ])  ==  "apple"
assert find_max([ "apple", "app", "ppl", "apple", "lpl", "pl", "le", "al", "lle" ])  ==  "apple"
assert find_max([ "apple", "app", "ppl", "apple", "lpl", "pl", "le", "al", "lle", "apl" ])  ==  "apple"
assert find_max([ "apple", "app", "ppl", "apple", "lpl", "pl", "le", "al", "lle", "apl", "appl" ])  ==  "apple"
assert find_max([ "apple", "app", "ppl", "apple", "lpl", "pl", "le", "al", "lle", "apl", "appl", "app" ])  ==  "apple"
assert find_max([ "apple", "app", "ppl", "apple", "lpl", "pl", "le", "al", "lle", "apl", "appl", "app", "a" ])  ==  "apple"
assert find_max(['foo']) == 'foo'
assert find_max(["", "a", "aa"]) == "a"
assert find_max(["", "", "", ""]) == ""
assert find_max(["", "", "", "", ""]) == ""
assert find_max(["", "", "", "", "", ""]) == ""
assert find_max(["", "", "", "", "", "", "a"]) == "a"
assert find_max(["", "", "", "", "", "", "a", "b"]) == "a"
assert find_max(["", "", "", "", "", "", "a", "b", "c"]) == "a"
assert find_max(["", "", "", "", "", "", "a", "b", "c", "d"]) == "a"
assert find_max(['one', 'one', 'one', 'two', 'one']) == 'one'
assert find_max(['one', 'one', 'one', 'one', 'two']) == 'one'
assert find_max(['one', 'one', 'one', 'two', 'two']) == 'one'
assert find_max(['asdf', 'zxcv', 'qwer']) == 'asdf'
assert find_max(['qwer', 'asdf', 'zxcv']) == 'asdf'
assert find_max(['asdf', 'zxcv', 'asdf']) == 'asdf'
assert find_max(['asdf', 'asdf', 'zxcv', 'asdf']) == 'asdf'
assert find_max(['asdf', 'qwer', 'zxcv', 'asdf']) == 'asdf'
assert find_max(['zxcv', 'asdf', 'asdf', 'asdf']) == 'asdf'
assert find_max(['asdf', 'qwer', 'zxcv', 'asdf', 'qwer']) == 'asdf'
assert find_max(['asdf', 'qwer', 'zxcv', 'asdf', 'qwer', 'zxcv']) == 'asdf'
assert find_max(['zxcv', 'qwer', 'zxcv', 'asdf', 'qwer', 'asdf', 'qwer']) == 'asdf'
assert find_max(['asdf', 'qwer', 'zxcv', 'asdf', 'qwer', 'zxcv', 'qwer']) == 'asdf'
assert find_max(["a", "b", "c", "a", "d", "a", "a"]) == "a"
assert find_max(["a", "b", "c", "a", "d", "e", "a"]) == "a"
assert find_max(['a', 'b', 'c', 'a']) == 'a'
assert find_max(['a', 'a', 'b', 'c']) == 'a'
assert find_max(['a', 'abc']) == 'abc'
assert find_max(['a', 'a', 'b']) == 'a'
assert find_max(['a', 'a', 'a', 'b']) == 'a'
assert find_max(['a', 'b', 'c', 'a', 'c']) == 'a'
assert find_max(['ab', 'ac', 'ab']) == 'ab'
assert find_max(['ba', 'ba', 'ba']) == 'ba'
assert find_max(['ba', 'ba', 'ba', 'ba']) == 'ba'
assert find_max(['ab', 'ab', 'ab']) == 'ab'
assert find_max(['ab', 'ab', 'ab', 'ab']) == 'ab'
assert find_max(['ab', 'ab', 'ab', 'ab', 'ab']) == 'ab'
assert find_max(['ab', 'ab', 'ab', 'ab', 'ab', 'ab']) == 'ab'
assert find_max(['ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab']) == 'ab'
assert find_max(['ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab']) == 'ab'
assert find_max(['a', 'ab', 'ab', 'ab', 'ab']) == 'ab'
assert find_max(['one', 'elephant', 'elephant', 'elephant']) == 'elephant'
assert find_max(['one', 'one', 'two']) == 'one'
assert find_max(['one', 'two', 'one']) == 'one'
assert find_max(["a", "a", "b", "c"]) == "a"
assert find_max(["a", "a"]) == "a"
assert find_max(["a", "a", "b"]) == "a"
assert find_max(["aa", "ab", "ab", "ba", "ca", "ca", "b", "bb"]) == "ab"
assert find_max(["aaa", "ab", "ab", "ba", "caa", "ca", "b", "bb", "ca", "ca"]) == "ab"
assert find_max(["aaa", "ab", "ab", "ba", "caa", "ca", "b", "bb", "ca", "ca", "ca"]) == "ab"
assert find_max(["aaa", "ab", "ab", "ba", "caa", "ca", "b", "bb", "ca", "ca", "ca", "ca"]) == "ab"
assert find_max(["a", ""]) == "a"
assert find_max(["ab", "abc", "cab"]) == "abc"
assert find_max(['hello', 'hello']) == 'hello'
assert find_max(['word', 'word']) == 'word'
assert find_max(['word']) == 'word'
assert find_max(['word', 'otherword']) == 'otherword'
assert find_max(['', '']) == ''
assert find_max(['', 'word']) == 'word'
assert find_max(['word', '', 'word']) == 'word'
assert find_max(['', '', '', 'word']) == 'word'
assert find_max(['', '', 'word', 'word']) == 'word'
assert find_max(['word', 'word', 'word', 'word', 'word']) == 'word'
assert find_max(['hi', 'hi', 'hi']) == 'hi'
assert find_max(['hi', 'ho', 'ho', 'hi']) == 'hi'
assert find_max(['hi', 'hi', 'hi', 'hi']) == 'hi'
assert find_max(['hi', 'hi', 'ho', 'ho', 'hi']) == 'hi'
assert find_max(['hi', 'hi', 'hi', 'ho', 'ho', 'hi']) == 'hi'
assert find_max(["", "b", "c", "b"]) == "b"
assert find_max(["", "ab", "a", "ab"]) == "ab"
assert find_max(["", "aa", "ab", "aa"]) == "ab"
assert find_max(["", "ab", "ab", "ab"]) == "ab"
assert find_max(["word"]) == "word"
assert find_max(["word", "word"]) == "word"
assert find_max(["ab", "ab", "ab", "ab"]) == "ab"
assert find_max(["", "a", "", "a"]) == "a"
assert find_max(["", "a", "", "a", ""]) == "a"
assert find_max(["", "a", "", "a", "a"]) == "a"
assert find_max(["a", "a", "a"]) == "a"
assert find_max(["ab", "abc", "b"]) == "abc"
assert find_max(["ab", "ab"]) == "ab"
assert find_max(["ab", "bb"]) == "ab"
assert find_max(["aa", "bb", "bb", "aa"]) == "aa"
assert find_max(["aa", "ab", "ab", "ba"]) == "ab"
assert find_max(["aa", "ab", "ba", "ab"]) == "ab"
assert find_max(["a", "a", "a", "a", "a"]) == "a"
assert find_max(["aba", "aba", "tabby", "aba"]) == "tabby"
assert find_max(["aba", "aba", "tabby", "dog"]) == "tabby"
assert find_max(["tabby", "aba", "tabby", "dog"]) == "tabby"
assert find_max(["a", "c", "a", "b", "a", "a"]) == "a"
assert find_max(["a"]) == "a"
assert find_max(['abc']) == 'abc'
assert find_max(['abbc']) == 'abbc'
assert find_max(['ab', 'abc']) == 'abc'
assert find_max(['a', 'ab']) == 'ab'
assert find_max(['a', 'abbb']) == 'abbb'
assert find_max(['abbb', 'ab']) == 'ab'
assert find_max(["", "", "c"]) == "c"
assert find_max(["", "a", "b"]) == "a"
assert find_max(["", "", "a", "b"]) == "a"
assert find_max(["", "aa", "bb"]) == "aa"
assert find_max(["a", "b", "c"]) == "a"
assert find_max(["a", "b", "c", "a"]) == "a"
assert find_max(["a", "b", "b", "b", "c", "a"]) == "a"
assert find_max(["a", "b", "a", "a", "b", "a", "a", "a"]) == "a"
assert find_max(["a", "a", "a", "a", "b", "a", "b", "a"]) == "a"
assert find_max(["a", "a", "a", "b", "b", "a", "a", "a"]) == "a"
assert find_max(['abc', 'abc', 'ab']) == 'abc'
assert find_max(['a', 'ab', 'ab']) == 'ab'
assert find_max(['a', 'a', 'a']) == 'a'
assert find_max(['hello', 'hello', 'hello']) == 'hello'
assert find_max(['hello', 'hello', 'hell', 'hello']) == 'hello'
assert find_max(['heello', 'hel']) == 'heello'
assert find_max(['I', 'love', 'Python', 'coding', 'Python']) == 'Python'
assert find_max(["aa", "ab", "ab", "ba", "ba"]) == "ab"
assert find_max(["ba", "aa", "ba", "ba"]) == "ba"
assert find_max(["a", "b", "a"]) == "a"
assert find_max(["a", "", "a"]) == "a"
assert find_max(["hello", "hel", "heel"]) == "hello"
assert find_max(["hello", "hel", "hee"]) == "hello"
assert find_max(["hello", "hel", "he"]) == "hello"
assert find_max(["he", "hee", "hel", "hell", "hello"]) == "hello"
assert find_max(["he", "hee", "he", "hell", "hello"]) == "hello"
assert find_max(["python", "python", "python"]) == "python"
assert find_max(["python", "java", "python", "python"]) == "python"
assert find_max([ 'aa', 'ab', 'ab', 'bb' ]) == 'ab'
assert find_max(['aaa', 'a', 'aaa', 'b', 'b', 'c', 'd', 'e']) == 'a'
assert find_max(['aaa', 'aaa']) == 'aaa'
assert find_max(['cat', 'dog', 'dog', 'cat']) == 'cat', "Test case 4 failed"
assert find_max(['dog', 'dog', 'cat', 'cat']) == 'cat', "Test case 5 failed"
assert find_max(['cat', 'dog', 'cat', 'cat']) == 'cat', "Test case 6 failed"
assert find_max(['racecar', 'car', 'car']) == 'racecar'
assert find_max(['']) == ''
assert find_max(['ba', 'ac', 'ca', 'cb']) == 'ac'
assert find_max(['aa', 'ab', 'ba', 'ab']) == 'ab'
assert find_max(['aa', 'ab', 'ab', 'ba']) == 'ab'
assert find_max(['ab', 'bb', 'bc', 'ba']) == 'ab'
assert find_max(['a', 'bb', 'ba', 'ab']) == 'ab'
assert find_max(["ab", "abcd"]) == "abcd"
assert find_max(["a", "a", "b", "c", "c"]) == "a"
assert find_max(['cat', 'hat', 'dog']) == 'cat'
assert find_max(['cat', 'hat', 'dog', 'hat', 'cat']) == 'cat'
assert find_max(["bbbb","aa","ccc"]) == "aa"
assert find_max(["a","b","c"]) == "a"
assert find_max(['aad']) == 'aad'
assert find_max(['aab', 'aac']) == 'aab'
assert find_max(["a", "a", "a", "a", "b"]) == "a"
assert find_max(["a", "b", "c", "c", "a"]) == "a"
assert find_max(["dog", "rachel", "rachel"]) == "rachel"
assert find_max(["abc"]) == "abc"
assert find_max(['', 'a', 'b', 'c', '', '']) == 'a'
assert find_max(['aba', 'aba']) == 'aba', 'Test case fail'
assert find_max(['', '', '']) == '' 
assert find_max(['aa', 'abb', 'acccc']) == 'abb'
assert find_max(["apple", "appple"]) == "apple"
assert find_max(['a', 'ab', 'aab']) == 'aab'
assert find_max(['aba', 'aba']) == 'aba'
assert find_max(["aba", "aba"]) == "aba"
assert find_max(["aa", "a", "a", "b"]) == "a"
