
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    if len(s) < 3:
      return False

    for i in range(len(s) - 2):
      
      if s[i] == s[i+1] and s[i+1] == s[i+2] and s[i] == s[i+2]:
        return False
    return True
assert is_happy("abc") == True
assert is_happy("aaaa") == False
assert is_happy("abbc") == False
assert is_happy("") == False
assert is_happy("abcabcabc") == True
assert is_happy("aaaabbbbc") == False
assert not is_happy("ababbacccc"), "Wrong answer"
assert is_happy("abcabcabc"), "Wrong answer"
assert is_happy("unhappy") == False
assert is_happy("happ") == False
assert is_happy("a") == False
assert False == is_happy("unhappy"), "should be unhappy"
assert False == is_happy("hhhhhapppy"), "should be unhappy"
assert True == is_happy("codefights"), "should be happy"
assert False == is_happy("aaa"), "should be unhappy"
assert is_happy("abcabcabc") is True
assert is_happy("abcabcdabcd") is True
assert is_happy("abcabcdabcdabcd") is True
assert is_happy("abcabcabcabcabc") is True
assert is_happy("abcabcabcabcabcd") is True
assert is_happy("abcabcabcabcabcdabcd") is True
assert is_happy("c") is False
assert is_happy("cc") is False
assert is_happy("") is False
assert is_happy("a") is False
assert is_happy("ab") is False
assert is_happy("abc") is True
assert is_happy("Abcdd") == False
assert is_happy("Ab") == False
assert is_happy("Abcddd") == False
assert is_happy("Abdcdd") == False
assert is_happy("AbcAbc") == True
assert is_happy("ababbabbbabb") == False
assert is_happy("ababbabbbababa") == False
assert is_happy("AaaaAabBb") == False
assert is_happy("AaaaBbb") == False
assert is_happy("abccabcc") == False
assert is_happy("aab") == False
assert is_happy("abcdabcdabcd") == True
assert is_happy("abcd") == True
assert is_happy("abcddc") == False
assert is_happy("abcdccc") == False
assert is_happy("abcddcc") == False
assert is_happy("hello") == False
assert is_happy("y") == False
assert is_happy("abbbcee") == False
assert is_happy("aabbccd") == False
assert is_happy("aabcc") == False
assert is_happy("dcabbccdd") == False
assert is_happy("aabcd") == False
assert is_happy("abcde") == True
assert is_happy("abcdef") == True
assert is_happy("abcdefg") == True
assert is_happy("aabbccddabcdeee") == False
assert is_happy("aabbccddabcdeeef") == False
assert is_happy("aabbccddabcdeeeff") == False
assert is_happy("ab") == False
assert is_happy("ac") == False
assert is_happy("aa") == False
assert is_happy("aaa") == False
assert is_happy("aaabbbccc") is False
assert is_happy("hhhh") == False
assert is_happy("hippy") == False
assert is_happy("happi") == False
assert is_happy("h") == False
assert is_happy("ha") == False
assert is_happy("hap") == True
assert is_happy("haapy") == False
assert is_happy("hpppy") == False
assert is_happy("hppp") == False
assert is_happy("hpp") == False
assert is_happy("abcccab") == False
assert is_happy("aabbbc") is False
assert is_happy("aa") is False
assert is_happy("hyappy") == False
assert is_happy("dbc") == True
assert is_happy("d") == False
assert is_happy("aabb") is False
assert is_happy("abcabcdabc") == True
assert is_happy("aababa") == False
assert is_happy("hapy") == True
assert is_happy("happyyy") == False
assert is_happy("abcdaabcdaabcda") == False
assert is_happy("aabbcc") == False
assert is_happy("aaabaaaab") == False
assert is_happy("iiiiii") == False
assert is_happy("abccba") == False
assert is_happy("abcabc") == True
assert is_happy("abcdabcd") is True
assert is_happy("happy") is False
assert False == is_happy("I'm not happy")
assert False == is_happy("aabaa")
assert False == is_happy("babaa")
assert False == is_happy("")
assert False == is_happy("aaa")
assert False == is_happy("aaaaa")
assert is_happy("abccabb") == False
assert is_happy("abcabcabcabc") == True
assert is_happy("abccabccabcc") == False
assert is_happy("abcabcabcabcc") == False
assert is_happy("abccabccabccab") == False
assert is_happy("abccabccabccabcc") == False
assert is_happy("abccabccabccabccab") == False
assert is_happy("abccabccabccabccabcc") == False
assert is_happy("abccabccabccabccabccab") == False
assert is_happy("abccabccabccabccabccabcc") == False
assert is_happy("abccabccabccabccabccabccab") == False
assert is_happy("abccabccabccabccabccabccabcc") == False
assert is_happy("aaa") is False
assert is_happy("abcabc") is True
assert is_happy("aaabb") is False
assert is_happy("aaaabbbb") is False
assert is_happy("abbd") == False
assert is_happy("happy") == False
assert is_happy("yy") == False
assert is_happy("xabxabxabxxx") == False
assert is_happy("abxabxabxabxabx") == True
assert is_happy("abxabxabxabxabxabxabx") == True
assert is_happy("abcabcabcabcabc") == True
assert is_happy("abcdabc") == True
assert is_happy("aabb") == False
assert is_happy("aaabbbbcccddd") == False
assert is_happy("abcdabcdabcd") is True
assert is_happy("pythonprogramming") is False
assert is_happy("hello") is False
assert is_happy("xxyxyz") is False
assert is_happy("xxyyxz") is False
assert is_happy("xxyyyz") is False
assert is_happy("Happi") == False
assert is_happy("HappyHappiHappi") == False
assert is_happy("i") == False
assert is_happy("ace") == True
assert is_happy("abcabcabcabcabcabc") == True
assert is_happy("aab") is False
assert is_happy("aaaa") is False
assert is_happy("abbabb") is False
assert is_happy("aabbcabc") is False
assert is_happy("abcabc"), "is_happy should return True"
assert not is_happy("aabaa"), "is_happy should return False"
assert not is_happy("aabaaa"), "is_happy should return False"
assert not is_happy("abaaba"), "is_happy should return False"
assert is_happy("xyzwx") == True
assert is_happy("happisad") == False
assert is_happy("aabccb") == False
assert is_happy("aabccbddeeffgg") == False
assert is_happy("aaaaaa") == False
assert is_happy("abccab") == False
assert is_happy("happyhappyhappyhh") == False
assert is_happy("j") == False
assert is_happy("jj") == False
assert is_happy("jk") == False
assert is_happy("jkjj") == False
assert is_happy("jkjkjj") == False
assert is_happy("jkjkjkk") == False
assert is_happy("jkjkjkjj") == False
assert is_happy("jkjkjkjkjj") == False
assert is_happy("abacabcc") == False
assert is_happy("abbb") is False
assert is_happy("aabbcc") is False
assert is_happy("aabbbccc") is False
assert is_happy("HAAPY") == False
assert is_happy("HAPP") == False
assert is_happy("HAPPYTH") == False
assert is_happy("aaaabbb") == False
assert is_happy("xyy") == False
assert is_happy("abcdxyz") == True
assert is_happy("abcdeabcde") == True
assert is_happy("abcc") == False
assert is_happy("myhappy") == False
assert is_happy("happpp") == False
assert is_happy("happyunhappyhappy") == False
assert is_happy("haaaappy") == False
assert is_happy("haaappy") == False
assert is_happy("haappy") == False
assert is_happy("happpy") == False
assert is_happy("happyy") == False
assert is_happy("happyyyyyy") == False
assert is_happy("happyab") == False
assert is_happy("happyabb") == False
assert is_happy("happp") == False
assert is_happy("aabbccddeef") is False
assert is_happy("xyz") is True
assert is_happy("xxyyyzz") is False
assert is_happy("ababbbabb") == False
assert is_happy("aaabbbab") == False
assert is_happy("aabbabccc") == False
assert is_happy("abcabcabcc") == False
assert is_happy("aaaaaaaa") == False
assert is_happy("aabaaabaaa") == False
assert is_happy("abaaaabaaa") == False
assert is_happy("aaaaaaabaa") == False
assert is_happy("abaabaaa") == False
assert is_happy("aaaabaaaa") == False
assert is_happy("aaaaabbaaa") == False
assert is_happy("abaabbaaa") == False
assert is_happy("abaabbbaaa") == False
assert False == is_happy("abccbabc")
assert False == is_happy("abcabcaaa")
assert is_happy("aabbb") == False
assert is_happy("v") == False
assert is_happy("xyzxyz") == True
assert is_happy("aaabbb") == False
assert is_happy("abb") == False
assert is_happy("aaab") == False
assert is_happy("aabbaa") == False
assert is_happy("aaabb") == False
assert is_happy("aaabaaa") == False
assert is_happy("aaaaa") == False
assert is_happy("aaaab") == False
assert is_happy("aaaaab") == False
assert is_happy("baa") == False
assert is_happy("baaa") == False
assert is_happy("abcabcabcabcabcabcabc") == True
assert is_happy("aabbccb") == False
assert is_happy("aaabbccca") == False
assert is_happy("aaabbcccabc") == False
assert is_happy("aaabbcccabcde") == False
assert is_happy("aaabbcccabcdefg") == False
assert is_happy("aaabbcccabcdefghi") == False
assert is_happy("aaabbcccabcdefghijk") == False
assert is_happy("Aab") == True
assert is_happy("aabbaaaa") == False
assert is_happy("abccab") is False
assert is_happy("abcccabc") is False
assert is_happy("abcabcabcabcabcabcabcabcabc") is True
assert is_happy("abcabcabcabcabcabcabcabcabcc") is False
assert is_happy("hhappy") == False
assert is_happy("123456789") == True
assert is_happy("aabcaab") == False
assert is_happy("happpppy") == False
assert is_happy("ayy") == False
assert is_happy("ay") == False
assert is_happy("abbab") is False
assert is_happy("saa") == False
assert is_happy("abcaa") is False
assert is_happy("abccba") is False
assert is_happy("aabbcacba") is False
assert is_happy("jfkdlsajfkdlsa") is True
assert is_happy("kkk") is False
assert is_happy("aaabbbccc") == False
assert is_happy("abc123abc") == True
assert is_happy("abc123abc123abc") == True
assert is_happy("abccaa") == False
assert is_happy("abccbaabccba") == False
assert is_happy("abcabcabca") == True
assert is_happy("aaaaaaaaa") is False
assert is_happy("abcdefghijklmnopqrstuvwxyz") is True
assert is_happy("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") is True
assert is_happy("abcabcabb") == False
assert is_happy("bbc") == False
assert is_happy("fabaab") == False
assert is_happy("abcab") == True
assert is_happy("xyz") == True
assert is_happy("aabbccc") is False
assert is_happy("aabbccddd") is False
assert is_happy("aaabbccdd") is False
assert is_happy("aabbccddde") is False
assert is_happy("aaabaaaa") == False
assert is_happy("1234234") == True
assert is_happy("exam") == True
