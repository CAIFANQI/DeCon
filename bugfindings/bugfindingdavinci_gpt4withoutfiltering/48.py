

def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    for i in range(len(text)):
        if text[i] != text[len(text) - i]:
            return False
    return True
assert is_palindrome("kayak") == True
assert is_palindrome("kajak") == True
assert is_palindrome("kajakz") == False
assert is_palindrome("kajak ") == False
assert is_palindrome("") == True
assert is_palindrome("abab") is False
assert is_palindrome("tenet") is True
assert is_palindrome("banana") is False
assert is_palindrome("straw warts") is True
assert is_palindrome('abccba') == True
assert is_palindrome('abccbA') == False
assert is_palindrome('abc') == False
assert is_palindrome('madam') == True
assert is_palindrome('abba') == True
assert is_palindrome('racecar') == True
assert is_palindrome('dented') == False
assert is_palindrome('f') == True
assert is_palindrome('fo') == False
assert is_palindrome('aibohphobia') == True
assert is_palindrome('Live not on evil') == False
assert is_palindrome("abcba") == True
assert is_palindrome("abcd") == False
assert is_palindrome("a1b1b1a") == True
assert is_palindrome("abcde") == False
assert is_palindrome(" ") == True
assert is_palindrome("1") == True
assert is_palindrome('saippuakivikauppias') == True
assert is_palindrome('asdffdsa') == True
assert is_palindrome('a') == True
assert is_palindrome('') == True
assert is_palindrome('ab') == False
assert is_palindrome('Madam') == False
assert is_palindrome('mAdam') == False
assert is_palindrome('#Madam') == False
assert is_palindrome('Mada"m') == False
assert is_palindrome('a santa at NASA') == False
assert is_palindrome('Malayala') == False
assert is_palindrome("aaaaaa")
assert is_palindrome("racecar")
assert is_palindrome("")
assert not is_palindrome("aaab")
assert not is_palindrome("Python")
assert not is_palindrome("farvaz")
assert not is_palindrome("dsfsdfdsf")
assert not is_palindrome("asd")
assert not is_palindrome("asdasdqw")
assert is_palindrome("abcdefg") == False
assert is_palindrome("racecar") == True
assert is_palindrome("bobob") == True
assert is_palindrome("bobo") == False
assert is_palindrome("a") == True
assert is_palindrome("not") == False
assert is_palindrome("mom")
assert is_palindrome("wow")
assert is_palindrome("madam")
assert is_palindrome("level")
assert is_palindrome("rats live on no evil star")
assert is_palindrome("civic")
assert is_palindrome("alula")
assert is_palindrome("kayak")
assert is_palindrome("redivider")
assert is_palindrome("refer")
assert is_palindrome("deified")
assert is_palindrome("rotator")
assert is_palindrome("sagas")
assert is_palindrome("solos")
assert is_palindrome("sexes")
assert is_palindrome("abb") is False
assert is_palindrome("civic") is True
assert is_palindrome("racecar") is True
assert is_palindrome("") is True
assert is_palindrome("dude") is False
assert is_palindrome("agnesi") is False
assert is_palindrome("kayak") is True
assert is_palindrome("kayakk") is False
assert is_palindrome("kayakya") is False
assert is_palindrome('madman') == False
assert is_palindrome('a')
assert is_palindrome('absba')
assert not is_palindrome('normal')
assert not is_palindrome('Hello, Python!')
assert is_palindrome("abcba") is True
assert is_palindrome("abcd") is False
assert is_palindrome("Abba Zabba, you're my only friend") is False
assert is_palindrome("anna") is True
assert is_palindrome("walter") is False
assert is_palindrome("hannah") is True
assert is_palindrome("madam") is True
assert is_palindrome("level") is True
assert is_palindrome("noon") is True
assert is_palindrome("motor") == False
assert is_palindrome("walter") == False
assert is_palindrome('test') == False
assert is_palindrome('repaper') == True
assert is_palindrome('Able was I, ere I saw Paris!') == False
assert is_palindrome('Madam') is False
assert is_palindrome("racer") is False
assert is_palindrome("oOo") is True
assert is_palindrome("OoO") is True
assert is_palindrome("radarr") is False
assert is_palindrome("radar") is True
assert is_palindrome("madame") is False
assert is_palindrome("amanaplanacanalpandemonium") == False
assert is_palindrome('maam') == True
assert is_palindrome('civic') == True
assert is_palindrome('tacocat') == True
assert is_palindrome('123321') == True
assert is_palindrome('1234321') == True
assert is_palindrome('c') == True
assert is_palindrome('abbab') == False
assert is_palindrome("poop") is True
assert is_palindrome("poopie") is False
assert is_palindrome("a") == True, "Single letter"
assert is_palindrome("kayak") == True, "A palindrome"
assert is_palindrome("kayaks") == False, "Not a palindrome"
assert is_palindrome("1221") == True, "Starts with a number"
assert is_palindrome("some text") == False, "Not a palindrome"
assert is_palindrome("a")
assert is_palindrome("aasaa")
assert is_palindrome("abca") == False
assert is_palindrome("ana")
assert is_palindrome("radar")
assert is_palindrome("rotor")
assert is_palindrome("tattarrattat")
assert is_palindrome("banana") == False
assert is_palindrome("aa") == True
assert is_palindrome("aaron") == False
assert is_palindrome("radar") == True
assert is_palindrome("aaabbbccc") == False
assert is_palindrome("amanaplanacanalpanama") == True
assert is_palindrome("algorithm") == False
assert is_palindrome('greetings') == False
assert is_palindrome('1000000001')
assert is_palindrome('Fish hsif') == False
assert is_palindrome('pennep')
assert is_palindrome("lagerregal")
assert is_palindrome("malayalam")
assert is_palindrome("3111113")
assert is_palindrome(" ")
assert is_palindrome("  ")
assert is_palindrome(" a ")
assert is_palindrome(" a a ")
assert is_palindrome(" a  a ")
assert is_palindrome("  a  a  ")
assert is_palindrome("\t")
assert is_palindrome("\t\t")
assert is_palindrome("\t\t\t")
assert is_palindrome("\t\t\t\t")
assert is_palindrome("ab") == False
assert is_palindrome("abba") == True
assert is_palindrome("abcabcabc") == False
assert is_palindrome("abbaabba") == True
assert is_palindrome("ababba") == False
assert is_palindrome("abbabba") == True
assert is_palindrome("aba") == True
assert is_palindrome("z") == True
assert is_palindrome('abcba')
assert is_palindrome('abcdcba')
assert is_palindrome('abbc') == False
assert is_palindrome('abcdcb') == False
assert is_palindrome('abba')
assert is_palindrome('kayak')
assert is_palindrome('aibohphobia')
assert not is_palindrome('palindrome')
assert not is_palindrome('this is not a palindrome')
assert is_palindrome("aaaaaaa") == True
assert is_palindrome("abcdcba") == True
assert is_palindrome('acba') == False
assert not is_palindrome('random string')
assert is_palindrome('car') == False
assert is_palindrome('racecar')
assert is_palindrome('abcdeedcba')
assert is_palindrome('amanaplanacanalpandemonium') is False
assert is_palindrome('cdefghijk') is False
assert is_palindrome("foobar") == False
assert is_palindrome("aba")
assert is_palindrome("AaA")
assert is_palindrome("abab") == False
assert is_palindrome("madam") == True
assert is_palindrome("madame") == False
assert is_palindrome("abcdba") == False
assert is_palindrome("abb aa") is False
assert is_palindrome("a") is True
assert is_palindrome('kajak') == True
assert is_palindrome('kajak i łódka') == False
assert not is_palindrome("kajak..jak")
assert not is_palindrome("kajak..jaka")
assert not is_palindrome("kajak..jaka.")
assert not is_palindrome("kajak..jaka...")
assert is_palindrome("b") is True
assert is_palindrome('toyota') is False
assert is_palindrome("abba")
assert is_palindrome("x")
assert is_palindrome("anna")
assert is_palindrome("redder")
assert is_palindrome("6")
assert is_palindrome("-")
assert is_palindrome("aa") is True
assert is_palindrome("aba") is True
assert is_palindrome("abba") is True
assert is_palindrome("abca") is False
assert is_palindrome("saippuakauppias") is True
assert is_palindrome('abba ') == False
assert is_palindrome(' abba') == False
assert is_palindrome('madam i’m adam') == False
assert is_palindrome("no") == False
assert is_palindrome("no way!") == False
assert is_palindrome("tacocat") == True
assert is_palindrome("no!") == False
assert is_palindrome("apple") == False
assert is_palindrome("car") == False
assert is_palindrome("palindrome") == False
assert not is_palindrome("chewbacca")
assert not is_palindrome("banana")
assert is_palindrome("aaaaaaaaaaaaaaaaaaaaaa") == True
assert is_palindrome("abcb") == False
assert is_palindrome('abba bab') == False
assert is_palindrome('abbccbba') == True
assert is_palindrome('abbc cbba') == True
assert is_palindrome('abbba cbba') == False
assert is_palindrome('Abba cbba') == False
assert is_palindrome("abccba") is True
assert is_palindrome("ab") is False
assert is_palindrome("abc") is False
assert is_palindrome("abcdba") is False
assert is_palindrome('palindrome') == False
assert is_palindrome(" ") is True
assert is_palindrome("   ") is True
assert is_palindrome("abc") == False
assert is_palindrome("donut") == False
assert is_palindrome("civic") == True
assert is_palindrome("hey") == False
assert is_palindrome("dude") == False
assert is_palindrome("raccoon") == False
assert is_palindrome('civic')
assert is_palindrome('radar')
assert is_palindrome('rotor')
assert is_palindrome('anna')
assert is_palindrome('redder')
assert is_palindrome('madam')
assert is_palindrome('mom')
assert is_palindrome('noon')
assert is_palindrome('refer')
assert is_palindrome('101')
assert is_palindrome('deleveled')
assert is_palindrome('detartrated')
assert is_palindrome('dewed')
assert is_palindrome('evitative')
assert is_palindrome("yoy") == True
assert is_palindrome("abcabc") == False
assert is_palindrome('')
assert not is_palindrome('ab')
assert not is_palindrome('abca')
assert is_palindrome("aabbaa") is True
assert is_palindrome("ababa") is True
assert is_palindrome("abaab") is False
assert is_palindrome("aabba") is False
assert is_palindrome("aaaa") is True
assert is_palindrome("neveroddoreven") == True
assert is_palindrome("1234") == False
assert is_palindrome("123454321") == True
assert is_palindrome('abcdcba') == True
assert is_palindrome('abcd') == False
assert is_palindrome("abccba") == True
assert is_palindrome("abcda") == False
assert is_palindrome("abcdea") == False
assert is_palindrome("abcba ") == False
assert is_palindrome(" abcba") == False
assert is_palindrome(" ab cd ba ") == False
assert is_palindrome('level')
assert is_palindrome('wasitacaroracatisaw')
assert is_palindrome('alula')
assert is_palindrome('releveler')
assert is_palindrome('rotator')
assert is_palindrome('tenet')
assert is_palindrome('stats')
assert is_palindrome("peep")
assert is_palindrome("tacocat")
assert not is_palindrome("pineapple")
assert not is_palindrome("a nut for a jar of tuna")
assert is_palindrome('abccba')
assert not is_palindrome('abbac')
assert not is_palindrome('aabbac')
assert not is_palindrome(' aabbac')
assert not is_palindrome('aabbac ')
assert not is_palindrome('aabbac  ')
assert is_palindrome("abb") == False
assert is_palindrome("bbb") == True
assert is_palindrome("c") == True
assert is_palindrome("alma") == False, "alma is not a palindrome"
assert is_palindrome("alula") == True, "alula is a palindrome"
assert is_palindrome("anna") == True, "anna is a palindrome"
assert is_palindrome("notamatch") == False, "notamatch is not a palindrome"
assert is_palindrome("abccba")
assert is_palindrome("abcba")
assert not is_palindrome("random")
assert is_palindrome('night') == False
assert is_palindrome('12321') == True
assert is_palindrome('123212') == False
assert is_palindrome('abbccbba')
assert is_palindrome('abaaba')
assert is_palindrome('aaa')
assert not is_palindrome('abc')
assert not is_palindrome('abcbaa')
assert not is_palindrome('aacba')
assert not is_palindrome('bba')
assert not is_palindrome('ba')
assert not is_palindrome('aab')
assert not is_palindrome('aaba')
assert is_palindrome('bob') == True
assert is_palindrome('cat') == False
assert is_palindrome('fantastic') == False
assert is_palindrome('wasitacaroracatisaw') == True
assert is_palindrome('heh') == True
assert is_palindrome('he') == False
assert is_palindrome('banana') == False
assert is_palindrome('hannah') == True
assert is_palindrome('maxim') == False
assert is_palindrome('anna') == True
assert is_palindrome("Rise to vote sir") == False
assert is_palindrome("mom") == True
assert is_palindrome("hello") == False
assert is_palindrome("true") == False
assert is_palindrome("ab ba") == True
assert is_palindrome("ab_ba") == True
assert is_palindrome("ab+ba") == True
assert is_palindrome("9ab+ba9") == True
assert is_palindrome("race a car") == False
assert is_palindrome("race a car;") == False
assert is_palindrome("   ") == True
assert is_palindrome("  a  ") == True
assert is_palindrome("  abc  ") == False
assert is_palindrome("  ab ba  ") == True
assert is_palindrome(" ab ba ") == True
assert is_palindrome("a bb a") == True
