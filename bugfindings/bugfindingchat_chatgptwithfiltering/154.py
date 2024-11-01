
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
assert cycpattern_check("hello", "lohel") == True
assert cycpattern_check("hello", "llohe") == True
assert cycpattern_check("hello", "hello") == True
assert cycpattern_check("hello", "olhel") == False
assert cycpattern_check("hello", "lohelx") == False
assert cycpattern_check("hello", "llohee") == False
assert cycpattern_check("hello", "world") == False
assert cycpattern_check("hello", "h") == True
assert cycpattern_check("hello", "e") == True
assert cycpattern_check("hello", "ohell") == True
assert cycpattern_check("hello", "hloel") == False
assert cycpattern_check("abcde", "edcba") == False
assert cycpattern_check("abcde", "cdeab") == True
assert cycpattern_check("abcde", "abcde") == True
assert cycpattern_check("abcde", "abcd") == True
assert cycpattern_check("abcde", "edcb") == False
assert cycpattern_check("hello", "lehol") == False
assert cycpattern_check("abcde", "fghij") == False
assert cycpattern_check('abcdef', 'cdefab') == True
assert cycpattern_check('abcdef', 'efabcd') == True
assert cycpattern_check('abcdef', 'fabcde') == True
assert cycpattern_check('abcdef', 'abcdef') == True
assert cycpattern_check('abcdef', 'abc') == True
assert cycpattern_check('abcdef', 'def') == True
assert cycpattern_check('abcdef', 'xyz') == False
assert cycpattern_check('abcdef', 'defabcxyz') == False
assert cycpattern_check("abcd", "dabc") == True
assert cycpattern_check("abcd", "cdab") == True
assert cycpattern_check("abcd", "abcd") == True
assert cycpattern_check("abcd", "abcdabcd") == False
assert cycpattern_check('abcdef', 'defcba') == False
assert cycpattern_check('abcdef', 'defabc') == True
assert cycpattern_check('abcde', 'bcd') == True
assert cycpattern_check('abcde', 'def') == False
assert cycpattern_check('abcde', 'abc') == True
assert cycpattern_check("hello", "leloh") == False
assert cycpattern_check("hello", "helle") == False
assert cycpattern_check("abcdefg", "gabcdef") == True
assert cycpattern_check("abcdefg", "fgabcde") == True
assert cycpattern_check("abcdefg", "defgabc") == True
assert cycpattern_check("abcdefg", "abcdefg") == True
assert cycpattern_check("abcdefg", "xyz") == False
assert cycpattern_check("abcde", "cda") == False
assert cycpattern_check("abcde", "bcd") == True
assert cycpattern_check("abcde", "decb") == False
assert cycpattern_check('hello', 'llohe') == True
assert cycpattern_check('hello', 'ohell') == True
assert cycpattern_check('hello', 'hello') == True
assert cycpattern_check('hello', 'oellh') == False
assert cycpattern_check("abcde", "abc") == True
assert cycpattern_check("abcde", "def") == False
assert cycpattern_check("hello", "llohe") == True, "Test case 2 failed"
assert cycpattern_check("hello", "ohell") == True, "Test case 3 failed"
assert cycpattern_check("hello", "hello") == True, "Test case 4 failed"
assert cycpattern_check("hello", "world") == False, "Test case 5 failed"
assert cycpattern_check('hello', 'helloo') == False
assert cycpattern_check('hello', 'helo') == False
assert cycpattern_check('hello', 'olhel') == False
assert cycpattern_check('hello', 'lloh') == False
assert cycpattern_check("hello", "lohelh") == False
assert cycpattern_check("abcde", "eabcd") == True
assert cycpattern_check("abcde", "cdefg") == False
assert cycpattern_check('abcde', 'deabc') == True
assert cycpattern_check('abcde', 'abcdeabcd') == False
assert cycpattern_check("hello", "loh") == False
assert cycpattern_check("hello", "llo") == True
assert cycpattern_check("hello", "he") == True
assert cycpattern_check("hello", "el") == True
assert cycpattern_check("hello", "lo") == True
assert cycpattern_check("hello", "o") == True
assert cycpattern_check("hello", "ll") == True
assert cycpattern_check("hello", "hlelo") == False
assert cycpattern_check('abcd', 'bcda') == True
assert cycpattern_check('abcd', 'dabc') == True
assert cycpattern_check('abcd', 'abcd') == True
assert cycpattern_check('abcd', 'dcba') == False
assert cycpattern_check("abcde", "deabc") == True
assert cycpattern_check('abcde', 'cdeab') == True
assert cycpattern_check('abcde', 'bcdea') == True
assert cycpattern_check('abcde', 'efg') == False
assert cycpattern_check('abcde', 'abcde') == True
assert cycpattern_check('hello', 'he') == True
assert cycpattern_check('hello', 'leh') == False
assert cycpattern_check("hello", "oellh") == False
assert cycpattern_check("hello", "hlello") == False
assert cycpattern_check("hello", "ol") == True
assert cycpattern_check("hello", "l") == True
assert cycpattern_check("hello", "") == True
assert cycpattern_check("abcde", "ab") == True
assert cycpattern_check("rotation", "tion") == True
assert cycpattern_check("rotation", "ation") == True
assert cycpattern_check("rotation", "on") == True
assert cycpattern_check("rotation", "ation")
assert cycpattern_check("abcd", "dcba") == False
assert cycpattern_check("abcde", "bcdea") == True
assert cycpattern_check('hello', 'llohe') == True, "Test case 2 failed"
assert cycpattern_check('hello', 'lohe') == False, "Test case 5 failed"
assert cycpattern_check('hello', 'hello') == True, "Test case 6 failed"
assert cycpattern_check('hello', 'helloworld') == False
assert cycpattern_check("abcde", "abced") == False
assert cycpattern_check('abcde', 'de') == True
assert cycpattern_check('abcde', 'ced') == False
assert cycpattern_check('hello', 'hlelo') == False
assert cycpattern_check('hello', 'world') == False
assert cycpattern_check('abcdefg', 'gabcdef') == True, "Test case 2 failed"
assert cycpattern_check('abcdefg', 'defgh') == False, "Test case 3 failed"
assert cycpattern_check('abcd', 'ab') == True
assert cycpattern_check('abcd', 'ac') == False
assert cycpattern_check('abcd', 'efgh') == False
assert cycpattern_check('abcd', 'abcdef') == False
assert cycpattern_check("abcdef", "defabc") == True, "Test case 2 failed"
assert cycpattern_check("abcdef", "efabcd") == True, "Test case 3 failed"
assert cycpattern_check("abcdef", "fabcde") == True, "Test case 4 failed"
assert cycpattern_check("abcdef", "abcdef") == True, "Test case 5 failed"
assert cycpattern_check("abcdef", "fedcba") == False, "Test case 6 failed"
assert cycpattern_check("abcdef", "abcdefg") == False, "Test case 7 failed"
assert cycpattern_check('hello', 'lehol') == False
assert cycpattern_check('abcdefg', 'gabcd') == False
assert cycpattern_check("abcdef", "d") == True
assert cycpattern_check("abcdef", "abcdefg") == False
assert cycpattern_check("abcdefg", "defg") == True
assert cycpattern_check("abcdefg", "efg") == True
assert cycpattern_check("abcdefg", "fg") == True
assert cycpattern_check("abcdefg", "g") == True
assert cycpattern_check("abcdefg", "abcd") == True
assert cycpattern_check("abcdefg", "bcdefg") == True
assert cycpattern_check("abcdefg", "cde") == True
assert cycpattern_check("abcdefg", "def") == True
assert cycpattern_check("abcdefg", "ef") == True
assert cycpattern_check("abcdefg", "f") == True
assert cycpattern_check("abcdefg", "abc") == True
assert cycpattern_check("abcdefg", "bcd") == True
assert cycpattern_check("abcdefg", "c") == True
assert cycpattern_check("abcdefg", "cdeffg") == False
assert cycpattern_check("abcdefg", "efgg") == False
assert cycpattern_check("abcdefg", "fgg") == False
assert cycpattern_check("abcdefg", "gg") == False
assert cycpattern_check("abcdefg", "abcdg") == False
assert cycpattern_check("abcdefg", "bcdefgg") == False
assert cycpattern_check("abcdefg", "cdeg") == False
assert cycpattern_check("word", "word") == True, "Test case 2 failed"
assert cycpattern_check("hello", "llohe") == True, "Test case 3 failed"
assert cycpattern_check("abc", "cba") == False, "Test case 4 failed"
assert cycpattern_check("abcdefg", "gabcdef") == True, "Test case 5 failed"
assert cycpattern_check("abcdefg", "efgabcd") == True
assert cycpattern_check("abcde", "edc") == False
assert cycpattern_check('abcde', 'edcba') == False
assert cycpattern_check('abcde', 'cdeab') == True, 'Test Case 2 Failed'
assert cycpattern_check('abcde', 'bcdea') == True, 'Test Case 4 Failed'
assert cycpattern_check("abcdefg", "abcdefgabc") == False
assert cycpattern_check("abcdefg", "defgabcdefg") == False
assert cycpattern_check('hello', 'lohel') == True
assert cycpattern_check('hello', 'ellho') == False
assert cycpattern_check('hello', 'loh') == False
assert cycpattern_check('hello', 'ohell') == True, "Test case 3 failed"
assert cycpattern_check('hello', 'hello') == True, "Test case 4 failed"
assert cycpattern_check('hello', 'world') == False, "Test case 5 failed"
assert cycpattern_check('hello', 'llo') == True, "Test case 6 failed"
assert cycpattern_check('hello', 'lo') == True, "Test case 7 failed"
assert cycpattern_check('hello', 'el') == True, "Test case 8 failed"
assert cycpattern_check('abcde', 'bc') == True
assert cycpattern_check('hello', 'llohe') == True, 'Test Case 2 Failed'
assert cycpattern_check('hello', 'elloh') == True, 'Test Case 3 Failed'
assert cycpattern_check('hello', 'ohell') == True, 'Test Case 4 Failed'
assert cycpattern_check('hello', 'hello') == True, 'Test Case 5 Failed'
assert cycpattern_check('hello', 'world') == False, 'Test Case 6 Failed'
assert cycpattern_check('hello', 'lohe') == False, 'Test Case 8 Failed'
assert cycpattern_check('hello', 'ohel') == False, 'Test Case 9 Failed'
assert cycpattern_check('hello', 'helloo') == False, 'Test Case 10 Failed'
assert cycpattern_check("hello", "hlole") == False
assert cycpattern_check("hello", "loleh") == False
