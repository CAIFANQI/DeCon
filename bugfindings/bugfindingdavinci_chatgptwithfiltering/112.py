
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
assert reverse_delete("abccb","a") == ("bccb", True)
assert reverse_delete("abcabc", "abc") == ("", True)
assert reverse_delete("aaabb","a") == ("bb",True)
assert reverse_delete("abc","abc") == ("",True)
assert reverse_delete("xyz", "xyz") == ("", True)
assert reverse_delete("abc", "abc") == ("", True)
assert reverse_delete("abc","abc") == ("", True)
assert reverse_delete("abcabcabc","abc") == ("",True)
assert reverse_delete("ba","ba") == ("",True)
assert reverse_delete("banana","b") == ('anana', True)
assert reverse_delete("banana","banana") == ('', True)
assert reverse_delete("abcabcabc","abc") == ("", True)
assert reverse_delete("abcabc","abc") == ("", True)
assert reverse_delete("test","test") == ("",True)
assert reverse_delete("ababab","a") == ('bbb', True)
assert reverse_delete("abb","b") == ("a", True)
assert reverse_delete("abac", "c") == ("aba", True)
assert reverse_delete("zabcd", "abcd") == ("z", True)
assert reverse_delete("abc","ab") == ("c",True)
assert reverse_delete("abcdabcd","abcd") == ("",True)
assert reverse_delete("ashley","ashley") == ("",True)
assert reverse_delete("ayy","a") == ("yy",True)
assert reverse_delete("qw","w") == ("q",True)
assert reverse_delete("abac","c") == ("aba",True)
assert reverse_delete("ab","ab") == ('', True)
assert reverse_delete("abc", "ab") == ("c", True)
assert reverse_delete("ab", "ab") == ("", True)
assert reverse_delete("meme","meme") == ("", True)
