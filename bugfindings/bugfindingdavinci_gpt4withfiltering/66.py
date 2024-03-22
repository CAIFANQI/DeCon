
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
assert digitSum("") == 0
assert digitSum("a") == 0
assert digitSum('abc') == 0
assert digitSum('$2.00') == 0
assert digitSum('1') == 0
assert digitSum("dgdjgdjgdjgdjgdjgd") == 0, "error in digitSum"
assert digitSum("dgoiwjdoiqwjdoiqwjdoiqwjdoiqwjdiojd") == 0, "error in digitSum"
assert digitSum("@%*&^$&") == 0
assert digitSum('A') == 65
assert digitSum('AA') == 130
assert digitSum("!Ak!") == 65, "Test failed"
assert digitSum("") == 0, "Test digitSum: basic"
assert digitSum('aa') == 0
assert digitSum('aaa') == 0
assert digitSum('a') == 0
assert digitSum('') == 0
assert digitSum("12") == 0
assert digitSum("12,3") == 0
assert digitSum("$%^&") == 0
assert digitSum("A") == 65
assert digitSum("abc") == 0
assert digitSum(";:?!*&#") == 0
assert (digitSum("") == 0), "digitSum"
assert digitSum("aaaa") == 0
assert digitSum("A1") == 65
assert digitSum('abcde') == 0
assert digitSum("123") == 0
assert digitSum("a1b2c3d4e5") == 0
assert digitSum("a!b@c#d$e%") == 0
assert digitSum('123') == 0
assert digitSum("Az") == 65
assert digitSum("AzA") == 130
assert digitSum("AzA1a") == 130
assert digitSum("aaaaaa") == 0
assert digitSum('a1b2c3') == 0
assert digitSum('abcdefghijklmnopqrstuvwxyz') == 0
assert digitSum("aA") == 65
assert digitSum("aaA") == 65
assert digitSum('i am cool') == 0
assert digitSum("asd") == 0
assert digitSum("aBcd1234") == 66
assert digitSum("4649") == 0
assert digitSum("!@#$%^&*()") == 0
assert digitSum("7") == 0
assert digitSum('566') == 0, 'Wrong'
assert digitSum('sos') == 0, 'Wrong Answer'
assert digitSum('0123456789') == 0, 'Wrong Answer'
assert digitSum('aBc') == 66
assert digitSum('-a') == 0
assert digitSum('a-') == 0
assert digitSum('-') == 0
assert digitSum("1") == 0
assert digitSum("*") == 0
assert digitSum("abcd") == 0
assert digitSum("ab&%c") == 0
assert digitSum("**aaaAA") == 130
assert digitSum('1.0FEB') == (70 + 69 + 66)
assert digitSum('1.FEB1') == (70 + 69 + 66)
assert digitSum('34') == 0
assert digitSum("ab") == 0
assert digitSum("Abc") == 65
assert digitSum("") == 0, "Wrong answer"
assert digitSum("Z") == 90, "Wrong answer"
assert digitSum("abcdef") == 0
assert digitSum("F") == 70
assert digitSum(list("A" * 100)) == 6500
assert digitSum('Z') == 90
assert digitSum('abc123') == 0
assert digitSum('---11!') == 0
assert digitSum('.') == 0
assert digitSum('aaaa') == 0
assert digitSum('1223') == 0
