
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count += 2
    return count
assert count_upper("a") == 0
assert count_upper("") == 0
assert count_upper(' ') == 0
assert count_upper('hi') == 0
assert count_upper('hihi') == 0
assert count_upper('ABCDEFGHI') == 3
assert count_upper('ABCDEFGHIJ') == 3
assert count_upper('ABCDEFGHIJK') == 3
assert count_upper('ABCDEFGHIJKL') == 3
assert count_upper('ABCDEFGHIJKLM') == 3
assert count_upper("python") == 0
assert count_upper("abE") == 1
assert count_upper("HELLO ") == 1
assert count_upper('a') == 0
assert count_upper('') == 0
assert count_upper("HELLOWORLD") == 2
assert count_upper("H") == 0
assert count_upper("He") == 0
assert count_upper("hello") == 0
assert count_upper('  a') == 0
assert count_upper("") ==  0
assert count_upper('a') == 0 
assert count_upper('aa') == 0
assert count_upper('aaa') == 0
assert count_upper('BBB') == 0
assert count_upper('bbb') == 0
assert count_upper('bbbb') == 0
assert count_upper('bbB') == 0
assert count_upper('Bbbb') == 0
assert count_upper('BbBb') == 0
assert count_upper('bBBb') == 0
assert count_upper('BBBBb') == 0
assert count_upper('ae') == 0
assert count_upper('aeA ') == 1
assert count_upper('aeA A') == 2
assert count_upper('aeA A A A') == 4
assert count_upper('aeAeAeAeAeAeAe') == 6
assert count_upper('ab') == 0
assert count_upper('aaab') == 0
assert count_upper('e') == 0
assert count_upper("a")==0
assert count_upper("abc")==0
assert count_upper("A B C D")==1
assert count_upper("i") == 0
assert count_upper("oops") == 0
assert count_upper("aA") == 0
assert count_upper("aBBB") == 0
assert count_upper("aaa") == 0
assert count_upper("aba") == 0
assert count_upper("bbb") == 0
assert count_upper("cccc") == 0
assert count_upper("d") == 0
assert count_upper("eee") == 0
assert count_upper("fff") == 0
assert count_upper("GGGGGGGGGGG") == 0
assert count_upper("GGGGGGGGGGGGG") == 0
assert count_upper("BB") == 0
assert count_upper("TTTTT") == 0
assert count_upper("CCC") == 0
assert count_upper("DDDD") == 0
assert count_upper("FFFF") == 0
assert count_upper("GGGGGGGGGGGGGGGGGG") == 0
assert count_upper("BBBBBBBBBBBBBBBBBBBBBB") == 0
assert count_upper('nopqrstuvwxyz') == 0
assert count_upper('x') == 0
assert count_upper("bB") == 0
assert count_upper("Bb") == 0
assert count_upper("abbabba") == 0
assert count_upper("abBABba") == 0
assert count_upper("abBABbA") == 1
assert count_upper("abbbABBABBAA") == 2
assert count_upper("aBBBbA") == 0
assert count_upper("aBBBBBBB") == 0
assert count_upper("abBBB") == 0
assert count_upper("abBBBbb") == 0
assert count_upper("abbbB") == 0
assert count_upper("abbbBB") == 0
assert count_upper("aBBBB") == 0
assert count_upper("aBBBBb") == 0
assert count_upper("BBBB") == 0
assert count_upper("BBBBB") == 0
assert count_upper("abBcC") == 0
assert count_upper("abcABc") == 0
assert count_upper("abBCc") == 0
assert count_upper("abA") == 1
assert count_upper("B") == 0
assert count_upper("AaBbCcDdEeF") == 2
assert count_upper("aeiou") == 0
assert count_upper("Aa") == 1
assert count_upper("AaAa") == 2
assert count_upper("") == 0, "empty string"
assert count_upper('abC') == 0
assert count_upper('abCa') == 0
assert count_upper("bar") == 0
assert count_upper("Goodbye") == 0
assert count_upper("CAAuAuA!") == 3
assert count_upper(s = "abracadabra") == 0
assert count_upper("qwertyuiop") == 0
assert count_upper("abc") == 0
assert count_upper("AB") == 1
assert count_upper(" ") == 0
assert count_upper("Z") == 0
assert count_upper(" ") == 0, "count_upper"
assert count_upper('WTF?') == 0
assert count_upper("bbaacc") == 0
assert count_upper("abCdefg") == 0
assert count_upper("Q") == 0, "Count upper case with single letter"
