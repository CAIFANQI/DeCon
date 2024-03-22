

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
assert how_many_times("homer simpson", "simson") == 0, "homer simpson"
assert how_many_times("python", "o") == 1
assert how_many_times("the quick brown fox jumps over the lazy dog", "quick") == 1
assert how_many_times("the quick brown fox jumps over the lazy dog", "lazy") == 1
assert how_many_times("the quick brown fox jumps over the lazy dog", "brown") == 1
assert how_many_times("the quick brown fox jumps over the lazy dog", "jumps") == 1
assert how_many_times("ABCDE", "BCDE") == 1
assert how_many_times("ABCDE", "BDE") == 0
assert how_many_times("ab", "aba") == 0
assert how_many_times("ab", "abb") == 0
assert how_many_times("ab", "abab") == 0
assert how_many_times("ab", "aab") == 0
assert how_many_times("bananas", "naa") == 0
assert how_many_times("bananas", "naan") == 0
assert how_many_times("bananas", "naans") == 0
assert how_many_times("bananas", "nasa") == 0
assert how_many_times("bananas", "nnaa") == 0
assert how_many_times("bananas", "naanan") == 0
assert how_many_times("bananas", "naanana") == 0
assert how_many_times("bananas", "naananas") == 0
assert how_many_times("bananas", "naananaan") == 0
assert how_many_times("bananas", "naananaanaan") == 0
assert how_many_times("bananas", "naananaanas") == 0
assert how_many_times("bananas", "naananaanaanas") == 0
assert how_many_times("bananas", "naananaanasa") == 0
assert how_many_times("bananas", "naananaanasaa") == 0
assert how_many_times("bananas", "naananaanasaaa") == 0
assert how_many_times("abracadabra", "abr") == 2
assert how_many_times("the quick brown fox jumps over the lazy dog", "e") == 3
assert how_many_times("the quick brown fox jumps over the lazy dog", "x") == 1
assert how_many_times("ab", "a") == 1 # overlapping cases
assert how_many_times("ab", "bc") == 0 # non-overlapping cases
assert how_many_times("ab", "c") == 0 # non-overlapping cases
assert how_many_times("abcd", "e") == 0 # non-overlapping cases
assert how_many_times("abcd", "f") == 0 # non-overlapping cases
assert how_many_times("abcd", "g") == 0 # non-overlapping cases
assert how_many_times("abcd", "h") == 0 # non-overlapping cases
assert how_many_times("ab", "b") == 1, "b occurs once"
assert how_many_times("abababab", "abababab") == 1, "abababab occurs once"
assert how_many_times("python", "py") == 1
assert how_many_times("python", "pythno") == 0
assert how_many_times("abc abc abc abc abc abc abc abc", "abc abc abc abc abc") == 4
assert how_many_times("How many times does it rain", "how many times does it rain") == 0
assert how_many_times("abracadabra", "car") is 0
assert how_many_times("abcdef", "a") == 1
assert how_many_times("abcdefg", "b") == 1
assert how_many_times("abcdefg", "f") == 1
assert how_many_times("abcdefg", "hi") == 0
assert how_many_times("ABCDA", "BC") == 1
assert how_many_times("ABCDA", "A") == 2
assert how_many_times("abba", "a") == 2, "The substring a should be found twice in the original string abba"
assert how_many_times("This is a test string", "isa") == 0
assert how_many_times("This is a test string", "isa isa") == 0
assert how_many_times("This is a test string", "isa is isa") == 0
assert how_many_times("This is a test string", "a is isa") == 0
assert how_many_times("This is a test string", "a is isa isa") == 0
assert how_many_times("This is a test string", "a is isa is isa") == 0
assert how_many_times("This is a test string", "a is isa isa isa isa") == 0
assert how_many_times("abcabcbbc", "bca") == 1, "bca"
assert how_many_times("abcabcbbc", "bbc") == 1, "bbc"
assert how_many_times("abcabcbbc", "bbbbab") == 0, "bbbbab"
assert how_many_times("abcabcbbc", "aacc") == 0, "aacc"
assert how_many_times("abcabcbbc", "ccc") == 0, "ccc"
assert how_many_times("abcabcbbc", "aaa") == 0, "aaa"
assert how_many_times("abcabcbbc", "aaac") == 0, "aaac"
assert how_many_times("abcabcbbc", "aacb") == 0, "aacb"
assert how_many_times("abcabcbbc", "abbb") == 0, "abbb"
assert how_many_times("abcabcbbc", "abbc") == 0, "abbc"
assert how_many_times('abba', 'b') is 2
assert how_many_times('', 'a') is 0
assert how_many_times('', 'abc') is 0
assert how_many_times("ABCDEF", "AB") == 1
assert how_many_times("ABCDEF", "DEF") == 1
assert how_many_times("ABCDEF", "E") == 1
assert how_many_times("ABCDEF", "F") == 1
assert how_many_times("ABCDEF", "G") == 0
assert how_many_times("ABCDEF", "H") == 0
assert how_many_times("ABCDEF", "I") == 0
assert how_many_times("ABCDEF", "J") == 0
assert how_many_times("abcabcbb", "bb") == 1
assert how_many_times('abcab', 'abcabc') is 0
assert how_many_times('abcab', 'bc') is 1
assert how_many_times('abcab', 'aba') is 0
assert how_many_times('abcab', 'bb') is 0
assert how_many_times("abc", "ab") == 1
assert how_many_times("abc", "a") == 1
assert how_many_times("abc", "d") == 0
assert how_many_times("aac", "abc") == 0
assert how_many_times("aac", "acb") == 0
assert how_many_times("aac", "aac") == 1
assert how_many_times("abcd", "cd") == 1, "how_many_times works incorrectly"
assert how_many_times("aba", "ba") == 1, "how_many_times works incorrectly"
assert how_many_times("aasdfsdfasdf", "asdfsdfasdf") == 1, "how_many_times works incorrectly"
assert how_many_times('abcabc', 'bc') == 2
assert how_many_times('abcabc', 'c') == 2
assert how_many_times('', 'abc') == 0
assert how_many_times("python", "thon") == 1
assert how_many_times("python", "pyth") == 1
assert how_many_times("aba", "b") == 1
assert how_many_times("aba", "abb") == 0
assert how_many_times("a", "a") == 1
assert how_many_times("abba", "abb") == 1
assert how_many_times("abba", "ab") == 1
assert how_many_times('abccde', 'ac') is 0
assert how_many_times('abc', 'd') is 0
assert how_many_times('abc', 'ac') is 0
assert how_many_times('abc', 'ad') is 0
assert how_many_times('abc', 'ae') is 0
assert how_many_times("holahola", "ahola") == 1, "ahola"
assert how_many_times("ab", "b") == 1
assert how_many_times('abc', 'aba') == 0
assert how_many_times('abc', 'ac') == 0
assert how_many_times('ab', 'ac') == 0
assert how_many_times('a', 'ac') == 0
assert how_many_times('a', 'b') == 0
assert how_many_times('aa', 'aba') == 0
assert how_many_times('aa', 'abb') == 0
assert how_many_times("abc", "b") == 1
assert how_many_times("abc", "bc") == 1, "a"
assert how_many_times("abc", "ac") == 0, "a"
assert how_many_times("abc", "ac") == 0, "b"
assert how_many_times("abba", "ba") == 1, "ab"
assert how_many_times('', 'a') == 0
assert how_many_times("a", "aa") == 0
assert how_many_times("a", "b") == 0
assert how_many_times("ab", "ab") == 1
assert how_many_times("abbb", "abb") == 1
assert how_many_times("abbbbb", "abbb") == 1
assert how_many_times("abcabcbb", "cc") == 0
assert how_many_times("abcabcbb", "aca") == 0
assert how_many_times("abaaba", "aba") == 2
assert how_many_times("abcabcdef", "abcaaa") == 0
assert how_many_times("abcabcdef", "abcabcc") == 0
assert how_many_times("abcabcdef", "abcabcdd") == 0
assert how_many_times("abcabcdef", "abcabccd") == 0
assert how_many_times('a', 'ab') == 0
assert how_many_times('abcabcdefg', 'abbbbcc') == 0
assert how_many_times("abba", "aa") == 0
assert how_many_times("abba", "c") == 0
assert how_many_times('aabcc', 'a') ==  2
assert how_many_times('aabcc', 'ba') ==  0
assert how_many_times("abcde", "abc") == 1, "No. of abc times should be 1"
assert how_many_times("abcde", "xyz") == 0, "No. of abc times should be 0"
assert how_many_times("aac", "ac") == 1, "No. of ac times should be 1"
assert how_many_times("abcabd", "adb") == 0
assert how_many_times('abab', 'abcd') == 0
assert how_many_times("abasas", "ba") == 1, "case3"
assert how_many_times("abasas", "sa") == 1, "case4"
assert how_many_times("abasas", "asa") == 1, "case6"
assert how_many_times("abba", "ba") == 1
assert how_many_times("abcdef", "bc") == 1
assert how_many_times("dog", "cat") == 0
assert how_many_times("hello", "h" ) == 1
assert how_many_times('abcccd', 'abd') == 0
assert how_many_times('abcccd', 'abbbbc') == 0
assert how_many_times('', 'abccd') == 0
assert how_many_times("hola", "hola") == 1, "It should return the correct value"
assert how_many_times("hola", "lel") == 0
assert how_many_times("pizza", "zap") == 0
assert how_many_times('abcde', 'deabc') == 0
assert how_many_times("aaa", "aaa") == 1
assert how_many_times("aaa", "aa") == 2
assert how_many_times("abcabd", "bd") == 1
assert how_many_times("abc", "aabc") == 0
