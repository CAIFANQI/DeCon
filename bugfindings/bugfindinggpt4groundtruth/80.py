
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
assert 	is_happy("abcd") == True, "Wrong result for string: 'abcd'"
assert 	is_happy("aabbcc") == False, "Wrong result for string: 'aabbcc'"
assert 	is_happy("abbccddeef") == False, "Wrong result for string: 'abbccddeef'"
assert 	is_happy("aabbccdddeeef") == False, "Wrong result for string: 'aabbccdddeeef'"
assert 	is_happy("aabaaa") == False, "the result should be False"
assert 	is_happy("aabaaab") == False, "the result should be False"
assert 	is_happy("aba") == False
assert 	is_happy("abcd") == True
assert 	is_happy("abcb") == False
assert 	is_happy("aabb") == False
assert 	is_happy("abbcccaa") == False
assert 	is_happy("aabbccc") == False
assert 	is_happy("aaaa") == False
assert 	is_happy("aaaaab") == False
assert 	is_happy("aaaaabbb") == False
assert 	is_happy("aaaaababbb") == False
assert is_happy("aa") == False
assert is_happy("abcdef") == True
assert is_happy("aabaaa") == False
assert not is_happy("aaabbc")
assert not is_happy("aaabbb")
assert is_happy("abcdef")
assert is_happy("xyxy") == False
assert is_happy("xyla") == True
assert is_happy("xyxl") == False
assert is_happy("xy") == False
assert is_happy("x") == False
assert is_happy("l") == False
assert is_happy("xylaa") == False
assert is_happy("lal") == False
assert is_happy("la") == False
assert is_happy("a") == False
assert is_happy("aaa") == False
assert is_happy("lalalala") == False
assert is_happy("lalalalalal") == False
assert is_happy("lalalalalalalal") == False
assert 	is_happy("abbbc") == False
assert 	is_happy("abcab") == True
assert 	is_happy("cdeae") == False
assert 	is_happy("abcdeeefgghhiijjkklmno") == False
assert 	is_happy("abcdeeefgghhiijjkkllmmno") == False
assert 	is_happy("abcdeeefgghhiiiiijjkkllmmno") == False
assert 	is_happy("abcdeeefgghhiiijjjjkkllmmno") == False
assert 	is_happy("abcdeeefgghhiiijjjjkkllmmmmno") == False
assert not is_happy("abab")
assert 	is_happy("abab") == False
assert 	is_happy("abcabcabc") == True
assert 	is_happy("aabbccddeefgg") == False
assert 	is_happy("aabbc") == False
assert 	is_happy("abc") == True
assert 	is_happy("ab") == False
assert 	is_happy("abbc") == False
assert 	is_happy("abccb") == False
assert 	is_happy("abccbbaa") == False
