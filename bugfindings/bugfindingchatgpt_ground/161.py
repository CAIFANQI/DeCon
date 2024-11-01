
def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    flg = 0
    idx = 0
    new_str = list(s)
    for i in s:
        if i.isalpha():
            new_str[idx] = i
            flg = 1
        idx += 1
    s = ""
    for i in new_str:
        s += i
    if flg == 0:
        return s[len(s)::-1]
    return s
assert solve("") == ""
assert solve("123") == "321"
assert solve("abc") == "ABC"
assert solve("ABC") == "abc"
assert solve("AbC") == "aBc"
assert solve("12AaBbCc34") == "12aAbBcC34"
assert solve("aBcD") == "AbCd"
assert solve("aBcD123") == "AbCd123"
assert solve("aBcD!@#") == "AbCd!@#"
assert solve("abcXYZ#") == "ABCxyz#"
assert solve("aBcXyz") == "AbCxYZ"
assert solve("ABCXYZ") == "abcxyz"
assert solve('12345') == '54321'
assert solve('') == ''
assert solve('aBcDeFg') == 'AbCdEfG'
assert solve("12345") == "54321"
assert solve("hELLO wORLD!") == "Hello World!"
assert solve("aBCDeFg") == "AbcdEfG"
assert solve("AbCdEfG") == "aBcDeFg"
assert solve("1234567890") == "0987654321"
assert solve("UPPERCASE") == "uppercase"
assert solve("lowercase") == "LOWERCASE"
assert solve("MiXeD CaSe") == "mIxEd cAsE"
assert solve("aBcDeF") == "AbCdEf"
assert solve("UPPER lower") == "upper LOWER"
assert solve("aBc") == "AbC"
assert solve("a1B2c3") == "A1b2C3"
assert solve("HeLlO") == "hElLo"
assert solve("AbCd") == "aBcD"
assert solve("AbCdEfGhIjKlMnOpQrStUvWxYz") == "aBcDeFgHiJkLmNoPqRsTuVwXyZ"
assert solve("aBcDeFgHiJkLmNoPqRsTuVwXyZ") == "AbCdEfGhIjKlMnOpQrStUvWxYz"
assert solve('aBcDeF') == 'AbCdEf'
assert solve('ABCDEF') == 'abcdef'
assert solve("A1B2C3") == "a1b2c3"
assert solve("abc123") == "ABC123"
assert solve("ABC123") == "abc123"
assert solve("aBc123") == "AbC123"
assert solve("A1b2C3") == "a1B2c3"
assert solve('AbCdEf') == 'aBcDeF'
assert solve('aB1C2d3E4f') == 'Ab1c2D3e4F'
assert solve("hEllO") == "HeLLo"
assert solve("1234") == "4321"
assert solve("ABCD") == "abcd"
assert solve('ABC') == 'abc'
assert solve('abc123') == 'ABC123'
assert solve('ABC123') == 'abc123'
assert solve('aBc') == 'AbC'
assert solve('aBc123') == 'AbC123'
assert solve(" ") == " "
assert solve("hELLO, wORLD!") == "Hello, World!"
assert solve("hElLo, WoRlD!") == "HeLlO, wOrLd!"
assert solve('!@#$%^&*()') == ')(*&^%$#@!'
assert solve('AbCdeF') == 'aBcDEf'
assert solve("aBc123!") == "AbC123!"
assert solve("AbC123") == "aBc123"
assert solve("aBc123 ") == "AbC123 "
assert solve("WORLD") == "world"
assert solve("!!!") == "!!!"
assert solve("!@#$%^") == "^%$#@!"
assert solve("aBcDeF!") == "AbCdEf!"
assert solve("hElLo WoRlD") == "HeLlO wOrLd"
assert solve("abcdEFGH") == "ABCDefgh"
assert solve("123abc") == "123ABC"
assert solve("UPPER CASE") == "upper case"
assert solve("lower case") == "LOWER CASE"
assert solve("12345") == '54321'
assert solve("abc123") == 'ABC123'
assert solve("") == ''
assert solve("hElLo") == "HeLlO"
assert solve("a") == "A"
assert solve("A") == "a"
assert solve("a1b2c3") == "A1B2C3"
assert solve("123abcXYZ") == "123ABCxyz"
assert solve("ABCDEF") == "abcdef"
assert solve("a b c") == "A B C"
assert solve("hello123") == "HELLO123"
assert solve("AbCdEf") == "aBcDeF"
assert solve("a1B2c3D4") == "A1b2C3d4"
assert solve("HELLO WORLD!") == "hello world!"
assert solve("ABCdef") == "abcDEF"
assert solve("hElLo, wOrLd!") == "HeLlO, WoRlD!"
assert solve("HeLLo123") == "hEllO123"
assert solve("HELLO") == "hello"
assert solve("hElLo, WOrLd!") == "HeLlO, woRlD!"
assert solve("ABCdef") == 'abcDEF'
assert solve("!!@#$%") == '%$#@!!'
assert solve("h3lLo") == "H3LlO"
assert solve("UPPER") == "upper"
assert solve("lower") == "LOWER"
assert solve("123abc456") == "123ABC456"
assert solve('abcd') == 'ABCD'
assert solve('ABCD') == 'abcd'
assert solve('aBcD') == 'AbCd'
assert solve("1a2b3c") == "1A2B3C"
assert solve("ABC!@#") == "abc!@#"
