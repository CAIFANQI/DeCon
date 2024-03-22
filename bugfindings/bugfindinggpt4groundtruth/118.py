
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
assert 	get_closest_vowel("abct") == ""
assert 	get_closest_vowel("bc") == ""
assert 	get_closest_vowel("a") == ""
assert 	get_closest_vowel("aa") == ""
assert 	get_closest_vowel("aaa") == ""
assert 	get_closest_vowel("aee") == ""
assert 	get_closest_vowel("eeeeee") == ""
assert get_closest_vowel('bbbb') == ''
assert get_closest_vowel('bbbba') == ''
assert get_closest_vowel('bbbbb') == ''
assert get_closest_vowel('bbbbbb') == ''
assert get_closest_vowel('bbbbbbb') == ''
assert 	get_closest_vowel("st") == ""
assert 	get_closest_vowel("meutmeut") == ""
assert 	get_closest_vowel("meutststmeut") == ""
assert 	get_closest_vowel("stststst") == ""
assert 	get_closest_vowel("ststststst") == ""
assert 	get_closest_vowel("qwe") == ""
assert 	get_closest_vowel("qw") == ""
assert 	get_closest_vowel('fooa') == '', 'fooa -> '
assert 	get_closest_vowel('a') == '', 'a -> '
assert 	get_closest_vowel('a') == '', "Should be empty"
assert 	get_closest_vowel('azazaz') == 'a', "Should be a"
assert 	get_closest_vowel('qzqzqzqaq') == 'a', "Should be a"
assert 	get_closest_vowel('car') == 'a'
assert 	get_closest_vowel('abc') == ''
assert 	get_closest_vowel('abcc') == ''
assert 	get_closest_vowel('abcd') == ''
assert 	get_closest_vowel('a') == ''
assert 	get_closest_vowel('e') == ''
assert 	get_closest_vowel('d') == ''
assert 	get_closest_vowel('b') == ''
assert 	get_closest_vowel('t') == ''
assert 	get_closest_vowel("aEq9") 	== ""
assert 	get_closest_vowel("qQQsSd") 	== ""
assert get_closest_vowel("test") == "e"
assert get_closest_vowel("australia") == "a"
assert get_closest_vowel("zachary") == "a"
assert get_closest_vowel("c") == ""
assert get_closest_vowel("") == ""
assert get_closest_vowel("a") == ""
assert 	get_closest_vowel("aaiou") == ""
assert 	get_closest_vowel("qjk") == ""
assert 	get_closest_vowel("aeiou") == ""
assert 	get_closest_vowel("bcd") == ""
assert 	get_closest_vowel('abc') == '', 'abc'
assert 	get_closest_vowel('abcba') == '', 'abcba'
assert 	get_closest_vowel('abcbaa') == '', 'abcbaa'
assert 	get_closest_vowel('abcbaaa') == '', 'abcbaaa'
assert 	get_closest_vowel('abcd') == '', 'abcd'
assert 	get_closest_vowel('aacb') == '', 'aacb'
assert 	get_closest_vowel('aaaaa') == '', 'aaaaa'
assert 	get_closest_vowel('aaaaaa') == '', 'aaaaaa'
assert 	get_closest_vowel('a') == '', 'a'
assert 	get_closest_vowel('aa') == '', 'aa'
assert 	get_closest_vowel('x') == '', "Vowels in the beginning and ending don't count"
assert 	get_closest_vowel('z') == '', "Vowels in the beginning and ending don't count"
assert 	get_closest_vowel('xv') == '', "Vowels in the beginning and ending don't count"
assert 	get_closest_vowel('y') == '', "Vowels in the beginning and ending don't count"
assert get_closest_vowel('shrimp') == 'i'
assert 	get_closest_vowel('hello world') == 'o', 'hello world'
