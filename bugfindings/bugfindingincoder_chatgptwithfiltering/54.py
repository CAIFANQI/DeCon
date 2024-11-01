

def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    return s0 == s1
assert same_chars("aaa", "aaa") == True
assert same_chars("abc", "ab") == False
assert same_chars("a", "a") == True
assert same_chars("a", "b") == False
assert same_chars("aaaaa","aaaaa") == True
assert same_chars("a","a") == True
assert same_chars("aa","a") == True
assert same_chars("anagram", "anagram") == True
assert same_chars("Hello", "olle") == False
assert same_chars("Hello", "Hello") == True
assert same_chars("ello", "ello") == True
assert same_chars("ello", "Hello") == False
assert same_chars("Hello", "oello") == False
assert same_chars("Hello", "olleo") == False
assert same_chars("oello", "Hello") == False
assert same_chars("olleo", "Hello") == False
assert same_chars("Hello", "ehllo") == False
assert same_chars("Hello", "HelLO") == False
assert same_chars("eHllo", "ello") == False
assert same_chars("eHllo", "olle") == False
assert same_chars("ehllo", "ello") == False
assert same_chars("ehllo", "olle") == False
assert same_chars("ehllo", "Hello") == False
assert same_chars("abacate", "aacatte") == False
assert same_chars("abacate", "abacte") == True
assert same_chars("abacate", "abaccde") == False
assert same_chars("abacate", "abacde") == False
assert same_chars("apple", "ap") is False
assert same_chars("ap", "ap") is True
assert same_chars("ap", "ppl") is False
assert not same_chars('I', 'ams')
assert not same_chars('I', 'i')
assert not same_chars('I', 'ia')
assert not same_chars('I', 'Ia')
assert not same_chars('I', 'A')
assert not same_chars('I', 'O')
assert not same_chars('I', 'OI')
assert not same_chars('I', 'Oii')
assert not same_chars('I', 'Oiii')
assert not same_chars('I', 'Oiiii')
assert not same_chars('I', 'Oiiiii')
assert not same_chars('I', 'Oiiiiii')
assert not same_chars('I', 'Oiiiiiii')
assert not same_chars('I', 'Oiiiiiiii')
assert not same_chars('I', 'Oiiiiiiiii')
assert not same_chars('I', 'Oiiiiiiiiii')
assert not same_chars('I', 'Oiiiiiiiiiii')
assert same_chars('howdy', 'howdy') == True
assert same_chars('howdy', 'howdz') == False
assert same_chars('hello', 'halllo') == False
assert same_chars('howdy', 'wowdz') == False
assert same_chars('howdy', 'yowdz') == False
assert same_chars('howdy', 'yowde') == False
assert same_chars('howdy', 'wowde') == False
assert same_chars('hello', 'helllo') == True
assert same_chars('hello', 'hello') == True
assert same_chars('helo', 'lohe') == True
assert same_chars('helo', 'hellohe') == True
assert same_chars('helo', 'helo') == True
assert same_chars('helo', 'helollo') == True
assert same_chars('', '') == True
assert same_chars('', 'helo') == False
assert same_chars('helo', '') == False
assert same_chars("apple", "aple"), "apple"
assert same_chars("pizza", "piza"), "pizza"
assert same_chars("a", "a"), "a"
assert same_chars("abcdef", "abcdef"), "abcdef"
assert same_chars("abcd", "abcd"), "abcd"
assert same_chars("abcd", "abdc"), "abcd"
assert same_chars("qwertyuiop", "qwertyuiop"), "qwertyuiop"
assert same_chars('ab', 'b') == False
assert same_chars('abcdef', 'abcef') == False
assert same_chars('', 'a') == False
assert same_chars('a', '') == False
assert same_chars('a', 'b') == False
assert same_chars('ab', 'ab') == True
assert same_chars('ab', 'ab ') == False
assert same_chars('a', 'c') == False
assert same_chars('ab', 'bc') == False
assert same_chars('abc', 'abc') == True
assert same_chars('abc', 'abd') == False
assert same_chars('a', 'a') == True
assert same_chars('a', 'ab') == False
assert same_chars('aabc', 'aabc') == True
assert same_chars('abc', 'abca') == True
assert same_chars('abca', 'abca') == True
assert same_chars("abcd", "abcd") == True
assert same_chars("ab", "ab") == True
assert same_chars("ab", "ac") == False
assert same_chars("ab", "acd") == False
assert same_chars("ab", "acde") == False
assert same_chars("ab", "abe") == False
assert same_chars("ab", "abf") == False
assert same_chars("c", "a") == False
assert same_chars("a", "c") == False
assert same_chars("abc", "acb") == True
assert same_chars("abc", "abc") == True
assert same_chars("", "") == True
assert same_chars("abc", "cba") == True
assert same_chars("ab", "ba") == True
assert same_chars("ab", "aba") == True
assert same_chars("ab", "abba") == True
assert same_chars("ba", "ab") == True
assert same_chars("ba", "aba") == True
assert same_chars("sames", "sames") == True
assert same_chars("abba", "abaB") == False
assert same_chars("abba", "aba") == True
assert same_chars("abba", "ab" * 3) == True
assert same_chars("abba", "abba") == True
assert same_chars("abba", "bbb") == False
assert same_chars("abba", "aabb") == True
assert same_chars("abba", "abbaa") == True
assert same_chars('abc', 'acb')
assert same_chars('abc', 'cab')
assert not same_chars('abc', 'aca')
assert not same_chars('abc', 'caa')
assert same_chars('helllo', 'helllo') == True
assert same_chars("cat", "dog") == 0
assert same_chars("kitten", "cat") == 0
assert same_chars("cat", "kitten") == 0
assert not same_chars("abc", "aac")
assert same_chars("abc", "abc")
assert same_chars("abba", "abbb") == True
assert same_chars("abc", "bcd") is False
assert same_chars("abc", "abd") is False
assert same_chars("foo", "bar") == False
assert same_chars('ab', 'a') == False
assert same_chars("abacus", "abacus") == True
assert same_chars("abacus", "abacusz") == False
assert same_chars("banana", "banana") == True
assert same_chars('aa', 'ab') == False
assert same_chars('', 'abc') == False
assert same_chars('abc', '') == False
assert same_chars('abc', 'ab') == False
assert same_chars('', 'aabc') == False
assert same_chars("ab", "ab") is True
assert same_chars("ab", "a") is False
assert same_chars("aaa", "aa") is True
assert same_chars("aaa", "aab") is False
assert same_chars("aa", "ab") is False
assert same_chars("a", "ab") is False
assert same_chars("ab", "abc") == False
assert same_chars("xyz", "abc") == False
assert same_chars('abd', 'abd') == True
assert same_chars('abd', 'abe') == False
assert same_chars('abc', 'abe') == False
assert same_chars('abe', 'abc') == False
assert same_chars('a', 'abc') == False
assert same_chars('abc', 'a') == False
assert same_chars("cat", "cat") is True
assert same_chars("rabbit", "rabbit") is True
assert same_chars("rabbit", "mouse") is False
assert same_chars("abcde", "ac") == False
assert same_chars("abcde", "abc") == False
assert same_chars("abcde", "bcde") == False
assert same_chars("abcde", "abcde") == True
assert same_chars("abcde", "abcdef") == False
assert not same_chars("lemon", "orange")
assert not same_chars("lemon", "lemons")
assert not same_chars("lemon", "lemont")
assert not same_chars("lemon", "limon")
assert not same_chars("lemon", "noon")
assert not same_chars("lemon", "een")
assert not same_chars("lemon", "one")
assert not same_chars("lemon", "e")
assert not same_chars("lemon", "mon")
assert same_chars('test', 'taste') == False
assert same_chars('test','st') == False
assert same_chars("hello", "hallo") == False
assert same_chars("H", "HH") == 1
assert same_chars("H", "HHH") == 1
assert not same_chars('abc', 'aab')
assert same_chars("dog", "dog") == True
assert same_chars("cat", "dog") == False
assert same_chars("cat", "car") == False
assert same_chars("cat", "cars") == False
assert same_chars("apple", "apple") == True
assert same_chars("apple", "orange") == False
assert same_chars("cat", "cat") == True
assert same_chars("dog", "cat") == False
assert same_chars("abcde", "cdea") == False
assert same_chars("abcde", "abce") == False
assert same_chars("aabc", "abc") == True
assert same_chars("ab", "a") == False
assert same_chars("abc", "aabc") == True
assert not same_chars('abc', 'def')
assert not same_chars('abc', 'abd')
assert not same_chars('abc', 'aaa')
assert not same_chars('abc', 'aaaa')
assert same_chars('abcd', 'acde') == False
assert same_chars("a", "b") is False
assert same_chars("aa", "bb") is False
assert same_chars('hello', 'world') == False
assert same_chars('aaaa', 'aaaa') == True
assert same_chars('aaa', 'a') == True
assert same_chars('aaa', 'aa') == True
assert same_chars('hijkl', 'nopq') == False
assert same_chars('hijkl', 'qj') == False
assert same_chars('hijkl', 'rj') == False
assert same_chars('hijkl', 'pq') == False
assert same_chars('hijkl', 'q') == False
assert not same_chars("ab", "ac")
assert same_chars("a", "a")
assert not same_chars("a", "c")
assert not same_chars("a", "ab")
assert same_chars("abcd", "aaa") == False
assert same_chars("aaa", "abcd") == False
assert same_chars("hello", "hey") == False
assert same_chars("hello", "hello") == True
assert same_chars("hey", "heo") == False
assert same_chars("hey", "hey") == True
assert same_chars("a", "ab") == False
assert same_chars("abcd", "abc") == False
assert same_chars("abca", "abcd") == False
assert same_chars("aaba", "abca") == False
assert not same_chars('a', 'c')
assert not same_chars('a', 'bc')
assert not same_chars('h', 'hello')
assert same_chars("helo", "hello") == True
assert same_chars("hello", "helllo") == True
assert same_chars("hello", "elllo") == False
assert same_chars("abc", "acd") == False
assert same_chars("hello", "world") == False
assert same_chars("cat", "cata") == True
assert same_chars("cat", "caca") == False
assert same_chars("cat", "cact") == True
assert same_chars("abc", "bc") == False
assert same_chars("abc", "abcde") == False
assert same_chars("abcd", "abcde") == False
assert same_chars("ab", "ab")
assert not same_chars("ab", "bc")
assert not same_chars('a', 'b')
assert not same_chars('a', 'ab')
assert not same_chars('abc', 'ba')
assert not same_chars('a', 'ac')
assert same_chars("hello", "hello") == 1
assert same_chars("leetcode", "leetcode") == True
assert same_chars("racecar", "racecar") == True
assert same_chars("cat", "racecar") == False
assert same_chars("hello", "hellO") == False
assert same_chars("aa", "ab") == False
assert same_chars("aa", "aa") == True
assert same_chars("hello", "ello") == False
assert same_chars("hello", "world!") == False
assert same_chars('abcd', 'abdcd') == True
assert same_chars('abcde', 'acde') == False
assert same_chars('abcde', 'abcde') == True
assert same_chars("word", "words") == False
assert same_chars("asdf", "asdf")
assert not same_chars("asdf", "asdfx")
assert same_chars("hi", "i") == False
assert not same_chars('abc', 'ab')
assert not same_chars('abc', 'bbc')
assert same_chars("hello", "lol") == False
assert same_chars("hello", "hello ") == False
assert not same_chars("cat", "dog")
assert not same_chars("cat", "python")
assert not same_chars("cat", "doge")
assert same_chars('cat', 'dog') == False
assert same_chars('cat', 'racat') == False
assert same_chars('cat', 'carrot') == False
assert same_chars('cat', 'catcat') == True
assert not same_chars('abba', 'abbbbc')
assert same_chars("hello", "hello")
assert not same_chars("hello", "ello")
assert same_chars('aaa', 'aab') == False
assert same_chars("Hello", "Hola") == 0
assert same_chars("Hello", "Hi!") == 0
assert not same_chars("harry", "harrod")
assert same_chars("python", "pyth") == False
assert same_chars("python", "pythns") == False
assert same_chars('hello', 'hall') == False
assert same_chars("same", "sam") == False
