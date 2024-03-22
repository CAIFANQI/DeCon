
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
assert digitSum('') == 0
assert digitSum('ab1') == 0
assert digitSum("") == 0, "digits sum is incorrect"
assert digitSum("  \t  \n\r") == 0, "digits sum is incorrect"
assert digitSum("0") == 0, "digits sum is incorrect"
assert digitSum('000') == 0
assert digitSum("01234567890") == 0
assert digitSum("012345678901234") == 0
assert digitSum("01230045670") == 0
assert digitSum("0123004567") == 0
assert digitSum("01230045678") == 0
assert digitSum("012300456790") == 0
assert digitSum("01230045679012") == 0
assert digitSum("012300456790123") == 0
assert digitSum("0123004567901234") == 0
assert digitSum("01234567890123456789") == 0
assert digitSum("") == 0, "The function digitSum should return 0"
assert digitSum('aa') == 0
assert digitSum('1234567890123') == 0
assert digitSum('123345678901234567') == 0
assert digitSum('1234567890') == 0
assert digitSum("a") == 0
assert digitSum("") == 0
assert digitSum('A') == 65
assert digitSum('abc') == 0
assert digitSum(' ') == 0
assert digitSum('   ') == 0
assert digitSum('') == 0, 'empty string'
assert digitSum(' ') == 0, 'white space'
assert digitSum("1") == 0
assert digitSum("2") == 0
assert digitSum('aaa') == 0
assert digitSum('a') == 0
assert digitSum("0") == 0
assert digitSum("00") == 0
assert digitSum('ab12c') ==  0
assert digitSum('') ==  0
assert digitSum("789") == 0
assert digitSum("234") == 0
assert digitSum("345") == 0
assert digitSum("56") == 0
assert digitSum("909") == 0
assert digitSum("ab1") == 0
assert digitSum("1234") == 0
assert digitSum("123456789") == 0
assert digitSum("abbccc") == 0
assert digitSum("abcdef") == 0
assert digitSum("abbcccdeff") == 0
assert digitSum("abc") == 0
assert digitSum('8') == 0
assert digitSum('0') == 0
assert digitSum('abc123') == 0
