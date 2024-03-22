
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
assert is_happy('abc') == True
assert is_happy("aabbcc") == False
assert is_happy("aaa") == False
assert is_happy("abcdefg") == True
assert is_happy("aaaabbbbcccc") == False
assert is_happy("abcdabcdabcd") == True
assert is_happy('aaa') == False
assert is_happy('abcdef') == True
assert is_happy('abbcc') == False
assert is_happy('aabbcc') == False
assert is_happy("happiness") == False
assert is_happy("happyy") == False
assert is_happy("aab") == False
assert is_happy("abcd") == True
assert is_happy("aabbccddee") == False
assert is_happy("a") == False
assert is_happy("aa") == False
assert is_happy("abc") == True
assert is_happy("abb") == False
assert is_happy("abcabc") == True
assert is_happy("abcdabc") == True
assert is_happy("abcdabcd") == True
assert is_happy("abcdabce") == True
assert is_happy("abcdabcf") == True
assert is_happy("abcdabcg") == True
assert is_happy("abcdabch") == True
assert is_happy("abcdabci") == True
assert is_happy("abcdabcj") == True
assert is_happy("abcdabck") == True
assert is_happy("abcdabcl") == True
assert is_happy("abcdabcm") == True
assert is_happy("abcdabcn") == True
assert is_happy("abcdabco") == True
assert is_happy("abcdabcp") == True
assert is_happy("abcdabcq") == True
assert is_happy("abcdabcr") == True
assert is_happy("abcdabcs") == True
assert is_happy("abcdabct") == True
assert is_happy("abcdabcu") == True
assert is_happy("abcdabcv") == True
assert is_happy("abcdabcw") == True
assert is_happy("abcdabcx") == True
assert is_happy("abcdabcy") == True
assert is_happy("abcdabcz") == True
assert is_happy("ab") == False
assert is_happy("aabbccdd") == False
assert is_happy("abcabcabc") == True
assert is_happy('abcdabcabc') == True
assert is_happy("abcdefghi") == True
assert is_happy('aab') == False
assert is_happy('abcdabc') == True
assert is_happy("abcde") == True
assert is_happy("abcdef") == True
assert is_happy("abcdee") == False
assert is_happy("abccde") == False
assert is_happy("abbccc") == False
assert is_happy("abccccc") == False
assert is_happy("abcccccc") == False
assert is_happy("abccccccc") == False
assert is_happy("abcccccccc") == False
assert is_happy("abccccccccc") == False
assert is_happy("abcccccccccc") == False
assert is_happy("abccccccccccc") == False
assert is_happy("abcccccccccccc") == False
assert is_happy("abccccccccccccc") == False
assert is_happy("abcccccccccccccc") == False
assert is_happy("abccccccccccccccc") == False
assert is_happy("abcccccccccccccccc") == False
assert is_happy("abccccccccccccccccc") == False
assert is_happy("abcccccccccccccccccc") == False
assert is_happy("abccccccccccccccccccc") == False
assert is_happy("abcccccccccccccccccccc") == False
assert is_happy("abccccccccccccccccccccc") == False
assert is_happy("abcccccccccccccccccccccc") == False
assert is_happy("abccccccccccccccccccccccc") == False
assert is_happy("abcccccccccccccccccccccccc") == False
assert is_happy("abccccccccccccccccccccccccc") == False
assert is_happy("abcccccccccccccccccccccccccc") == False
assert is_happy("abccccccccccccccccccccccccccc") == False
assert is_happy("abcccccccccccccccccccccccccccc") == False
assert is_happy("abccccccccccccccccccccccccccccc") == False
assert is_happy("abcccccccccccccccccccccccccccccc") == False
assert is_happy("abccccccccccccccccccccccccccccccc") == False
assert is_happy("abcccccccccccccccccccccccccccccccc") == False
assert is_happy("abccccccccccccccccccccccccccccccccc") == False
assert is_happy("abcccccccccccccccccccccccccccccccccc") == False
assert is_happy("abccccccccccccccccccccccccccccccccccc") == False
assert is_happy("abcccccccccccccccccccccccccccccccccccc") == False
assert is_happy("abccccccccccccccccccccccccccccccccccccc") == False
assert is_happy("abcccccccccccccccccccccccccccccccccccccc") == False
assert is_happy("abccccccccccccccccccccccccccccccccccccccc") == False
assert is_happy("abcccccccccccccccccccccccccccccccccccccccc") == False
assert is_happy("abccccccccccccccccccccccccccccccccccccccccc") == False
assert is_happy("abcccccccccccccccccccccccccccccccccccccccccc") == False
assert is_happy("abccccccccccccccccccccccccccccccccccccccccccc") == False
assert is_happy("abcccccccccccccccccccccccccccccccccccccccccccc") == False
assert is_happy("abccccccccccccccccccccccccccccccccccccccccccccc") == False
assert is_happy("abcccccccccccccccccccccccccccccccccccccccccccccccc") == False
assert is_happy("abccccccccccccccccccccccccccccccccccccccccccccccccc") == False
assert is_happy("abcccccccccccccccccccccccccccccccccccccccccccccccccccc") == False
assert is_happy("abccccccccccccccccccccccccccccccccccccccccccccccccccccc") == False
assert is_happy("abcccccccccccccccccccccccccccccccccccccccccccccccccccccccc") == False
assert is_happy("abcccccccccccccccccccccccccccccccccccccccccccccccccccccc") == False
assert is_happy("abccccccccccccccccccccccccccccccccccccccccccccccccccccccc") == False
assert is_happy('abcdefgh') == True
assert is_happy("aaa") == False, "Error: Test Case 2"
assert is_happy("abcd") == True, "Error: Test Case 3"
assert is_happy('abcd') == True
assert is_happy("") == False
assert is_happy("aabbcc") == False, "Test case 2 failed"
assert is_happy("abcdabc") == True, "Test case 3 failed"
assert is_happy("aaa") == False, "Test case 4 failed"
assert is_happy("aaa") == False, "Test case 2 failed"
assert is_happy("abcdef") == True, "Test case 4 failed"
assert is_happy("aabbcc") == False, "Test case 5 failed"
assert is_happy('aaabbbccc') == False
assert is_happy('abcdefghi') == True
assert is_happy("aabbccddeeffg") == False
assert is_happy("aab") == False, "Error: Test Case 2"
assert is_happy("abcdefg") == True, "Error: Test Case 4"
assert is_happy("aaa") == False, "Error: Test Case 5"
assert is_happy("abbcccddddeeeeeffffff") == False
assert is_happy("abccba") == False
assert is_happy("abb") == False, "Error: Test Case 2"
assert is_happy("aaa") == False, "Error: Test Case 3"
assert is_happy("abcd") == True, "Error: Test Case 4"
assert is_happy('abcdefghijk') == True
assert is_happy("aabbc") == False
assert is_happy("happ") == False
assert is_happy("abbb") == False
assert is_happy("abbccc") == False, "Test case 3 failed"
assert is_happy("abcd") == True, "Test case 4 failed"
assert is_happy("aaabbbccc") == False
assert is_happy("aabbcc") == False, "Error: Test Case 2"
assert is_happy("abcdefgh") == True, "Error: Test Case 4"
