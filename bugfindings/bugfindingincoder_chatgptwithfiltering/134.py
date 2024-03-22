
def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.upper()) <= 122) else False
assert check_if_last_char_is_a_letter('abe cde') == False
assert check_if_last_char_is_a_letter('abf cde') == False
assert check_if_last_char_is_a_letter('abg cde') == False
assert check_if_last_char_is_a_letter('abh cde') == False
assert check_if_last_char_is_a_letter('ar') == False
assert check_if_last_char_is_a_letter('') == False
assert check_if_last_char_is_a_letter(' ') == False
assert check_if_last_char_is_a_letter('abcde') == False
assert check_if_last_char_is_a_letter('abcdefghijklmnopqrstuvwxyz') == False
assert check_if_last_char_is_a_letter('abc') == False
assert check_if_last_char_is_a_letter('a bcd') == False
assert check_if_last_char_is_a_letter('asdasd!') is False
assert check_if_last_char_is_a_letter('asdasd#') is False
assert check_if_last_char_is_a_letter('asdasd$') is False
assert check_if_last_char_is_a_letter('asdasd%') is False
assert check_if_last_char_is_a_letter('asdasd&') is False
assert check_if_last_char_is_a_letter('asdasd*') is False
assert check_if_last_char_is_a_letter('asdasd(') is False
assert check_if_last_char_is_a_letter('asdasd]') is False
assert check_if_last_char_is_a_letter('asdasd') is False
assert check_if_last_char_is_a_letter('hijklmnopqrstuvwxy') == False
assert check_if_last_char_is_a_letter('hijklmnopqrstuvwxy1') == False
assert check_if_last_char_is_a_letter('hijklmnopqrstuvwxyab') == False
assert check_if_last_char_is_a_letter('hijklmnopqrstuvwxyab1') == False
assert check_if_last_char_is_a_letter('hijklmnopqrstuvwxyab123') == False
assert check_if_last_char_is_a_letter('hijklmnopqrstuvwxyab0123') == False
assert check_if_last_char_is_a_letter('hijklmnopqrstuvwxyab012') == False
assert check_if_last_char_is_a_letter("0word") == False
assert check_if_last_char_is_a_letter("0words") == False
assert check_if_last_char_is_a_letter("word0word") == False
assert check_if_last_char_is_a_letter("word0words") == False
assert check_if_last_char_is_a_letter("0word0words") == False
assert check_if_last_char_is_a_letter("word0words0word") == False
assert check_if_last_char_is_a_letter("word0words0words") == False
assert check_if_last_char_is_a_letter("0word0words0words") == False
assert check_if_last_char_is_a_letter('a') == True
assert check_if_last_char_is_a_letter('123') == False
assert check_if_last_char_is_a_letter('123abc') == False
assert not check_if_last_char_is_a_letter('abracad')
assert not check_if_last_char_is_a_letter('abracada')
assert not check_if_last_char_is_a_letter('abraca')
assert not check_if_last_char_is_a_letter('abrac')
assert not check_if_last_char_is_a_letter('abra')
assert not check_if_last_char_is_a_letter('abr')
assert not check_if_last_char_is_a_letter('ab')
assert check_if_last_char_is_a_letter("abc def ghi jkl mn") == False
assert check_if_last_char_is_a_letter("abc def ghi jkl mnop") == False
assert check_if_last_char_is_a_letter("A") is True
assert check_if_last_char_is_a_letter('ab') == False
assert check_if_last_char_is_a_letter('ab ') == False
assert check_if_last_char_is_a_letter('aba') == False
assert check_if_last_char_is_a_letter('ab cdefg') == False
assert check_if_last_char_is_a_letter('aba cdefg') == False
assert check_if_last_char_is_a_letter('aba cd efg') == False
assert check_if_last_char_is_a_letter('aba cd efg ') == False
assert check_if_last_char_is_a_letter('aba cd efg g h i') == True
assert check_if_last_char_is_a_letter("python?") == False
assert check_if_last_char_is_a_letter("python!") == False
assert check_if_last_char_is_a_letter("python,,") == False
assert check_if_last_char_is_a_letter("python.") == False
assert check_if_last_char_is_a_letter("python.?") == False
assert check_if_last_char_is_a_letter("python.!") == False
assert check_if_last_char_is_a_letter("python,.") == False
assert check_if_last_char_is_a_letter("A") == True
assert check_if_last_char_is_a_letter("0") == False
assert check_if_last_char_is_a_letter("9") == False
assert check_if_last_char_is_a_letter("1") == False
assert check_if_last_char_is_a_letter("!") == False
assert check_if_last_char_is_a_letter("?") == False
assert check_if_last_char_is_a_letter("b") == True
assert check_if_last_char_is_a_letter("b?") == False
assert check_if_last_char_is_a_letter("c!") == False
assert check_if_last_char_is_a_letter("c?") == False
assert check_if_last_char_is_a_letter('aba') is False
assert check_if_last_char_is_a_letter('aa') is False
assert check_if_last_char_is_a_letter('ab') is False
assert check_if_last_char_is_a_letter('') is False
assert check_if_last_char_is_a_letter(' ') is False
assert check_if_last_char_is_a_letter('1') is False
assert check_if_last_char_is_a_letter('0') is False
assert not check_if_last_char_is_a_letter('abcd')
assert check_if_last_char_is_a_letter('bc') == False
assert check_if_last_char_is_a_letter('cde') == False
assert check_if_last_char_is_a_letter('fg') == False
assert check_if_last_char_is_a_letter('abc defg') == False
assert check_if_last_char_is_a_letter('abc defg ') == False
assert check_if_last_char_is_a_letter('abc def g ') == False
assert check_if_last_char_is_a_letter('abc def g hi') == False
assert check_if_last_char_is_a_letter('no') is False
assert check_if_last_char_is_a_letter('yes') is False
assert check_if_last_char_is_a_letter('123') is False
assert check_if_last_char_is_a_letter('abc123') is False
assert check_if_last_char_is_a_letter('!') is False
assert check_if_last_char_is_a_letter('$') is False
assert check_if_last_char_is_a_letter('@') is False
assert check_if_last_char_is_a_letter('$@') is False
assert not check_if_last_char_is_a_letter('Hello world!')
assert not check_if_last_char_is_a_letter('Hello world')
assert not check_if_last_char_is_a_letter('Hello ')
assert not check_if_last_char_is_a_letter(' ')
assert not check_if_last_char_is_a_letter('')
assert check_if_last_char_is_a_letter('qwertyui') == False
assert check_if_last_char_is_a_letter("abc defgh") == False
assert check_if_last_char_is_a_letter("abc def gh") == False
assert check_if_last_char_is_a_letter("abc defghijk") == False
assert check_if_last_char_is_a_letter("abc defghijklm") == False
assert check_if_last_char_is_a_letter("abc defghijklmno") == False
assert check_if_last_char_is_a_letter("abc def ghijklmnop") == False
assert check_if_last_char_is_a_letter("abc def ghijklmnopqrs") == False
assert check_if_last_char_is_a_letter('This is a string!') == False
assert check_if_last_char_is_a_letter('This') == False
assert check_if_last_char_is_a_letter('Th') == False
assert check_if_last_char_is_a_letter('aaa') == False
assert check_if_last_char_is_a_letter('   ') == False
assert check_if_last_char_is_a_letter('aabb') == False
assert check_if_last_char_is_a_letter('aabbc') == False
assert check_if_last_char_is_a_letter('1') == False
assert check_if_last_char_is_a_letter('a b c') == True
assert check_if_last_char_is_a_letter('a b c ') == False
assert check_if_last_char_is_a_letter('abc') is False
assert check_if_last_char_is_a_letter('string') is False
assert check_if_last_char_is_a_letter('string1') is False
assert check_if_last_char_is_a_letter('string11') is False
assert check_if_last_char_is_a_letter('string11a') is False
assert check_if_last_char_is_a_letter('  string') is False
assert check_if_last_char_is_a_letter('a')
assert not check_if_last_char_is_a_letter('!')
assert check_if_last_char_is_a_letter('goodbye') is False
assert check_if_last_char_is_a_letter('b')
assert check_if_last_char_is_a_letter('dog') is False
assert check_if_last_char_is_a_letter('dogdog') is False
assert check_if_last_char_is_a_letter('dogcat') is False
assert check_if_last_char_is_a_letter('abb') is False
assert check_if_last_char_is_a_letter('abcde') is False
assert check_if_last_char_is_a_letter('xyz') is False
assert check_if_last_char_is_a_letter('xyz') == False
assert check_if_last_char_is_a_letter('dog') == False
assert check_if_last_char_is_a_letter('potato') == False
assert check_if_last_char_is_a_letter('banana') == False
assert check_if_last_char_is_a_letter('1234') == False
assert check_if_last_char_is_a_letter('H') is True
assert check_if_last_char_is_a_letter('h ') is False
assert check_if_last_char_is_a_letter('xyz ') == False
assert check_if_last_char_is_a_letter('hi') == False
assert check_if_last_char_is_a_letter('hello') == False
assert check_if_last_char_is_a_letter('hibye1234') == False
assert check_if_last_char_is_a_letter('Hello!') is False
assert check_if_last_char_is_a_letter('Hello@') is False
assert check_if_last_char_is_a_letter('Hello There') is False
assert check_if_last_char_is_a_letter('Hello ') is False
assert check_if_last_char_is_a_letter('Hello?') is False
assert check_if_last_char_is_a_letter('  ') is False
assert check_if_last_char_is_a_letter('abcdz') == False
assert check_if_last_char_is_a_letter('Hello, World!') == False
assert check_if_last_char_is_a_letter("dog") == False
assert check_if_last_char_is_a_letter('abbcde') == False
assert check_if_last_char_is_a_letter('abbbcde') == False
assert check_if_last_char_is_a_letter('abbcd') == False
assert check_if_last_char_is_a_letter('abbbcdef') == False
assert check_if_last_char_is_a_letter('abbbcdefdefdefdef') == False
assert check_if_last_char_is_a_letter('a b a') is True
assert not check_if_last_char_is_a_letter('abb')
assert not check_if_last_char_is_a_letter('abc')
assert not check_if_last_char_is_a_letter('abbb')
assert not check_if_last_char_is_a_letter('abbbb')
assert check_if_last_char_is_a_letter("AB CDE") is False
assert check_if_last_char_is_a_letter('ab cd') == False
assert not check_if_last_char_is_a_letter('1')
assert not check_if_last_char_is_a_letter('  ')
assert not check_if_last_char_is_a_letter('\t')
assert not check_if_last_char_is_a_letter('   ')
assert check_if_last_char_is_a_letter('abcA') == False
assert check_if_last_char_is_a_letter('abc ') == False
assert check_if_last_char_is_a_letter('abc de') == False
assert check_if_last_char_is_a_letter("A B") == True
assert check_if_last_char_is_a_letter("ab B") == True
assert check_if_last_char_is_a_letter("ab b") == True
assert check_if_last_char_is_a_letter("B A") == True
assert check_if_last_char_is_a_letter("ab A B") == True
assert check_if_last_char_is_a_letter("B A A") == True
assert check_if_last_char_is_a_letter('abc  ') == False
assert check_if_last_char_is_a_letter('abc   ') == False
assert check_if_last_char_is_a_letter('Hello World') == False
assert check_if_last_char_is_a_letter('Hello Wolrd!') == False
assert check_if_last_char_is_a_letter("abcde") == False, "Should be False."
assert check_if_last_char_is_a_letter("abc efg hij") == False, "Should be False."
assert check_if_last_char_is_a_letter("abcde fgh") == False, "Should be False."
assert check_if_last_char_is_a_letter('hello1') == False
assert check_if_last_char_is_a_letter('hell2') == False
assert check_if_last_char_is_a_letter('abcABC') == False
assert check_if_last_char_is_a_letter('a b c') is True
assert check_if_last_char_is_a_letter('dogs') is False
assert check_if_last_char_is_a_letter('cats') is False
assert check_if_last_char_is_a_letter('123 ') is False
assert check_if_last_char_is_a_letter('Hello') == False
assert check_if_last_char_is_a_letter('!') == False
assert check_if_last_char_is_a_letter("") == False
assert not check_if_last_char_is_a_letter('abcde')
assert not check_if_last_char_is_a_letter('abc ')
assert not check_if_last_char_is_a_letter('abc 123')
assert not check_if_last_char_is_a_letter('123')
assert not check_if_last_char_is_a_letter('abc abc 123')
assert check_if_last_char_is_a_letter("abc") == False
assert check_if_last_char_is_a_letter("abc de fg") == False
assert check_if_last_char_is_a_letter('This is test') == False
assert check_if_last_char_is_a_letter('Hello123') == False
assert check_if_last_char_is_a_letter('abc123 123') == False
assert check_if_last_char_is_a_letter('abc def') is False
assert check_if_last_char_is_a_letter("Hey, What's the weather like?") == False
assert check_if_last_char_is_a_letter("Hello World") == False
assert check_if_last_char_is_a_letter('abc dabcd e') is True
assert check_if_last_char_is_a_letter('abc defg hijklmnopqrs stuvwxz') is False
assert check_if_last_char_is_a_letter('abc!@#') == False
