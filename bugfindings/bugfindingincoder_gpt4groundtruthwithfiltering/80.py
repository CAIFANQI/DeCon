
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    if len(s) < 3:
      return False

    for i in range(len(s) - 2):
      
      if s[i] == s[i+1] and s[i+1] == s[i+2] and s[i] == s[i+2]:
        return False
    return True
assert is_happy('abca') == True
assert is_happy('abcde') == True
assert is_happy('abcdea') == True
assert is_happy('abcdeab') == True
assert is_happy('abcdeabc') == True
assert is_happy('abcdeabcd') == True
assert is_happy('abcdef') == True
assert is_happy('abcdefg') == True
assert is_happy('abcdefgh') == True
assert is_happy('abcdefghi') == True
assert is_happy('abcdefghij') == True
assert is_happy('abcdefghijk') == True
assert is_happy('abcdefghijkl') == True
assert is_happy('abcdefghijklm') == True
assert is_happy('abcdefghijklmn') == True
assert is_happy('abcdefghijklmno') == True
assert is_happy('abcdefghijklmnop') == True
assert is_happy('abcdefghijklmnopq') == True
assert is_happy('abcdefghijklmnopqrs') == True
assert is_happy("Happy Happy Happy Happy") == False
assert is_happy("Happy Happy Happy Happy Happy Happy Happy Happy") == False
assert is_happy("Happy Happy Happy Happy Happy Happy Happy Happy Happy Happy") == False
assert is_happy('Hael') == True
assert is_happy("happys") == False
assert is_happy("happyles") == False
assert is_happy("hhappyle") == False
assert is_happy("happyoo") == False
assert is_happy("happyo") == False
assert is_happy("HAPpy") == True
assert is_happy("HAPpY") == True
assert is_happy("HAPpyS") == True
assert is_happy("HAPpysS") == True
assert is_happy("HAPpySs") == True
assert is_happy("HApyPpySs") == True
assert is_happy("haPpySs") == True
assert is_happy("ab") == False
assert is_happy("abacaba") == False
assert is_happy("nothappy") == False
assert is_happy("alabala") == False
assert is_happy("aba") == False
assert is_happy("abba") == False
assert not is_happy('H')
assert not is_happy('He')
assert not is_happy('Hell')
assert not is_happy('Hello1')
assert not is_happy('Helloo')
assert not is_happy('Helloo1')
assert not is_happy('Hell1')
assert not is_happy('HellL')
assert not is_happy('HellO')
assert not is_happy('HellOo')
assert not is_happy('HellOo1')
assert is_happy('HeLlO') 
assert is_happy('HeLlO')
assert is_happy('') == False
assert is_happy('abac') == False
assert is_happy('abacabca') == False
assert is_happy('abacabbba') == False
assert is_happy('abacabbbab') == False
assert is_happy('abacabbbba') == False
assert is_happy('abacabbbbab') == False
assert is_happy('abacabbbbaba') == False
assert is_happy('abacabbbbabab') == False
assert is_happy('abacabbbbababa') == False
assert is_happy('abacabbbbababacabbbbababa') == False
assert is_happy('abacabbbbababacabbbbababacabbbbababa') == False
assert is_happy('abacabbbbababacabbbbababacabbbbababacabbbbababa') == False
assert is_happy('abacabbbbababacabbbbababacabbbbababacabbbbababacabbbbababacabbbbababa') == False
assert is_happy("no") == False, "no is not happy"
assert is_happy("abracadabra") == False, "abracadabra has no distinct 3-letter segments"
assert is_happy("abracadabracabd") == False, "abracadabracabd has no distinct 3-letter segments"
assert is_happy("abracadabracabdab") == False, "abracadabracabdab has no distinct 3-letter segments"
assert is_happy("abracadabracabdabracabd") == False, "abracadabracabdabd has no distinct 3-letter segments"
assert is_happy("bbb") == False
assert is_happy("ba") == False
assert is_happy("abbcdefghijk") == False
assert is_happy('abcabc') == True
assert is_happy('abcc') == False
assert is_happy('abccbc') == False
assert is_happy('abbcc') == False
assert is_happy('abbbcc') == False
assert is_happy('abbccc') == False
assert is_happy('abbbbcc') == False
assert is_happy('abbcccdef') == False
assert is_happy('abbbbcccde') == False
assert is_happy('abbcccdefg') == False
assert is_happy('abbbbcccdefgg') == False
assert is_happy('abbcccdefggg') == False
assert is_happy('abbcccdefggggg') == False
assert is_happy('abbbbcccdefggggggg') == False
assert is_happy('abbbbcccdefggggggggggg') == False
assert is_happy(" ") == False
assert is_happy('aaab') == False
assert is_happy('aabcc') == False
assert is_happy('abdabdabd') == True
assert is_happy("app") is False
assert is_happy("pp") is False
assert is_happy("pple") is False
assert is_happy("aaaa") is False
assert is_happy("apple") is False
assert is_happy("appple") is False
assert is_happy("aa") is False
assert is_happy("Happy Birthday") == False
assert is_happy("HAPPY birTHday") == False
assert is_happy("aaaabc") is False
assert is_happy("aabbcc") is False
assert is_happy("abbb") is False
assert is_happy("aaaaab") is False
assert is_happy("abbbbb") is False
assert is_happy("abccc") is False
assert is_happy("abbbbbc") is False
assert is_happy("aaabb") is False
assert is_happy("abbbbbbb") is False
assert is_happy("abbbccc") is False
assert is_happy("aaabbbccc") is False
assert is_happy("aabbcccddd") is False
assert is_happy("abbcccddd") is False
assert is_happy("abbcccdddeee") is False
assert is_happy("abbbcccdddeee") is False
assert is_happy("abbbbbbbbbbb") is False
assert is_happy("abbbcccdddd") is False
assert is_happy("abbbcccdddeeee") is False
assert is_happy("aaabbbcccdddeeee") is False
assert is_happy("aabbcccddddddd") is False
assert is_happy("aabbcccdddeeee") is False
assert is_happy("SHEEPINGSAKES") is False
assert is_happy("SHEEPINGSAKE") is False
assert is_happy("abc")
assert not is_happy("aab")
assert is_happy("happypp") == False
assert not is_happy("Happykay")
assert not is_happy("HappykayHappy")
assert not is_happy("HappykayHappykayHappy")
assert not is_happy("HappykayHappykayHappykayHappy")
assert is_happy('happypineapplefleflef') == False
assert is_happy('pineapplepineapple') == False
assert is_happy('apple') == False
assert is_happy('appleflefleflef') == False
assert is_happy('applefleflefle') == False
assert is_happy('appleflefleflefle') == False
assert is_happy("cba") is True
assert is_happy("bb") is False
assert is_happy("aaabbb") is False
assert is_happy("aaabbc") is False
assert is_happy("aaabbbb") is False
assert is_happy("aaaaaaaaaa") is False
assert is_happy("aba") ==  False
assert is_happy("aabc") ==  False
assert is_happy("e") ==  False
assert is_happy("ab") ==  False
assert is_happy("abaabc") ==  False
assert is_happy("abaabcde") == False
assert is_happy("abaabcdeabaabcde") == False
assert is_happy("aaaa") ==  False
assert is_happy("aaaaa") ==  False
assert is_happy("leetleet") == False
assert is_happy("leetleetcode") == False
assert is_happy("hello") ==  False
assert is_happy("hell0") ==  False
assert is_happy("hell0hell0hell0") == False
assert is_happy("leetlee") ==  False
assert is_happy("loveleet") == 0
assert not is_happy('aab')
assert not is_happy('aba')
assert not is_happy('')
assert not is_happy('a')
assert not is_happy('ba')
assert not is_happy("Happy Birthday to you!")
assert not is_happy("Happy Birthday")
assert not is_happy("Happy Birthday to you too")
assert not is_happy("Happy Birthday to you")
assert is_happy("aabc") == False
assert is_happy("aaaa") == False
assert is_happy("aaaaa") == False
assert is_happy("abcaabc") == False
assert is_happy("abcaab") == False
assert is_happy("abcabab") == False
assert is_happy("hello") == False
assert is_happy("happyleyyy") == 0
assert is_happy("happyleyyyyy") == 0
assert is_happy("happyleyyyzzz") == 0
assert is_happy("happyleyyyyzle") == 0
assert is_happy("happyleyyyzzzleyyy") == 0
assert is_happy("happyleyyyzzzleyyyyzle") == 0
assert is_happy("abaa") is False
assert is_happy("b") is False
assert is_happy("aaa") is False
assert is_happy("a") is False
assert not is_happy("happyp")
assert not is_happy("happys")
assert not is_happy("happypa")
assert not is_happy("happysa")
assert not is_happy("happyps")
assert not is_happy("happypaa")
assert not is_happy("happypsa")
assert is_happy('aba') == False
assert is_happy('aabba') == False
assert is_happy('abbabbaba') == False
assert is_happy('abbabbababaa') == False
assert is_happy("abcd"), "abcd"
assert is_happy('AA') == False
assert is_happy('abca')
assert is_happy("abca") == True
assert is_happy("abcabc") == True
assert is_happy("") == False
assert is_happy('ABCD') == True
assert is_happy('ABA') == False
assert is_happy('ABABA') == False
assert not is_happy("aaba")
assert not is_happy("aabcaaa")
assert not is_happy("aabaa")
assert not is_happy("a")
assert not is_happy("")
assert not is_happy("aaaaaaaa")
assert is_happy('abcabb') == False
assert is_happy("aa") == False
assert is_happy('abc') == True
assert is_happy("happypen") == False
assert is_happy("happyp") == False
assert is_happy("hapyp") == False
assert is_happy("Happy birthday!!") == False
assert is_happy("Happy bday") == False
assert is_happy("aaab") == False, "aaab"
assert is_happy("a") == False, "a"
assert is_happy("haphee") is False
assert is_happy("hahhee") is False
assert is_happy("hahheee") is False
assert is_happy("hahheeeee") is False
assert is_happy("ABAB") == False
assert is_happy("ABABABBA") == False
assert is_happy("abaabc") == False
assert is_happy("How")
assert not is_happy("Helloo")
assert not is_happy("Hellor")
assert not is_happy("Hellroo")
assert not is_happy("Hellrroo")
assert not is_happy("Hellrooo")
assert is_happy("Acute")
assert not is_happy("HappySad")
assert not is_happy("happy")
assert not is_happy("happyS")
assert not is_happy("HappyNice")
assert not is_happy("happySadNice")
assert not is_happy("abbacccddd")
assert not is_happy("aa")
assert is_happy('abcc') is False
assert is_happy('aa') is False
assert is_happy('aa') == False
assert is_happy('abacaba') == False
assert is_happy('abcabcabc') == True
assert is_happy("abced") == True
assert is_happy("bba") is False
assert is_happy("hAPpy")
assert not is_happy("happygg")
assert not is_happy("hhhhhh")
assert not is_happy("hhhhhhhhhhh")
assert is_happy('a'*100) == False
assert not is_happy('aabb')
assert not is_happy('abbabba')
assert not is_happy('aa')
assert not is_happy('aaaa')
assert not is_happy('baaba')
assert is_happy('rabracadaar') == False
assert is_happy("abaa") == False
assert is_happy("abaabb") == False
assert is_happy("ababab") == False
assert is_happy("happy dinner") == False
assert is_happy("babcb") == False
