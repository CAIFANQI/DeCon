
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
assert 	cycpattern_check("abcd", "bcdef") == False
assert 	cycpattern_check("abcd", "abcd") == True
assert 	cycpattern_check("abcd", "abcde") == False
assert 	cycpattern_check("abcd", "acde") == False
assert 	cycpattern_check("abcd", "bde") == False
assert 	cycpattern_check( "abab", "abab") == True
assert 	cycpattern_check( "abab", "ab") == True
assert 	cycpattern_check( "abab", "a") == True
assert 	cycpattern_check( "abab", "") == True
assert 	cycpattern_check( "abab", "aab") == True
assert 	cycpattern_check('abcd','cdab')==True
assert 	cycpattern_check( "a", "apple" ) == False, 'Wrong answer'
assert 	(cycpattern_check('pineapple', 'apple') == True)
assert 	(cycpattern_check('apple', 'pine') == False)
assert 	(cycpattern_check('apple', 'apple') == True)
assert 	(cycpattern_check('apple', 'p') == True)
assert 	(cycpattern_check('apple', 'e') == True)
assert 	(cycpattern_check('apple', 'l') == True)
assert 	(cycpattern_check('apple', 'le') == True)
assert 	(cycpattern_check('apple', 'eap') == False)
assert 	(cycpattern_check('apple', 'app') == True)
assert 	cycpattern_check("abacus", "ba")
assert 	cycpattern_check("abacus", "bac")
assert 	cycpattern_check("abacus", "aab")
assert 	cycpattern_check("abacus", "abac")
assert 	cycpattern_check("abacus", "acb")
assert 	cycpattern_check("abacus", "cba")
assert 	cycpattern_check("abacus", "b")
assert 	cycpattern_check("ab", "a") == True
assert 	cycpattern_check("ab", "bc") == False
assert 	cycpattern_check("ab", "ab") == True
assert 	cycpattern_check("ab", "b") == True
assert 	cycpattern_check("ab", "ba") == True
assert 	cycpattern_check('alice', 'bob') == False
assert 	cycpattern_check('alice', 'lice') == True
assert 	cycpattern_check('alice', 'lic') == True
assert 	cycpattern_check('alice', 'ice') == True
assert 	cycpattern_check('alice', 'cali') == True
assert 	cycpattern_check('alice', 'ic') == True
assert 	cycpattern_check('alice', 'a') == True
assert 	(cycpattern_check("apple", "pleap"))
assert 	(cycpattern_check("apple", "app"))
assert not (cycpattern_check("waterbottle", "worbottle"))
assert not (cycpattern_check("app", "apple"))
assert 	(cycpattern_check("tiger", "r"))
assert 	(cycpattern_check("tiger", "gi"))
assert 	(cycpattern_check("tiger", "it"))
assert 	(cycpattern_check("tiger", "t"))
assert cycpattern_check("hello", "ll") == True
assert cycpattern_check("hello", "hllo") == False
assert cycpattern_check("hello", "ello") == True
assert cycpattern_check("hello", "o") == True
assert cycpattern_check('abcd', 'bcd')
assert cycpattern_check('abcd', 'cdab')
assert cycpattern_check('abcd', 'cd')
assert cycpattern_check('abcd', 'd')
assert cycpattern_check('abcd', 'abcd')
assert cycpattern_check('abcd', 'ab')
assert cycpattern_check('abcd', 'bc')
assert not cycpattern_check('abcd', 'ac')
