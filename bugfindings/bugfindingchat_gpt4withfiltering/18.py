

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
assert how_many_times("hellohellohello", "hello") == 3
assert how_many_times("aaaaaa", "aa") == 5
assert how_many_times("abcdefg", "xyz") == 0
assert how_many_times("aaaaaa", "aaa") == 4
assert how_many_times("ababababab", "aba") == 4, "Test case 2 failed"
assert how_many_times("aaaaa", "aa") == 4, "Test case 3 failed"
assert how_many_times("abcabcabc", "abc") == 3, "Test case 4 failed"
assert how_many_times("abcabcabc", "abcd") == 0, "Test case 5 failed"
assert how_many_times("hello world", "world") == 1, "Test case 2 failed"
assert how_many_times("ababab", "aba") == 2, "Test case 4 failed"
assert how_many_times("aaa", "aaaa") == 0, "Test case 5 failed"
assert how_many_times("abcdefg", "cde") == 1, "Test case 6 failed"
assert how_many_times("aaaaaaa", "aa") == 6, "Test case 3 failed"
assert how_many_times("aaaaaaa", "aa") == 6, "Test case 2 failed"
assert how_many_times("abcdefg", "abc") == 1, "Test case 3 failed"
assert how_many_times("abcdefg", "xyz") == 0, "Test case 4 failed"
assert how_many_times("aaaaaaa", "aaa") == 5, "Test case 5 failed"
assert how_many_times("hello", "ll") == 1
assert how_many_times("hello", "o") == 1
assert how_many_times("hello", "a") == 0
assert how_many_times("hello", "hello") == 1
assert how_many_times("aaaaa", "aa") == 4
assert how_many_times("abcdabcdabcd", "abc") == 3
assert how_many_times('abcabcabc', 'abc') == 3
assert how_many_times('abababab', 'aba') == 3
assert how_many_times('aaaaa', 'aaa') == 3
assert how_many_times('aaaaa', 'aaaa') == 2
assert how_many_times("banana", "ana") == 2, "Test case 2 failed"
assert how_many_times("abababab", "aba") == 3, "Test case 3 failed"
assert how_many_times("aaaaa", "aa") == 4, "Test case 5 failed"
assert how_many_times("mississippi", "iss") == 2
assert how_many_times('aaaaaa', 'aa') == 5
assert how_many_times("aaaaa", "aa") == 4, "Test case 2 failed"
assert how_many_times("abcabcabc", "abc") == 3, "Test case 3 failed"
assert how_many_times("123123123", "123") == 3, "Test case 4 failed"
assert how_many_times("hello", "h") == 1
assert how_many_times("hello", "x") == 0
assert how_many_times("ababababab", "aba") == 4
assert how_many_times("ababab", "aba") == 2, "Test case 5 failed"
assert how_many_times("abcabcabc", "abc") == 3, "Test case 2 failed"
assert how_many_times("abcabcabc", "abcd") == 0, "Test case 4 failed"
assert how_many_times("abababab", "aba") == 3
assert how_many_times("abcabcabc", "abc") == 3
assert how_many_times("hello", "e") == 1
assert how_many_times("hello", "hhello") == 0
assert how_many_times("hello", "hhelloh") == 0
assert how_many_times("abababab", "ab") == 4
assert how_many_times("abcdabcdabcd", "abcd") == 3
assert how_many_times("banana", "an") == 2
assert how_many_times("mississippi", "ss") == 2
assert how_many_times('abcdefg', 'hij') == 0
assert how_many_times("abcdabcdabcdabcd", "abcd") == 4
assert how_many_times("aaaaa", "a") == 5, "Test case 5 failed"
assert how_many_times("hellohellohello", "h") == 3, "Test case 5 failed"
assert how_many_times("hello world", "l") == 3
assert how_many_times("hello world", "ll") == 1
assert how_many_times("hello world", "lo") == 1
assert how_many_times("hello world", "ld") == 1
assert how_many_times("hello world", "hello") == 1
assert how_many_times("hello world", "world") == 1
assert how_many_times("hello world", "e") == 1
assert how_many_times("hello world", " ") == 1
assert how_many_times("hello world", "x") == 0
assert how_many_times("abababab", "bab") == 3
assert how_many_times("abababab", "baba") == 2
assert how_many_times("abababab", "bababa") == 1
assert how_many_times("hello", "lo") == 1
assert how_many_times("hello", "el") == 1
assert how_many_times("aaaaaa", "aa") == 5, "Error: Test Case 2"
assert how_many_times("abcabcabc", "abc") == 3, "Error: Test Case 3"
assert how_many_times("abababab", "aba") == 3, "Error: Test Case 4"
assert how_many_times("aaa", "aaaa") == 0, "Error: Test Case 5"
assert how_many_times("abcdabcdabcd", "abcd") == 3, "Test case 4 failed"
assert how_many_times("aaaaaa", "aaa") == 4, "Test case 5 failed"
assert how_many_times("ababab", "ab") == 3, "Test case 2 failed"
assert how_many_times("aaaaa", "aa") == 4, "Test case 4 failed"
assert how_many_times("abcdefg", "xyz") == 0, "Test case 5 failed"
assert how_many_times("aaaaaaa", "aa") == 6
assert how_many_times("abcdefg", "abc") == 1
assert how_many_times('aaaaa', 'aa') == 4
assert how_many_times('abcabcabc', 'c') == 3
assert how_many_times("abcdefg", "xyz") == 0, "Test case 3 failed"
assert how_many_times("hello", "z") == 0
assert how_many_times("hello", "he") == 1
assert how_many_times("hello", "hel") == 1
assert how_many_times("hello", "hell") == 1
assert how_many_times("hello", "helloo") == 0
assert how_many_times("hello", "hellooo") == 0
assert how_many_times("hello", "helloooo") == 0
assert how_many_times("hello", "hellooooo") == 0
assert how_many_times("hello", "helloooooo") == 0
assert how_many_times("hello", "hellooooooo") == 0
assert how_many_times("hello", "helloooooooo") == 0
assert how_many_times("hello", "hellooooooooo") == 0
assert how_many_times("hello", "helloooooooooo") == 0
assert how_many_times("hello", "hellooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooooooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooooooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooooooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooooooooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooooooooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooooooooooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooooooooooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "helloooooooooooooooooooooooooooooooooooooooooooooooooo") == 0
assert how_many_times("hello", "hellooooooooooooooooooooooooooooooooooooooooooooooooooo") == 0
assert how_many_times("abcdef", "xyz") == 0
assert how_many_times("hellohellohello", "hello") == 3, 'Test Case 2 Failed'
assert how_many_times("hello", "hello") == 1, 'Test Case 3 Failed'
assert how_many_times("hellohellohello", "hi") == 0, 'Test Case 4 Failed'
assert how_many_times("aaaaa", "aa") == 4, 'Test Case 5 Failed'
assert how_many_times("abcdefg", "hij") == 0, 'Test Case 6 Failed'
assert how_many_times("aaaaaa", "aa") == 5, "Test case 2 failed"
assert how_many_times("abcdef", "xyz") == 0, "Test case 3 failed"
assert how_many_times("abcdefg", "hij") == 0
assert how_many_times("abcabcabcabc", "abc") == 4
assert how_many_times("aaa", "aaaa") == 0
assert how_many_times("abcabcabc", "def") == 0
assert how_many_times("abcdefg", "abcdefg") == 1
assert how_many_times("hello", "ello") == 1
assert how_many_times("hello", "llo") == 1
assert how_many_times('ababab', 'aba') == 2
assert how_many_times('aaaa', 'aa') == 3
assert how_many_times('abcdefg', 'xyz') == 0
