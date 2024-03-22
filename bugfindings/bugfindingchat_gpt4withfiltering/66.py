
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    if s == "": return 0
    return sum(ord(char) if char.islower() else 0 for char in s)
assert digitSum("abc") == 0
assert digitSum("aBc") == 66
assert digitSum("123") == 0
assert digitSum("") == 0
assert digitSum("abc123") == 0
assert digitSum('123') == 0, "Error: Test Case 3"
assert digitSum('a1B2c3') == 66, "Error: Test Case 4"
assert digitSum("12345") == 0
assert digitSum("abcdefghijklmnopqrstuvwxyz") == 0
