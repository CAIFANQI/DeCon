

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.lower()
assert flip_case("") == ""
assert flip_case("aBcDeF") == "AbCdEf"
assert flip_case("abcdefg") == "ABCDEFG"
assert flip_case("aBcDeFg") == "AbCdEfG"
assert flip_case("aBcD") == "AbCd"
assert flip_case("WORLD") == "world"
assert flip_case("HeLLo") == "hEllO"
assert flip_case('') == ''
assert flip_case('AbCdEfGhIjKlMnOpQrStUvWxYz') == 'aBcDeFgHiJkLmNoPqRsTuVwXyZ'
assert flip_case('aBcD') == 'AbCd'
assert flip_case('aBcDeFg') == 'AbCdEfG'
assert flip_case("PYTHON") == "python"
assert flip_case('aBcDeFgHiJkLmNoPqRsTuVwXyZ') == 'AbCdEfGhIjKlMnOpQrStUvWxYz'
assert flip_case("AbCdEfG") == "aBcDeFg"
assert flip_case('abcdefghijklmnopqrstuvwxyz') == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
assert flip_case('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'abcdefghijklmnopqrstuvwxyz'
assert flip_case("XYZ") == "xyz"
assert flip_case("abcDEF") == "ABCdef"
assert flip_case("aBcDeFgHiJ") == "AbCdEfGhIj"
assert flip_case("aBcDeFgHiJkLmNoPqRsTuVwXyZ") == "AbCdEfGhIjKlMnOpQrStUvWxYz"
assert flip_case("abcdefghijklmnopqrstuvwxyz") == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
assert flip_case("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "abcdefghijklmnopqrstuvwxyz"
assert flip_case("Python") == "pYTHON"
assert flip_case('abcdefg') == 'ABCDEFG'
assert flip_case("FlIpCaSe") == "fLiPcAsE"
assert flip_case('AbCdEfG') == 'aBcDeFg'
assert flip_case("AbCdEfGhIjKlMnOpQrStUvWxYz") == "aBcDeFgHiJkLmNoPqRsTuVwXyZ"
assert flip_case("hElLo") == "HeLlO"
assert flip_case('hElLo') == 'HeLlO'
assert flip_case('WORLD') == 'world'
assert flip_case('Python') == 'pYTHON'
assert flip_case("aBcDeFgHiJkL") == "AbCdEfGhIjKl"
assert flip_case("HeLlO") == "hElLo"
assert flip_case('aBcDeF') == 'AbCdEf'
assert flip_case("wORLD") == "World"
assert flip_case("WorlD") == "wORLd"
assert flip_case("eXaMpLe") == "ExAmPlE"
assert flip_case('HELLO') == 'hello'
assert flip_case('abcDEF') == 'ABCdef'
