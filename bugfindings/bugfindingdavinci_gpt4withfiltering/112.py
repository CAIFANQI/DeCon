
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
assert reverse_delete("abccb","b") == ("acc", False)
assert reverse_delete("bababa", "ab") == ("", True)
assert reverse_delete("abcabc", "abc") == ("", True)
assert reverse_delete("", "") == ("", True)
assert reverse_delete("abcba","a") == ("bcb",True)
assert reverse_delete("", "z") == ("", True)
assert reverse_delete("aaabb","a") == ("bb",True)
assert reverse_delete("abc","abc") == ("",True)
assert reverse_delete("a","aaa") == ("",True)
assert reverse_delete("aba","a") == ("b",True)
assert reverse_delete("a", "a") == ("", True)
assert reverse_delete("xyz", "xyz") == ("", True)
assert reverse_delete("abccb", "bc") == ("a", True)
assert reverse_delete("abc", "abc") == ("", True)
assert reverse_delete("abxabc","abc") == ("x",True)
assert reverse_delete("abcdcba","b") == ("acdca", True)
assert reverse_delete("abc","abc") == ("", True)
assert reverse_delete("abcdefgh","a") == ('bcdefgh', False)
assert reverse_delete("abacaba","aba") == ("c",True)
assert reverse_delete("abcabcabc","abc") == ("",True)
assert reverse_delete("abba","ba") == ("",True)
assert reverse_delete("ba","ba") == ("",True)
assert reverse_delete("abacaba","aba") == ('c', True)
assert reverse_delete("kabanana","ab") == ('knn', False)
assert reverse_delete("kabanana","banak") == ('', True)
assert reverse_delete("banana","b") == ('anana', True)
assert reverse_delete("banana","banana") == ('', True)
assert reverse_delete("abcabcabc","abc") == ("", True)
assert reverse_delete("abcabc","abc") == ("", True)
assert reverse_delete("","abc") == ("", True)
assert reverse_delete("","") == ("", True)
assert reverse_delete("aaa","a") == ("", True)
assert reverse_delete("abcde","edcba") == ("", True)
assert reverse_delete("redder","w") == ("redder", True)
assert reverse_delete("abc","a") == ('bc', False)
assert reverse_delete("racecar","x") == ("racecar",True)
assert reverse_delete("cat","act") == ("",True)
assert reverse_delete("test","test") == ("",True)
assert reverse_delete("aaa","a") == ("",True)
assert reverse_delete("uoft","") == ("uoft",False)
assert reverse_delete("","o") == ("",True)
assert reverse_delete("a","a") == ("",True)
assert reverse_delete("","") == ("",True)
assert reverse_delete("abcd","x") == ("abcd",False)
assert reverse_delete("xabzzbax","xba") == ("zz",True)
assert reverse_delete("qwertyuiop","y") == ("qwertuiop",False)
assert reverse_delete("qwertyuiop","w") == ("qertyuiop",False)
assert reverse_delete("qwertyuiop","u") == ("qwertyiop",False)
assert reverse_delete("qwertyuiop","o") == ("qwertyuip",False)
assert reverse_delete("qwertyuiop","p") == ("qwertyuio",False)
assert reverse_delete("abab","c") == ('abab', False)
assert reverse_delete("aaaa","a") == ('', True)
assert reverse_delete("ababab","a") == ('bbb', True)
assert reverse_delete("abacaba","") == ("abacaba",True)
assert reverse_delete("abb","b") == ("a", True)
assert reverse_delete("apple","a") == ("pple", False)
assert reverse_delete("bb","b") == ("", True)
assert reverse_delete("abc","ad") == ("bc",False)
assert reverse_delete("abcde","abc") == ("de",False)
assert reverse_delete("aaaaaaaaa","b") == ("aaaaaaaaa",True)
assert reverse_delete("abracadabra","s") == ("abracadabra",False)
assert reverse_delete("abcabc","y") == ("abcabc",False)
assert reverse_delete("aaaccccbbb","ac") == ("bbb",True)
assert reverse_delete("abac", "c") == ("aba", True)
assert reverse_delete("zabcd", "abcd") == ("z", True)
assert reverse_delete("zabcd", "xabcd") == ("z", True)
assert reverse_delete("zabcd", "") == ("zabcd", False)
assert reverse_delete("xax","x") == ("a",True)
assert reverse_delete("","a") == ("",True)
assert reverse_delete("xabxab","xb") == ("aa",True)
assert reverse_delete("abc", "c") == ("ab", False)
assert reverse_delete("dfsdfs","s") == ("dfdf", False)
assert reverse_delete("qwerty", "q") == ("werty", False)
assert reverse_delete("qwerty", "tr") == ("qwey", False)
assert reverse_delete("sadf", "qwer") == ("sadf", False)
assert reverse_delete("abc","ab") == ("c",True)
assert reverse_delete("redivider", "") == ("redivider", True)
assert reverse_delete("", "abc") == ("", True)
assert reverse_delete("aaaaa","a") == ("",True)
assert reverse_delete("abcdabcd","abcd") == ("",True)
assert reverse_delete("abcba","b") == ("aca",True)
assert reverse_delete("abcba","ab") == ("c",True)
assert reverse_delete("xyz","ab") == ("xyz",False)
assert reverse_delete("xyz","a") == ("xyz",False)
assert reverse_delete("abcz","") == ("abcz",False)
assert reverse_delete("wqwqwqwqwqwqwqwqwqwq","a") == ("wqwqwqwqwqwqwqwqwqwq", False)
assert reverse_delete("abcd","a") == ("bcd",False)
assert reverse_delete("ashley","aey") == ("shl",False)
assert reverse_delete("ashley","ashley") == ("",True)
assert reverse_delete("ashley","") == ("ashley",False)
assert reverse_delete("ayy","a") == ("yy",True)
assert reverse_delete("ayy","x") == ("ayy",False)
assert reverse_delete("abracadabra","abc") == ("rdr",True)
assert reverse_delete("", "mo") == ("", True)
assert reverse_delete("", "asdf") == ("", True)
assert reverse_delete("adcbe", "e") == ("adcb", False)
assert reverse_delete("abac","a") == ("bc",False)
assert reverse_delete("qw","w") == ("q",True)
assert reverse_delete("ala", "a") == ("l", True)
assert reverse_delete("ala", "alat") == ("", True)
assert reverse_delete("", "st") == ("", True)
assert reverse_delete("ala", "") == ("ala", True)
assert reverse_delete("abcabc","c") == ('abab', False)
assert reverse_delete("a","a") == ('', True)
assert reverse_delete("c","b") == ('c', True)
assert reverse_delete("","b") == ('', True)
assert reverse_delete("b","b") == ('', True)
assert reverse_delete("","") == ('', True)
assert reverse_delete("abccba", "abc") == ("", True)
assert reverse_delete("abacaba","cc") == ("abaaba",True)
assert reverse_delete("abcd","effg") == ("abcd", False)
assert reverse_delete("aaaa","aa") == ("", True)
assert reverse_delete("abcccba","c") == ("abba", True)
assert reverse_delete("abcccba","d") == ("abcccba", True)
assert reverse_delete("abcccba","abc") == ("", True)
assert reverse_delete("aa","a") == ("", True)
assert reverse_delete("aa","b") == ("aa", True)
assert reverse_delete("aabcdeeccba","abce") == ("d", True)
assert reverse_delete("aabcdeeccba","aec") == ("bdb", True)
assert reverse_delete("", "b") == ("", True)
assert reverse_delete("abcde", "") == ("abcde", False)
assert reverse_delete("a", "b") == ("a", True)
assert reverse_delete("aa", "b") == ("aa", True)
assert reverse_delete("aa", "a") == ("", True)
assert reverse_delete("racecar","r") == ("aceca", True)
assert reverse_delete("abacaba","c") == ("abaaba",True)
assert reverse_delete("abc","cba") == ("",True)
assert reverse_delete("abc","def") == ("abc",False)
assert reverse_delete("asfdsafasd","b") == ("asfdsafasd",False)
assert reverse_delete("abcc","c") == ("ab",False)
assert reverse_delete("abc","c") == ("ab",False)
assert reverse_delete("abc","b") == ("ac",False)
assert reverse_delete("abac","c") == ("aba",True)
assert reverse_delete("abac","ab") == ("c",True)
assert reverse_delete("cabac","ca") == ("b",True)
assert reverse_delete("aaaa","aa") == ("",True)
assert reverse_delete("abacab","ab") == ("c",True)
assert reverse_delete("abbacabb","ab") == ("c",True)
assert reverse_delete("abbacabb","ba") == ("c",True)
assert reverse_delete("ababaababaab","ba") == ("",True)
assert reverse_delete("ababaababaab","baab") == ("",True)
assert reverse_delete("ababaababaab","ababa") == ("",True)
assert reverse_delete("ababaababaab","baabab") == ("",True)
assert reverse_delete("ababaababaab","") == ("ababaababaab",False)
assert reverse_delete("abba","ad") == ("bb",True)
assert reverse_delete("aaaa","abcd") == ("",True)
assert reverse_delete("a","b") == ("a",True)
assert reverse_delete("abcd","d") == ("abc",False)
assert reverse_delete("ab","ab") == ('', True)
assert reverse_delete("adc","") == ('adc', False)
assert reverse_delete("aqwerty","") == ('aqwerty', False)
assert reverse_delete("","a") == ('', True)
assert reverse_delete("","ab") == ('', True)
assert reverse_delete("abcdcba","e") == ("abcdcba",True)
assert reverse_delete("","aba") == ('', True)
assert reverse_delete("abcdef","ab") == ("cdef", False)
assert reverse_delete("water", "aeiou") == ("wtr", False)
assert reverse_delete("watermelon", "aeiou") == ("wtrmln", False)
assert reverse_delete("", "aeiou") == ("", True)
assert reverse_delete("hello", "a") == ("hello", False)
assert reverse_delete("hello","el") == ("ho", False)
assert reverse_delete("","a") == ("", True)
assert reverse_delete("hello","le") == ("ho", False)
assert reverse_delete("hello","l") == ("heo",False)
assert reverse_delete("abc", "ab") == ("c", True)
assert reverse_delete("ab", "abc") == ("", True)
assert reverse_delete("ab", "ab") == ("", True)
assert reverse_delete("a", "abc") == ("", True)
assert reverse_delete("a", "ab") == ("", True)
assert reverse_delete("", "ab") == ("", True)
assert reverse_delete("", "a") == ("", True)
assert reverse_delete("qwerty","q") == ("werty",False)
assert reverse_delete("","b") == ("", True)
assert reverse_delete("abba","b") == ("aa", True)
assert reverse_delete("abba","a") == ("bb", True)
assert reverse_delete("abba","ab") == ("", True)
assert reverse_delete("abbac","acb") == ("", True)
assert reverse_delete("abca","abcba") == ("", True)
assert reverse_delete("aba", "a") == ("b", True)
assert reverse_delete("abba", "a") == ("bb", True)
assert reverse_delete("abca", "ac") == ("b", True)
assert reverse_delete("abcba", "abc") == ("", True)
assert reverse_delete("abcba", "ab") == ("c", True)
assert reverse_delete("abcba", "a") == ("bcb", True)
assert reverse_delete("abcba", "aaa") == ("bcb", True)
assert reverse_delete("python","java") == ("python", False)
assert reverse_delete("abacaba","z") == ("abacaba", True)
assert reverse_delete("radar","r") == ("ada",True)
assert reverse_delete("radar","") == ("radar",True)
assert reverse_delete("testtTt","") == ("testtTt",False)
assert reverse_delete("abcdef", "ca") == ("bdef",False)
assert reverse_delete("meme","em") == ("", True)
assert reverse_delete("meme","meem") == ("", True)
assert reverse_delete("meme","emem") == ("", True)
assert reverse_delete("meme","meme") == ("", True)
assert reverse_delete("meme","ememe") == ("", True)
assert reverse_delete("meme","mmee") == ("", True)
assert reverse_delete("meme","emme") == ("", True)
assert reverse_delete("meme","meeme") == ("", True)