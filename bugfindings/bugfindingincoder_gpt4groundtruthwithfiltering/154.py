
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
assert cycpattern_check('abra','abra')==True
assert cycpattern_check('abraabra','abra')==True
assert cycpattern_check('abraabraabra','abraabra')==True
assert cycpattern_check('abraabraabraabra','abraabra')==True
assert cycpattern_check('abraabraabraabraabra','abraabra')==True
assert cycpattern_check('abraabraabraabraabraabraabra','abraabra')==True
assert cycpattern_check('abraabraabraabraabraabraabraabraabra','abraabra')==True
assert cycpattern_check('abraabraabraabraabraabraabraabraabraabra','abraabra')==True
assert cycpattern_check('abraabraabraabraabraabraabraabraabraabraabra','abraabra')==True
assert cycpattern_check('abc','abc') == True
assert cycpattern_check('abb','abb') == True
assert cycpattern_check('abbb','abb') == True
assert cycpattern_check('abbbbb','abb') == True
assert cycpattern_check('ba', 'ab') == True
assert cycpattern_check('a', 'a') == True
assert cycpattern_check('ab', 'b') == True
assert cycpattern_check('ab', 'ab') == True
assert cycpattern_check('word', 'word') is True
assert cycpattern_check('word', 'wowo') is False
assert cycpattern_check('word', 'wowowo') is False
assert cycpattern_check('word', 'wowowowo') is False
assert cycpattern_check('word', 'wowowowowo') is False
assert cycpattern_check('word', 'wowowowowowowo') is False
assert cycpattern_check('word', 'wowowowowowowowowo') is False
assert cycpattern_check("abc", "ab") == True
assert cycpattern_check("abc", "abe") == False
assert cycpattern_check("abc", "abd") == False
assert cycpattern_check("ab", "a") == True
assert cycpattern_check("ab", "ab") == True
assert cycpattern_check('abcd', 'aacd') == False
assert cycpattern_check('abcd', 'abcd') == True
assert cycpattern_check('abcd', 'abca') == False
assert cycpattern_check('abcd', 'abxd') == False
assert cycpattern_check('abcd', 'axyz') == False
assert cycpattern_check('aba', 'aba') == True
assert cycpattern_check('abc', 'abc') == True
assert cycpattern_check('abc', 'aba') == False
assert cycpattern_check('abd', 'aba') == False
assert cycpattern_check('abd', 'cd') == False
assert cycpattern_check('abd', 'bcda') == False
assert cycpattern_check('abd', 'abaabc') == False
assert cycpattern_check('abaabc', 'abaabc') == True
assert cycpattern_check('abc', 'abb') == False
assert cycpattern_check('abc', 'abcc') == False
assert cycpattern_check('abcabc', 'abc') == True
assert cycpattern_check('abcabc', 'abca') == True
assert cycpattern_check('abcabc', 'abcc') == True
assert cycpattern_check('abcabc', 'abbcc') == False
assert cycpattern_check('abcabcdef', 'abc') == True
assert cycpattern_check('abcabcdef', 'abca') == True
assert cycpattern_check('abcabcdef', 'abcc') == True
assert cycpattern_check('abcabcdef', 'abcabcdef') == True
assert cycpattern_check('abcabcdef', 'abcccbadef') == False
assert cycpattern_check("apple", "apple") == True
assert cycpattern_check("apple", "aapl") == False
assert cycpattern_check("apple", "ppple") == False
assert cycpattern_check("apple", "pppple") == False
assert cycpattern_check('abaca', 'aba') == True
assert cycpattern_check('abaca', 'aab') == True
assert cycpattern_check('abaca', 'baca') == True
assert cycpattern_check('abaca', 'caba') == True
assert cycpattern_check('a', 'b') == False
assert cycpattern_check('ab', 'a') == True
assert cycpattern_check('ab', 'ba') == True
assert cycpattern_check('ba', 'bb') == False
assert cycpattern_check('bb', 'ba') == False
assert cycpattern_check('ab', 'ac') == False
assert cycpattern_check('ac', 'ab') == False
assert cycpattern_check('ac', 'a') == True
assert cycpattern_check('ac', 'ac') == True
assert cycpattern_check('aa', 'a') == True
assert cycpattern_check('aa', 'aa') == True
assert cycpattern_check("abacaba", "bac") == True
assert cycpattern_check("abacaba", "abacaba") == True
assert cycpattern_check("abacaba", "abc") == True
assert cycpattern_check("abacaba", "abac") == True
assert cycpattern_check("abacaba", "aabc") == False
assert cycpattern_check("abacaba", "abcde") == False
assert cycpattern_check("abacaba", "aa") == False
assert cycpattern_check("abacaba", "abcd") == False
assert cycpattern_check('alabama', 'abama') == True
assert cycpattern_check('alabama', 'abamay') == False
assert cycpattern_check('alabama', 'abamaga') == False
assert cycpattern_check('alabama', 'abamag') == False
assert cycpattern_check('alabama', 'abamya') == False
assert cycpattern_check('alabama', 'abamye') == False
assert cycpattern_check('alabama', 'abamaye') == False
assert cycpattern_check('alabama', 'abamaya') == False
assert cycpattern_check('alabama', 'abamayo') == False
assert cycpattern_check('alabama', 'abamayi') == False
assert cycpattern_check('alabama', 'abamayu') == False
assert cycpattern_check('alabama', 'abamai') == False
assert cycpattern_check('ab', 'aba') == False
assert cycpattern_check('ab', 'abb') == False
assert cycpattern_check('ab', 'abab') == False
assert cycpattern_check('ab', 'abbb') == False
assert cycpattern_check('ab', 'abba') == False
assert cycpattern_check('ab', 'abbbb') == False
assert cycpattern_check('ab', 'abbbbbb') == False
assert cycpattern_check('abba', 'ba') == True
assert cycpattern_check('abba', 'abba') == True
assert cycpattern_check("abracadabra", "bracadada") == False
assert cycpattern_check("abracadabra", "abracada") == True
assert cycpattern_check("abracadabra", "abracad") == True
assert cycpattern_check("abracadabra", "abraca") == True
assert cycpattern_check("abracadabra", "abrac") == True
assert cycpattern_check("abracadabra", "abra") == True
assert cycpattern_check('a', 'ab') == False
assert cycpattern_check('ba', 'ba') == True
assert cycpattern_check('ab', 'aab') == False
assert cycpattern_check('ab', 'aabb') == False
assert cycpattern_check('ab', 'abaabc') == False
assert cycpattern_check('ab', 'abaab') == False
assert cycpattern_check('ab', 'abaabb') == False
assert cycpattern_check('ab', 'abaabba') == False
assert cycpattern_check('ab', 'abaabbacba') == False
assert cycpattern_check('ab', 'abaabcba') == False
assert cycpattern_check('abc','acd') == False
assert cycpattern_check('abc','acde') == False
assert cycpattern_check('abc','abcde') == False
assert cycpattern_check('abc','abbc') == False
assert cycpattern_check('abc','abbd') == False
assert cycpattern_check('abc','abbdac') == False
assert cycpattern_check('abc','abbdacd') == False
assert cycpattern_check('abc','abbdacde') == False
assert cycpattern_check('abc','abbdacc') == False
assert cycpattern_check('abc','abbdacdb') == False
assert cycpattern_check('abc','abbdacdbc') == False
assert cycpattern_check('abc','abbdacdbcc') == False
assert cycpattern_check('abc','abbdacdbccd') == False
assert cycpattern_check('abc','abbdacdbcccc') == False
assert cycpattern_check('abc','abbdacdbcccdd') == False
assert cycpattern_check('abc','abbdacdbcccdde') == False
assert cycpattern_check('abc','abbdacdbcccd') == False
assert cycpattern_check('abcd', 'abccd') is False
assert cycpattern_check('abcd', 'acbd') is False
assert cycpattern_check('ab', 'abcd') is False
assert cycpattern_check('abcd', 'abb') is False
assert cycpattern_check('a', 'abcd') is False
assert cycpattern_check('ab', 'abc') is False
assert cycpattern_check('', 'abc') is False
assert cycpattern_check('', 'ab') is False
assert cycpattern_check('', 'a') is False
assert cycpattern_check("abba", "abb") == True
assert cycpattern_check("abba", "aba") == False
assert cycpattern_check("abba", "aBa") == False
assert cycpattern_check("abba", "aBb") == False
assert cycpattern_check("abba", "aBB") == False
assert cycpattern_check("abba", "aBBa") == False
assert cycpattern_check("abba", "aBba") == False
assert cycpattern_check("abba", "aB") == False
assert cycpattern_check("abba", "abaB") == False
assert cycpattern_check('aba', 'ab') == True
assert cycpattern_check('aba', 'abc') == False
assert cycpattern_check('aba', 'abaa') == False
assert cycpattern_check('abaaaaa', 'aba') == True
assert cycpattern_check('abaaaaa', 'abaab') == False
assert cycpattern_check('abaab', 'aba') == True
assert cycpattern_check('abaab', 'abbb') == False
assert cycpattern_check('abbba', 'abbb') == True
assert cycpattern_check('aa', 'ab') == False
assert cycpattern_check('ab', 'abc') == False
assert cycpattern_check('aab', 'aba') == True
assert cycpattern_check('aab', 'aab') == True
assert cycpattern_check('aab', 'aaa') == False
assert cycpattern_check("python", "cpython") == False
assert cycpattern_check("python", "pythyo") == False
assert cycpattern_check("python", "pythyca") == False
assert cycpattern_check("python", "pythycay") == False
assert cycpattern_check("python", "pythycanu") == False
assert cycpattern_check("python", "pythycanpu") == False
assert cycpattern_check("python", "pythycanpy") == False
assert cycpattern_check("python", "pythycanytu") == False
assert cycpattern_check("a", "bca") == False, "acb"
assert cycpattern_check("a", "bcc") == False, "acbd"
assert cycpattern_check("ab", "cc") == False, "bccd"
assert cycpattern_check("aab","aab") == True
assert cycpattern_check("aab","aac") == False
assert cycpattern_check("aac","aab") == False
assert cycpattern_check("aba","aba") == True
assert cycpattern_check("aba","abb") == False
assert cycpattern_check("aba","abc") == False
assert cycpattern_check('ab', 'abd') is False
assert cycpattern_check('ab', 'adb') is False
assert cycpattern_check('ab', 'a') is True
assert cycpattern_check('ab', 'ba') is True
assert cycpattern_check("a", "b") == False
assert cycpattern_check("ab", "baa") == False
assert cycpattern_check("ba", "ba") == True
assert cycpattern_check("a", "a") == True
assert cycpattern_check("ab", "b") == True
assert cycpattern_check("ab", "aba") == False
assert cycpattern_check("a", "ba") == False
assert cycpattern_check("ab", "ba")
assert cycpattern_check('a', 'at') == False
assert cycpattern_check('a', 'aa') == False
assert cycpattern_check('abba', 'aba') == False
assert cycpattern_check('abba', 'abbb') == False
assert cycpattern_check('abb', 'aba') == False
assert cycpattern_check('abb', 'abba') == False
assert cycpattern_check('abba', 'abb') == True
assert cycpattern_check('abbb', 'abba') == False
assert cycpattern_check('hello', 'hello') == True
assert cycpattern_check('hello', 'helo') == False
assert cycpattern_check('hello', 'ehello') == False
assert cycpattern_check('hello', 'helle') == False
assert cycpattern_check('hello', 'helll') == False
assert cycpattern_check('hello', 'hele') == False
assert cycpattern_check('hello', 'hellll') == False
assert cycpattern_check("abcabc", "abc")
assert cycpattern_check("abcc", "bcc")
assert cycpattern_check("abcc", "abc")
assert cycpattern_check("a", "a")
assert cycpattern_check("abb", "ab")
assert cycpattern_check("abb", "bab")
assert cycpattern_check("bab", "bab")
assert cycpattern_check("baba", "baba")
assert cycpattern_check("baba", "bab")
assert cycpattern_check("babab", "babab")
assert cycpattern_check("babab", "bab")
assert cycpattern_check("bababa", "bababa")
assert cycpattern_check("bababaa", "bababaa")
assert cycpattern_check("ab", "abcde") == False
assert cycpattern_check("ab", "abb") == False
assert cycpattern_check("aaa", "aaaaa") == False
assert cycpattern_check("aaa", "aaaa") == False
assert cycpattern_check("aaa", "a") == True
assert cycpattern_check("a", "ab") == False
assert cycpattern_check("ab", "cba") == False
assert cycpattern_check("aa", "a") == True
assert cycpattern_check("aba", "aba") == True
assert cycpattern_check("ab", "aa") == False
assert cycpattern_check('abcc', 'abc') == True
assert cycpattern_check('abcc', 'abcc') == True
assert cycpattern_check('abc', 'ab') == True
assert cycpattern_check('abbac', 'abaaba') == False
assert cycpattern_check('abbac', 'abbabac') == False
assert cycpattern_check('abba', 'baba') == False
assert cycpattern_check('abba', 'ababa') == False
assert cycpattern_check('abba', 'abbaba') == False
assert cycpattern_check('abba', 'abbabac') == False
assert cycpattern_check("abc", "abc") == True
assert cycpattern_check("ab", "cde") == False
assert cycpattern_check("abc", "de") == False
assert cycpattern_check("abcd", "ab") == True
assert cycpattern_check("abcd", "abcd") == True
assert cycpattern_check('the', 'the') == True
assert cycpattern_check('the', 'hti') == False
assert cycpattern_check('the', 'thethethe') == False
assert cycpattern_check('the', 'thathe') == False
assert cycpattern_check('the', 'thethae') == False
assert cycpattern_check('the', 'hte') == False
assert cycpattern_check('the', 'hthe') == False
assert cycpattern_check('the', 'thethehe') == False
assert cycpattern_check('the', 'thetheh') == False
assert cycpattern_check('the', 'thetheht') == False
assert cycpattern_check('the', 'thethehtte') == False
assert cycpattern_check('the', 'thethehtteeth') == False
assert cycpattern_check('the', 'thethehtheth') == False
assert cycpattern_check('the', 'thethehthethe') == False
assert cycpattern_check('the', 'thethehthetheth') == False
assert cycpattern_check("wrd","wrd") is True
assert cycpattern_check("wrd","word") is False
assert cycpattern_check("wrd","woRd") is False
assert cycpattern_check("ab", "bca") == False
assert cycpattern_check("ab", "acb") == False
assert cycpattern_check("ab", "abca") == False
assert cycpattern_check('bb','ab') == False
assert cycpattern_check('aab','ab') == True
assert cycpattern_check('aa','a') ==  True
assert cycpattern_check('aa','aa') ==  True
assert cycpattern_check('aaaa','aaaa') == True
assert cycpattern_check('aaaaa','aaaaaaaa') == False
assert cycpattern_check('bbbbb','bbbb') == True
assert cycpattern_check('bbbbb','bbbbb') == True
assert cycpattern_check('bbbbb','bbbbbb') ==  False
assert cycpattern_check("dog", "do") == True
assert cycpattern_check("dog", "god") == False
assert cycpattern_check("dog", "dogs") == False
assert cycpattern_check("dog", "gods") == False
assert cycpattern_check("dog", "dogg") == False
assert cycpattern_check("dogs", "god") == False
assert cycpattern_check('','a') == False
assert cycpattern_check('aa','a') == True
assert cycpattern_check('aa','aac') == False
assert cycpattern_check('aa','aab') == False
assert cycpattern_check('aa','abac') == False
assert cycpattern_check('aa','abbc') == False
assert cycpattern_check('aa','abccd') == False
assert cycpattern_check("aba", "ab") == True, "abba"
assert cycpattern_check("abba", "abba") == True, "abba"
assert cycpattern_check("abba", "aba") == False, "aba"
assert cycpattern_check("abcde","abcde") == True
assert cycpattern_check("abcde","bcdea") == True
assert cycpattern_check("abcde","abcdeab") == False
assert cycpattern_check('aab', 'ab') == True
assert cycpattern_check('aa', 'aac') == False
assert cycpattern_check('', 'aa') == False
assert cycpattern_check('', 'b') == False
assert cycpattern_check('', 'ac') == False
assert cycpattern_check('', 'ab') == False
assert cycpattern_check('car', 'car') == True
assert cycpattern_check('', 'a') == False
assert cycpattern_check('bab', 'bab') == True
assert cycpattern_check('bab', 'aba') == False
assert cycpattern_check('bab', 'abb') == True
assert cycpattern_check('bab', 'baa') == False
assert cycpattern_check('baa', 'baa') == True
assert cycpattern_check('baa', 'bab') == False
assert cycpattern_check('baa', 'bba') == False
assert cycpattern_check("a", "abd") is False
assert cycpattern_check("abc", "abc") is True
assert cycpattern_check("abc", "abd") is False
assert cycpattern_check("abcd", "abcd") is True
assert cycpattern_check("abcd", "abdc") is False
assert cycpattern_check("abacadaba","abac") == True
assert cycpattern_check("abacadaba","abaca") == True
assert cycpattern_check('word', 'wrd') is False
assert cycpattern_check('word', 'woRd') is False
assert cycpattern_check("halo","halo") == True, "halo"
assert cycpattern_check("hello","hi") == False, "hello"
assert cycpattern_check("halo","hillo") == False, "halo"
assert cycpattern_check("halo","halolo") == False, "halo"
assert cycpattern_check("halo","halohell") == False, "halo"
assert cycpattern_check("pizza", "zypiza") == False
assert cycpattern_check("pizza", "yzpiza") == False
assert cycpattern_check("pizza", "pizza") == True
assert cycpattern_check("pizza", "pizze") == False
assert cycpattern_check("abcdef", "a") == True
assert cycpattern_check("abcdef", "abd") == False
assert cycpattern_check("abcdef", "abds") == False
assert cycpattern_check("abcdef", "cd") == True
assert cycpattern_check("abcdef", "abdc") == False
assert cycpattern_check("abcdef", "abdcde") == False
assert cycpattern_check("abcdef", "abcde") == True
assert cycpattern_check('abaca', 'bacaca') == False
assert cycpattern_check('abaca', 'cbaca') == False
assert cycpattern_check('abaca', 'bac') == True
assert cycpattern_check('abaca', 'bab') == False
assert not cycpattern_check('cat', 'cats')
assert not cycpattern_check('cat', 'tac')
assert not cycpattern_check('cat', 'tacc')
assert cycpattern_check("ab", "ac") == False
assert cycpattern_check('abcde', 'cd') == True
assert cycpattern_check('abcdefg', 'ed') == True
assert cycpattern_check('abcdefg', 'fgh') == False
assert cycpattern_check('abcde', 'fgh') == False
assert cycpattern_check('abccba', 'abbbb') == False
assert cycpattern_check('abccba', 'aba') == False
assert cycpattern_check('a', 'abd') is False
assert cycpattern_check('ab', 'abccd') is False
assert cycpattern_check("rabbit", "rabbit") == True
assert cycpattern_check("rabbit", "pit") == False
assert cycpattern_check('code', 'dcope') is False
assert cycpattern_check('code', 'odeco') is False
assert cycpattern_check('code', 'doco') is False
assert cycpattern_check('code', 'copy') is False
assert cycpattern_check('code', 'docop') is False
assert cycpattern_check("ab", "bcb") == False
assert cycpattern_check("tester", "etses") == False
assert cycpattern_check("word", "wow") == False
assert cycpattern_check('cat', 'caa') == False
assert cycpattern_check('the', 'htes') == False
assert cycpattern_check('aaaa', 'aa') == True
assert cycpattern_check('baab', 'aba') == True
assert cycpattern_check("word","word") == True
assert cycpattern_check('word', 'worood') == False
assert cycpattern_check('word', 'woorld') == False
assert cycpattern_check('word', 'word') == True
assert cycpattern_check('word', 'world') is False
assert cycpattern_check('rab', 'rabbies') == False
assert cycpattern_check('hello','helloo') == False
assert cycpattern_check('abcd', 'abxde') == False
assert cycpattern_check('at','ta') is True
assert cycpattern_check('at','tact') is False
assert cycpattern_check('at','tatcat') is False
