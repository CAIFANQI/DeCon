
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(len(b) - l + 1):
            if a[i:i+l] == pat[j:j+l]:
                return True
    return False
assert cycpattern_check('abcdabcd' , 'cdab') == True
assert cycpattern_check('abc' , 'cab') == True
assert cycpattern_check('abcd', 'cdab') == True, 'Test 2'
assert cycpattern_check('abcd', 'abcd') == True, 'Test 3'
assert cycpattern_check('abcd', 'bcda') == True, 'Test 4'
assert cycpattern_check('abcd', 'dabc') == True, 'Test 5'
assert cycpattern_check('abcd', 'abf') == False, 'Test 7'
assert cycpattern_check('AABAAB' , 'BAA')
assert cycpattern_check('AABAAB' , 'AAB')
assert cycpattern_check('AABAAB' , 'AABAAB')
assert not cycpattern_check('AABAAB' , 'ABABAB')
assert not cycpattern_check('AABAAB' , 'ABABABAAB')
assert cycpattern_check("amanaplanacanal" , "acanal") == True
assert cycpattern_check("amanaplanacanal" , "banana") == False
assert cycpattern_check("abcdabcdabcy" , "abcdabcy") == True
assert cycpattern_check("abcabxabcdabxabcdabcdabcy" , "abcdabcy") == True
assert cycpattern_check("abcabxabcdabxaabcdabcabxabcdabcdabcy" , "abcdabca") == True
assert cycpattern_check("abcabxabcdabxaabaabaaaabcdabxabcdabcdabcy" , "aabaabaaa") == True
assert cycpattern_check("abcd" , "abcd") == True, "Check your function"
assert cycpattern_check("abc" , "def") == False, "Check your function"
assert cycpattern_check("abcabc" , "cab") == True, "Check your function"
assert cycpattern_check("Naman" , "nam") == False
assert cycpattern_check("abcabcabcabc", "bca") == True
assert cycpattern_check("abcabcabcabc", "xyz") == False
assert cycpattern_check('abc' , 'cat') == False
assert cycpattern_check('abacd' , 'dabac') == True, 'Should be True'
assert cycpattern_check('abacd' , 'abccd') == False, 'Should be False'
assert cycpattern_check('abacd' , 'bacad') == False, 'Should be False'
assert cycpattern_check('abacd' , 'cdabb') == False, 'Should be False'
assert cycpattern_check('abacd' , 'acbba') == False, 'Should be False'
assert cycpattern_check('abacd' , 'cbdda') == False, 'Should be False'
assert cycpattern_check("abcabcabcabc", "cab") == True
assert cycpattern_check("adaacabacabacabacabacabacabacaba", "acb") == True
assert cycpattern_check("abcabcabcabc", "aaaaa") == False
assert cycpattern_check('niinni' , 'inn') == True
assert cycpattern_check('abcd' , 'caaa') == False
assert cycpattern_check("BANANA" , "NANA") == True , "wrong"
assert cycpattern_check("BANANA" , "ANA") == True , "wrong"
assert cycpattern_check("BANANA" , "NA") == True , "wrong"
assert cycpattern_check("BANANA" , "A") == True , "wrong"
assert cycpattern_check("BANANA" , "AAAA") == False , "wrong"
assert cycpattern_check("BANANA" , "ZZZZ") == False , "wrong"
assert cycpattern_check('adadad' , 'xada') == False
assert cycpattern_check('adadad' , 'adad') == True
assert cycpattern_check('adadad' , 'dad') == True
assert cycpattern_check('adadad' , 'd') == True
assert cycpattern_check('adadad' , 'ad') == True
assert cycpattern_check('adadad' , 'ada') == True
assert cycpattern_check('cdrtdr' , 'drt') == True
assert cycpattern_check('cdrtdr' , 'rt') == True
assert cycpattern_check('cdrtdr' , 't') == True
assert cycpattern_check('cdrtdr' , 'dr') == True
assert cycpattern_check('cdrtdr' , 'rd') == True
assert cycpattern_check('cdrtdr' , 'd') == True
assert cycpattern_check('cdrtdr' , 'cdr') == True
assert cycpattern_check('cdrtdr' , 'drt')
assert cycpattern_check("tangfantang", "fan") == True
assert cycpattern_check("tangfantang", "ang") == True
assert cycpattern_check("tangfantang", "tang") == True
assert cycpattern_check("tangfantang", "fanfan") == False
assert cycpattern_check("tangfantang", "angfan") == True
assert cycpattern_check("abca" , "ba") == True
assert cycpattern_check("abca" , "ab") == True
assert cycpattern_check("abca" , "abc") == True
assert cycpattern_check("abca" , "cab") == True
assert cycpattern_check("abca" , "bca") == True
assert cycpattern_check("abca" , "ac") == True
assert cycpattern_check("abca" , "cb") == True
assert cycpattern_check("abca" , "bc") == True
assert cycpattern_check("abca" , "ca") == True
assert cycpattern_check('abc', 'abcdabcabc') == False
assert cycpattern_check('abc', 'abcdabcd') == False
assert cycpattern_check('abc', 'abcdab') == False
assert cycpattern_check('Relation', 'tio') == True
assert cycpattern_check('Relation', 'tion') == True
assert cycpattern_check('Relation', 'ship') == False
assert cycpattern_check("aaaaa","aaaa")
assert cycpattern_check("abcdabcdabcdabcd","cdabcdab")
assert cycpattern_check("aaabaaabaaabaaab","abaaabaa")
assert cycpattern_check("aaabaaabaaabaaab","aaabaaab")
assert cycpattern_check("aaabaaabaaabaaab","aaabaa")
assert cycpattern_check("aaabaaabaaabaaab","aaab")
assert cycpattern_check("aabaabaabaabaaba","abaabaab")
assert cycpattern_check("abcdabcdabcdabcd","abcdabcd")
assert cycpattern_check("aaabaaabaaabaaab","aabaaaba")
assert cycpattern_check("abcabcabcabcabc","abcabcabc")
assert cycpattern_check("abcabcabcabcabc","bcabcabca")
assert cycpattern_check("abcabcabcabcabc","cabcabcab")
assert cycpattern_check("abcde" , "abced") == False
assert cycpattern_check("abc" , "cab") == True
assert cycpattern_check("abcde" , "c") == True
assert cycpattern_check("abcde" , "cd") == True
assert cycpattern_check("abcde" , "cdab") == True
assert cycpattern_check("abcde" , "x") == False
assert cycpattern_check("abaaac" , "bc") == False
assert cycpattern_check('abcdefgh' , 'efg')
assert cycpattern_check('abcdefgh' , 'cde')
assert cycpattern_check('abcdefgh' , 'defgh')
assert cycpattern_check('abcdefgh' , 'bcdefgh')
assert cycpattern_check('abcdefgh' , 'abcdefgh')
assert cycpattern_check('abcdefgh' , 'ab')
assert cycpattern_check('abcdefgh' , 'a')
assert cycpattern_check('abcdefgh' , 'gh')
assert cycpattern_check('abcdefgh' , 'g')
assert cycpattern_check('abcdefgh' , 'h')
assert cycpattern_check('abcdefgh' , 'bc')
assert cycpattern_check("xxyyzz" , "zyz") == True
assert cycpattern_check("xxyyzz" , "xxx") == False
assert cycpattern_check("xxyyzz" , "yyy") == False
assert cycpattern_check("xxyyzz" , "zzz") == False
assert cycpattern_check("laxdas","sasdas") == False
assert cycpattern_check("abcde", "cde") == True
assert cycpattern_check("abcde", "abcd") == True
assert cycpattern_check("abcde", "bce") == False
assert cycpattern_check("abcde", "xyz") == False
assert cycpattern_check("abcde", "cda") == False
assert cycpattern_check("spicy","icy") == True, "Wrong answer"
assert cycpattern_check("spicy","spy") == False, "Wrong answer"
assert cycpattern_check('abcdefgh' , 'defghabc') == True
assert cycpattern_check('abcdefgh' , 'eab') == False
assert cycpattern_check("1223344556" , "1223344556") == True , "Test case failed"
assert cycpattern_check("1223344556" , "5612233445") == True , "Test case failed"
assert cycpattern_check("1223344556" , "99") == False , "Test case failed"
assert cycpattern_check("1223344556" , "8888") == False , "Test case failed"
assert cycpattern_check("abcabcabcabc", "abcabcabc") == True, "Error in cycpattern_check"
assert cycpattern_check("abcabcabcabc", "abc") == True, "Error in cycpattern_check"
assert cycpattern_check("abcabcabcabc", "cab") == True, "Error in cycpattern_check"
assert cycpattern_check("cycpattern_check", "pattern") == True, "Error in cycpattern_check"
assert cycpattern_check("abcabcabcabc", "bcabcabc") == True, "Error in cycpattern_check"
assert cycpattern_check("abcabcabcabc", "bcabcabcab") == True, "Error in cycpattern_check"
assert cycpattern_check("abcabcabcabc", "bcabcabcabc") == True, "Error in cycpattern_check"
assert cycpattern_check("abcabcabcabc", "a") == True, "Error in cycpattern_check"
assert cycpattern_check("abcde" , "cdeab") == True
assert cycpattern_check('kabcdab' , 'abcd') == True
assert cycpattern_check('kabcdab' , 'dab') == True
assert cycpattern_check('kabcdab' , 'cdab') == True
assert cycpattern_check("yabzab" , "abz") == True
assert cycpattern_check("abzab" , "abz") == True
assert cycpattern_check("abcab" , "abca") == True
assert cycpattern_check("abcab" , "abab") == False
assert cycpattern_check("xyz" , "xy") == True
assert cycpattern_check("xyz" , "yx") == True
assert cycpattern_check("xyz" , "yzx") == True
assert cycpattern_check("xyz" , "zxy") == True
assert cycpattern_check('abcabcabcabc', 'cabc') == True
assert cycpattern_check('abcabcabcabc', 'abcabc') == True
assert cycpattern_check('abcabcabcabc', 'abcabcabcabc') == True
assert cycpattern_check('abcabcabcabc', 'abcabcabcabcabc') == False
assert cycpattern_check('abcabcabcabc', 'xyz') == False
assert cycpattern_check('abcde', 'abcde') == True, 'error 2'
assert cycpattern_check('abced', 'deabc') == False, 'error 3'
assert cycpattern_check('xyzabc' , 'abc') == True
assert cycpattern_check('abc' , 'abc') == True
assert cycpattern_check('abc' , 'bca') == True
assert cycpattern_check('abcd' , 'abc') == True
assert cycpattern_check('abcd' , 'cdab') == True
assert cycpattern_check('abcd' , 'dabc') == True
assert cycpattern_check('abcd' , 'bcda') == True
assert cycpattern_check('abcd' , 'abcd') == True
assert cycpattern_check('aaaaaa' , 'aaa') == True
assert cycpattern_check('aaaaaa' , 'a') == True
assert cycpattern_check('a' , 'a') == True
assert cycpattern_check('abcab' , 'abc') == True
assert cycpattern_check('abcab' , 'ab') == True
assert cycpattern_check("hellohi" , "llo") == True
assert cycpattern_check("hellohi" , "he") == True
assert cycpattern_check("hellohi" , "hel") == True
assert cycpattern_check("hellohi" , "llohi") == True
assert cycpattern_check("hellohi" , "lohi") == True
assert cycpattern_check("hellohi" , "ohi") == True
assert cycpattern_check("hellohi" , "hi") == True
assert cycpattern_check("hellohi" , "el") == True
assert cycpattern_check("hellohi" , "lo") == True
assert cycpattern_check('abxaba', 'ab') == True, 'Test 2'
assert cycpattern_check('kadak','kadak') == True
assert cycpattern_check('kadak','dakk') == False
assert cycpattern_check('kadak','kaa') == False
assert cycpattern_check('kadak','a') == True
assert cycpattern_check('kadak','add') == False
assert cycpattern_check('kadak','kkaad') == False
assert True == cycpattern_check('abdca', 'bd')
assert cycpattern_check('abcde','cdeab') == True , 'Test 2 Failed'
assert cycpattern_check('abcde','abced') == False , 'Test 3 Failed'
assert cycpattern_check("tech", "tech")
assert cycpattern_check("tech", "et")
assert cycpattern_check("tech", "ch")
assert cycpattern_check("tech", "te")
assert cycpattern_check("tech", "tec")
assert cycpattern_check('abcde', 'cdeb') == True
assert cycpattern_check('abcde', 'acb') == False
assert cycpattern_check("abcd", "abxcd") is False, "Wrong Result"
assert cycpattern_check("abcd", "xabxcd") is False, "Wrong Result"
assert cycpattern_check('abcde', 'bcdea') == True
assert cycpattern_check('abcde', 'cdea') == False
assert cycpattern_check('abcde', 'deab') == False
assert cycpattern_check('abcde', 'edcab') == False
assert cycpattern_check('abcde', 'abced') == False
assert cycpattern_check('abcde', 'abcdea') == False
assert cycpattern_check('abcde', 'abcdeab') == False
assert cycpattern_check('abcde', 'abcdeabc') == False
assert cycpattern_check("abxaba" , "aba") == True , "cycpattern_check: test 2 failed"
assert cycpattern_check("abxaba" , "abx") == True , "cycpattern_check: test 3 failed"
assert cycpattern_check("abxaba" , "ba") == True , "cycpattern_check: test 4 failed"
assert cycpattern_check("abxaba" , "xab") == True , "cycpattern_check: test 5 failed"
assert cycpattern_check("abxaba" , "xaba") == True , "cycpattern_check: test 6 failed"
assert cycpattern_check("abxaba" , "axab") == True , "cycpattern_check: test 7 failed"
assert cycpattern_check("abxaba" , "xabx") == False , "cycpattern_check: test 8 failed"
assert cycpattern_check("abcd" , "cdab") == True, "wrong answer"
assert cycpattern_check("abc" , "bdca") == False, "wrong answer"
assert cycpattern_check("abc" , "ca") == False, "wrong answer"
assert cycpattern_check("abxaba" , "ba") == True
assert cycpattern_check("abxaba" , "aba") == True
assert cycpattern_check("abxaba" , "xab") == True
assert cycpattern_check("abxaba" , "xaba") == True
assert cycpattern_check("abxaba" , "abax") == True
assert cycpattern_check("abxaba" , "abxa") == True
assert cycpattern_check("abxaba" , "baxa") == True
assert cycpattern_check("abxaba" , "xabx") == False
assert cycpattern_check("abxaba" , "abxabx") == False
assert cycpattern_check("abxaba" , "xabxab") == False
assert cycpattern_check("abxaba" , "xabxaba") == False
assert cycpattern_check("abxaba" , "xabxabax") == False
assert cycpattern_check('mpyagf', 'agfmpy')
assert cycpattern_check('mpyagf', 'mpyagf')
assert cycpattern_check('mpyagf', 'yagfmp')
assert cycpattern_check('mpyagf', 'gfmpya')
assert cycpattern_check('mpyagf', 'fmpyag')
assert cycpattern_check("abacabacabacabac", "acab")
assert cycpattern_check("abacabacabacabac", "baca")
assert cycpattern_check("abacabacabacabac", "abac")
assert cycpattern_check("abacabacabacabac", "abacabac")
assert cycpattern_check("abacabacabacabac", "cabacabacabac")
assert not cycpattern_check("abacabacabacabac", "cabacabacabacab")
assert not cycpattern_check("abacabacabacabac", "abacabacabacabaca")
assert cycpattern_check("aaabcd" , "bcd")
assert cycpattern_check("abcd" , "bcd")
assert cycpattern_check("abcdef" , "ef")
assert cycpattern_check("abcdef" , "def")
assert cycpattern_check("abcdef" , "fde")
assert cycpattern_check("abcdef" , "abc")
assert cycpattern_check("abcdef" , "abcdef")
assert cycpattern_check('Saravanan', 'avanan') == True
assert cycpattern_check('Saravanan', 'ava') == True
assert cycpattern_check('Saravanan', 'anavan') == True
assert cycpattern_check('Saravanan', 'sa') == False
assert cycpattern_check('Saravanan', 'avan') == True
assert cycpattern_check('SPONDYLOSIS', 'SPONLY') == False
assert cycpattern_check('PYTHON', 'TOLT') == False
assert cycpattern_check('CHALAZION', 'ALA') == True
assert cycpattern_check('CHALAZION', 'ALAS') == False
assert cycpattern_check('NEVUS', 'EU') == False
assert cycpattern_check('NEVUS', 'N') == True
assert cycpattern_check('SPHENOPALATINE', 'PALA') == True
assert cycpattern_check('SPHENOPALATINE', 'PALAS') == False
assert cycpattern_check('PALATINE', 'PALA') == True
assert cycpattern_check('PALATINE', 'PALAS') == False
assert cycpattern_check('PALATINE', 'PAL') == True
assert cycpattern_check("tomato" , "tom") == True
assert cycpattern_check("tomato" , "pot") == False
assert cycpattern_check("675454754" , "754") == True
assert cycpattern_check("675454754" , "475") == True
assert cycpattern_check("abcda","dabc") == True, "something is wrong"
assert cycpattern_check("aaaaa","aaa") == True, "something is wrong"
assert cycpattern_check("abcde","dabc") == True, "something is wrong"
assert cycpattern_check("abcdef", "def") == True
assert cycpattern_check("abcdef", "abc") == True
assert cycpattern_check("abcdef", "xyz") == False
assert cycpattern_check('aaaaa' , 'aaa')
assert cycpattern_check('abcabcabcabcabcabcabcabc' , 'cabcabcabc')
assert cycpattern_check("abcde", "abce") == False
assert cycpattern_check("abcde", "cabc") == False
assert cycpattern_check("abcde", "defg") == False
assert cycpattern_check("abcde", "1234") == False
assert cycpattern_check('abcdabcd' , 'cdabcdab') == True
assert cycpattern_check('abcdefgabcdefgabcdefg' , 'efgabcdabcdabcdabcd') == False
assert cycpattern_check('abcabcabcabcabcabcabc', 'ab') == True, 'test 2'
assert cycpattern_check('abcabcabcabcabcabcabc', 'ccc') == False, 'test 3'
assert cycpattern_check("cdeab", "abcde") == True, "Should be True"
assert cycpattern_check("abcde", "cde") == True, "Should be True"
assert cycpattern_check("abcde", "bcd") == True, "Should be True"
assert cycpattern_check("abcde", "ab") == True, "Should be True"
assert cycpattern_check("abcde", "abcde") == True, "Should be True"
assert cycpattern_check("abcde", "abcdef") == False, "Should be False"
assert cycpattern_check("cdeab", "abcdef") == False, "Should be False"
assert cycpattern_check("abcde", "def") == False, "Should be False"
assert cycpattern_check("abcde", "bde") == False, "Should be False"
assert cycpattern_check("abcde", "bdec") == False, "Should be False"
assert cycpattern_check('cabaa', 'baaa') == True
assert cycpattern_check('abaa', 'abaa') == True
assert cycpattern_check('abaa', 'baaa') == True
assert cycpattern_check('aaaa', 'abaa') == False
assert cycpattern_check('aaaa', 'baaa') == False
assert cycpattern_check('aaaa', 'aaaa') == True
assert cycpattern_check('abaa', 'aaaa') == False
assert cycpattern_check('abcabcabc', 'abcabc') == True
assert cycpattern_check('abcabcabc', 'cabcab') == True
assert cycpattern_check('abcabcabc', 'bcabca') == True
assert cycpattern_check('abcabcabc', 'abc') == True
assert cycpattern_check('abcabcabc', 'cab') == True
assert cycpattern_check('abcabcabc', 'bca') == True
assert cycpattern_check('abcabcabc', 'abcabcabc') == True
assert cycpattern_check("abcab","dca") == False
assert cycpattern_check("abcab","ab") == True
assert cycpattern_check("abcab","abcab") == True
assert cycpattern_check("abcab","cab") == True
assert cycpattern_check('happening' , 'king') == False , 'error3'
assert cycpattern_check('abcabcabcabc', 'bc') == True
assert cycpattern_check('AB','A') == True
assert cycpattern_check('ABAB','BAB') == True
assert cycpattern_check('ABAB','BAA') == True
assert cycpattern_check('ABAB','AAB') == True
assert cycpattern_check('ABAB','BABA') == True
assert cycpattern_check('ABAB','B') == True
assert cycpattern_check('ABAB','A') == True
assert cycpattern_check('ABAB','BABBA') == False
assert cycpattern_check('ABAB','AAABAAB') == False
assert cycpattern_check('baa', 'aa') == True
assert cycpattern_check('baaaaaaaaa', 'aaaxx') == False
assert cycpattern_check('aabaaaaaaa', 'aaa') == True
assert cycpattern_check('abaaaaaacab', 'acab') == True
assert cycpattern_check('abaaaaaacab', 'aac') == True
assert cycpattern_check('abaaaaaacab', 'ac') == True
assert cycpattern_check('abaaaaaacab', 'ab') == True
assert cycpattern_check('abaaaaaacab', 'a') == True
assert cycpattern_check('abaaaaaacab', 'c') == True
assert cycpattern_check('abaaaaaacab', 'ca') == True
assert cycpattern_check('abaaaaaacab', 'cab') == True
assert cycpattern_check('abaaaaaacab', 'acabb') == False
assert cycpattern_check('abaaaaaacab', 'acabc') == False
assert cycpattern_check("abcde","abc") == True
assert cycpattern_check("abcde","cde") == True
assert cycpattern_check("hello" , "lll") == False , "Test 2 Failed"
assert cycpattern_check("h" , "h") == True , "Test 6 Failed"
assert cycpattern_check("hello" , "llllllllllllllllllllll") == False , "Test 7 Failed"
assert cycpattern_check("hellooooo" , "loo") == True , "Test 8 Failed"
assert cycpattern_check("abc" , "aaa") == False
assert cycpattern_check('abxabe','abe') == True
assert cycpattern_check('abcabc','abc') == True
assert cycpattern_check('abcabc','bca') == True
assert cycpattern_check('abcabc','cab') == True
assert cycpattern_check('abcabc','abcabc') == True
assert cycpattern_check('abcabc','bcabca') == True
assert cycpattern_check('abcabc','cabcab') == True
assert cycpattern_check('aaaaa','aaa') == True
assert cycpattern_check('aaaaa','aaaa') == True
assert cycpattern_check('abcabcabcabc','abc') == True
assert cycpattern_check('abcabcabcabc','bca') == True
assert cycpattern_check('abcabcabcabc','cab') == True
assert cycpattern_check('abcabcabcabc','abcabc') == True
assert cycpattern_check('abcabcabcabc','bcabca') == True
assert cycpattern_check('abcabcabcabc','cabcab') == True
assert cycpattern_check('abcabcabcabc','abcabcabcabc')
assert cycpattern_check("racecar" , "car") == True
assert cycpattern_check("apple" , "pple") == True
assert cycpattern_check("apple" , "plle") == False
assert cycpattern_check("elvis","iv") == True
assert cycpattern_check("drona","nadro") == True
assert cycpattern_check("drona","ndro") == True
assert cycpattern_check("drona","rona") == True
assert cycpattern_check("trick","kric") == True
assert cycpattern_check("trick","rick") == True
assert cycpattern_check("trick","tick") == False
assert cycpattern_check("drona","rdona") == False
assert cycpattern_check('ABCD', 'AB') == True
assert cycpattern_check('ABCD', 'BC') == True
assert cycpattern_check('ABCD', 'CD') == True
assert cycpattern_check('ABCD', 'ABD') == False
assert cycpattern_check('ABCD', 'CDA') == False
assert cycpattern_check('ABCD', 'DAB') == False
assert cycpattern_check("aacdcca" , "cdcca") == True
assert cycpattern_check("aacdcca" , "aacdcca") == True
assert cycpattern_check("aacdcca" , "aa") == True
assert cycpattern_check("aaaa" , "aaa") == True
assert cycpattern_check("aaaa" , "a") == True
assert cycpattern_check("aaa" , "aaaa") == False
assert cycpattern_check('aaaa','aaa') == True, 'failed'
assert cycpattern_check('aabaaa','baa') == True, 'failed'
assert cycpattern_check('abcabcabc','abc') == True, 'failed'
assert cycpattern_check('aaabb','aab') == True, 'failed'
assert cycpattern_check('aaabb','bab') == True, 'failed'
assert cycpattern_check('aaabb','bba') == True, 'failed'
assert cycpattern_check('aaabb','aba') == True, 'failed'
assert cycpattern_check('abcaabcaabca','bca') == True, 'failed'
assert cycpattern_check('abcabcabcabc','abc') == True, 'failed'
assert cycpattern_check('aaaaa','aaaa') == True, 'failed'
assert cycpattern_check('abcdabcdabcd','bcd') == True, 'failed'
assert cycpattern_check('abcdeabcdeabcde','abc')
assert cycpattern_check('test', 'est') == True
assert cycpattern_check('test', 'best') == False
assert cycpattern_check('test', 't') == True
assert cycpattern_check('test', 'set') == False
assert cycpattern_check("abababab" , "baba") == True
assert cycpattern_check('ABAC', 'BAC')
assert cycpattern_check('ABAC', 'AC')
assert cycpattern_check('CABAC', 'BAC')
assert cycpattern_check('ABAC', 'ABAC')
assert cycpattern_check('CABAC', 'CABAC')
assert cycpattern_check('BACAB', 'BACAB')
assert cycpattern_check('BACAB', 'ACAB')
assert cycpattern_check('BACAB', 'CAB')
assert cycpattern_check('BACAB', 'AB')
assert cycpattern_check('AACAB', 'ACAB')
assert cycpattern_check('AABAC', 'ABAC')
assert cycpattern_check('CABAC', 'ABAC')
assert cycpattern_check('ABAC', 'AB')
assert cycpattern_check('ABCD', 'CDAB')
assert cycpattern_check('ABCD', 'DABC')
assert cycpattern_check('abcdbabc', 'abc') == True, 'test 2'
assert cycpattern_check('abcdbabc', 'abca') == False, 'test 3'
assert cycpattern_check('abcab' , 'ba') == True , 'test 2'
assert cycpattern_check('sstt' , 'ts') == True , 'test 3'
assert cycpattern_check('abcdab' , 'ab') == True , 'test 4'
assert cycpattern_check('abcabd' , 'ce') == False , 'test 6'
assert cycpattern_check('abcabd' , 'abcabd') == True , 'test 7'
assert cycpattern_check('abcabd' , 'cabdab') == True , 'test 8'
assert cycpattern_check('abcab', 'ab') == True
assert cycpattern_check('abcab', 'abcab') == True
assert cycpattern_check('abcabcabcabc', 'bcabcabcabca') == True
assert cycpattern_check('abcabcabcabc', 'cabcabcabcab') == True
assert cycpattern_check("abc", "bca") == True, "test 2 failed"
assert cycpattern_check("abc", "bca") == True, "test 3 failed"
assert cycpattern_check("abc", "bca") == True, "test 4 failed"
assert cycpattern_check("abc", "bca") == True, "test 5 failed"
assert cycpattern_check("abc", "bca") == True, "test 6 failed"
assert cycpattern_check("abc", "bca") == True, "test 7 failed"
assert cycpattern_check("abc", "bca") == True, "test 8 failed"
assert cycpattern_check("abc", "bca") == True, "test 9 failed"
assert cycpattern_check("abc", "bca") == True, "test 10 failed"
assert cycpattern_check("abc", "bca") == True, "test 11 failed"
assert cycpattern_check("abc", "bca") == True, "test 12 failed"
assert cycpattern_check("abcdefghi","ef") == True, "Ef is present in the first string."
assert cycpattern_check("abcdefghi","fg") == True, "Fg is present in the first string."
assert cycpattern_check("abcdefghi","gh") == True, "Gh is present in the first string."
assert cycpattern_check("abcdefghi","hi") == True, "Hi is present in the first string."
assert cycpattern_check("abcdefghi","ab") == True, "Ab is present in the first string."
assert cycpattern_check("abcdefghi","bc") == True, "Bc is present in the first string."
assert cycpattern_check("abcdefghi","cd") == True, "Cd is present in the first string."
assert cycpattern_check("abcdefghi","efg") == True, "Efg is present in the first string."
assert cycpattern_check("abcdefghi","fgh") == True, "Fgh is present in the first string."
assert cycpattern_check('abcdefgh' , 'bcd')
assert cycpattern_check('abcdefgh' , 'fgh')
assert cycpattern_check('abacd' , 'bac')
assert cycpattern_check('abacd' , 'cda')
assert cycpattern_check('abcdefghabcdefgh' , 'abcdefgh')
assert cycpattern_check('abcdefghabcdefgh' , 'bcd')
assert cycpattern_check('abcdefghabcdefgh' , 'fghab')
assert cycpattern_check('abcdefghabcdefgh' , 'fgh')
assert cycpattern_check('abcdefghabcdefgh' , 'cdefghab')
assert cycpattern_check('abcdefghabcdefgh' , 'abcdef')
assert not cycpattern_check('abacd' , 'abcd')
assert cycpattern_check('ABCD','BCDA') == True, 'error2'
assert cycpattern_check('ABCD','CDAB') == True, 'error4'
assert cycpattern_check('ABCD','DABC') == True, 'error5'
assert cycpattern_check('ABCD','ABCD') == True, 'error6'
assert cycpattern_check('ABCD','DABCD') == False, 'error7'
assert cycpattern_check('ABCD','ABCC') == False, 'error8'
assert cycpattern_check('ABCD','ABCB') == False, 'error9'
assert cycpattern_check("abcde", "abc") == True
assert cycpattern_check("abcde", "bcde") == True
assert cycpattern_check("abcde", "abcde") == True
assert cycpattern_check("abcde", "a") == True
assert cycpattern_check("abcde", "ab") == True
assert cycpattern_check("abcde", "b") == True
assert cycpattern_check("abcde", "bc") == True
assert cycpattern_check("abcde", "bcd") == True
assert cycpattern_check("abcde", "c") == True
assert cycpattern_check("abcde", "cd") == True
assert cycpattern_check("abcde", "d") == True
assert cycpattern_check("abcde", "de") == True
assert cycpattern_check("abcde" , "abced") == False , "Test failed"
assert cycpattern_check("AATTC" , "GATTAA") == False
assert cycpattern_check('abcd', 'cddb') == False
assert cycpattern_check('abcd', 'abcd') == True
assert cycpattern_check('xyzw', 'zwxy') == True
assert cycpattern_check('abcdefgh', 'abc') == True
assert cycpattern_check('abcdef', 'bcd')
assert cycpattern_check('abcdef', 'def')
assert cycpattern_check('abcdef', 'abc')
assert not cycpattern_check('abcdef', 'xab')
assert not cycpattern_check('abcdef', 'yab')
assert cycpattern_check('abc', 'xyz') == False
assert cycpattern_check('abc', 'abc') == True
assert cycpattern_check('abc', 'cab') == True
assert cycpattern_check("abcde", "deabc") == True, "deabc is substring in abcde"
assert cycpattern_check("abcde", "abcde") == True, "abcde is substring in abcde"
assert cycpattern_check("abcde", "bcdeb") == False, "bcdeb is not substring in abcde"
assert cycpattern_check('abcd' , 'bcda') == True, 'Test 2 Failed!'
assert cycpattern_check('abc' , 'cab') == True, 'Test 3 Failed!'
assert cycpattern_check('abc' , 'caba') == False, 'Test 5 Failed!'
