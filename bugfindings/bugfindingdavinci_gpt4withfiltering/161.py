
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
assert solve("w") == "W"
assert solve("d") == "D"
assert solve("aaaaaAAaaaaaa") == "AAAAAaaAAAAAA"
assert solve("abc") == "ABC"
assert solve("abcde") == "ABCDE"
assert solve("ABCDE") == "abcde"
assert solve("The quick brown fox jumped over the lazy dog.") == "tHE QUICK BROWN FOX JUMPED OVER THE LAZY DOG."
assert solve("z") == "Z"
assert solve('#qw3@rty') == '#QW3@RTY'
assert solve('%4sss') == '%4SSS'
assert solve('@!kjf') == '@!KJF'
assert solve('9') == '9'
assert solve('aBcD') == 'AbCd'
assert solve('!!!') == '!!!'
assert solve("aBcD") == "AbCd"
assert solve("ABC") == "abc"
assert solve("123") == "321"
assert solve("A_bcd") == "a_BCD"
assert solve('Hello world!') == 'hELLO WORLD!'
assert solve('1234567890') == '0987654321'
assert solve('123') == '321'
assert solve(' ') == ' '
assert solve('aBcd') == 'AbCD'
assert solve('a') == 'A'
assert solve('1') == '1'
assert solve('1a2') == '1A2'
assert solve('1a2B') == '1A2b'
assert solve("aBcDeFg") == "AbCdEfG"
assert solve("1234567890") == "0987654321"
assert solve("HELLO") == "hello"
assert solve("12345") == "54321"
assert solve("za:za") == "ZA:ZA"
assert solve("ab:cd") == "AB:CD"
assert solve("1:2:3:4:5") == "5:4:3:2:1"
assert solve(":::") == ":::"
assert solve('abcde') == 'ABCDE'
assert solve('abcde12345') == 'ABCDE12345'
assert solve('abcd.!') == 'ABCD.!'
assert solve('12345') == '54321'
assert solve("abcdefghijklmnopqrstuvwxyz") == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
assert solve("---") == "---"
assert solve("aBc") == "AbC"
assert solve("A1b2c") == "a1B2C"
assert solve("//") == "//"
assert solve(" ") == " "
assert solve("//a1") == "//A1"
assert solve("...aBc") == "...AbC"
assert solve('AbCd') == 'aBcD'
assert solve('1234') == '4321'
assert solve("1X2x3X4x5X6x7") == "1x2X3x4X5x6X7"
assert solve("X") == "x"
assert solve("!") == "!"
assert solve("aBcDeFgH") == "AbCdEfGh"
assert solve("1") == "1"
assert solve("My name is john") == "mY NAME IS JOHN"
assert solve('aBcDeFg1') == 'AbCdEfG1'
assert solve('A B C D E F G1') == 'a b c d e f g1'
assert solve('aBc123') == 'AbC123'
assert solve('aB') == 'Ab'
assert solve('ABCDEF') == 'abcdef'
assert solve('AbCdEf') == 'aBcDeF'
assert solve('123456') == '654321'
assert solve('abcdef') == 'ABCDEF'
assert solve('abc123') == 'ABC123'
assert solve('123abc') == '123ABC'
assert solve('123abc456') == '123ABC456'
assert solve('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'abcdefghijklmnopqrstuvwxyz'
assert solve('abcdefghijklmnopqrstuvwxyz') == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
assert solve('xyz') == 'XYZ'
assert solve('XyZ') == 'xYz'
assert solve('.') == '.'
assert solve('!') == '!'
assert solve("ABCDEFG") == "abcdefg"
assert solve("abcdefg") == "ABCDEFG"
assert solve("ABCD") == "abcd"
assert solve("a1bcd") == "A1BCD"
assert solve("A1BCD") == "a1bcd"
assert solve("ab12") == "AB12"
assert solve("AbCd") == "aBcD"
assert solve("1234") == "4321"
assert solve("AbCdEfGhIjKlMnOpQrStUvWxYz") == "aBcDeFgHiJkLmNoPqRsTuVwXyZ"
assert solve("123456") == "654321"
assert solve('*1a*(3a') == '*1A*(3A'
assert solve('**a**') == '**A**'
assert solve('*0*') == '*0*'
assert solve('a0A') == 'A0a'
assert solve('a0a') == 'A0A'
assert solve('0A0') == '0a0'
assert solve('0a0') == '0A0'
assert solve('A0A') == 'a0a'
assert solve('*a*') == '*A*'
assert solve('0a*') == '0A*'
assert solve('0a*()') == '0A*()'
assert solve('#@a') == '#@A'
assert solve("Hello, World!") == "hELLO, wORLD!"
assert solve("123 Hello, World!") == "123 hELLO, wORLD!"
assert solve("321") == "123"
assert solve("a") == "A"
assert solve("A") == "a"
assert solve("aBcDeF") == "AbCdEf"
assert solve("@#$#@") == "@#$#@"
assert solve("1a2b3c") == "1A2B3C"
assert solve("HGK") == "hgk"
assert solve("A12") == "a12"
assert solve("A1B2") == "a1b2"
assert solve("0123456789") == "9876543210"
assert solve("Hello World") == "hELLO wORLD"
assert solve("Algorithms 123") == "aLGORITHMS 123"
assert "aBc12#$" == solve("AbC12#$")
assert solve('this is my string') == 'THIS IS MY STRING'
assert solve('K') == 'k'
assert solve("HeLlO") == "hElLo"
assert solve("abcdef") == "ABCDEF"
assert solve("@!#$%^&") == "&^%$#!@"
assert solve("hELLO") == "Hello"
assert solve('AAAaaa') == 'aaaAAA'
assert solve("1a2b3c4D") == "1A2B3C4d"
assert solve("hELLO wORLD!") == "Hello World!"
assert solve('ABC') == 'abc'
assert solve('$$$') == '$$$'
assert solve('A1234!') == 'a1234!'
assert solve('!ABC!') == '!abc!'
assert solve('!1234ABC!') == '!1234abc!'
assert solve('^1234!ABC_!') == '^1234!abc_!'
assert solve('!ABC@') == '!abc@'
assert solve('H') == 'h'
assert solve('H!') == 'h!'
assert solve('H@') == 'h@'
assert solve('h') == 'H'
assert solve('h!') == 'H!'
assert solve('h@') == 'H@'
assert solve('H1') == 'h1'
assert solve('H1!') == 'h1!'
assert solve('H1@') == 'h1@'
assert solve('h1') == 'H1'
assert solve('h1!') == 'H1!'
assert solve('h1@') == 'H1@'
assert solve('H1e') == 'h1E'
assert solve("hellooooo") == "HELLOOOOO"
assert solve("     ") == "     "
assert solve("asdfghjkl;") == "ASDFGHJKL;"
assert solve("This is a test") == "tHIS IS A TEST"
assert solve('z') == 'Z'
assert solve('1a2b3c') == '1A2B3C'
assert solve("HelloWorld") == "hELLOwORLD"
assert solve("123456789") == "987654321"
assert solve('aBcD123') == 'AbCd123'
assert solve('2aBcDeFgHiJ') == '2AbCdEfGhIj'
assert solve('12') == '21'
assert solve("HackerRank.com presents 'Pythonist 2'.") == "hACKERrANK.COM PRESENTS 'pYTHONIST 2'."
assert solve("!s? t+'") == "!S? T+'"
assert solve("Abc") == "aBC"
assert solve("AbCdEf") == "aBcDeF"
assert solve(";lkjh") == ";LKJH"
assert solve("dfgHJ") == "DFGhj"
assert solve("asdfghjkl") == "ASDFGHJKL"
assert solve("1qaz2wsx3edc") == "1QAZ2WSX3EDC"
assert solve("qazwsxedcrfv") == "QAZWSXEDCRFV"
assert solve("Hello, World?") == "hELLO, wORLD?"
assert solve('ABCDE') == 'abcde'
assert solve('aBcDe') == 'AbCdE'
assert solve('12ab34') == '12AB34'
assert solve('AaBbCc') == 'aAbBcC'
assert solve('a123#') == 'A123#'
assert solve('#AaBb1') == '#aAbB1'
assert solve('#') == '#'
assert solve("code") == "CODE"
assert solve("a"*50) == "A"*50
assert solve("!!!") == "!!!"
assert solve("Hello") == "hELLO"
assert solve("42") == "24"
assert solve("1a2b3c4d5e") == "1A2B3C4D5E"
assert solve("String.py") == "sTRING.PY"
assert solve('abcd1234') == 'ABCD1234'
assert solve("ABC1234") == "abc1234"
assert solve("Yay Python") == "yAY pYTHON"
assert solve("Yay") == "yAY"
assert solve("Python") == "pYTHON"
assert solve("The") == "tHE"
assert solve("aAbB") == "AaBb"
assert solve("AaBb") == "aAbB"
assert solve("AaBbCc") == "aAbBcC"
assert solve('mnopQrstuVWxyz') == 'MNOPqRSTUvwXYZ'
assert solve('abcD123') == 'ABCd123'
assert solve('ABCD') == 'abcd'
assert solve('Aa1b2c3dEe') == 'aA1B2C3DeE'
assert solve('A1b2c3dEe') == 'a1B2C3DeE'
assert solve('0Abc') == '0aBC'
assert solve("Hello World 123") == "hELLO wORLD 123"
assert solve("aA") == "Aa"
assert solve("a1b2c3") == "A1B2C3"
assert solve("1BcdE") == "1bCDe"
assert solve("c") == "C"
assert solve("1a") == "1A"
assert solve("1A") == "1a"
assert solve("1Aa") == "1aA"
assert solve("1ab") == "1AB"
assert solve("1aB") == "1Ab"
assert solve("1AaB") == "1aAb"
assert solve("hI, there") == "Hi, THERE"
assert solve("Hi, there") == "hI, THERE"
assert solve('abc def') == 'ABC DEF'
assert solve('1a2b3c4d') == '1A2B3C4D'
assert solve('A') == 'a'
assert solve('Aa') == 'aA'
assert solve('AaB') == 'aAb'
assert solve('aAb') == 'AaB'
assert solve('BbA') == 'bBa'
assert solve('bBa') == 'BbA'
assert solve('Bb') == 'bB'
assert solve('B') == 'b'
assert solve('b') == 'B'
assert solve('Z') == 'z'
assert solve('C') == 'c'
assert solve('Bc') == 'bC'
assert solve('bC') == 'Bc'
assert solve('aBc') == 'AbC'
assert solve('aBC') == 'Abc'
assert solve("asdfgh") == "ASDFGH"
assert solve("ASDFGH") == "asdfgh"
assert "AbcdE" == solve("aBCDe")
assert "A" == solve("a")
assert "abcde" == solve("ABCDE")
assert "ABCDE" == solve("abcde")
assert "aBcDe" == solve("AbCdE")
assert solve("hELLO wORLD") == "Hello World"
assert solve("1A2b3c4D5e6F") == "1a2B3C4d5E6f"
assert solve('HELLO') == 'hello'
assert solve('For1') == 'fOR1'
assert solve('fOR1') == 'For1'
assert solve("One line of text.") == "oNE LINE OF TEXT."
assert "aBcD" == solve("AbCd")
assert "abCD" == solve("ABcd")
assert "ABcd" == solve("abCD")
assert "ABCD" == solve("abcd")
assert "JAVASCRIPT" == solve("javascript")
assert solve("aBcDef") == "AbCdEF"
assert solve("345hgf") == "345HGF"
assert "aBcDeFgHiJkLmNoPqRsTuVwXyZ" == solve("AbCdEfGhIjKlMnOpQrStUvWxYz")
assert "!" == solve("!")
assert "aBcDeFgHiJkLmNoPqRsTuVwXyZ!" == solve("AbCdEfGhIjKlMnOpQrStUvWxYz!")
assert solve('abcd') == 'ABCD'
assert solve('!2#$aASD') == '!2#$Aasd'
assert solve("aBcDe") == "AbCdE"
assert solve("abcd!#$%*()@") == "ABCD!#$%*()@"
assert solve("1 4 6 4") == "4 6 4 1"
assert solve('this is a string') == 'THIS IS A STRING'
assert solve('AAaBbCcDd') == 'aaAbBcCdD'
assert solve('a1b2c3d4E5f6') == 'A1B2C3D4e5F6'
assert solve('abcd ef') == 'ABCD EF'
assert solve('a1b2c3d4e5f6') == 'A1B2C3D4E5F6'
assert solve('123456789') == '987654321'
assert solve("Zephyr") == "zEPHYR"
assert solve('AbcDe') == 'aBCdE'
assert solve('A1B2C3D4') == 'a1b2c3d4'
assert solve('bb') == 'BB'
assert solve('12AB') == '12ab'
assert solve('aaaa') == 'AAAA'
assert solve('AaAa') == 'aAaA'
assert solve('aa') == 'AA'
assert solve('AA') == 'aa'
assert solve("QWERTY") == "qwerty"
assert solve("abcdefGHI") == "ABCDEFghi"
assert solve("   ") == "   "
assert solve(" abc ") == " ABC "
assert solve("No reverse here!") == "nO REVERSE HERE!"
assert solve('Hello World!') == 'hELLO wORLD!'
assert solve("5") == "5"
assert solve("qwErTy") == "QWeRtY"
assert solve('TeSt') == 'tEsT'
assert solve('1z') == '1Z'
assert solve('z1') == 'Z1'
assert solve('1z1') == '1Z1'
assert solve('121') == '121'
assert solve('1A2b3C') == '1a2B3c'
assert solve('aBcDeFg') == 'AbCdEfG'
assert solve('2A3B4C5D6E7F8G9H0I') == '2a3b4c5d6e7f8g9h0i'
assert solve('1A2B3C') == '1a2b3c'
assert solve('abcABC') == 'ABCabc'
assert solve('abc123abc') == 'ABC123ABC'
assert solve("a2kA") == "A2Ka"
assert solve("hi") == "HI"
assert solve("HD") == "hd"
assert solve("solve") == "SOLVE"
assert solve("Solve") == "sOLVE"
assert solve("#*$&") == "&$*#"
assert solve("1h8e") == "1H8E"
assert solve("1A2B3C4D5E") == "1a2b3c4d5e"
assert solve("1a2b3c4d5e6f") == "1A2B3C4D5E6F"
assert solve("1A2B3C4D5E6F") == "1a2b3c4d5e6f"
assert solve("AbC") == "aBc"
assert solve("-1a2b3c4d5e6f") == "-1A2B3C4D5E6F"
assert solve("-1A2B3C4D5E6F") == "-1a2b3c4d5e6f"
