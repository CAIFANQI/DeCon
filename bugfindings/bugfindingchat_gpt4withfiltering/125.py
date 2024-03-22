
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
assert split_words('hello world') == ['hello', 'world']
assert split_words('hello,world') == ['hello', 'world']
assert split_words("hello,world") == ["hello", "world"], "Test case 2 failed"
assert split_words("") == 0, "Test case 6 failed"
assert split_words("Hello,world") == ["Hello", "world"]
assert split_words("hello,world") == ["hello", "world"]
assert split_words("hello,world") == ['hello', 'world']
assert split_words("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
assert split_words('h,e,l,l,o,w,o,r,l,d') == ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
assert split_words("helloworld") == 6
assert split_words("hello,world,how,are,you") == ["hello", "world", "how", "are", "you"]
assert split_words("a,b,c") == ['a', 'b', 'c']
assert split_words('ABCDE') == 0
assert split_words('a,b,c,d,e') == ['a', 'b', 'c', 'd', 'e']
assert split_words('a,b,c,d,e,f') == ['a', 'b', 'c', 'd', 'e', 'f']
assert split_words("Hello,world") == ['Hello', 'world']
assert split_words("Hello,world!") == ["Hello", "world!"]
assert split_words("Hello,world!!") == ["Hello", "world!!"]
assert split_words('hello,world,how,are,you') == ['hello', 'world', 'how', 'are', 'you']
assert split_words('hello world how are you') == ['hello', 'world', 'how', 'are', 'you']
assert split_words('helloworld,howareyou') == ['helloworld', 'howareyou']
assert split_words('hello,worldhowareyou') == ['hello', 'worldhowareyou']
assert split_words('helloworldhow,areyou') == ['helloworldhow', 'areyou']
assert split_words('helloworldhow,areyou,doing') == ['helloworldhow', 'areyou', 'doing']
assert split_words('helloworldhow,areyou,doing,today') == ['helloworldhow', 'areyou', 'doing', 'today']
assert split_words('helloworldhow,areyou,doing,today,myfriend') == ['helloworldhow', 'areyou', 'doing', 'today', 'myfriend']
assert split_words('helloworldhow,areyou,doing,today,my,friend') == ['helloworldhow', 'areyou', 'doing', 'today', 'my', 'friend']
assert split_words("HELLO,world") == ['HELLO', 'world']
assert split_words("HELLO WORLD") == ['HELLO', 'WORLD']
assert split_words("a,b,c,d") == ['a', 'b', 'c', 'd']
assert split_words("abc") == 1
assert split_words("hello world how are you") == ['hello', 'world', 'how', 'are', 'you']
assert split_words("1,2,3,4,5,6,7,8,9,10") == ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
assert split_words("a,b,c,d,e") == ["a", "b", "c", "d", "e"]
assert split_words("hello,world!") == ['hello', 'world!']
assert split_words("hello,world,my,name,is,Alice") == ["hello", "world", "my", "name", "is", "Alice"], "Test case 5 failed"
assert split_words("hello,world,hello,world") == ["hello", "world", "hello", "world"]
assert split_words("hello,world,how,are,you,today") == ['hello', 'world', 'how', 'are', 'you', 'today']
assert split_words("hello world!") == ['hello', 'world!']
