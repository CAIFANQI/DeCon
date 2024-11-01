

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.lower()
assert flip_case("hello") == "HELLO"
assert flip_case("hello-") == "HELLO-"
assert flip_case("hello--") == "HELLO--"
assert flip_case("hello---") == "HELLO---"
assert flip_case("hello world!") == "HELLO WORLD!"
assert flip_case("HELLO") == "hello"
assert flip_case("hello123") == "HELLO123"
assert flip_case("hello1234") == "HELLO1234"
assert flip_case("hello12345") == "HELLO12345"
assert flip_case("hello123456") == "HELLO123456"
assert flip_case("hello1234567") == "HELLO1234567"
assert flip_case("hello2") == "HELLO2", "Third test case"
assert flip_case("HELLO") == "hello", "Fifth test case"
assert flip_case("hello4") == "HELLO4", "Seventh test case"
assert flip_case("hello8") == "HELLO8", "Fourteenth test case"
assert flip_case("a b c") == "A B C"
assert flip_case("a b c d e") == "A B C D E"
assert flip_case("a") == "A"
assert flip_case("c") == "C"
assert flip_case("d") == "D"
assert flip_case("hello!") == "HELLO!"
assert flip_case("aa") == "AA"
assert flip_case("aBc") == "AbC"
assert flip_case("hello world") == "HELLO WORLD"
assert flip_case("HELLO WORLD") == "hello world", "should return 'hello world'"
assert flip_case("010101") == "010101"
assert flip_case("0o0o101001") == "0O0O101001"
assert flip_case("0x101001") == "0X101001"
assert flip_case("0b101001") == "0B101001"
assert flip_case("0B101001") == "0b101001"
assert flip_case("0X101001") == "0x101001"
assert flip_case('ABC') == 'abc'
assert flip_case('A') == 'a'
assert flip_case('a') == 'A'
assert flip_case('0a') == '0A'
assert flip_case('') == ''
assert flip_case('abc') == 'ABC'
assert flip_case('hELLO') == 'Hello'
assert flip_case('HELLO') == 'hello'
assert flip_case("02345") == "02345"
assert flip_case("023456789") == "023456789"
assert flip_case("01234567") == "01234567"
assert flip_case("012345678") == "012345678"
assert flip_case("0123456790") == "0123456790"
assert flip_case("0123456789") == "0123456789"
assert flip_case("012345") == "012345"
assert flip_case("01234567890") == "01234567890"
assert flip_case("Hello World!123") == "hELLO wORLD!123"
assert flip_case('HI') == 'hi'
assert flip_case('H') == 'h'
assert flip_case('h') == 'H'
assert flip_case("!@#$%^&*()_+") == "!@#$%^&*()_+"
assert flip_case("H") == "h"
assert flip_case("h") == "H"
assert flip_case("z") == "Z"
assert flip_case("zz") == "ZZ"
assert flip_case("hi") == "HI"
assert flip_case("i") == "I"
assert flip_case("!i") == "!I"
assert flip_case("!hello world!") == "!HELLO WORLD!"
assert flip_case("!!!") == "!!!" # no change
assert flip_case("!!") == "!!" # no change
assert flip_case("!hi") == "!HI"
assert flip_case("!hi there") == "!HI THERE"
assert flip_case(" hello world  ") == " HELLO WORLD  "
assert flip_case("hello, world!") == "HELLO, WORLD!"
assert flip_case("hello, world!!!") == "HELLO, WORLD!!!"
assert flip_case("HI") == "hi", "Incorrect flip"
assert flip_case('Java') == 'jAVA'
assert flip_case('C++') == 'c++'
assert flip_case('C#') == 'c#'
assert flip_case('Ruby') == 'rUBY'
assert flip_case('Python') == 'pYTHON'
assert flip_case('abcABC') == 'ABCabc'
assert flip_case('abcdef') == 'ABCDEF'
assert flip_case('HELLO WORLD') == 'hello world'
assert flip_case("12345") == "12345"
assert flip_case("wtf") == "WTF", 'Passed'
assert flip_case("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "abcdefghijklmnopqrstuvwxyz"
assert flip_case('AB') == 'ab'
assert flip_case('!') == '!'
assert flip_case('123') == '123'
assert flip_case('123!') == '123!'
assert flip_case('!123') == '!123'
assert flip_case('Hello World') == 'hELLO wORLD'
assert flip_case('UPPER') == 'upper'
assert flip_case('abcde') == 'ABCDE'
assert flip_case("abc") == "ABC"
