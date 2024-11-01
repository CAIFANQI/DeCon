

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
assert 	how_many_times('hahaha', 'x') == 0
assert 	how_many_times('', 'a') == 0
assert 	how_many_times('', 'h') == 0
assert 	how_many_times('', 'x') == 0
assert 	how_many_times('a', 'a') == 1
assert 	how_many_times('haha', 'a') == 2
assert 	how_many_times('hahahahaha', 'x') == 0
assert 	how_many_times(string = "a", substring = "a") == 1,'something is wrong'
assert 	how_many_times(string = "aaaaa", substring = "b") == 0,'something is wrong'
assert 	how_many_times('ababababab', 'a') == 5, 'ababababab'
assert 	how_many_times('ababababab', 'aa') == 0, 'ababababab'
assert 	how_many_times('ababababab', 'aaaa') == 0, 'ababababab'
assert 	how_many_times(string="", substring="AA") == 0, "Not all expected matches were found"
assert 	how_many_times(string="AABA", substring="A") == 3, "Not all expected matches were found"
assert 	how_many_times('abc', 'abc') == 1, 'No overlaping'
assert 	how_many_times('aaaa', 'abc') == 0, 'No overlaping'
assert 	how_many_times('abaa', 'aba') == 1, 'Overlaping case'
assert 	how_many_times('aaaa', 'aba') == 0, 'No overlaping'
assert 	how_many_times('aa', 'aa') == 1
assert 	how_many_times('abracadabra', 'a') == 5
assert 	how_many_times('abracadabra', 'abrac') == 1
assert 	how_many_times('abracadabra', 'cadabra') == 1
assert 	how_many_times('abracadabra', 'cadbra') == 0
assert 	how_many_times("aaaaa", "ba") == 0
assert 	how_many_times('aa', 'b') == 0
assert 	how_many_times('aaa', 'b') == 0
assert 	how_many_times('a', 'b') == 0
assert 	how_many_times('b', 'a') == 0
assert 	how_many_times('b', 'b') == 1
assert 	how_many_times('aaaaaa', 'aa') == 5
assert 	how_many_times('aaaaaa', 'ab') == 0
assert 	how_many_times('aaaaaa', 'b') == 0
