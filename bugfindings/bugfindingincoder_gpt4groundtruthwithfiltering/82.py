
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(3, l):
        if l % i == 0:
            return False
    return True
assert prime_length('2') == False
assert prime_length('10') == True
assert prime_length('12') == True
assert prime_length('14') == True
assert prime_length('16') == True
assert prime_length('18') == True
assert prime_length('20') == True
assert prime_length('22') == True
assert prime_length('24') == True
assert prime_length('26') == True
assert prime_length('28') == True
assert prime_length('30') == True
assert prime_length('32') == True
assert prime_length("10") == True
assert prime_length("11") == True
assert prime_length("12") == True
assert prime_length("13") == True
assert prime_length("14") == True
assert prime_length("15") == True
assert prime_length("16") == True
assert prime_length("17") == True
assert prime_length("18") == True
assert prime_length("19") == True
assert prime_length("20") == True
assert prime_length("21") == True
assert prime_length("22") == True
assert prime_length("23") == True
assert prime_length("24") == True
assert prime_length("25") == True
assert prime_length("26") == True
assert prime_length("27") == True
assert prime_length("28") == True
assert prime_length("29") == True
assert prime_length("30") == True
assert prime_length("31") == True
assert prime_length("32") == True
assert prime_length("aa") == True
assert prime_length("ab") == True
assert prime_length("abc") == True
assert prime_length("abcde") == True
assert prime_length("abcdeaa") == True
assert prime_length("abcdeaabcde") == True
assert prime_length("abcdeaabcdeaa") == True
assert prime_length("abcdeaabcdeaabcde") == True
assert prime_length("abcdeaabcdeaabcdeaa") == True
assert prime_length("abcdeaabcdeaabcdeaabcde") == True
assert prime_length("2") == False
assert prime_length("6") == False
assert prime_length("33") == True
assert prime_length("34") == True
assert prime_length('abcde') == True
assert prime_length('abcdef') == False
assert prime_length('abc') == True
assert prime_length('') == False
assert prime_length('a') == False
assert prime_length('aba') == True
assert prime_length('abba') == False
assert prime_length('abbbb') == True
assert prime_length('abbbba') == False
assert prime_length('abbbbbb') == True
assert prime_length('abbbbbba') == False
assert prime_length('abbbbbbbbb') == False
assert prime_length('x') is False
assert prime_length('abbbcbca') is False
assert prime_length('abbbcbcdef') is False
assert prime_length('abbbcbcdefgh') is False
assert prime_length('abbbcbcdefghiabc') is False
assert prime_length('abbasafafafaf') == True
assert prime_length('abbasafafafafaf') == False
assert prime_length('abbasafafafafafafafafaf') == True
assert prime_length('abbasafafafafafafafafafafaf') == False
assert prime_length('abb') == True
assert prime_length('aabb') == False
assert prime_length('aabba') == True
assert prime_length('abbaba') == False
assert prime_length('abbabab') == True
assert prime_length('abbabababab') == True
assert prime_length('abbababababab') == True
assert prime_length('abbababababababab') == True
assert prime_length('abbabababababababab') == True
assert prime_length('abbabababababababababab') == True
assert prime_length('abbababababababababababababab') == True
assert prime_length('ab') == True
assert prime_length('abcdefghijk') == True
assert prime_length('abcdefghijklm') == True
assert prime_length('abcdefghijklmnopqrs') == True
assert prime_length('abcdefghijklmnopqrst') == False
assert prime_length('abcdefghijklmnopqrstuvw') == True
assert prime_length('abcdefghijklmnopqrstuvwx') == False
assert prime_length('12345678901') == True
assert prime_length('1234567890123') == True
assert prime_length('12345678901234567891') == False
assert prime_length('abba') is False
assert prime_length('abbab') is True
assert prime_length('abbaabbb') is False
assert prime_length('abbaabbba') is False
assert prime_length('abbaabbbbbbbbb') is False
assert prime_length('abbaabbbbbbbbbb') is False
assert prime_length('abbaabbbbbbbbbbb') is False
assert prime_length('abbaabbbbbbbbbbbbbbbbb') is False
assert prime_length('abbaabbbbbbbbbbbbbbbbbbb') is False
assert prime_length('abca') == False
assert prime_length('bcbb') == False
assert prime_length('ccbb') == False
assert prime_length('abcdefg') == True
assert prime_length('abcdefghi') == False
assert prime_length('abcdefghij') == False
assert prime_length('abcdefghijkl') == False
assert prime_length('abcdefghijklmn') == False
assert prime_length('abcdefghijklmno') == False
assert prime_length('abcdefghijklmnop') == False
assert prime_length("1") == False
assert prime_length("123456789") == False
assert prime_length("abcde1") == False
assert prime_length("abcde123456789") == False
assert prime_length("abcdefg1") == False
assert prime_length("abcdefg12") == False
assert prime_length("abcdefg123456789") == False
assert prime_length("1abc") == False
assert prime_length("123456789abc") == False
assert prime_length("1abcde") == False
assert prime_length("1abcde12") == False
assert prime_length("1abcde123456789") == False
assert prime_length("1abcdefg") == False
assert prime_length("1abcdefg1") == False
assert prime_length("1abcdefg12") == False
assert prime_length('aaab') == False
assert prime_length('aaaabb') == False
assert prime_length('aaaabbcd') == False
assert prime_length('abbccdd') == True
assert prime_length('bbbccdd') == True
assert prime_length('bbbbbccddbbba') == True
assert prime_length('bbbbbccddbbbaabbc') == True
assert prime_length('bbbbbccddbbbaabbcab') == True
assert prime_length("0") is False
assert prime_length("1") is False
assert prime_length("9") is False
assert prime_length("abba") is False
assert prime_length("abcdeabba") is False
assert prime_length("abbaabcde") is False
assert prime_length("abbaabbcd") is False
assert prime_length("abbaabbccd") is False
assert prime_length("abbaabbccdde") is False
assert prime_length("abbaabbccddeef") is False
assert prime_length("abbaabbccddeefg") is False
assert prime_length("abbaabbccddeefgh") is False
assert prime_length("abbaabbccddeefghij") is False
assert prime_length("abbaabbccddeefghijkl") is False
assert prime_length("123456789") is False
assert prime_length("111") == True
assert prime_length("131") == True
assert prime_length("11131") == True
assert prime_length("1311131") == True
assert prime_length("13111313131") == True
assert prime_length("1311131313131") == True
assert prime_length("3") == False
assert prime_length("4") == False
assert prime_length("37") == True
assert prime_length("38") == True
assert prime_length("41") == True
assert prime_length("47") == True
assert prime_length("48") == True
assert prime_length("59") == True
assert prime_length("60") == True
assert prime_length("61") == True
assert prime_length("62") == True
assert prime_length("67") == True
assert prime_length("71") == True
assert prime_length("72") == True
assert prime_length("73") == True
assert prime_length('abac') == False
assert prime_length('abacab') == False
assert prime_length('abacaba') == True
assert prime_length('abacabacaba') == True
assert prime_length('abacabacabacaba') == False
assert prime_length("12345") == True
assert prime_length("12347") == True
assert prime_length("z") == False
assert prime_length("") == False
assert prime_length("123451") == False
assert prime_length("1234567890") == False
assert prime_length("1234567890123") == True
assert prime_length("12345678901234") == False
assert prime_length("12345678901234567890") == False
assert prime_length("123456789012345678901") == False
assert prime_length("12345678901234567890123") == True
assert prime_length("123456789012345678901234") == False
assert prime_length("123456789012345678901234567890") == False
assert prime_length("hello") == True
assert prime_length('aabbba') == False
assert prime_length('abcabd') == False
assert prime_length('abdabd') == False
assert prime_length('abdabdabd') == False
assert prime_length('abdabdabdabdabd') == False
assert prime_length('abdabdabdabdabdabd') == False
assert prime_length('abdabdabdabdabdabdabd') == False
assert prime_length('abdabdabdabdabdabdabdabd') == False
assert prime_length(' ') == False
assert prime_length('abbbbc') == False
assert prime_length('abbbbccc') == False
assert prime_length('abbbbccce') == False
assert prime_length('abbbbbbbbc') == False
assert prime_length('abbbbbbbbbccf') == True
assert prime_length('abbbbbbbbbbbbbbbbbbbbccc') == False
assert prime_length('abbbbbbbbbbbbbbbbbbbbccce') == False
assert prime_length('abbbbbbbbbbbbbbbbbbbbcce') == False
assert prime_length('abcd') == False
assert prime_length('abcc') == False
assert prime_length('abbb') == False
assert prime_length('abbab') == True
assert prime_length('abbababbbaaa') == False
assert prime_length('abcdeabcdeab') == False
assert prime_length('abeab') == True
assert prime_length('abeabeabec') == False
assert prime_length('abeabeabecda') == False
assert prime_length('abs') == True
assert prime_length('abcabcdefab') == True
assert prime_length('abdceee') == True
assert prime_length('abcedee') == True
assert prime_length('abccdeee') == False
assert prime_length('abcccdeee') == False
assert prime_length('abcccdeeeef') == True
assert prime_length('abcccdeeeeee') == False
assert prime_length('abcccdeeeeeeee') == False
assert prime_length('abcccdeeeeeeeee') == False
assert prime_length('abcccdeeeeeeeeee') == False
assert prime_length('aa') == True
assert prime_length("aaa") == True
assert prime_length("bbbb") == False
assert prime_length("abba") == False
assert prime_length("abbaabba") == False
assert prime_length("aabb") == False
assert prime_length("abbaabbaabba") == False
assert prime_length("aaaa") == False
assert prime_length("aaaaa") == True
assert prime_length("aaaaaaa") == True
assert prime_length("aaaaaaaaaaa") == True
assert prime_length("aaaaaaaaaaaaa") == True
assert prime_length("aaaaaaaaaaaaaaaaa") == True
assert prime_length("aaaaaaaaaaaaaaaab") == True
assert prime_length("4234") == False
assert prime_length("1212") == False
assert prime_length("1230000") == True
assert prime_length("1230012") == True
assert prime_length("123001234") == False
assert prime_length("120000000000000000000000") == False
assert prime_length('abcd') is False
assert prime_length('aa') is True
assert prime_length('abac') is False
assert prime_length('abfg') is False
assert prime_length('abcefg') is False
assert prime_length('abdf') is False
assert prime_length('abde') is False
assert prime_length('abdefg') is False
assert prime_length('abdfgh') is False
assert prime_length("45") == True
assert prime_length("50") == True
assert prime_length("153") == True, "153 is not a prime number"
assert prime_length("1") == False, "1 is not a prime number"
assert prime_length("5") == False, "5 is not a prime number"
assert prime_length("35") == True, "35 is a prime number"
assert prime_length("55") == True, "55 is a prime number"
assert prime_length("66") == True, "66 is a prime number"
assert prime_length("77") == True, "77 is a prime number"
assert prime_length("111111") == False, "111111 is not a prime number"
assert prime_length('abcabcdefdefdef') == False
assert prime_length('abc') is True
assert prime_length('a') is False
assert prime_length("100") == True
assert prime_length("1000") == False
assert prime_length('12345') == True
assert prime_length("a") == False
assert prime_length("a123") == False
assert prime_length('') is False
assert prime_length("2") is False
assert prime_length("5") is False
assert prime_length("55") is True
assert prime_length("asdf1") == True
assert prime_length("1234567") == True
assert prime_length("1234567890123456") == False
assert prime_length("123456789012345678") == False
assert prime_length("12345678901234567899") == False
assert prime_length("123456789012345678990") == False
assert prime_length('a' * 1001) == False
assert prime_length('abdef') == True
assert prime_length('abe') == True
assert prime_length('abeef') == True
assert prime_length('abef') == False
assert prime_length('abefef') == False
assert prime_length('abbccd') == False
assert prime_length('abccd') == True
assert prime_length('abccddcba') == False
assert prime_length("abcd") == False
assert prime_length("a" * 10) == False
assert prime_length("a" * 8) == False
assert prime_length("a") is False
assert prime_length("") is False
assert prime_length("test12") is False
assert prime_length("test12abc") is False
assert prime_length("test123") is True
assert prime_length("test12test") is False
assert prime_length('abab') == False
assert prime_length('abcabca') == True
assert prime_length('42.0') is False
assert prime_length('4') is False
assert prime_length('42 hello') is False
assert prime_length('42 hello world') is False
assert prime_length('hi') == True
assert prime_length('hey') == True
assert prime_length('hiya') == False
assert prime_length('hiyaa') == True
assert prime_length('hiyaba') == False
assert not prime_length('')
assert not prime_length('1')
assert prime_length("11112") == True, "11112"
assert prime_length("11112233") == False, "11112233"
assert prime_length('abc')
assert prime_length("bb") == True
assert prime_length("c") == False
assert prime_length("ccc") == True
assert prime_length("bca") == True
assert prime_length("aA") == True
assert prime_length('abbcccbdbdaebabae') == True
assert prime_length('123') == True
assert prime_length('9') == False
assert prime_length("9") == False
assert prime_length("121") == True
assert prime_length("2345") == False
assert prime_length("1238") == False
assert prime_length("143") == True
assert prime_length("1438") == False
assert prime_length("131717") == False
assert prime_length("163") == True
assert prime_length("16384") == True
assert prime_length("abbbc") == True
assert prime_length("hi")
assert not prime_length("hihi")
assert prime_length("a") == False, "String should contain an even number"
assert prime_length("122") == True
assert prime_length('789')
assert prime_length('12345678901')
