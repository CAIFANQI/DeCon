
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
assert count_upper("") == 0
assert count_upper("Aaa") == 1
assert count_upper("AaA") == 2
assert count_upper("hey") == 0
assert count_upper("hi") == 0
assert count_upper("h") == 0
assert count_upper("AaBbCcDdEe") == 2
assert count_upper("cats") == 0
assert count_upper("I am a dumb dummy.") == 1
assert count_upper("A") == 1
assert count_upper("qwertyuiop") == 0
assert count_upper("abcAE") == 1
assert count_upper("a") == 0
assert count_upper("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 5
assert count_upper("h3ll0 w0r1d") == 0
assert count_upper("abcde") == 0, "count_upper fails on abcde"
assert count_upper("") == 0, "count_upper fails on empty string"
assert count_upper("Hi") == 0
assert count_upper(".") == 0
assert count_upper("Abc") == 1
assert count_upper("Aba") == 1, "Wrong Answer"
assert count_upper("AAAAAB") == 3
assert count_upper("AaAaAa") == 3
assert count_upper("bBbBbB") == 0
assert count_upper("apples") == 0
assert count_upper("EvenlyIndexed") == 2
assert count_upper("Oscar") == 1
assert count_upper("Oscar Wilde") == 1
assert count_upper("OSCAR WILDE") == 2
assert count_upper("wilde oscar") == 0
assert count_upper("oscar") == 0
assert count_upper("AbCdE") == 2
assert count_upper("abcde") == 0
assert count_upper("AbC") == 1
assert count_upper("ABa") == 1
assert count_upper("aB") == 0
assert count_upper("Aa") == 1
assert count_upper("AaAa") == 2
assert count_upper("AaAaAaAa") == 4
assert count_upper("aaaa") == 0
assert count_upper("XyA") == 1
assert count_upper("XYZ") == 0
assert count_upper("XYZxyz") == 0
assert count_upper("XYz") == 0
assert count_upper("XY") == 0
assert count_upper("X") == 0
assert count_upper("YZ") == 0
assert count_upper("XYZyz") == 0
assert count_upper("XyZ") == 0
assert count_upper("aaaaaaaa") == 0
assert count_upper("blue") == 0
assert count_upper("aEIOU") == 2
assert count_upper("AeIoUY") == 3
assert count_upper("aeiou") == 0
assert count_upper("aeiouyAEIOU") == 3
assert count_upper("BOo") == 0
assert count_upper("aBc") == 0
assert count_upper("eViL") == 0
assert count_upper("AeIoU") == 3
assert count_upper("aEio") == 0
assert count_upper("ABCDEFG") == 2
assert count_upper("abcdefg") == 0
assert count_upper("ABCDEFGabcdefg") == 2
assert count_upper("abcdefghijklmnopqrstuvwxyz") == 0
assert count_upper("hehehehe") == 0
assert count_upper("abaeiouuuuuAAbAEIOUUUU") == 5
assert count_upper("AEIoU") == 3
assert count_upper("abc") == 0
assert count_upper("aBcD") == 0
assert count_upper("aBCd") == 0
assert count_upper("aBcDe") == 0
assert count_upper("aBCdE") == 1
assert count_upper("aBcDeF") == 0
assert count_upper("aBCdEf") == 1
assert count_upper("Aba") == 1
assert count_upper("AaAeEiIoO") == 5
assert count_upper("Hello") == 0
assert count_upper("hElLo") == 0
assert count_upper("AaAA") == 2
assert count_upper("AAaaa") == 1
assert count_upper("123456789") == 0
assert count_upper("e") == 0
assert count_upper("aEiOu") == 0
assert count_upper("foo") == 0
assert count_upper("Joe") == 0
assert count_upper("This string has no vowels.") == 0
assert count_upper("!@#$%^&*()_+") == 0
assert count_upper("abcdE") == 1
assert 0 == count_upper('abcdefghijklmnopqrstuvwxyz')
assert count_upper("hello") == 0
assert count_upper("AI") == 1
assert count_upper("hell") == 0
assert count_upper("JavaScript") == 0
assert count_upper("EoIaU") == 3
assert count_upper("aBcDef") == 0, "Wrong number of uppercase"
assert count_upper("Hello, world!") == 0
assert count_upper("pickle") == 0
assert count_upper("AaBbCc") == 1
assert count_upper("abC") == 0
assert count_upper("ABc") == 1
assert count_upper("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH") == 0
assert count_upper("I") == 1
assert count_upper("eF") == 0
assert count_upper("ABCDEF") == 2
assert count_upper("abcdef") == 0
assert count_upper("E") == 1
assert count_upper("I have a car and a house.") == 1
assert count_upper("#hjb8*'^") == 0
assert count_upper("j") == 0
assert count_upper("this is a test") == 0
assert count_upper("WHAT IS GOING ON") == 3
assert count_upper("ok") == 0
assert count_upper("b") == 0
assert count_upper("c") == 0
assert count_upper("d") == 0
assert count_upper("f") == 0
assert count_upper("g") == 0
assert count_upper("i") == 0
assert count_upper("k") == 0
assert count_upper("l") == 0
assert count_upper("m") == 0
assert count_upper("n") == 0
assert count_upper("o") == 0
assert count_upper("p") == 0
assert count_upper("q") == 0
assert count_upper("r") == 0
assert count_upper("s") == 0
assert count_upper("t") == 0
assert count_upper("u") == 0
assert count_upper("v") == 0
assert count_upper("w") == 0
assert count_upper("x") == 0
assert count_upper("y") == 0
assert count_upper("z") == 0
assert count_upper("heLLo world") == 0
assert count_upper("Ab") == 1
assert count_upper("AbCd") == 1
assert count_upper("AbCdEfG") == 2
assert count_upper("abcdefghij") == 0
assert count_upper("eep") == 0
assert count_upper("ABCeO") == 2
assert count_upper("ABCeo") == 1
