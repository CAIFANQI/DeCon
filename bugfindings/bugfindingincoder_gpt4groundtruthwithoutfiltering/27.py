

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.lower()
assert flip_case("hello") == "HELLO"
assert flip_case("HELLO") == "hello"
assert flip_case("HELLO") == "hello", "Fifth test case"
assert flip_case("a") == "A"
assert flip_case("c") == "C"
assert flip_case("d") == "D"
assert flip_case("aa") == "AA"
assert flip_case("aBc") == "AbC"
assert flip_case('ABC') == 'abc'
assert flip_case('A') == 'a'
assert flip_case('a') == 'A'
assert flip_case('') == ''
assert flip_case('abc') == 'ABC'
assert flip_case('hELLO') == 'Hello'
assert flip_case('HELLO') == 'hello'
assert flip_case('HI') == 'hi'
assert flip_case('H') == 'h'
assert flip_case('h') == 'H'
assert flip_case("H") == "h"
assert flip_case("h") == "H"
assert flip_case("z") == "Z"
assert flip_case("zz") == "ZZ"
assert flip_case("hi") == "HI"
assert flip_case("i") == "I"
assert flip_case("HI") == "hi", "Incorrect flip"
assert flip_case('Java') == 'jAVA'
assert flip_case('Ruby') == 'rUBY'
assert flip_case('Python') == 'pYTHON'
assert flip_case('abcABC') == 'ABCabc'
assert flip_case('abcdef') == 'ABCDEF'
assert flip_case("wtf") == "WTF", 'Passed'
assert flip_case("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "abcdefghijklmnopqrstuvwxyz"
assert flip_case('AB') == 'ab'
assert flip_case('UPPER') == 'upper'
assert flip_case('abcde') == 'ABCDE'
assert flip_case("abc") == "ABC"
