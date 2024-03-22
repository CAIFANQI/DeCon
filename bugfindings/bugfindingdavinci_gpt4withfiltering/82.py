
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(3, l):
        if l % i == 0:
            return False
    return True
assert prime_length("") == False
assert prime_length("hello") == True
assert prime_length("this is a long string") == False
assert prime_length("hi") == True
assert prime_length("this is a string") == False
assert prime_length("this is a very long string") == False
assert prime_length("abc") == True
assert prime_length("123456789") == False
assert prime_length('xxx') == True
assert prime_length('xxxx') == False
assert prime_length('xxxxx') == True
assert prime_length('xxxxxx') == False
assert prime_length('xxxxxxx') == True
assert prime_length('xxxxxxxx') == False
assert prime_length('xxxxxxxxxx') == False
assert prime_length('11') == True
assert prime_length('abcabc') == False
assert prime_length('a') == False
assert prime_length('') == False
assert prime_length("I am a string with a length of 28") == False
assert prime_length("my test is a prime") == False
assert prime_length("Vestibulum mattis neque ut enim blandit, id ornare lorem sollicitudin.") == False
assert prime_length("XY"), "XY has length 2"
assert prime_length("XyZ"), "XyZ has length 3"
assert not prime_length("AbCdEfGh"), "AbCdEfGh has length 8"
assert prime_length("ab") == True
assert prime_length("abcd") == False
assert prime_length("Hello") == True
assert prime_length('bingo') == True
assert prime_length('student') == True
assert prime_length('cat') == True
assert prime_length("Peter") == True
assert prime_length("abcef") is True
assert prime_length(' ') is False
assert prime_length("helloworld") == False
assert prime_length("a") == False
assert prime_length("abba") == False
assert prime_length('abcd') == False
assert prime_length('abcde') == True
assert prime_length('abcdef') == False
assert prime_length("asdfas") == False
assert prime_length('google') == False
assert prime_length('go') == True
assert prime_length("abcabc") == False
assert prime_length("Lorem ipsum") == True
assert prime_length("Lorem") == True
assert prime_length("aaaaaaaaa") == False
assert True == prime_length("se")
assert prime_length('hello') == True
assert prime_length("Goodbye") is True, "prime_length: 'Goodbye'"
assert prime_length("a") is False, "prime_length: 'a'"
assert prime_length("abcdefghijklmnopqrstuvwxyz") is False, "prime_length: 'abcdefghijklmnopqrstuvwxyz'"
assert False == prime_length("abcdef")
assert True == prime_length("lorem ipsum")
assert prime_length('This is a new string') == False
assert prime_length("to be or not to be") is False
assert prime_length("HELLO THERE") is True
assert prime_length("abcdefghi") == False
assert prime_length("abcdefghijklmno") == False
assert prime_length('abce') is False
assert prime_length('abcdefghi') is False
assert prime_length('abce') == False
assert prime_length('abcdefghi') == False
assert prime_length("string") == False
assert prime_length("tacocat") == True
assert prime_length("computer") == False
assert prime_length("abcdefghijklmnopqrstuvwxyz") == False
assert prime_length("shlomi is the best") is False
assert prime_length("a") is False
assert prime_length(' ') == False
assert prime_length("abcde") == True
assert prime_length("abcdef") == False
assert prime_length("abcdefg") == True
assert prime_length("abcdefgh") == False
assert prime_length("Amun") == False
assert prime_length('abcdefgh') == False
assert False == prime_length("foobar")
assert False == prime_length("")
assert prime_length('antidisestablishmentarianism') is False
assert prime_length('supercalifragilisticexpialidocious') is False
assert prime_length('') is False
assert prime_length('1234567890') is False
assert prime_length('abc') is True
assert prime_length('home') is False
assert prime_length('Are you a prime?') == False
assert prime_length('programming') == True
assert prime_length('false') == True
assert prime_length('true') == False
assert prime_length('ab') == True
assert prime_length('abacabaabacaba') == False
assert prime_length("aaba") == False
assert prime_length("abcdefghijklmnopqrstuvwxyzz") == False
assert prime_length("abcdefghijklmnopqrstuvwxyz1234567891") == False
assert prime_length('abac') == False
assert prime_length('abc') == True
assert prime_length('E') is False
assert prime_length('HELLO') is True
assert prime_length('A_VERY_LONG_STRING') is False
assert prime_length("abcd abcd") == False
assert prime_length("at") == True
assert prime_length('Python') == False
assert prime_length('aa') == True
assert prime_length(' a ') == True
assert prime_length('    ') == False
assert prime_length('abcabcabcabcabcd') == False
assert prime_length('cdab') == False
assert prime_length('cd') == True
assert prime_length('Once upon a time in a land far far away') is False
assert prime_length('World') is True
assert prime_length('Pybites') is True
assert prime_length('123456789') is False
assert prime_length('137') is True
assert prime_length('13') is True
assert prime_length('9') is False
assert prime_length("abb") == True
assert prime_length("abbc") == False
assert prime_length("abbccddee") == False
assert prime_length("abbccddeee") == False
assert prime_length("abbccddeeef") == True
assert prime_length("abbccddeeeff") == False
assert prime_length("abbccddeeeffg") == True
assert prime_length("abbccddeeeffgg") == False
assert prime_length("abbccddeeeffggg") == False
assert prime_length("hellooooo") == False
assert prime_length("hey") == True
assert prime_length("Hello there") == True
assert prime_length("the quick brown fox jumped over the lazy dog") == False
assert prime_length("bobbobbob") == False
assert prime_length("bobob") == True
assert prime_length("bobobobobobobob") == False
assert prime_length("I have a dog") == False
assert prime_length("abcabcabca") == False
assert False == prime_length("h")
assert prime_length("1234567") == True
assert prime_length('door') == False
assert prime_length('car') == True
assert prime_length('abcde') is True
assert prime_length("John Doe") == False
assert prime_length("My Name") == True
assert prime_length('1') == False
assert prime_length('kalpana') == True
assert prime_length('kalpanacse') == False
assert prime_length('kalpanacseu') == True
assert prime_length(" ") == False
assert prime_length("fo") == True
assert prime_length("XYZ") == True
assert prime_length("ABCD") == False
assert prime_length("python") == False
assert prime_length("thisisalongstring") == True
