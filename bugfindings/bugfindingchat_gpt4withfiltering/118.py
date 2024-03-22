
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
assert get_closest_vowel("hello") == "e"
assert get_closest_vowel("orange") == "a"
assert get_closest_vowel("strawberry") == "e"
assert get_closest_vowel('world') == 'o'
assert get_closest_vowel('xylophone') == 'o'
assert get_closest_vowel('rhythm') == ''
assert get_closest_vowel("world") == "o"
assert get_closest_vowel("python") == "o"
assert get_closest_vowel("cherry") == "e"
assert get_closest_vowel("apple") == ""
assert get_closest_vowel("book") == ""
assert get_closest_vowel("cat") == "a"
assert get_closest_vowel("dog") == "o"
assert get_closest_vowel("fish") == "i"
assert get_closest_vowel("yellow") == "o"
assert get_closest_vowel("grapefruit") == "e"
assert get_closest_vowel("watermelon") == "o"
assert get_closest_vowel("blueberry") == "e"
assert get_closest_vowel("raspberry") == "e"
assert get_closest_vowel("plum") == "u"
assert get_closest_vowel("fig") == "i"
assert get_closest_vowel("date") == "a"
assert get_closest_vowel("pomegranate") == "a"
assert get_closest_vowel("tangerine") == "i"
assert get_closest_vowel("mango") == "a"
assert get_closest_vowel("jupyter") == "e"
assert get_closest_vowel("grape") == "a"
assert get_closest_vowel("vowel") == "e"
assert get_closest_vowel("string") == "i"
assert get_closest_vowel('grape') == 'a'
assert get_closest_vowel('blueberry') == 'e'
assert get_closest_vowel('watermelon') == 'o'
assert get_closest_vowel('cherry') == 'e'
assert get_closest_vowel("elephant") == "a"
assert get_closest_vowel('python') == 'o'
assert get_closest_vowel('engineering') == 'i'
assert get_closest_vowel('statistics') == 'i'
assert get_closest_vowel('xyz') == ''
assert get_closest_vowel("xylophone") == "o"
assert get_closest_vowel("rhythm") == ""
assert get_closest_vowel("engineering") == "i"
assert get_closest_vowel("statistics") == "i"
assert get_closest_vowel("analysis") == "i"
assert get_closest_vowel("structure") == "u"
assert get_closest_vowel("orange") == 'a'
assert get_closest_vowel("strawberry") == 'e'
assert get_closest_vowel("cherry") == 'e'
assert get_closest_vowel("grape") == 'a'
assert get_closest_vowel("lemon") == "o"
assert get_closest_vowel('computer') == 'e'
assert get_closest_vowel('machine') == 'i'
assert get_closest_vowel('learning') == 'i'
assert get_closest_vowel('hello world') == 'o'
assert get_closest_vowel('test') == 'e'
assert get_closest_vowel('closest') == 'e'
assert get_closest_vowel('stand') == 'a'
assert get_closest_vowel("programming") == "i"
assert get_closest_vowel("ruby") == "u"
assert get_closest_vowel('laptop') == 'o'
assert get_closest_vowel('desktop') == 'o'
assert get_closest_vowel('tablet') == 'e'
assert get_closest_vowel('phone') == 'o'
assert get_closest_vowel('speaker') == 'e'
assert get_closest_vowel('headphones') == 'e'
assert get_closest_vowel('microphone') == 'o'
assert get_closest_vowel('light') == 'i'
assert get_closest_vowel('fan') == 'a'
assert get_closest_vowel('oven') == 'e'
assert get_closest_vowel('stove') == 'o'
assert get_closest_vowel('washing') == 'i'
assert get_closest_vowel('dryer') == 'e'
assert get_closest_vowel('cleaner') == 'e'
assert get_closest_vowel('carpet') == 'e'
assert get_closest_vowel('shampoo') == 'a'
assert get_closest_vowel('toothbrush') == 'u'
assert get_closest_vowel('towel') == 'e'
assert get_closest_vowel('paper') == 'e'
assert get_closest_vowel('tissue') == 'i'
assert get_closest_vowel('pen') == 'e'
assert get_closest_vowel('pencil') == 'i'
assert get_closest_vowel('ruler') == 'e'
assert get_closest_vowel("apricot") == "o"
assert get_closest_vowel("nectarine") == "i"
assert get_closest_vowel("pear") == ""
assert get_closest_vowel("lime") == "i"
assert get_closest_vowel("cashew") == "e"
assert get_closest_vowel("almond") == "o"
assert get_closest_vowel("pecan") == "a"
assert get_closest_vowel("hazelnut") == "u"
assert get_closest_vowel('orange') == 'a'
assert get_closest_vowel('strawberry') == 'e'
assert get_closest_vowel('pear') == ''
assert get_closest_vowel('lemon') == 'o'
assert get_closest_vowel('lime') == 'i'
assert get_closest_vowel("melon") == "o"
assert get_closest_vowel("sky") == ""
assert get_closest_vowel("gym") == ""
assert get_closest_vowel('frog') == 'o'
assert get_closest_vowel("consonant") == "a"
assert get_closest_vowel("close") == "o"
assert get_closest_vowel("empty") == ""
assert get_closest_vowel("English") == "i"
assert get_closest_vowel("xyz") == ""
assert get_closest_vowel("jupiter") == "e"
assert get_closest_vowel("rabbit") == "i"
assert get_closest_vowel("snake") == "a"
assert get_closest_vowel("turtle") == "u"
assert get_closest_vowel("umbrella") == "e"
assert get_closest_vowel("violin") == "i"
assert get_closest_vowel("zebra") == "e"
assert get_closest_vowel("pistachio") == "a"
assert get_closest_vowel("acorn") == "o"
assert get_closest_vowel("corn") == "o"
assert get_closest_vowel("carrot") == "o"
assert get_closest_vowel("cucumber") == "e"
assert get_closest_vowel("pepper") == "e"
assert get_closest_vowel("garlic") == "i"
assert get_closest_vowel("turmeric") == "i"
assert get_closest_vowel("cardamom") == "o"
assert get_closest_vowel("milk") == "i"
assert get_closest_vowel("salt") == "a"
assert get_closest_vowel("cumin") == "i"
assert get_closest_vowel("paprika") == "i"
assert get_closest_vowel("oregano") == "a"
assert get_closest_vowel("parsley") == "e"
assert get_closest_vowel("sage") == "a"
assert get_closest_vowel("mint") == "i"
assert get_closest_vowel("dill") == "i"
assert get_closest_vowel("fennel") == "e"
assert get_closest_vowel("lavender") == "e"
assert get_closest_vowel("rose") == "o"
assert get_closest_vowel("tulip") == "i"
assert get_closest_vowel("lily") == "i"
assert get_closest_vowel("mouse") == ""
assert get_closest_vowel("jungle") == "u"
assert get_closest_vowel("nut") == "u"
assert get_closest_vowel("bottle") == "o"
