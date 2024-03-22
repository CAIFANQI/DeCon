
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
assert get_closest_vowel('Pirates') == 'e'
assert get_closest_vowel('cake') == 'a'
assert get_closest_vowel("abe") == ""
assert get_closest_vowel('cat') == 'a'
assert get_closest_vowel('vbnm') == ''
assert get_closest_vowel('hellllloy') == 'o'
assert get_closest_vowel('hellllloyy') == 'o'
assert get_closest_vowel('heyyelloy') == 'o'
assert get_closest_vowel('heyyelloyy') == 'o'
assert get_closest_vowel('heyyelloyyy') == 'o'
assert get_closest_vowel('heyyelloyyyy') == 'o'
assert get_closest_vowel('heyyelloyyyyy') == 'o'
assert get_closest_vowel('heyyelloyyyyyy') == 'o'
assert get_closest_vowel('heyyelloyyyyyyy') == 'o'
assert get_closest_vowel('heyyelloyyyyyyyy') == 'o'
assert get_closest_vowel('heyyelloyyyyyyyyy') == 'o'
assert get_closest_vowel('abcedefgh') == 'e'
assert get_closest_vowel('abcedefghi') == 'e'
assert get_closest_vowel("hello") == "e"
assert get_closest_vowel("hell") == "e"
assert get_closest_vowel('abbb') == ''
assert get_closest_vowel('abbbb') == ''
assert get_closest_vowel('abbbba') == ''
assert get_closest_vowel('zab') == 'a'
assert get_closest_vowel('elephant') == 'a'
assert get_closest_vowel('dog') == 'o'
assert get_closest_vowel('eDDg') == ''
assert get_closest_vowel('eDDG') == ''
assert get_closest_vowel('eDdG') == ''
assert get_closest_vowel('helo') == 'e'
assert get_closest_vowel('abcef') == 'e'
assert get_closest_vowel('bananab') == 'a'
assert get_closest_vowel('a') == ''
assert get_closest_vowel('bab') == 'a'
assert get_closest_vowel('het') == 'e'
assert get_closest_vowel('heht') == 'e'
assert get_closest_vowel('aa') == ""
assert get_closest_vowel('abba') == ""
assert get_closest_vowel('abcdefg') == 'e'
assert get_closest_vowel('cdef') == 'e'
assert get_closest_vowel('cdefeg') == 'e'
assert get_closest_vowel('hello') == 'e'
assert get_closest_vowel('words') == 'o'
assert get_closest_vowel('WoRd') == 'o'
assert get_closest_vowel('WoRdS') == 'o'
assert get_closest_vowel('word') == 'o'
assert get_closest_vowel('DorD') == 'o'
assert get_closest_vowel('dorD') == 'o'
assert get_closest_vowel('doRd') == 'o'
assert get_closest_vowel("z") == ""
assert get_closest_vowel("qwe") == ""
assert get_closest_vowel("QWE") == ""
assert get_closest_vowel("zA") == ""
assert get_closest_vowel("za") == ""
assert get_closest_vowel("ABEYSOMETIMES") == 'E'
assert get_closest_vowel('Kayak') == 'a'
assert get_closest_vowel("hellohello") == "e"
assert get_closest_vowel('Hello') == 'e'
assert get_closest_vowel('hell') == 'e'
assert get_closest_vowel('p') == ''
assert get_closest_vowel(' ') == ''
assert get_closest_vowel("yes") == "e"
assert get_closest_vowel("Orange") == "a"
assert get_closest_vowel("Abcdefg") == "e"
assert get_closest_vowel("Abcdcdefg") == "e"
assert get_closest_vowel("Aebcdefg") == "e"
assert get_closest_vowel("Aebcdef") == "e"
assert get_closest_vowel("hola") == "o"
assert get_closest_vowel("holA") == "o"
assert get_closest_vowel("hey") == "e"
assert get_closest_vowel("hay") == "a"
assert get_closest_vowel("was") == "a"
assert get_closest_vowel("a") == ""
assert get_closest_vowel("abcde") == ""
assert get_closest_vowel('') == ''
assert get_closest_vowel('aaaaa') == ''
assert get_closest_vowel('ab') == ''
assert get_closest_vowel("car") == 'a'
assert get_closest_vowel("cat") == 'a'
assert get_closest_vowel('apple') == ''
assert get_closest_vowel("aaa") == ""
assert get_closest_vowel("aaaaa") == ""
assert get_closest_vowel("Aardvark") ==  "a"
assert get_closest_vowel("AardvarkEaten") ==  "e"
assert get_closest_vowel("Cat") ==  "a"
assert get_closest_vowel("Hat") ==  "a"
assert get_closest_vowel("Cats") ==  "a"
assert get_closest_vowel("Holy") ==  "o"
assert get_closest_vowel("Mice") ==  "i"
assert get_closest_vowel('Happiness') == 'e'
assert get_closest_vowel('Love') == 'o'
assert get_closest_vowel('Test') == 'e'
assert get_closest_vowel('Yep') == 'e'
assert get_closest_vowel('Hola') == 'o'
assert get_closest_vowel('app') is ''
assert get_closest_vowel('p') is ''
assert get_closest_vowel('') is ''
assert get_closest_vowel('Word') == 'o'
assert get_closest_vowel('abca') == ''
assert get_closest_vowel("abba") == ""
assert get_closest_vowel("ab") == ""
assert get_closest_vowel("abbaabbbaaa") == ""
assert get_closest_vowel("asdf") == ''
assert get_closest_vowel('xy') == ''
assert get_closest_vowel("god") == "o"
assert get_closest_vowel("aass") == ""
assert get_closest_vowel('watermelon') == 'o'
assert get_closest_vowel('abba') == ''
assert get_closest_vowel('abccba') == ''
assert get_closest_vowel('rajat') == 'a'
assert get_closest_vowel('heyy') == 'e'
assert get_closest_vowel('ramen') == 'e'
assert get_closest_vowel('abadel') == 'e'
assert get_closest_vowel('klmjen') == 'e'
assert get_closest_vowel('app') == ''
assert get_closest_vowel("cat") == "a"
