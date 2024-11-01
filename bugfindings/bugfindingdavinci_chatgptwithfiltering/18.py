

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    times = 0

    for i in range(len(string) - len(substring)):
        if string[i:i+len(substring)] == substring:
            times += 1

    return times
assert how_many_times('aaaaaaaa', 'a') == 8
assert how_many_times('aaaaaaaa', 'aa') == 7
assert how_many_times('ssssssss', 'ss') == 7
assert how_many_times('ssssssss', 'sss') == 6
assert how_many_times('ssssssss', 'ssss') == 5
assert how_many_times('ssssssss', 'sssss') == 4
assert how_many_times('ssssssss', 'ssssss') == 3
assert how_many_times('ssssssss', 'sssssss') == 2
assert how_many_times('ssssssss', 'ssssssss') == 1
assert how_many_times('ssssssss', 'sssssssss') == 0
assert how_many_times('ssssssss', 'ssssssssss') == 0
assert how_many_times('abcdabcd', 'ab') == 2
assert how_many_times('lalalalalalala', 'la') == 7
assert how_many_times('abababa', 'aba') == 3
assert how_many_times('haha', 'haa') == 0
assert how_many_times('ababab', 'aba') == 2
assert how_many_times('xx', 'yy') == 0
assert how_many_times('abcdeabc', 'abc') == 2
assert how_many_times('abcdeabc', 'def') == 0
assert how_many_times('GGATC', 'GATC') == 1
assert how_many_times('AAAAA', 'AA') == 4
assert how_many_times('hello world', 'l') == 3
assert how_many_times('hello world', 'hello') == 1
assert how_many_times('hello world', 'a') == 0
assert how_many_times('babababa', 'baba') == 3
assert how_many_times('hahaha', 'aha') == 2
assert how_many_times('ad', 'da') == 0
assert how_many_times('Hello, world!', 'l') == 3
assert how_many_times('Hello, world!', 'Hello') == 1
assert how_many_times('aaa', 'aa') == 2
assert how_many_times('abcabcabc', 'abc') == 3
assert how_many_times('bananap', 'na') == 2
assert how_many_times('bananap', 'bana') == 1
assert how_many_times('bananap', 'bananap') == 1
assert how_many_times('abcabcabcabc', 'abc') == 4
assert how_many_times('babababa', 'nonsense') == 0
assert how_many_times('abcdef', 'abc') == 1
assert how_many_times('abcabc', 'abc') == 2
assert how_many_times('abcabc', 'ab') == 2
assert how_many_times('aaaa', 'aa') == 3
assert how_many_times('123123', '123') == 2
assert how_many_times('123123', '12') == 2
assert how_many_times('123123', '1234') == 0
assert how_many_times('123123', '123123') == 1
assert how_many_times('aaaa', 'aaaa') == 1
assert how_many_times('abc', 'abc') == 1
assert how_many_times('aaaaa', 'aa') == 4
assert how_many_times('aba', 'b') == 1
assert how_many_times('aba', 'ab') == 1
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaa', 'aaac') == 0
assert how_many_times('aaac', 'aaac') == 1
assert how_many_times('aaac', 'ac') == 1
assert how_many_times('candy', 'c') == 1
assert how_many_times('candy', 'and') == 1
assert how_many_times('candy', 'andy') == 1
assert how_many_times('candy', 'andycandyn') == 0
assert how_many_times('aaaa', 'a') == 4
assert how_many_times('aaaa', 'aaa') == 2
assert how_many_times('aaaa', 'aaaaa') == 0
assert how_many_times('abcabcabcabc', 'c') == 4
assert how_many_times('abcabcabcabc', 'd') == 0
assert how_many_times('abcabcabcabc', 'ab') == 4
assert how_many_times('hello world, you are so beautiful', 'o') == 4
assert how_many_times('hello world, you are so beautiful', ' ') == 5
assert how_many_times('torontotoronto', 'toronto') == 2
assert how_many_times('aaabbaaa', 'b') == 2
assert how_many_times('abababab', 'ab') == 4
assert how_many_times('aaaaa', 'a') == 5
assert how_many_times('aabaaabaaaba', 'a') == 9
assert how_many_times('aabaaabaaaba', 'b') == 3
assert how_many_times('abab', 'abab') == 1
assert how_many_times('ab', 'ab') == 1
assert how_many_times('a', 'a') == 1
assert how_many_times('ababab', 'ab') == 3
assert how_many_times('ababa', 'ab') == 2
assert how_many_times('ababab', 'a') == 3
assert how_many_times('ababab', 'b') == 3
assert how_many_times('I would like to be like you', 'love') == 0
assert how_many_times('I would like to be like you', 'you') == 1
assert how_many_times('abcd', 'a') == 1
assert how_many_times('abcd', 'b') == 1
assert how_many_times('abcd', 'c') == 1
assert how_many_times('abcd', 'd') == 1
assert how_many_times('abcd', 'ab') == 1
assert how_many_times('abcd', 'bc') == 1
assert how_many_times('abcd', 'cd') == 1
assert how_many_times('abcd', 'abc') == 1
assert how_many_times('abcd', 'bcd') == 1
assert how_many_times('abcd', 'ac') == 0
assert how_many_times('abcd', 'abd') == 0
assert how_many_times('ABAAB', 'AB') == 2
assert how_many_times('ABAAB', 'ABAAB') == 1
assert how_many_times('ABAAB', 'ABAA') == 1
assert how_many_times('ABAAB', 'ABAABAA') == 0
assert how_many_times('ABAAB', 'ABAABAAA') == 0
assert how_many_times('ABAAB', 'AAB') == 1
assert how_many_times('ABAAB', 'BAA') == 1
assert how_many_times('ABAAB', 'ABBA') == 0
assert how_many_times('ABAAB', 'ABAAA') == 0
assert how_many_times('ABAAB', 'AAAB') == 0
assert how_many_times('ABAAB', 'AAA') == 0
assert how_many_times('ABAAB', 'AAAA') == 0
assert how_many_times('ABAAB', 'BBBB') == 0
assert how_many_times('Hello World', 'lo') == 1
assert how_many_times('Hello World', 'Hello') == 1
assert how_many_times('Hello World', 'Helloo') == 0
assert how_many_times('Hello World', 'l') == 3
assert how_many_times('Hello World', 'o') == 2
assert how_many_times('apple', 'p') == 2
assert how_many_times('apple', 'le') == 1
assert how_many_times('apple', 'lep') == 0
assert how_many_times('apple', 'apple') == 1
assert how_many_times('appleapple', 'apple') == 2
assert how_many_times('appleappleapple', 'apple') == 3
assert how_many_times('', 'a') == 0
assert how_many_times('cbcd', 'c') == 2
assert how_many_times('cbcd', 'cd') == 1
assert how_many_times('cbcd', 'cb') == 1
assert how_many_times('abcdabcd', 'cd') == 2
assert how_many_times('abcdabcd', 'bc') == 2
assert how_many_times('this is a string', 'this') == 1
assert how_many_times('this is a string', 'thisl') == 0
assert how_many_times('this is a string', 'ring') == 1
assert how_many_times('foo', 'oo') == 1
assert how_many_times('foo', 'foofoo') == 0
assert how_many_times('foo', 'foo') == 1
assert how_many_times('aaaccca', 'ca') == 1
assert how_many_times('aaaaa', 'ba') == 0
assert how_many_times('abcabc', 'a') == 2
assert how_many_times('abcabc', 'b') == 2
assert how_many_times('aaa', 'aaa') == 1
assert how_many_times('aaa', 'aaaa') == 0
assert how_many_times('abcabcabc', 'abcabc') == 2
assert how_many_times('abcabcabc', 'abcabcabc') == 1
assert how_many_times('', 'abc') == 0
assert how_many_times('', 'na') == 0, 'Test 3'
assert how_many_times('chocolate', 'ze') == 0, 'Test 4'
assert how_many_times('this is a beautiful day', 'day') == 1
assert how_many_times('a', 'ab') == 0
assert how_many_times('abcdabcd', 'abcd') == 2
assert how_many_times('test', 'e') == 1
assert how_many_times('test', 's') == 1
assert how_many_times('test', 'test') == 1
assert how_many_times('testestest', 'test') == 3
assert how_many_times('testestest', 'testes') == 2
assert how_many_times('testestest', 'es') == 3
assert how_many_times('tes', 'test') == 0
assert how_many_times('', 'test') == 0
assert how_many_times('FooBar', 'Bar') == 1
assert how_many_times('FooBar', 'Foo') == 1
assert how_many_times('FooBar', 'FooBar') == 1
assert how_many_times('FooBarFooBar', 'FooBar') == 2
assert how_many_times('FooBarFooBar', 'Foo') == 2
assert how_many_times('TESTTESTTEST', 'TEST') == 3
assert how_many_times('AAABBbBbB', 'AA') == 2
assert how_many_times('bananabanana', 'nan') == 2
assert how_many_times('bananabanana', 'ban') == 2
assert how_many_times('bananabanana', 'b') == 2
assert how_many_times('bananabanana', 'x') == 0
assert how_many_times('baaab', 'aa') == 2
assert how_many_times('c', 'cc') == 0
assert how_many_times('', 'cc') == 0
assert how_many_times('nana', 'nana') == 1
assert how_many_times('nana', 'nanananananananananana') == 0
assert how_many_times('nana', 'aaaaa') == 0
assert how_many_times('nana', ' ') == 0
assert how_many_times('', 'non empty string') == 0
assert how_many_times('non empty string', '') == 17
assert how_many_times('a', 'aa') == 0
assert how_many_times('', 'aa') == 0
assert how_many_times('abcababc', 'b') == 3
assert how_many_times('abcababc', 'd') == 0
assert how_many_times('abcababc', 'abcab') == 1
assert how_many_times('abcababc', 'abcabc') == 0
assert how_many_times('abcababc', 'aabcab') == 0
assert how_many_times('hello', 'h') == 1
assert how_many_times('hello', 'o') == 1
assert how_many_times('hello', 'x') == 0
assert how_many_times('hello', 'hello') == 1
assert how_many_times('helloh', 'hello') == 1
assert how_many_times('hellloh', 'loh') == 1
assert how_many_times('abacaba', 'c') == 1
assert how_many_times('abacaba', 'e') == 0
assert how_many_times('What is not here is here what?', 'here') == 2
assert how_many_times('What is not here is here what?', 'is') == 2
assert how_many_times('aaa', 'b') == 0
assert how_many_times('', 'b') == 0
assert how_many_times('', '') == 1
assert how_many_times('aaaaaaaaaaaa', 'a') == 12
assert how_many_times('asdfgh', 'sd') == 1
assert how_many_times('asdfgh', 'df') == 1
assert how_many_times('asdfgh', 'gh') == 1
assert how_many_times('asdfgh', 'asd') == 1
assert how_many_times('asdfgh', 'fgh') == 1
assert how_many_times('asdfgh', 'asdfgh') == 1
assert how_many_times('hello there', ' ') == 1
assert how_many_times('hello there', 'hello') == 1
assert how_many_times('hello there', 'e') == 3
assert how_many_times('hello there', 'there') == 1
assert how_many_times('aaaaaaaaaa', 'aa') == 9
assert how_many_times('aaaaaaaaaa', 'a') == 10
assert how_many_times('aaaaaaaaaa', 'b') == 0
assert how_many_times('ABC', 'B') == 1
assert how_many_times('ABC', 'C') == 1
assert how_many_times('ABC', 'D') == 0
assert how_many_times('ABC', 'AB') == 1
assert how_many_times('ABC', 'ABC') == 1
assert how_many_times('ABC', 'ABD') == 0
assert how_many_times('AAAA', 'A') == 4
assert how_many_times('AAAA', 'AA') == 3
assert how_many_times('AAAA', 'AAA') == 2
assert how_many_times('AAAA', 'AAAA') == 1
assert how_many_times('AAAA', 'AAAAA') == 0
assert how_many_times('AAAA', 'AAB') == 0
assert how_many_times('ABCDEFG', 'EF') == 1
assert how_many_times('bobobobobobobobobobobobobobobob', 'bob') == 15
assert how_many_times('aabaabaaa', 'aab') == 2
assert how_many_times('aa', 'a') == 2
assert how_many_times('hello', 'b') == 0
assert how_many_times('abbbbbbcd', 'bbbbbbbb') == 0
assert how_many_times('abbbbbbcd', 'c') == 1
assert how_many_times('abbbbbbcd', 'cb') == 0
assert how_many_times('abbbbbbcd', 'cbb') == 0
assert how_many_times('abbbbbbcd', 'bc') == 1
assert how_many_times('aabaaab', 'aa') == 3
assert how_many_times('cabca', 'ca') == 2
assert how_many_times('cabca', 'ab') == 1
assert how_many_times('cabca', 'bc') == 1
assert how_many_times('cabca', 'a') == 2
assert how_many_times('cabca', 'b') == 1
assert how_many_times('cabca', 'd') == 0
assert how_many_times('aab', 'aa') == 1
assert how_many_times('aab', 'aaa') == 0
assert how_many_times('aab', 'aaaa') == 0
assert how_many_times('aaabbbccc', 'bb') == 2
assert how_many_times('aaabbbccc', 'abc') == 0
assert how_many_times('abcabcabc', 'zzz') == 0
assert how_many_times('I love Python', 'love') == 1
assert how_many_times('I love Python and love programming', 'love') == 2
assert how_many_times('aaaaaa', 'aab') == 0
assert how_many_times('aaaaaa', 'b') == 0
assert how_many_times('foofoofoo', 'foo') == 3
assert how_many_times('banana', 'ana') == 2
assert how_many_times('banana', 'ban') == 1
assert how_many_times('banana', 'nana') == 1
assert how_many_times('banana', 'banana') == 1
assert how_many_times('abcdef', 'a') == 1
assert how_many_times('abcdef', 'b') == 1
assert how_many_times('abcdef', 'c') == 1
assert how_many_times('abcdef', 'd') == 1
assert how_many_times('abcdef', 'e') == 1
assert how_many_times('abcdef', 'f') == 1
assert how_many_times('abcdef', 'aa') == 0
assert how_many_times('abcdef', 'ab') == 1
assert how_many_times('abcdef', 'ac') == 0
assert how_many_times('abcdef', 'ad') == 0
assert how_many_times('abcdef', 'ae') == 0
assert how_many_times('abcdef', 'af') == 0
assert how_many_times('abcdef', 'ba') == 0
assert how_many_times('abcdef', 'bd') == 0
assert how_many_times('abcdef', 'be') == 0
assert how_many_times('banana', 'na') == 2
assert how_many_times('abcdef', 'ef') == 1
assert how_many_times('abcdef', 'efg') == 0
assert how_many_times('abbabbabb', 'bb') == 3
assert how_many_times('', 'll') == 0
assert how_many_times('ll', 'll') == 1
assert how_many_times('llll', 'll') == 3
assert how_many_times('lll', 'll') == 2
assert how_many_times('abcdefabcdef', 'ef') == 2
assert how_many_times('abcdefabcdef', 'abc') == 2
assert how_many_times('abcdefabcdef', 'abcdef') == 2
assert how_many_times('abcdefabcdef', 'abcdefabcdef') == 1
assert how_many_times('приветпривет', 'привет') == 2
assert how_many_times('wowow', 'ow') == 2
assert how_many_times('awesome', 'e') == 2
assert how_many_times('amazing', 'zing') == 1
assert how_many_times('cocacola', 'co') == 2
assert how_many_times('bobobob', 'bb') == 0
assert how_many_times('bobobob', 'aaa') == 0
assert how_many_times('bobobob', 'bba') == 0
assert how_many_times('ababaab', 'abc') == 0
assert how_many_times('hihihi', 'hi') == 3
assert how_many_times('hihihi', 'x') == 0
assert how_many_times('', 'hello') == 0
assert how_many_times('CATCAT', 'CAT') == 2
assert how_many_times('CATCAT', 'A') == 2
assert how_many_times('CATCAT', 'T') == 2
assert how_many_times('CATCAT', 'G') == 0
assert how_many_times('CATCAT', 'CATCAT') == 1
assert how_many_times('CATCAT', 'CATCA') == 1
assert how_many_times('CATCAT', 'ATCAT') == 1
assert how_many_times('CATCAT', 'CA') == 2
assert how_many_times('CATCAT', 'C') == 2
assert how_many_times('CATCAT', 'AT') == 2
assert how_many_times('CATCAT', 'ATG') == 0
assert how_many_times('hello world!', 'l') == 3
assert how_many_times('hello world!', 'hello') == 1
assert how_many_times('hello world!', 'world') == 1
assert how_many_times('a' * 1000 + 'b' * 1000, 'a') == 1000
assert how_many_times('ab', 'a') == 1
assert how_many_times('aab', 'a') == 2
assert how_many_times('aab', 'b') == 1
assert how_many_times('aaab', 'a') == 3
assert how_many_times('aaaab', 'a') == 4
assert how_many_times('banana', 'a') == 3
assert how_many_times('banana', 'b') == 1
assert how_many_times('banana', 'n') == 2
assert how_many_times('banana', 'x') == 0
assert how_many_times('aaaaa', 'aaa') == 3
assert how_many_times('aaaaa', 'aaaa') == 2
assert how_many_times('aaaaa', 'aaaaa') == 1
assert how_many_times('asdasdasd', 'asd') == 3
assert how_many_times('asdasdasd', 'as') == 3
assert how_many_times('asdasdasd', 'z') == 0
assert how_many_times('ab', 'b') == 1
assert how_many_times('ba', 'a') == 1
assert how_many_times('baba', 'ba') == 2
assert how_many_times('ababababababab', 'aba') == 6
assert how_many_times('ababababababab', 'ba') == 6
assert how_many_times('hello', 'lo') == 1
assert how_many_times('hello', 'he') == 1
assert how_many_times('hello', 'l') == 2
assert how_many_times('hello', 'e') == 1
assert how_many_times('hhehelloooo', 'he') == 2
assert how_many_times('wowomgzomg', 'omg') == 2
assert how_many_times('hello my love', ' ') == 2
assert how_many_times('abcdef', 'cd') == 1
assert how_many_times('whereareyou', 'you') == 1
assert how_many_times('whereareyou', 'youyou') == 0
assert how_many_times('hello', 'llll') == 0
assert how_many_times('', 'llll') == 0
assert how_many_times('aaaaaa', 'aa') == 5
assert how_many_times('wewillwewillrockyou', 'we') == 2
assert how_many_times('wewillwewillrockyou', 'wewill') == 2
assert how_many_times('wewillwewillrockyou', 'rock') == 1
assert how_many_times('wewillwewillrockyou', 'you') == 1
assert how_many_times('wewillwewillrockyou', 'will') == 2
assert how_many_times('wewillwewillrockyou', 'wewillrockyou') == 1
assert how_many_times('dwadwadwad', 'adw') == 2
assert how_many_times('dwadwadwad', 'awd') == 0
assert how_many_times('aabaaaaab', 'a') == 7
assert how_many_times('aabaaaaab', 'b') == 2
assert how_many_times('aaaaaaaaa', 'ab') == 0
assert how_many_times('aaaaaaaaa', '') == 10
assert how_many_times('bcabcabcabcabc', 'abc') == 4
assert how_many_times('hello', 'll') == 1
assert how_many_times('hello', 'hel') == 1
assert how_many_times('hello', 'lhe') == 0
assert how_many_times('hello', 'lllo') == 0
assert how_many_times('hello', 'llo') == 1
assert how_many_times('b', 'a') == 0
assert how_many_times('abc', 'a') == 1
assert how_many_times('aba', 'aba') == 1
assert how_many_times('aba', 'abb') == 0
assert how_many_times('ababab', 'bab') == 2
assert how_many_times('abababa', 'bab') == 2
assert how_many_times('asdfsdfsdfsasdf', 'asdf') == 2
assert how_many_times('asdfasdf', 'asdfasdf') == 1
assert how_many_times('aaaaaaaa', 'aaaaaaaa') == 1
assert how_many_times('aaaaaaaa', 'aaaaaaa') == 2
assert how_many_times('aaaaaaaa', 'aaaaaa') == 3
assert how_many_times('', 'at') == 0
assert how_many_times('aaaababaabaaab', 'aaabaa') == 0
assert how_many_times('hellohello', 'l') == 4
assert how_many_times('hellohello', 'lo') == 2
assert how_many_times('hellohello', 'hello') == 2
assert how_many_times('hellohellooo', 'hello') == 2
assert how_many_times('hellohellooo', 'ooo') == 1
assert how_many_times('', 'x') == 0
assert how_many_times('hellohello', 'b') == 0
assert how_many_times('hellohello', 'hell') == 2
assert how_many_times('hellohello', 'hellohello') == 1
assert how_many_times('hellohello', 'hellohelloo') == 0
assert how_many_times('abba', 'bb') == 1
assert how_many_times('bbba', 'bb') == 2
assert how_many_times('bbba', 'bbb') == 1
assert how_many_times('bbbb', 'bb') == 3
assert how_many_times('abb', 'ab') == 1
assert how_many_times('abb', 'bb') == 1
assert how_many_times('abcde', 'abc') == 1
assert how_many_times('abcde', 'abcde') == 1
assert how_many_times('abcde', 'bcd') == 1
assert how_many_times('123a123a123a', '123a') == 3
assert how_many_times('123A123a123a', '123a') == 2
assert how_many_times('abcdabcd', 'abcdabcdabcd') == 0
assert how_many_times('AAAaaa', 'aa') == 2
assert how_many_times('wololo', 'lol') == 1
assert how_many_times('wololo', 'olo') == 2
assert how_many_times('aaaaa', 'b') == 0
assert how_many_times('aaabaaab', 'aaab') == 2
assert how_many_times('a', 'abc') == 0
assert how_many_times('aaaab', 'aaab') == 1
assert how_many_times('ab', 'abab') == 0
assert how_many_times('ab', 'aba') == 0
assert how_many_times('ab', 'abc') == 0
assert how_many_times('abcabc', 'aba') == 0
assert how_many_times('zab', 'a') == 1
assert how_many_times('abc', 'c') == 1
assert how_many_times('abc', 'd') == 0
assert how_many_times('abcabcabc', 'b') == 3
assert how_many_times('abcabcabc', 'bc') == 3
assert how_many_times('00000000', '0') == 8
assert how_many_times('a', 'b') == 0
assert how_many_times('bbb', 'bb') == 2
assert how_many_times('aaaaa', 'aaaaaa') == 0
assert how_many_times('Hello, world!', 'W') == 0
assert how_many_times('Hello, world!', 'wo') == 1
assert how_many_times('abcabcabc', 'ab') == 3
assert how_many_times('abcabcabc', 'a') == 3
assert how_many_times('abcabcabc', 'c') == 3
assert how_many_times('abcabcabc', 'd') == 0
assert how_many_times('this is this and that is this', 'that') == 1
assert how_many_times('this is this and that is this', 'and') == 1
