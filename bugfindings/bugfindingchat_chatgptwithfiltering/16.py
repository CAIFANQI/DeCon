

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    return len(set(string))
assert count_distinct_characters("hello") == 4
assert count_distinct_characters("HELLO") == 4
assert count_distinct_characters("hEllo") == 4
assert count_distinct_characters("aaaaaa") == 1
assert count_distinct_characters('HELLO') == 4
assert count_distinct_characters('Hello') == 4
assert count_distinct_characters('hElLo') == 4
assert count_distinct_characters('') == 0
assert count_distinct_characters("Hello") == 4
assert count_distinct_characters("abcdefghijklmnopqrstuvwxyz") == 26
assert count_distinct_characters("abcabcabc") == 3
assert count_distinct_characters("abAB") == 2
assert count_distinct_characters("hElLo") == 4
assert count_distinct_characters("AAABBBCCC") == 3
assert count_distinct_characters("") == 0
assert count_distinct_characters("world") == 5
assert count_distinct_characters("Python") == 6
assert count_distinct_characters('') == 0, 'Test Case 4 Failed'
assert count_distinct_characters('aaaaaa') == 1, 'Test Case 5 Failed'
assert count_distinct_characters("HeLlO") == 4
assert count_distinct_characters('aabbcc') == 3
assert count_distinct_characters('aAbBcC') == 3
assert count_distinct_characters('aaa') == 1
assert count_distinct_characters("HELLO") == 4, "Test case 2 failed"
assert count_distinct_characters("") == 0, "Test case 5 failed"
assert count_distinct_characters('abcdabcd') == 4
assert count_distinct_characters('Hello') == 4, 'Test Case 2 Failed'
assert count_distinct_characters('') == 0, 'Test Case 5 Failed'
assert count_distinct_characters("World") == 5
assert count_distinct_characters("WORLD") == 5
assert count_distinct_characters("abcdefg") == 7
assert count_distinct_characters("AaBbCc") == 3
assert count_distinct_characters("abc") == 3
assert count_distinct_characters('abcabcabc') == 3
assert count_distinct_characters('aaaaa') == 1
assert count_distinct_characters("aaa") == 1
assert count_distinct_characters('world') == 5
assert count_distinct_characters("World") == 5, "Test case 2 failed"
assert count_distinct_characters("aaaaaa") == 1, "Test case 4 failed"
assert count_distinct_characters("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 26
assert (count_distinct_characters("Hello") == 4)
assert (count_distinct_characters("abcde") == 5)
assert (count_distinct_characters("abcdabcd") == 4)
assert (count_distinct_characters("") == 0)
assert count_distinct_characters('Mississippi') == 4
assert count_distinct_characters('abcdefghijklmnopqrstuvwxyz') == 26
assert count_distinct_characters('abcdefg') == 7
assert count_distinct_characters("abababab") == 2
assert count_distinct_characters("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz") == 26
assert count_distinct_characters("world") == 5, "Test case 2 failed"
assert count_distinct_characters("abcdefghijklmnopqrstuvwxyz") == 26, "Test case 4 failed"
assert count_distinct_characters("apple") == 4
assert count_distinct_characters("banana") == 3
assert count_distinct_characters("abcdefg") == 7, "Test case 2 failed"
assert count_distinct_characters("") == 0, "Test case 4 failed"
assert count_distinct_characters("hEllO") == 4
assert count_distinct_characters("AAAaaa") == 1
assert count_distinct_characters("a") == 1
assert count_distinct_characters("aa") == 1
assert count_distinct_characters("aAa") == 1
assert count_distinct_characters("abcABC") == 3
assert count_distinct_characters("aabbcc") == 3
assert count_distinct_characters('aaaaaa') == 1, 'Test Case 3 Failed'
assert count_distinct_characters("aaaaa") == 1, "Test case 5 failed"
assert count_distinct_characters("abcabc") == 3
assert count_distinct_characters("orange") == 6
assert count_distinct_characters('aAaBbBcCc') == 3
assert count_distinct_characters("aaaaaaa") == 1
assert count_distinct_characters("abcde") == 5
assert count_distinct_characters('a') == 1
assert count_distinct_characters('aa') == 1
assert count_distinct_characters('abc') == 3
assert (count_distinct_characters("abcdefg") == 7)
assert (count_distinct_characters("aaa") == 1)
assert count_distinct_characters('aaaaa') == 1, 'Test Case 3 Failed'
assert count_distinct_characters("aaaaa") == 1, "Test case 3 failed"
assert count_distinct_characters("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 26, "Test case 5 failed"
assert count_distinct_characters("aaaaa") == 1
assert count_distinct_characters("heLLo") == 4
