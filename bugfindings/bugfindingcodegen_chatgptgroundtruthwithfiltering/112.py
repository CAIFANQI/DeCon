
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
assert 	reverse_delete("", "abxyz") == ("", True)
assert 	reverse_delete("abc", "ab") == ("c", True)
assert 	reverse_delete("abc", "ba") == ("c", True)
assert 	reverse_delete("abc", "abc") == ("", True)
assert 	reverse_delete("abc", "a") == ("bc", False)
assert 	reverse_delete("abc", "abcba") == ("", True)
assert reverse_delete('', '') == ('', True), 'wrong result'
assert reverse_delete('abcdef', 'abcd') == ('ef', False), 'wrong result'
assert 	reverse_delete('', 'cd') == ('', True)
assert 	reverse_delete('', '') == ('', True)
assert 	reverse_delete('','bcde') == ('', True)
assert 	reverse_delete('','') == ('', True)
assert 	reverse_delete('abc', 'z') == ('abc', False)
assert 	reverse_delete('abc', 'a') == ('bc', False)
assert 	reverse_delete('aabccdd', 'dd') == ('aabcc', False), 'wrong result'
assert 	reverse_delete('', 'c') == ('', True), 'wrong result'
assert reverse_delete('a', 'a') == ('', True)
assert reverse_delete('', '') == ('', True)
assert 	reverse_delete('abcab', 'z') == ('abcab', False)
assert 	reverse_delete('abcab', '') == ('abcab', False)
assert 	reverse_delete('abc', 'xyz') == ('abc', False)
assert 	reverse_delete('abc', 'abc') == ('', True)
assert 	reverse_delete('aac', 'a') == ('c', True)
assert 	reverse_delete('abc', 'ab') == ('c', True)
