
def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    if len(word) < 3:
        return " "

    vowels = {"a", "e", "i", "o", "u", "A", "E", 'O', 'U', 'I'}
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            if (word[i+1] not in vowels) and (word[i-1] not in vowels):
                return word[i]
    return " "
assert "i" == get_closest_vowel("chime")
assert "" == get_closest_vowel("aisle")
assert get_closest_vowel("btw") == ""
assert get_closest_vowel("tfbb") == ""
assert get_closest_vowel("fdfdf") == ""
assert get_closest_vowel("b") == ""
assert get_closest_vowel("") == ""
assert get_closest_vowel("zgdzdwzrwz") == ""
assert get_closest_vowel("A") == ""
assert get_closest_vowel("Tibor") == "o"
assert get_closest_vowel("t") == ""
assert get_closest_vowel("tT") == ""
assert get_closest_vowel("aa") == ""
assert get_closest_vowel("bBbB") == ""
assert get_closest_vowel("Bb") == ""
assert get_closest_vowel("TatjanaT") == "a"
assert get_closest_vowel("wqcjm") == ""
assert get_closest_vowel("musa") == "u"
assert get_closest_vowel("alih") == "i"
assert get_closest_vowel("habib") == "i"
assert get_closest_vowel("as") == ""
assert '' == get_closest_vowel('Woooo')
assert '' == get_closest_vowel('bckwrm')
assert "" == get_closest_vowel("fff")
assert "" == get_closest_vowel("ie")
assert "" == get_closest_vowel("ae")
assert "" == get_closest_vowel("i")
assert "" == get_closest_vowel("a")
assert "" == get_closest_vowel("")
assert get_closest_vowel("abc") == ""
assert get_closest_vowel("flow") == "o"
assert get_closest_vowel("hello") == "e"
assert get_closest_vowel("dismantle") == "a"
assert get_closest_vowel("ln") == ""
assert get_closest_vowel("ry") == ""
assert get_closest_vowel("azxcvbnm") == ""
assert get_closest_vowel("qwert") == "e"
assert get_closest_vowel("mnbvcxz") == ""
assert get_closest_vowel("mimipipim") == "i"
assert "e" == get_closest_vowel("Hacker")
assert "u" == get_closest_vowel("Puggo")
assert "o" == get_closest_vowel("code")
assert "a" == get_closest_vowel("car")
assert get_closest_vowel("w") == ""
assert get_closest_vowel("orange") == "a", "Failed on orange"
assert get_closest_vowel("a") == "", "Failed on a"
assert get_closest_vowel("z") == "", "Failed on z"
assert get_closest_vowel("b") == "", "Failed on b"
assert get_closest_vowel("abcde") == "", "Failed on abcde"
assert get_closest_vowel("abcdE") == "", "Failed on abcdE"
assert get_closest_vowel("abcdEA") == "", "Failed on abcdEA"
assert get_closest_vowel("stol") == "o"
assert get_closest_vowel("Stol") == "o"
assert get_closest_vowel("srtol") == "o"
assert get_closest_vowel("sTol") == "o"
assert get_closest_vowel("sTolme") == "o"
assert get_closest_vowel("jstol") == "o"
assert get_closest_vowel("jstolm") == "o"
assert get_closest_vowel("jjstol") == "o"
assert get_closest_vowel("jjsTol") == "o"
assert get_closest_vowel("jjsTolm") == "o"
assert get_closest_vowel("jjsTolmm") == "o"
assert get_closest_vowel("jjstolmm") == "o"
assert get_closest_vowel("Hello") == "e"
assert get_closest_vowel("hannah") == "a"
assert get_closest_vowel("some") == "o"
assert get_closest_vowel("B") == ""
assert get_closest_vowel("br") == ""
assert get_closest_vowel("hecljn") == "e"
assert get_closest_vowel("simplest") == "e"
assert get_closest_vowel("sore") == "o"
assert get_closest_vowel("boy") == "o"
assert get_closest_vowel("ee") == ""
assert get_closest_vowel("ii") == ""
assert get_closest_vowel("oo") == ""
assert get_closest_vowel("uu") == ""
assert get_closest_vowel("MM") == ""
assert get_closest_vowel("woooAooAoowAw") == "A"
assert get_closest_vowel("woooAooAoowAwAw") == "A"
assert get_closest_vowel("woooAooAoowAwAwAw") == "A"
assert "" == get_closest_vowel("xr")
assert get_closest_vowel("asdfgh") == ""
assert get_closest_vowel("a") == ""
assert get_closest_vowel("ae") == ""
assert get_closest_vowel("h") == ""
assert get_closest_vowel("hewwo") == "e"
assert get_closest_vowel("aeiou") == ""
assert get_closest_vowel("aaaaa") == ""
assert get_closest_vowel("bcd") == ""
assert get_closest_vowel("bab") == "a"
assert '' == get_closest_vowel('baa')
assert '' == get_closest_vowel('bbb')
assert '' == get_closest_vowel('aeiou')
assert '' == get_closest_vowel('')
assert get_closest_vowel("scary") == "a"
assert get_closest_vowel("peter") == "e"
assert get_closest_vowel("fr") == ""
assert get_closest_vowel("grrr") == ""
assert get_closest_vowel("star") == "a"
assert get_closest_vowel("stare") == "a"
assert get_closest_vowel("starer") == "e"
assert get_closest_vowel("Sphinx") == "i"
assert get_closest_vowel("ok") == ""
assert get_closest_vowel("python") == "o"
assert get_closest_vowel("function") == "u"
assert get_closest_vowel("teat") == ""
assert get_closest_vowel("lyk") == ""
assert get_closest_vowel("notebbok") == "o"
assert get_closest_vowel("notebbbok") == "o"
assert get_closest_vowel("book") == ""
assert get_closest_vowel("bbb") == ""
assert get_closest_vowel("at") == ""
assert get_closest_vowel("zebra") == "e"
assert get_closest_vowel("e") == ""
assert get_closest_vowel("i") == ""
assert get_closest_vowel("o") == ""
assert get_closest_vowel("u") == ""
assert get_closest_vowel("y") == ""
assert "" == get_closest_vowel("z")
assert get_closest_vowel("aaa") == ""
assert get_closest_vowel("TtT") == ""
assert "" == get_closest_vowel("coumbe"), "Wrong answer"
assert "" == get_closest_vowel("gg"), "Wrong answer"
assert "" == get_closest_vowel("ggggy"), "Wrong answer"
assert "" == get_closest_vowel("gggggg"), "Wrong answer"
assert "" == get_closest_vowel("eou"), "Wrong answer"
assert "" == get_closest_vowel("yk"), "Wrong answer"
assert "" == get_closest_vowel("mbe"), "Wrong answer"
assert "" == get_closest_vowel("gqbv"), "Wrong answer"
assert get_closest_vowel("Zealousness") == "e"
assert get_closest_vowel("COCK") == "O"
assert get_closest_vowel("script") == "i"
assert get_closest_vowel("why") == ""
assert get_closest_vowel("No") == ""
assert get_closest_vowel("cdd") == ""
assert get_closest_vowel("rrd") == ""
assert get_closest_vowel("tft") == ""
assert get_closest_vowel("Pkmpshlet") == "e"
assert get_closest_vowel("Pmpshlt") == ""
assert get_closest_vowel("in") == ""
assert get_closest_vowel("CtC") == ""
assert get_closest_vowel("ab") == ""
assert get_closest_vowel("abec") == "e"
assert get_closest_vowel("helo") == "e"
assert get_closest_vowel("Word") == "o"
assert get_closest_vowel("Python") == "o"
assert get_closest_vowel("Sai Gon") == "o"
assert get_closest_vowel("slap") == "a"
assert get_closest_vowel("snap") == "a"
assert get_closest_vowel("lonely") == "e"
assert get_closest_vowel("slut") == "u"
assert get_closest_vowel("crap") == "a"
assert get_closest_vowel("crash") == "a"
assert get_closest_vowel("crusher") == "e"
assert get_closest_vowel("trash") == "a"
assert get_closest_vowel("ac") == ""
assert get_closest_vowel("hhe") == ""
assert get_closest_vowel("no") == ""
assert get_closest_vowel("pb") == ""
assert get_closest_vowel("xcb") == ""
assert get_closest_vowel("xab") == "a"
assert get_closest_vowel("one") == ""
assert get_closest_vowel("dog") == "o"
assert get_closest_vowel("cat") == "a"
assert get_closest_vowel("you") == ""
assert 'e' == get_closest_vowel('mnfkebf')
assert 'i' == get_closest_vowel('bfid')
assert 'o' == get_closest_vowel('fqfoqn')
assert 'a' == get_closest_vowel('fqfoqan')
assert get_closest_vowel("omg") == ""
assert get_closest_vowel("pythons") == "o"
assert get_closest_vowel("fhtagn") == "a"
assert get_closest_vowel("jelly") == "e"
assert '' == get_closest_vowel('bbrrkkk')
assert get_closest_vowel("vow") == "o"
assert get_closest_vowel("university") == "i"
assert get_closest_vowel("nthu") == ""
assert get_closest_vowel("ntu") == ""
assert get_closest_vowel("nt") == ""
assert get_closest_vowel("aabbc") == ""
assert get_closest_vowel("hotel") == "e"
assert get_closest_vowel("reword") == "o"
assert get_closest_vowel("Y") == ""
assert get_closest_vowel("tb") == "", "There is no vowel between 2 consonants from the right"
assert get_closest_vowel("") == "", "Please input non-empty string"
assert get_closest_vowel("aoiou") == ""
assert get_closest_vowel("aiou") == ""
assert get_closest_vowel("bac") == "a", "Word contains only one vowel"
assert get_closest_vowel("brrrr") == ""
assert get_closest_vowel("smile") == "i"
assert get_closest_vowel("sssss") == ""
assert get_closest_vowel("fnb") == ""
assert get_closest_vowel("it") == ""
assert "" == get_closest_vowel("e")
assert "" == get_closest_vowel("o")
assert "" == get_closest_vowel("u")
assert "" == get_closest_vowel("AEIOU")
assert "" == get_closest_vowel("qwrt")
assert get_closest_vowel("hallo") == "a"
assert get_closest_vowel("hanako") == "a"
assert get_closest_vowel("s") == ""
assert get_closest_vowel("zbr") == ""
assert get_closest_vowel("abcdefg") == "e"
assert get_closest_vowel("I love") == "o"
assert get_closest_vowel("aLongwordwithintheword") == "o"
assert get_closest_vowel("bb") == ""
assert get_closest_vowel("Bbb") == ""
assert get_closest_vowel("zzz") == ""
assert get_closest_vowel("zoo") == ""
assert get_closest_vowel("sdfghjk") == ""
assert get_closest_vowel("strength") == "e"
assert get_closest_vowel("c") == ""
assert get_closest_vowel("cbeffff") == "e"
assert get_closest_vowel("aab") == ""
assert get_closest_vowel("QQQQQQQQQQ") == ""
assert get_closest_vowel("WasItADatEordidISayDat") == "a"
assert get_closest_vowel("AF") == ""
assert "" == get_closest_vowel("sdfgsdfgrtyuiii")
assert get_closest_vowel("cvb") == ""
assert get_closest_vowel("cvc") == ""
assert get_closest_vowel("vc") == ""
assert get_closest_vowel("cv") == ""
assert "o" == get_closest_vowel("show")
assert "i" == get_closest_vowel("cosmic")
assert "a" == get_closest_vowel("thrash")
assert "" == get_closest_vowel("st")
assert "" == get_closest_vowel("b")
assert "" == get_closest_vowel("aa")
assert get_closest_vowel("z") == ""
assert get_closest_vowel("sc") == ""
assert get_closest_vowel("re") == ""
assert get_closest_vowel("wfxaz") == "a"
assert get_closest_vowel("tet") == "e"
assert get_closest_vowel("xez") == "e"
assert get_closest_vowel("hc") == ""
assert get_closest_vowel("colon") == "o"
assert get_closest_vowel("bac") == "a"
assert get_closest_vowel("bbac") == "a"
assert get_closest_vowel("abcdeg") == "e"
assert get_closest_vowel("gym") == ""
assert get_closest_vowel("child") == "i"
assert get_closest_vowel("cycling") == "i"
assert get_closest_vowel("computer") == "e"
assert get_closest_vowel("geometry") == "e"
assert get_closest_vowel("homework") == "o"
assert get_closest_vowel("housework") == "o"
assert get_closest_vowel("Daddy") == "a"
assert get_closest_vowel("amir") == "i"
assert get_closest_vowel("HeLlo") == "e"
assert get_closest_vowel("la") == ""
assert get_closest_vowel("word") == "o"
assert get_closest_vowel("bcdfg") == ""
assert get_closest_vowel("pech") == "e"
assert get_closest_vowel("wtf") == ""
assert get_closest_vowel("bird") == "i"
assert get_closest_vowel("aaeiou") == ""
assert get_closest_vowel("tony") == "o"
assert get_closest_vowel("bcdacab") == "a"
assert get_closest_vowel("bcdbeb") == "e"
assert get_closest_vowel("tESt") == "E", "get_closest_vowel failed test 3"
assert get_closest_vowel("trt") == ""
assert get_closest_vowel("nose") == "o"
assert get_closest_vowel("darts") == "a"
assert get_closest_vowel("bij") == "i"
assert get_closest_vowel("kort") == "o"
assert get_closest_vowel("rt") == ""
assert get_closest_vowel("we") == ""
assert get_closest_vowel("hh") == ""
assert get_closest_vowel("jkll") == ""
assert get_closest_vowel("asd") == ""
assert get_closest_vowel("zjk") == ""
assert get_closest_vowel("dd") == ""
assert ('e' == get_closest_vowel('abecda') )
assert ('i' == get_closest_vowel('abecida') )
assert ('i' == get_closest_vowel('abecidIa') )
assert ('o' == get_closest_vowel('abecodia') )
assert ('o' == get_closest_vowel('abecodiOa') )
assert ('u' == get_closest_vowel('abecudia') )
assert ('u' == get_closest_vowel('abecudIUa') )
assert "" == get_closest_vowel("te")
assert get_closest_vowel("zit") == "i"
assert get_closest_vowel("zazz") == "a"
assert get_closest_vowel("example") == "a"
assert get_closest_vowel("labs") == "a"
assert get_closest_vowel("go") == ""
