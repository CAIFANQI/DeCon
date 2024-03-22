

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.lower()
assert flip_case("Hello World") == "hELLO wORLD"
assert flip_case("Python Programming") == "pYTHON pROGRAMMING"
assert flip_case("12345") == "12345"
assert flip_case("") == ""
assert flip_case("hElLo wOrLd") == "HeLlO WoRlD"
assert flip_case("Python is Fun") == "pYTHON IS fUN"
assert flip_case("aBcDeF") == "AbCdEf"
assert flip_case("abcdefg") == "ABCDEFG"
assert flip_case("hElLo WoRLd!") == "HeLlO wOrlD!"
assert flip_case("aBcDeFg") == "AbCdEfG"
assert flip_case("aBcD") == "AbCd"
assert flip_case("WORLD") == "world"
assert flip_case("HeLLo") == "hEllO"
assert flip_case("123") == "123"
assert flip_case("hELLO wORLD") == "Hello World"
assert flip_case('hELLO wORLD') == 'Hello World'
assert flip_case('12345') == '12345'
assert flip_case('') == ''
assert flip_case('AbCdEfGhIjKlMnOpQrStUvWxYz') == 'aBcDeFgHiJkLmNoPqRsTuVwXyZ'
assert flip_case('abc123') == 'ABC123'
assert flip_case('aBcD') == 'AbCd'
assert flip_case('123') == '123'
assert flip_case('123abc') == '123ABC'
assert flip_case('aBcDeFg') == 'AbCdEfG'
assert flip_case("abc123") == "ABC123"
assert flip_case("PYTHON") == "python"
assert flip_case('Python is Fun') == 'pYTHON IS fUN'
assert flip_case('aBcDeFgHiJkLmNoPqRsTuVwXyZ') == 'AbCdEfGhIjKlMnOpQrStUvWxYz'
assert flip_case("Python is Awesome") == "pYTHON IS aWESOME"
assert flip_case("AbCdEfG") == "aBcDeFg"
assert flip_case('abcdefghijklmnopqrstuvwxyz') == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
assert flip_case('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'abcdefghijklmnopqrstuvwxyz'
assert flip_case('1234567890') == '1234567890'
assert flip_case('!@#$%^&*()') == '!@#$%^&*()'
assert flip_case("XYZ") == "xyz"
assert flip_case(" ") == " "
assert flip_case("hElLO wOrld") == "HeLlo WoRLD"
assert flip_case("!@#$%^") == "!@#$%^"
assert flip_case("123456") == "123456"
assert flip_case('1234') == '1234'
assert flip_case("abcDEF") == "ABCdef"
assert flip_case("aBcDeFgHiJ") == "AbCdEfGhIj"
assert flip_case("Python is fun") == "pYTHON IS FUN"
assert flip_case("aBcDeFgHiJkLmNoPqRsTuVwXyZ") == "AbCdEfGhIjKlMnOpQrStUvWxYz"
assert flip_case("!!@@##") == "!!@@##"
assert flip_case("abcdefghijklmnopqrstuvwxyz") == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
assert flip_case("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "abcdefghijklmnopqrstuvwxyz"
assert flip_case("1234567890") == "1234567890"
assert flip_case("Python") == "pYTHON"
assert flip_case('abcdefg') == 'ABCDEFG'
assert flip_case("123$%^") == "123$%^"
assert flip_case("FlIpCaSe") == "fLiPcAsE"
assert flip_case('AbCdEfG') == 'aBcDeFg'
assert flip_case("AbCdEfGhIjKlMnOpQrStUvWxYz") == "aBcDeFgHiJkLmNoPqRsTuVwXyZ"
assert flip_case("!!!") == "!!!"
assert flip_case("HeLlO WoRlD") == "hElLo wOrLd"
assert flip_case('aBcDeFg12345') == 'AbCdEfG12345'
assert flip_case("Python is AWESOME") == "pYTHON IS awesome"
assert flip_case("hElLo") == "HeLlO"
assert flip_case('hElLo') == 'HeLlO'
assert flip_case('hElLo WoRlD') == 'HeLlO wOrLd'
assert flip_case('WORLD') == 'world'
assert flip_case('Python') == 'pYTHON'
assert flip_case("!@#$%") == "!@#$%"
assert flip_case("hElLo WoRlD") == "HeLlO wOrLd"
assert flip_case("aBcDeFgHiJkL") == "AbCdEfGhIjKl"
assert flip_case("aBcDeFgHiJkL12345") == "AbCdEfGhIjKl12345"
assert flip_case("HeLlO") == "hElLo"
assert flip_case('aBcDeF') == 'AbCdEf'
assert flip_case("hELLO wORLD!") == "Hello World!"
assert flip_case("wORLD") == "World"
assert flip_case("WorlD") == "wORLd"
assert flip_case('hELLO wORLD!') == 'Hello World!'
assert flip_case("hElLo wOrLd!") == "HeLlO WoRlD!"
assert flip_case("?!@#$%^&*()") == "?!@#$%^&*()"
assert flip_case("ABC123") == "abc123"
assert flip_case("eXaMpLe") == "ExAmPlE"
assert flip_case("Hello World!") == "hELLO wORLD!"
assert flip_case('HELLO') == 'hello'
assert flip_case('Python Programming') == 'pYTHON pROGRAMMING'
assert flip_case('abcDEF') == 'ABCdef'
