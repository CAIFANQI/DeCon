
def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    s = ''.join([char for char in s if char not in c])
    return (s,s[::-1] != s)
assert reverse_delete("aab", "a") == ("b", True)
assert reverse_delete('abb', 'a') == ('bb', True), 'Task 3'
assert reverse_delete('abc', '') == ('abc', False)
assert reverse_delete("abra", "") == ("abra", False)
assert reverse_delete('', '') == ('', True), ('', False)
assert reverse_delete('a', '') == ('a', True), ('a', False)
assert reverse_delete('abc','') == ('abc',False), 'Wrong result. Should be ("abc",False)'
assert reverse_delete('hello','hello') == ("",True)
assert reverse_delete('', '') == ('', True)
assert reverse_delete('abba', 'c') == ('abba', True)
assert reverse_delete('abc', 'b') == ('ac', False)
assert reverse_delete('abc', 'abc') == ('', True)
assert reverse_delete('', 'a') == ('', True), 'incorrect'
assert reverse_delete('', '') == ('', True), 'incorrect'
assert reverse_delete('', 'a') == ('', True)
assert reverse_delete("ab", "d") == ("ab", False)
assert reverse_delete('abc','') == ('abc', False)
assert reverse_delete('', '') == ('',True), 'test9'
assert reverse_delete('abc', 'ab') == ('c', True)
assert reverse_delete('abc', 'xyz') == ('abc', False)
