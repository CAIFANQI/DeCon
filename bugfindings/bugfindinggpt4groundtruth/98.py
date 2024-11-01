
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
assert count_upper('abc') == 0
assert count_upper('aBc') == 0
assert count_upper("abcde") == 0
assert count_upper("AbCdEf") == 2
assert 	count_upper("ABCD") == 1
assert 	count_upper("aBcdEfgh") == 1
assert 	count_upper("z") == 0
assert 	count_upper("") == 0
assert 	count_upper("1234") == 0
assert 	count_upper("1234!@#$%^&*()_+") == 0
assert 	count_upper('Hello') == 0
assert 	count_upper('hello world') == 0
assert count_upper('foobarBaz') == 0
assert count_upper('fooBarBaz') == 0
assert count_upper('FOObar') == 1
assert count_upper('FOOBar') == 1
assert count_upper('FoobarBaz') == 0
assert count_upper('Foobarbaz') == 0
assert count_upper('foobarbaz') == 0
assert count_upper('foobarBaz.') == 0
assert count_upper('foobar.') == 0
assert count_upper('foobar..') == 0
assert count_upper('.FOOBAR.') == 1
assert count_upper('.FOOBAR..') == 1
assert count_upper('.FOOBAR...') == 1
assert count_upper('...FOOBAR...') == 1
assert count_upper('Do not count') == 0
assert count_upper('Count, count, count, count!') == 0
assert 	count_upper("LIFE") == 0
assert 	count_upper("xXxXxXxXxX") == 0
assert 	count_upper(" ") == 0
assert 	count_upper("S") == 0
assert 	count_upper("s") == 0
assert 	count_upper("ss") == 0
assert 	count_upper("Ss") == 0
assert 	count_upper("sSs") == 0
assert 	count_upper("sSSs") == 0
assert 	count_upper("sSss") == 0
assert 	count_upper("sSsSs") == 0
assert 	count_upper("sSsSsS") == 0
assert 	count_upper("sSsSsSs") == 0
assert 	count_upper("sSsSsSsSs") == 0
assert 	count_upper('aA') == 0, 'Wrong answer for "aA"'
assert 	count_upper('abcde') == 0, 'Wrong answer for "abcde"'
