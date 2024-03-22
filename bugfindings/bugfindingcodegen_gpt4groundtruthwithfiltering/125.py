
def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(' ',',').split()
    else:
        return len([i for i in txt if i.islower() and ord(i)%2 == 0])
assert 	split_words("a b c d e f g h") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
assert 	split_words('This is another test') == ['This', 'is', 'another', 'test']
assert 	split_words('one,two,three') == ['one', 'two', 'three']
assert 	split_words('a,b,c,d') == ['a', 'b', 'c', 'd']
assert 	split_words('one,two,three,four,five,six') == ['one', 'two', 'three', 'four', 'five','six']
assert 	split_words('abcde,fghij,klmno,pqrst,uvwxy,z') == ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'z']
assert 	split_words('ab,cdefghijklmnopqrstuvwxyz') == ['ab', 'cdefghijklmnopqrstuvwxyz']
assert 	split_words('ab,cdefghijklmnopqrstuvwxy') == ['ab', 'cdefghijklmnopqrstuvwxy']
assert 	split_words('abc,def,ghijklmnopqrstuvwxyz') == ['abc', 'def', 'ghijklmnopqrstuvwxyz']
assert 	split_words('abc,def,ghijklmnopqrstuvwxy') == ['abc', 'def', 'ghijklmnopqrstuvwxy']
assert 	split_words('abc def') == ['abc', 'def']
assert split_words('abc,de,fgh') == ['abc', 'de', 'fgh']
assert split_words('a,bc') == ['a', 'bc']
assert split_words('abc,de') == ['abc', 'de']
assert split_words('abcde,fghij') == ['abcde', 'fghij']
assert split_words('abcdef,fghij') == ['abcdef', 'fghij']
assert split_words('abcdef,fghij,l') == ['abcdef', 'fghij', 'l']
assert 	split_words("abc,def") == ['abc', 'def']
assert 	split_words('a,b,c,d,e') == ['a', 'b', 'c', 'd', 'e']
assert 	split_words('a,b,c,d,e,f,g') == ['a', 'b', 'c', 'd', 'e', 'f', 'g']
assert 	split_words('a,b,c,d,e,f,g,h') == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
assert 	split_words('a,b,c,d,e,f,g,h,i') == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
assert 	split_words('a,b,c,d,e,f,g,h,i,j') == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
assert 	split_words('four,five') == ['four', 'five']
assert 	split_words('six seven eight') == ['six','seven', 'eight']
assert 	split_words('nine ten eleven twelve') == ['nine', 'ten', 'eleven', 'twelve']
assert 	split_words('thirteen fourteen fifteen sixteen') == ['thirteen', 'fourteen', 'fifteen','sixteen']
assert 	split_words('seventeen eighteen nineteen twenty') == ['seventeen', 'eighteen', 'nineteen', 'twenty']
assert 	split_words('twenty one') == ['twenty', 'one']
assert 	split_words('twenty one twenty') == ['twenty', 'one', 'twenty']
assert 	split_words('twenty one twenty one') == ['twenty', 'one', 'twenty', 'one']
assert 	split_words("one,two,three") == ["one", "two", "three"]
assert 	split_words("one,two,three,four,five") == ["one", "two", "three", "four", "five"]
assert 	split_words("one,two,three") == ['one', 'two', 'three']
assert 	split_words("one,two,three,four,five,six,seven") == ['one', 'two', 'three', 'four', 'five','six','seven']
assert 	split_words("one,two,three,four,five,six,seven,eight") == ['one', 'two', 'three', 'four', 'five','six','seven', 'eight']
assert 	split_words("one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty") == ['one', 'two', 'three', 'four', 'five','six','seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen','sixteen','seventeen', 'eighteen', 'nineteen', 'twenty']
assert 	split_words('a,b') == ['a', 'b']
assert 	split_words('a,b,c') == ['a', 'b', 'c']
assert 	split_words('a b c') == ['a', 'b', 'c']
assert 	split_words('abc,def,ghi') == ['abc', 'def', 'ghi']
assert 	split_words("Do you want to build a snowman?") == ['Do', 'you', 'want', 'to', 'build', 'a','snowman?'], 'ERROR: Wrong answer for input: "Do you want to build a snowman?"'
