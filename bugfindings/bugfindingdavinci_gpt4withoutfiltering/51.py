

def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u", "w", "y"]])
assert remove_vowels('hello') == 'hll'
assert remove_vowels('how are you') == 'hw r y'
assert remove_vowels("hello") == "hll"
assert remove_vowels("Funny") == "Fnny"
assert remove_vowels("Cool") == "Cl"
assert remove_vowels("Computer Science") == "Cmptr Scnc"
assert remove_vowels("a") == ""
assert remove_vowels("e") == ""
assert remove_vowels("i") == ""
assert remove_vowels("o") == ""
assert remove_vowels("u") == ""
assert "PyMC3" == remove_vowels("PyMC3")
assert "PyMC" == remove_vowels("PyMC")
assert "1mC" == remove_vowels("1mC")
assert "PyM3" == remove_vowels("PyM3")
assert remove_vowels("") == ""
assert remove_vowels("aeiou") == ""
assert remove_vowels("HERE ARE MY HIDDEN VOWELS!") == "HR R MY HDDN VWLS!"
assert remove_vowels("here are my hidden vowels!") == "hr r my hddn vwls!"
assert remove_vowels("How are you doing?") == "Hw r y dng?"
assert remove_vowels("Ala ma kota") == "l m kt"
assert remove_vowels('hey man') == 'hy mn'
assert remove_vowels('hey man nice to meet you') == 'hy mn nc t mt y'
assert remove_vowels("goodbye") == "gdby"
assert remove_vowels("b") == "b"
assert remove_vowels("bcd") == "bcd"
assert remove_vowels("aeiouaeiou") == ""
assert remove_vowels("aeiouAEIOUaeiou") == ""
assert remove_vowels('I am going to school!') == ' m gng t schl!'
assert remove_vowels("aAbEefIijOopUus") == "bfjps"
assert remove_vowels('HELLO WORLD') == 'HLL WRLD'
assert remove_vowels('aloha world') == 'lh wrld'
assert remove_vowels('The Book of Mormon') == 'Th Bk f Mrmn'
assert remove_vowels('HI THERE!') == 'H THR!'
assert remove_vowels("You are one good man in bad place") == "Y r n gd mn n bd plc"
assert remove_vowels('soap') == 'sp'
assert remove_vowels('shampoo') == 'shmp'
assert remove_vowels('String') == 'Strng'
assert remove_vowels('Banana') == 'Bnn'
assert remove_vowels('Test') == 'Tst'
assert remove_vowels('Good') == 'Gd'
assert remove_vowels("breakfasts") == "brkfsts"
assert remove_vowels("beds") == "bds"
assert remove_vowels("hello world") == "hll wrld"
assert remove_vowels("samar") == "smr"
assert remove_vowels('Ritish') == 'Rtsh'
assert remove_vowels('aCe') == 'C'
assert remove_vowels('aeoiu') == ''
assert remove_vowels("World") == "Wrld"
assert remove_vowels("This is a sentence.") == "Ths s  sntnc."
assert remove_vowels("world") == "wrld"
assert remove_vowels('Kolya') == 'Kly'
assert remove_vowels('Katya') == 'Kty'
assert remove_vowels("aaaeeeiooouuuAEEEIOOOUUU") == ""
assert remove_vowels("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "bcdfghjklmnpqrstvwxyz1234567890BCDFGHJKLMNPQRSTVWXYZ"
assert remove_vowels("evangeliou") == "vngl"
assert remove_vowels("Hello world") == "Hll wrld"
assert remove_vowels("Python") == "Pythn"
assert remove_vowels("Github") == "Gthb"
assert remove_vowels("What is your name?") == "Wht s yr nm?"
assert remove_vowels("How are you today?") == "Hw r y tdy?"
assert remove_vowels("I love you") == " lv y"
assert remove_vowels("this is my sentence") == "ths s my sntnc"
assert remove_vowels("123-#this is my sentence") == "123-#ths s my sntnc"
assert remove_vowels("Hello") == "Hll"
assert remove_vowels("Goodbye") == "Gdby"
assert remove_vowels('I like Python') == ' lk Pythn'
assert remove_vowels('aeiou') == ''
assert remove_vowels("abcdefghijklmnopqrstuvwxyz") == "bcdfghjklmnpqrstvwxyz"
assert remove_vowels("cs") == "cs"
assert remove_vowels("computer science") == "cmptr scnc"
assert remove_vowels('gym') == 'gym'
assert remove_vowels('fun') == 'fn'
assert remove_vowels("Happy Thanksgiving to all--even the haters and losers!") == 'Hppy Thnksgvng t ll--vn th htrs nd lsrs!'
assert remove_vowels('foo') == 'f'
assert remove_vowels('foobar') == 'fbr'
assert remove_vowels("computer") == "cmptr"
assert remove_vowels("AaBbCc") == "BbCc"
assert remove_vowels("Hello World!") == "Hll Wrld!"
assert remove_vowels("BIG DATA") == "BG DT"
assert remove_vowels('b') == 'b'
assert remove_vowels('abc') == 'bc'
assert remove_vowels('bacd') == 'bcd'
assert remove_vowels('bacdef') == 'bcdf'
assert remove_vowels('bacdEf') == 'bcdf'
assert remove_vowels('bacdeEf') == 'bcdf'
assert remove_vowels('bacdefE') == 'bcdf'
assert remove_vowels('bacdEfE') == 'bcdf'
assert remove_vowels('bacdeEfE') == 'bcdf'
assert remove_vowels('bcdf') == 'bcdf'
assert remove_vowels('bcdfE') == 'bcdf'
assert remove_vowels('bcdeEf') == 'bcdf'
assert remove_vowels('bcdeEfE') == 'bcdf'
assert remove_vowels('bcdefE') == 'bcdf'
assert remove_vowels('This is a test') == 'Ths s  tst'
assert remove_vowels('I am a student from France') == ' m  stdnt frm Frnc'
assert remove_vowels('hello world!') == 'hll wrld!'
assert remove_vowels('hello world!?') == 'hll wrld!?'
assert remove_vowels('hello world!?&^%') == 'hll wrld!?&^%'
assert remove_vowels('1234') == '1234'
assert remove_vowels("ab") == "b"
assert remove_vowels("bcdaeiou") == "bcd"
assert remove_vowels("abcdaeiou") == "bcd"
assert remove_vowels("codewars") == "cdwrs"
assert remove_vowels("AeoU") == ""
assert remove_vowels("I love Python") == " lv Pythn"
assert remove_vowels("python") == "pythn"
assert remove_vowels("This is a test") == "Ths s  tst"
assert remove_vowels('AEIOU') == ''
assert remove_vowels('ruby') == 'rby'
assert remove_vowels('tata') == 'tt'
assert remove_vowels('kaka') == 'kk'
assert remove_vowels('sasa') == 'ss'
assert remove_vowels('baba') == 'bb'
assert remove_vowels('yaya') == 'yy'
assert remove_vowels('dada') == 'dd'
assert remove_vowels('papa') == 'pp'
assert remove_vowels('mimi') == 'mm'
assert remove_vowels('nana') == 'nn'
assert remove_vowels('lolo') == 'll'
assert remove_vowels('coco') == 'cc'
assert remove_vowels('toto') == 'tt'
assert remove_vowels('momo') == 'mm'
assert remove_vowels('gogo') == 'gg'
assert remove_vowels('soso') == 'ss'
assert remove_vowels('lulu') == 'll'
assert remove_vowels('bobo') == 'bb'
assert remove_vowels('wewe') == 'ww'
assert remove_vowels('fafa') == 'ff'
assert remove_vowels("aaa bbb ccc") == " bbb ccc"
assert remove_vowels("this is my test") == "ths s my tst"
assert remove_vowels("word") == "wrd"
assert remove_vowels("aeiouAEIOU") == ""
assert remove_vowels("gym") == "gym"
assert remove_vowels("elaborate") == "lbrt"
assert remove_vowels("I") == ""
assert remove_vowels('I am a student') == ' m  stdnt'
assert remove_vowels("bye") == "by"
assert remove_vowels("compsci") == "cmpsc"
assert remove_vowels('I love Python') == ' lv Pythn'
assert remove_vowels('Prospect Ave.') == 'Prspct v.'
assert remove_vowels('What do you want to do today?') == 'Wht d y wnt t d tdy?'
assert remove_vowels("baz") == "bz"
assert remove_vowels('-bcd-fgh-jklmn-pqrst-vwxyz') == '-bcd-fgh-jklmn-pqrst-vwxyz'
assert remove_vowels('aieou') == ''
assert remove_vowels('AIEOU') == ''
assert remove_vowels('A b Cd Ef') == ' b Cd f'
assert remove_vowels("welcome") == "wlcm"
assert remove_vowels("tatyana") == "ttyn"
assert remove_vowels("hahaha") == "hhh"
assert remove_vowels("fun") == "fn"
assert remove_vowels("number") == "nmbr"
assert remove_vowels("testing") == "tstng"
assert remove_vowels("programming") == "prgrmmng"
assert remove_vowels("hello") == "hll", "Failed to remove vowels"
assert remove_vowels("bbb") == "bbb", "Failed to remove vowels"
assert remove_vowels('banana') == 'bnn'
assert remove_vowels('python') == 'pythn'
assert remove_vowels('welcome') == 'wlcm'
assert remove_vowels("poker") == "pkr"
assert remove_vowels('How are you?') == 'Hw r y?'
assert remove_vowels('Hello world!') == 'Hll wrld!'
assert remove_vowels('programmeren') == 'prgrmmrn'
assert remove_vowels('gast') == 'gst'
assert remove_vowels('koe') == 'k'
assert remove_vowels('Mathematics') == 'Mthmtcs'
assert remove_vowels("cat") == "ct"
assert remove_vowels("a1b2c3") == "1b2c3"
assert remove_vowels("testing, 1, 2, 3") == "tstng, 1, 2, 3"
assert remove_vowels("abcdefg") == "bcdfg"
assert remove_vowels("ABCDEFG") == "BCDFG"
assert remove_vowels('Hello World!') == 'Hll Wrld!'
assert remove_vowels('What is going on here') == 'Wht s gng n hr'
assert remove_vowels('aeiou') == '', 'test 2'
assert remove_vowels('nshafee') == 'nshf', 'test 3'
assert remove_vowels('asdf') == 'sdf'
assert remove_vowels('cs502') == 'cs502'
assert remove_vowels('aeiouAEIOU') == ''
assert remove_vowels('Please do not enter') == 'Pls d nt ntr'
