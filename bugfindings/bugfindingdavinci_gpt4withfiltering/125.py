
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
assert split_words('hello,world') == ['hello', 'world']
assert split_words("You had me at hello world") == ['You', 'had', 'me', 'at', 'hello', 'world']
assert split_words("") == 0
assert split_words('Hello,world!') == ['Hello', 'world!']
assert split_words('A') == 0
assert split_words('AA') == 0
assert split_words('ab') == 1
assert split_words('ab6,def!') == ['ab6', 'def!']
assert split_words('ab6,def!ghi') == ['ab6', 'def!ghi']
assert split_words('I like python and cat') == ['I', 'like', 'python', 'and', 'cat']
assert split_words("one two three") == ["one", "two", "three"]
assert split_words("1,2,3") == ["1", "2", "3"]
assert split_words("a,bb,c,ddd,eee,ff") == ["a", "bb", "c", "ddd", "eee", "ff"]
assert split_words('Hi my name is Agamemnon!') == ['Hi', 'my', 'name', 'is', 'Agamemnon!']
assert split_words('The,answer,to,the,question,is,42.') == ['The', 'answer', 'to', 'the', 'question', 'is', '42.']
assert split_words("The,cat,sat,on,the,mat") == ['The', 'cat', 'sat', 'on', 'the', 'mat']
assert split_words("Hello World") == ['Hello', 'World']
assert split_words("Hello,World") == ['Hello', 'World']
assert split_words("Hel,lo,World") == ['Hel', 'lo', 'World']
assert split_words('My name is Killer') == ['My', 'name', 'is', 'Killer']
assert split_words("test some text") == ["test", "some", "text"], "test some text"
assert split_words('abc,defg') == ['abc', 'defg']
assert split_words('one,two,three,four,five,six,seven,eight,nine,ten') == ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
assert split_words('ten,nine,eight,seven,six,five,four,three,two,one') == ['ten', 'nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two', 'one']
assert split_words('one two three four five six seven eight nine ten') == ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
assert split_words("abcd efg hijk lmnop qrst uvwxyz") == ['abcd', 'efg', 'hijk', 'lmnop', 'qrst', 'uvwxyz']
assert split_words("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
assert split_words("The,quick,brown,fox,jumps,over,the,lazy,dog") == ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
assert split_words('We,love,python') == ['We', 'love', 'python']
assert split_words('hello my name is') == ['hello', 'my', 'name', 'is']
assert split_words('h,e,l,l,o,m,y,n,a,m,e,i,s') == ['h', 'e', 'l', 'l', 'o', 'm', 'y', 'n', 'a', 'm', 'e', 'i', 's']
assert split_words('abcdefghijklmnopqrstuvwxyz') == 13
assert split_words('abc def ghi') == ['abc', 'def', 'ghi']
assert split_words('this,is,a,test') == ['this', 'is', 'a', 'test']
assert split_words("Hello,world!") == ['Hello', 'world!']
assert split_words("Hello,world") == ['Hello', 'world']
assert split_words("Hello world!") == ['Hello', 'world!']
assert split_words('first second third fourth') == ['first', 'second', 'third', 'fourth']
assert split_words('I love python') == ['I', 'love', 'python']
assert split_words('this is a lot of words') == ['this', 'is', 'a', 'lot', 'of', 'words']
assert split_words('this is another test') == ['this', 'is', 'another', 'test']
assert split_words('I am testing your code') == ['I', 'am', 'testing', 'your', 'code']
assert split_words('oh hello') == ['oh', 'hello']
assert split_words('thisisasentencewith,commas') == ['thisisasentencewith', 'commas']
assert split_words("abc") == 1
assert split_words("abc def") == ["abc","def"]
assert split_words('hi there') == ['hi', 'there']
assert split_words('i am a good man') == ['i', 'am', 'a', 'good', 'man']
assert split_words("TODO,TODO") == ["TODO", "TODO"]
assert split_words("TODO TODO") == ["TODO", "TODO"]
assert split_words('this,is,a,simple,test') == ['this', 'is', 'a', 'simple', 'test']
assert split_words('Thank you for taking the time') == ['Thank', 'you', 'for', 'taking', 'the', 'time']
assert split_words("The,Biomedical,Engineer") == ['The', 'Biomedical', 'Engineer']
assert split_words("Hello this is a test") == ['Hello', 'this', 'is', 'a', 'test']
assert split_words("Hello,world") == ["Hello", "world"]
assert split_words('abc def') == ['abc', 'def']
assert split_words('abc,def') == ['abc', 'def']
assert split_words("This is a sample sentence.") == ["This", "is", "a", "sample", "sentence."]
assert split_words("This is") == ["This", "is"]
assert ['these', 'are', 'some', 'words'] == split_words('these,are,some,words')
assert split_words("Cat and doG") == ["Cat", "and", "doG"]
assert split_words("the,cat,is,cute") == ["the", "cat", "is", "cute"]
assert split_words('milk,chocolate') == ['milk', 'chocolate']
assert (split_words('hello,world') == ['hello', 'world'])
assert split_words("Today is a good day") == ['Today', 'is', 'a', 'good', 'day']
assert split_words("Hello,Iamastring") == ['Hello', 'Iamastring']
assert split_words('one,two,three') == ['one', 'two', 'three']
assert split_words("Python is a pretty powerful language") == ['Python', 'is', 'a', 'pretty', 'powerful', 'language']
assert split_words('aaa,bbb') == ['aaa', 'bbb']
assert split_words('aaa,bbb,ccc') == ['aaa', 'bbb', 'ccc']
assert split_words('13,13') == ['13', '13']
assert split_words('13,14') == ['13', '14']
assert split_words('abc,def,ghi') == ['abc', 'def', 'ghi']
assert split_words('hello world') == ['hello', 'world']
assert split_words('ThisIsATextWithSpacesAndCommas,AndCommas') == ['ThisIsATextWithSpacesAndCommas', 'AndCommas']
assert split_words('a,b,c') == ['a', 'b', 'c']
assert split_words('abcdefghijklmnopqrstuvwxyz,abcdefghijklmnopqrstuvwxyz') == ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz']
assert split_words('abcdefghijklmnopqrstuvwxyz,abcdefghijklmnopqrstuvwxyz,abcdefghijklmnopqrstuvwxyz') == ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz']
assert split_words('heLlOab') == 3
assert split_words('the,boy,came,in,to,the,store') == ['the', 'boy', 'came', 'in', 'to', 'the', 'store']
assert split_words("this is a test") == ["this", "is", "a", "test"]
assert split_words('This,is,an,example') == ['This', 'is', 'an', 'example']
assert split_words('Elma,Eve,Adam') == ['Elma', 'Eve', 'Adam']
assert split_words('0nc0,1nc1,2nc2') == ['0nc0', '1nc1', '2nc2']
assert split_words('0nc0,1nc1,2nc2,3nc3,4nc4,5nc5,6nc6,7nc7,8nc8,9nc9') == ['0nc0', '1nc1', '2nc2', '3nc3', '4nc4', '5nc5', '6nc6', '7nc7', '8nc8', '9nc9']
assert split_words("I,love,python") == ['I', 'love', 'python']
assert (split_words("This simple sentence has no whitespaces") == ['This', 'simple', 'sentence', 'has', 'no', 'whitespaces'])
assert (split_words("This,is,a,simple,sentence,with,no,whitespaces") == ['This', 'is', 'a', 'simple', 'sentence', 'with', 'no', 'whitespaces'])
assert split_words("This,is,a,test") == ['This', 'is', 'a', 'test']
assert split_words("Learning programming is fun.") == ['Learning', 'programming', 'is', 'fun.']
assert split_words('abc,bcd,efg') == ['abc', 'bcd', 'efg']
assert split_words("I,am,happy") == ["I", "am", "happy"]
assert split_words("Never gonna give you up") == ['Never', 'gonna', 'give', 'you', 'up']
assert split_words("This,is,a,comma,separated,list") == ['This', 'is', 'a', 'comma', 'separated', 'list']
assert split_words('hi,hello') == ['hi', 'hello']
assert split_words("Dogs,are,cute") == ["Dogs", "are", "cute"]
assert ['Hello', 'World'] == split_words('Hello,World')
assert split_words('hi,there') == ['hi', 'there']
assert split_words('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z') == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
assert split_words("word word2 word3") == ["word", "word2", "word3"]
assert ['The', 'cow', 'jumped', 'over', 'the', 'moon'] == split_words('The cow jumped over the moon')
assert split_words("some,txt,with,commas") == ['some', 'txt', 'with', 'commas']
assert split_words('this,is,the,second,test') == ['this', 'is', 'the', 'second', 'test']
assert split_words("Hello World!") == ["Hello", "World!"]
assert split_words('This is just a simple test') == ['This', 'is', 'just', 'a', 'simple', 'test']
assert split_words('Or at least I hope so') == ['Or', 'at', 'least', 'I', 'hope', 'so']
assert split_words('The quick brown fox jumps over the lazy dog') == ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
assert split_words('Hello World') == ['Hello', 'World']
assert split_words('Hello,World') == ['Hello', 'World']
assert split_words('Abc,De,fgh') == ['Abc', 'De', 'fgh']
assert split_words('Hello Wrld') == ['Hello', 'Wrld']
assert split_words('Hello,Wrld') == ['Hello', 'Wrld']
assert split_words('this is a test') == ['this', 'is', 'a', 'test']
assert split_words('now is the time') == ['now', 'is', 'the', 'time']
assert split_words('now,is,the,time') == ['now', 'is', 'the', 'time']
assert split_words('This,is,a,test') == ['This', 'is', 'a', 'test']
assert split_words('potatoes,tomatoes,onions,and,garlic') == ['potatoes', 'tomatoes', 'onions', 'and', 'garlic']
assert split_words("Invalid: no whitespace") == ['Invalid:', 'no', 'whitespace']
assert split_words("A single word") == ['A', 'single', 'word']
assert ['hello','world','my','name','is','luis'] == split_words('hello,world,my,name,is,luis')
assert split_words('xyz') == 2
assert split_words('This,is,a,sentence') == ['This', 'is', 'a', 'sentence']
assert split_words('Hello world!') == ['Hello', 'world!']
assert split_words('my,name,is,Eliyahu') == ['my', 'name', 'is', 'Eliyahu']
assert split_words('my name is Eliyahu') == ['my', 'name', 'is', 'Eliyahu']
assert split_words("21,cat,dog") == ["21", "cat", "dog"]
assert split_words('the,fox,jumped,over,the,lazy,dog') == ['the', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
assert split_words("i like pie") == ["i", "like", "pie"]
assert split_words("I like pie") == ["I", "like", "pie"]
assert (split_words("hello there world") == ["hello", "there", "world"])
assert (split_words("the,the") == ["the", "the"])
assert (split_words("the the the") == ["the", "the", "the"])
assert (split_words("the the") == ["the", "the"])
assert split_words('lorem,ipsum,dolor,sit,amet') == ['lorem', 'ipsum', 'dolor', 'sit', 'amet']
