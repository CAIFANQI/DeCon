
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
assert check_if_last_char_is_a_letter('test. ') == False
assert check_if_last_char_is_a_letter('test?') == False
assert check_if_last_char_is_a_letter('test') == False
assert check_if_last_char_is_a_letter('test!') == False
assert check_if_last_char_is_a_letter('+') == False
assert check_if_last_char_is_a_letter('test12') == False
assert check_if_last_char_is_a_letter('test 12') == False
assert check_if_last_char_is_a_letter('test\n') == False
assert check_if_last_char_is_a_letter('test\t') == False
assert check_if_last_char_is_a_letter("C# is not a letter, but C is a letter") == False
assert check_if_last_char_is_a_letter("abc ") == False
assert check_if_last_char_is_a_letter("123") == False
assert check_if_last_char_is_a_letter("123 abc") == False
assert check_if_last_char_is_a_letter('a million') is False
assert check_if_last_char_is_a_letter('In 2015') is False
assert check_if_last_char_is_a_letter('As9') is False
assert check_if_last_char_is_a_letter('pencil') is False
assert check_if_last_char_is_a_letter("abc 123") == False
assert check_if_last_char_is_a_letter("abc. ") == False
assert check_if_last_char_is_a_letter("a. ") == False
assert check_if_last_char_is_a_letter("ab ") == False
assert check_if_last_char_is_a_letter("ab. ") == False
assert False == check_if_last_char_is_a_letter("Hello, World!.")
assert False == check_if_last_char_is_a_letter("Python!")
assert check_if_last_char_is_a_letter('b b.') == False
assert check_if_last_char_is_a_letter('b b,') == False
assert check_if_last_char_is_a_letter(' ') == False
assert check_if_last_char_is_a_letter('.') == False
assert check_if_last_char_is_a_letter(',') == False
assert check_if_last_char_is_a_letter(' b ') == False
assert check_if_last_char_is_a_letter(' b.') == False
assert check_if_last_char_is_a_letter(' b,') == False
assert check_if_last_char_is_a_letter("Hello World") == False
assert check_if_last_char_is_a_letter("!@#$%&^*{}") == False
assert check_if_last_char_is_a_letter('...') == False
assert check_if_last_char_is_a_letter('hello') == False
assert check_if_last_char_is_a_letter("I'm here") == False
assert check_if_last_char_is_a_letter("") == False
assert check_if_last_char_is_a_letter("Hello World ") == False
assert check_if_last_char_is_a_letter("Hello World!.") == False
assert check_if_last_char_is_a_letter("Hello World!..") == False
assert check_if_last_char_is_a_letter('The moon is blue') == False
assert check_if_last_char_is_a_letter("Hi") == False
assert check_if_last_char_is_a_letter("Hi, world!") == False
assert check_if_last_char_is_a_letter("hello world") == False
assert check_if_last_char_is_a_letter("hello, world!") == False
assert check_if_last_char_is_a_letter("   ") == False
assert False == check_if_last_char_is_a_letter("I'm hungry!")
assert False == check_if_last_char_is_a_letter("")
assert check_if_last_char_is_a_letter('abc#+') == False
assert check_if_last_char_is_a_letter('abc.%') == False
assert check_if_last_char_is_a_letter('abc-&@') == False
assert check_if_last_char_is_a_letter('Th!s 1s a v@ry str@nge str!ng,') == False
assert check_if_last_char_is_a_letter('Esto no tiene nada de raro') == False
assert check_if_last_char_is_a_letter('hello world') == False
assert check_if_last_char_is_a_letter('hello world. ') == False
assert check_if_last_char_is_a_letter('earth') == False
assert check_if_last_char_is_a_letter("A Last-Character Punctuation Check?") == False
assert check_if_last_char_is_a_letter("A Last-Character Punctuation Check.") == False
assert check_if_last_char_is_a_letter("A Last-Character Punctuation Check\n") == False
assert check_if_last_char_is_a_letter("A Last-Character Punctuation Check\t") == False
assert check_if_last_char_is_a_letter("A Last-Character Punctuation Check\r") == False
assert check_if_last_char_is_a_letter("A Last-Character Punctuation Check\r\n") == False
assert check_if_last_char_is_a_letter("A Last-Character Punctuation Check!") == False
assert check_if_last_char_is_a_letter("A Last-Character Punctuation Check/") == False
assert check_if_last_char_is_a_letter("A Last-Character Punctuation Check[") == False
assert check_if_last_char_is_a_letter('hello,world') == False
assert check_if_last_char_is_a_letter('!!') == False
assert check_if_last_char_is_a_letter("This sentence ends in a period.") == False
assert check_if_last_char_is_a_letter("This sentence ends in a period  .") == False
assert check_if_last_char_is_a_letter("This sentence ends in a period...") == False
assert check_if_last_char_is_a_letter("This sentence ends in a period") == False
assert check_if_last_char_is_a_letter("This sentence ends in a period,") == False
assert check_if_last_char_is_a_letter("This sentence ends in a period;") == False
assert check_if_last_char_is_a_letter("This sentence ends in a period!") == False
assert check_if_last_char_is_a_letter("This sentence ends in a period?") == False
assert check_if_last_char_is_a_letter("1") == False
assert check_if_last_char_is_a_letter("sdf-") == False
assert check_if_last_char_is_a_letter(" !!!!") == False
assert check_if_last_char_is_a_letter("aaaaa ") == False
assert check_if_last_char_is_a_letter("hep!") == False
assert check_if_last_char_is_a_letter("HI") == False
assert check_if_last_char_is_a_letter("?") == False
assert check_if_last_char_is_a_letter("hahaha!!!") == False
assert check_if_last_char_is_a_letter("Hello world") == False
assert check_if_last_char_is_a_letter("#123") == False
assert check_if_last_char_is_a_letter("$%hi12") == False
assert check_if_last_char_is_a_letter("abcabcabcabcabcabcabcabcabcabcabcabcabcabc.") == False
assert check_if_last_char_is_a_letter("abcabcabcabcabcabcabcabcabcabcabcabcabcabc:s") == False
assert check_if_last_char_is_a_letter("abcabcabcabcabcabcabcabcabcabcabcabcabcabc:") == False
assert check_if_last_char_is_a_letter("abcabcabcabcabcabcabcabcabcabcabcabcabcabc,") == False
assert check_if_last_char_is_a_letter("hello world!.") == False
assert check_if_last_char_is_a_letter("!!!!") == False
assert check_if_last_char_is_a_letter("hello123") == False
assert check_if_last_char_is_a_letter("heLlo") == False
assert check_if_last_char_is_a_letter("hello world, yo") == False
assert check_if_last_char_is_a_letter('hello world') is False
assert check_if_last_char_is_a_letter('hello world...') is False
assert check_if_last_char_is_a_letter('Hi, my name is!') == False
assert check_if_last_char_is_a_letter('Hi, my name is John') == False
assert check_if_last_char_is_a_letter('My name is John') == False
assert check_if_last_char_is_a_letter('Hello, how are you?') == False
assert check_if_last_char_is_a_letter('beach walk') == False
assert check_if_last_char_is_a_letter('foo.') == False
assert check_if_last_char_is_a_letter('green olives') == False
assert check_if_last_char_is_a_letter('orange.') == False
assert check_if_last_char_is_a_letter('hello. ') == False
assert check_if_last_char_is_a_letter('hello, world') == False
assert check_if_last_char_is_a_letter('hello world.') == False
assert check_if_last_char_is_a_letter("a1") == False
assert check_if_last_char_is_a_letter("a  ") == False
assert check_if_last_char_is_a_letter(' abc') == False
assert check_if_last_char_is_a_letter('abc1') == False
assert check_if_last_char_is_a_letter('1abc') == False
assert check_if_last_char_is_a_letter('123abc') == False
assert check_if_last_char_is_a_letter('abc123') == False
assert check_if_last_char_is_a_letter('abc123abc') == False
assert check_if_last_char_is_a_letter('1abc12') == False
assert check_if_last_char_is_a_letter(' abc ') == False
assert check_if_last_char_is_a_letter("stella's") == False
assert check_if_last_char_is_a_letter(" ") == False
assert check_if_last_char_is_a_letter("stellaw") == False
assert check_if_last_char_is_a_letter("stellaw 3") == False
assert False == check_if_last_char_is_a_letter('abc  ')
assert False == check_if_last_char_is_a_letter('  abc   ')
assert False == check_if_last_char_is_a_letter('  abc  def  ')
assert False == check_if_last_char_is_a_letter('  abc  def!  ')
assert False == check_if_last_char_is_a_letter('  abc-  def')
assert False == check_if_last_char_is_a_letter('  abc-  def  ')
assert False == check_if_last_char_is_a_letter('  abc  def-  ')
assert False == check_if_last_char_is_a_letter('  abc  def-  hij')
assert check_if_last_char_is_a_letter("abcd!") == False
assert check_if_last_char_is_a_letter("abcde ") == False
assert check_if_last_char_is_a_letter("abcde   ") == False
assert check_if_last_char_is_a_letter("abcde\n") == False
assert check_if_last_char_is_a_letter('1. Non-letter char at the end.') == False
assert check_if_last_char_is_a_letter('2. Letter char at the end...') == False
assert check_if_last_char_is_a_letter('3. Non-letter char at the end!') == False
assert check_if_last_char_is_a_letter('5. Non-letter char at the end?') == False
assert check_if_last_char_is_a_letter('Giraffe  ') == False
assert check_if_last_char_is_a_letter('Hi ') == False
assert check_if_last_char_is_a_letter('Hello') == False
assert check_if_last_char_is_a_letter('xD') == False
assert check_if_last_char_is_a_letter('abc') == False
assert check_if_last_char_is_a_letter('xD?') == False
assert check_if_last_char_is_a_letter('O_o') == False
assert check_if_last_char_is_a_letter('Abc') == False
assert check_if_last_char_is_a_letter('A1bc') == False
assert check_if_last_char_is_a_letter('a1bc') == False
assert check_if_last_char_is_a_letter('Hi there') == False
assert check_if_last_char_is_a_letter('Oh no') == False
assert check_if_last_char_is_a_letter("What about this?") is False
assert check_if_last_char_is_a_letter("This is a sentence, not a word.") is False
assert check_if_last_char_is_a_letter("The dog is hungry!") == False
assert check_if_last_char_is_a_letter('He llo, world!') == False
assert check_if_last_char_is_a_letter('Hello world!') == False
assert check_if_last_char_is_a_letter('Hello, world!!') == False
assert check_if_last_char_is_a_letter('Hello, world!.') == False
assert check_if_last_char_is_a_letter('abc 2') == False
assert check_if_last_char_is_a_letter('abcd') == False
assert check_if_last_char_is_a_letter('abc. 1') == False
assert check_if_last_char_is_a_letter('abc1. 2') == False
assert check_if_last_char_is_a_letter('1. 2') == False
assert check_if_last_char_is_a_letter(" abc") == False
assert check_if_last_char_is_a_letter("a b ") == False
assert check_if_last_char_is_a_letter("a bc") == False
assert check_if_last_char_is_a_letter(" abc ") == False
assert check_if_last_char_is_a_letter("hello world!") is False
assert check_if_last_char_is_a_letter("hello") is False
assert check_if_last_char_is_a_letter("hello123") is False
assert check_if_last_char_is_a_letter(" ") is False
assert check_if_last_char_is_a_letter("this is a test2.") is False
assert check_if_last_char_is_a_letter("this is a test2") is False
assert check_if_last_char_is_a_letter("what? no it's not!") is False
assert check_if_last_char_is_a_letter("i'm not a real word") is False
assert check_if_last_char_is_a_letter("i am a real word2.") is False
assert check_if_last_char_is_a_letter("no") == False
assert check_if_last_char_is_a_letter("yes.") == False
assert check_if_last_char_is_a_letter("yes!") == False
assert check_if_last_char_is_a_letter("yes") == False
assert check_if_last_char_is_a_letter("   maf.to.fu") == False
assert check_if_last_char_is_a_letter("   -maa.to.fu") == False
assert check_if_last_char_is_a_letter("free") == False
assert check_if_last_char_is_a_letter("PYTHON") == False
assert check_if_last_char_is_a_letter("!") == False
assert check_if_last_char_is_a_letter('hello!  ') == False
assert check_if_last_char_is_a_letter("hello!") is False
assert check_if_last_char_is_a_letter("hello?...?") is False
assert check_if_last_char_is_a_letter("hello!world") == False
assert check_if_last_char_is_a_letter("hello") == False
assert False == check_if_last_char_is_a_letter("amazing ")
assert False == check_if_last_char_is_a_letter("amazing?  ")
assert False == check_if_last_char_is_a_letter("amazing.  ")
assert check_if_last_char_is_a_letter("abc123abc") == False
assert check_if_last_char_is_a_letter("Hello there, how are you?") == False
assert check_if_last_char_is_a_letter('hello there...') == False
assert check_if_last_char_is_a_letter('123') == False
assert check_if_last_char_is_a_letter("abc is not a word") == False
assert check_if_last_char_is_a_letter("abc is not a word. ") == False
assert check_if_last_char_is_a_letter("institute") == False
assert check_if_last_char_is_a_letter("abc def") == False
assert check_if_last_char_is_a_letter('hello  there') == False
assert check_if_last_char_is_a_letter("@winning") == False
assert check_if_last_char_is_a_letter("winning") == False
assert check_if_last_char_is_a_letter("winner@") == False
assert check_if_last_char_is_a_letter("winner&") == False
assert check_if_last_char_is_a_letter("winning@.com") == False
assert check_if_last_char_is_a_letter("winner1") == False
assert check_if_last_char_is_a_letter("winner") == False
assert check_if_last_char_is_a_letter("@winner") == False
assert check_if_last_char_is_a_letter('Equal') == False
assert check_if_last_char_is_a_letter("") is False
assert check_if_last_char_is_a_letter("wrong") is False
assert check_if_last_char_is_a_letter("invalid!") is False
assert check_if_last_char_is_a_letter("1") is False
assert check_if_last_char_is_a_letter("{}") is False
assert False == check_if_last_char_is_a_letter("GeeksQuiz")
assert False == check_if_last_char_is_a_letter("Hi, my name is Alex!")
assert check_if_last_char_is_a_letter("hi") == False
assert check_if_last_char_is_a_letter("wow") == False
assert check_if_last_char_is_a_letter("banana.") == False
assert check_if_last_char_is_a_letter("banana") == False
assert check_if_last_char_is_a_letter('My favourite number is 7') == False
assert check_if_last_char_is_a_letter('Good morning!') == False
assert check_if_last_char_is_a_letter('6 a') == True
assert check_if_last_char_is_a_letter('f.bar') == False
assert check_if_last_char_is_a_letter("Well done!") == False
assert check_if_last_char_is_a_letter("I feel good!") == False
assert check_if_last_char_is_a_letter("I am good!") == False
assert check_if_last_char_is_a_letter('aa') == False
assert check_if_last_char_is_a_letter('^$') == False
assert check_if_last_char_is_a_letter('a-') == False
assert check_if_last_char_is_a_letter("!!!!!!!1") == False
assert check_if_last_char_is_a_letter("konrad123") == False
assert check_if_last_char_is_a_letter("abcd e") == True
assert check_if_last_char_is_a_letter("abcde") == False
assert check_if_last_char_is_a_letter("1 !@#$%^&*()") == False
assert False == check_if_last_char_is_a_letter("hey there!")
assert False == check_if_last_char_is_a_letter("what's up?")
assert check_if_last_char_is_a_letter('dododo') == False
assert check_if_last_char_is_a_letter('the quick brown fox jumped over the lazy dog') == False
assert check_if_last_char_is_a_letter('true') == False
assert check_if_last_char_is_a_letter("  ") == False
assert check_if_last_char_is_a_letter("Udacity") == False
assert check_if_last_char_is_a_letter('This is another simple sentence.') == False
assert check_if_last_char_is_a_letter('....This is a simple sentence.') == False
assert check_if_last_char_is_a_letter('Let’s go to the park.') == False
assert check_if_last_char_is_a_letter('?This is a simple sentence.') == False
assert check_if_last_char_is_a_letter('!@#$%^&*()_+') == False
assert check_if_last_char_is_a_letter('This is a simple sentence') == False
assert False == check_if_last_char_is_a_letter("Hello ...")
assert False == check_if_last_char_is_a_letter("Hello")
assert check_if_last_char_is_a_letter("but I'm still trying") == False
assert check_if_last_char_is_a_letter("to make things easier") == False
assert check_if_last_char_is_a_letter("It has to work") == False
assert check_if_last_char_is_a_letter("or maybe it will") == False
assert check_if_last_char_is_a_letter("but I know it's not true") == False
assert False == check_if_last_char_is_a_letter("hello world!.")
assert False == check_if_last_char_is_a_letter("hello world!...DA")
assert check_if_last_char_is_a_letter("hello world!") == False
assert check_if_last_char_is_a_letter("ba!") == False
assert check_if_last_char_is_a_letter("!b") == False
assert check_if_last_char_is_a_letter("!!a") == False
assert check_if_last_char_is_a_letter("Hi there!") == False
assert check_if_last_char_is_a_letter("Oh! Hi?") == False
assert False == check_if_last_char_is_a_letter("Hello world!")
assert False == check_if_last_char_is_a_letter("What? #")
assert False == check_if_last_char_is_a_letter("What? #1")
assert check_if_last_char_is_a_letter("hello, world ") == False
assert check_if_last_char_is_a_letter("hello, world.") == False
assert check_if_last_char_is_a_letter("abc.d") == False
assert check_if_last_char_is_a_letter("abc. def") == False
assert check_if_last_char_is_a_letter('  abc') == False
assert check_if_last_char_is_a_letter('Have a great day!') == False
assert check_if_last_char_is_a_letter('Trying out new features') == False
assert check_if_last_char_is_a_letter('Life is but a dream') == False
assert False == check_if_last_char_is_a_letter('abc? ')
assert False == check_if_last_char_is_a_letter('abcD?')
assert False == check_if_last_char_is_a_letter('abcD?e')
assert False == check_if_last_char_is_a_letter('abcD?e ')
assert False == check_if_last_char_is_a_letter('abcD?e @')
assert False == check_if_last_char_is_a_letter('abcD?e,')
assert False == check_if_last_char_is_a_letter('@')
assert False == check_if_last_char_is_a_letter(' ')
assert False == check_if_last_char_is_a_letter('')
assert check_if_last_char_is_a_letter("12:00") == False
assert check_if_last_char_is_a_letter("one, two, three") == False
assert check_if_last_char_is_a_letter('abc? def.') == False
assert check_if_last_char_is_a_letter('abcdefg') == False
assert check_if_last_char_is_a_letter("8") == False
assert check_if_last_char_is_a_letter("US") == False
assert check_if_last_char_is_a_letter("abc . c") == True
assert check_if_last_char_is_a_letter("abc . c ") == False
assert check_if_last_char_is_a_letter("Hello") == False
assert check_if_last_char_is_a_letter("Hello there") == False
assert check_if_last_char_is_a_letter('This is a string') == False
assert check_if_last_char_is_a_letter('Click the button') == False
assert check_if_last_char_is_a_letter('Welcome to ERS!') == False
assert check_if_last_char_is_a_letter('Hello!') == False
assert check_if_last_char_is_a_letter("hello_world!") == False
assert check_if_last_char_is_a_letter("hello-world!") == False
assert check_if_last_char_is_a_letter("hello.world!") == False
assert check_if_last_char_is_a_letter("hello;world!") == False
assert check_if_last_char_is_a_letter("hello,world!") == False
assert check_if_last_char_is_a_letter("hello?world!") == False
assert check_if_last_char_is_a_letter("hello'world!") == False
assert check_if_last_char_is_a_letter('hello world!?') == False
assert check_if_last_char_is_a_letter("This is a sentence") == False
assert check_if_last_char_is_a_letter("Hello World!") == False
assert check_if_last_char_is_a_letter("Hello World!?!?!") == False
assert check_if_last_char_is_a_letter("Hello World!?!?!!?!?!?!?!?!?!?!") == False
assert check_if_last_char_is_a_letter("hello!.") == False
assert check_if_last_char_is_a_letter("hello world. goodbye") == False
assert check_if_last_char_is_a_letter("hello world. ") == False
