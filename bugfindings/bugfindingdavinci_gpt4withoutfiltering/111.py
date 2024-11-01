
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    dict1={}
    list1=test.split(" ")
    t=1

    for i in list1:
        if(list1.count(i)>t) and i!='':
            t=list1.count(i)
    if t>0:
        for i in list1:
            if(list1.count(i)==t):
                
                dict1[i]=t
    return dict1
assert histogram("a b c") == {'a': 1, 'b': 1, 'c': 1}
assert histogram("a a b c c") == {'a': 2, 'c': 2}
assert histogram("a c") == {'a': 1, 'c': 1}
assert histogram("a a b b c c") == {'a': 2, 'b': 2, 'c': 2}
assert histogram("a") == {"a": 1}
assert histogram("a a b c c c d d") == {'c': 3}
assert histogram("a a b b c c d d d") == {'d': 3}
assert histogram("a a b b c c d d e e") == {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2}
assert histogram("") == {}
assert histogram("j j j j") == {'j': 4}
assert histogram("a") == {'a': 1}
assert histogram("A B C D") == {'A': 1, 'B': 1, 'C': 1, 'D': 1}
assert histogram("a A b C") == {'a': 1, 'A': 1, 'b': 1, 'C': 1}
assert histogram("a b c a") == {'a': 2}
assert histogram("a a b b") == {'a': 2, 'b': 2}
assert histogram("a b c d e f z z z z") == {'z': 4}
assert histogram("a  b  c  d") == {'a': 1, 'b': 1, 'c': 1, 'd': 1}
assert histogram("a b c d e f g a") == {"a": 2}
assert histogram("a b c d e f g h") == {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1, "g": 1, "h": 1}
assert histogram("a b c d e f g h a") == {"a": 2}
assert histogram("a a b b c") == {"a": 2, "b": 2}
assert histogram("a a b b c c c") == {"c": 3}
assert histogram("a b c d e b") == {'b': 2}
assert histogram("a b c d e c") == {'c': 2}
assert histogram("a b c d e d") == {'d': 2}
assert histogram("a b c d e e") == {'e': 2}
assert histogram("a b c d e e a") == {'a': 2, 'e': 2}
assert histogram("a b c d e e b") == {'b': 2, 'e': 2}
assert histogram("a b c d e e c") == {'c': 2, 'e': 2}
assert histogram("a b c d e e d") == {'d': 2, 'e': 2}
assert histogram("a b c d e e e") == {'e': 3}
assert histogram("a b b") == {'b': 2}
assert histogram("a a") == {'a': 2}
assert histogram("a b c d a e f b c a d") == {'a': 3}
assert histogram("a b c d a e f b c a d a b") == {'a': 4}
assert histogram("a b c a b") == {'a': 2, 'b': 2}
assert histogram("a") == {'a': 1}, "just one character"
assert histogram("a b") == {'a': 1, 'b': 1}, "two characters"
assert histogram("a a") == {'a': 2}, "a repeated character"
assert histogram("a b b") == {'b': 2}, "two repeated characters"
assert histogram("b a c c b") == {'b': 2, 'c': 2}, "multiple repeated characters"
assert histogram("a b c a d e c") == {'a': 2, 'c': 2}, "many repeated characters"
assert histogram("  a b c") == {'a': 1, 'b': 1, 'c': 1}
assert histogram("  a  ") == {'a': 1}
assert histogram("a b b b aa") == {'b': 3}
assert (histogram("a a b b c")) == {"a": 2, "b": 2}
assert histogram("a b a") == {'a': 2}
assert histogram("a b c c c") == {'c': 3}
assert histogram("a b c c d d d") == {'d': 3}
assert histogram("a b b c d f g h h") == {'b': 2, 'h': 2}
assert histogram("a b c d e f") == {'e': 1, 'f': 1, 'd': 1, 'c': 1, 'b': 1, 'a': 1}
assert histogram("a b c") == {'c': 1, 'b': 1, 'a': 1}
assert histogram("a a b b") == {'b': 2, 'a': 2}
assert histogram("b a b a") == {'b': 2, 'a': 2}
assert histogram("z z z z") == {'z': 4}
assert histogram("z z z") == {'z': 3}
assert histogram("z") == {'z': 1}
assert histogram("a b c a b c a b c") == {'a': 3, 'b': 3, 'c': 3}
assert histogram("a b c b c") == {'b': 2, 'c': 2}
assert histogram("a b c b a c") == {'a': 2, 'b': 2, 'c': 2}
assert histogram("a a bb ccc a") == {'a': 3}
assert histogram("a b c d e a b c d e d d e") == {"d": 4}
assert histogram("a b r a c a d a b r a") == {"a": 5}
assert histogram("a b a") == {"a": 2}
assert histogram("a b c d") == {"a": 1, "b": 1, "c": 1, "d": 1}
assert histogram("e d c d c b a") == {"d": 2, "c": 2}
assert histogram("d d d d") == {"d": 4}
assert histogram("d d d d c b a b c") == {"d": 4}
assert histogram("a b c d a b") == {'a': 2, 'b': 2}
assert histogram("a b b b c d e f f g") == {'b': 3}
assert histogram("a c a b") == {"a": 2}
assert histogram("a b a c a d") == {'a': 3}
assert histogram("a b c d e f g h i j k l m n o p q r s t u v w x y z") == {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1, "g": 1, "h": 1, "i": 1, "j": 1, "k": 1, "l": 1, "m": 1, "n": 1, "o": 1, "p": 1, "q": 1, "r": 1, "s": 1, "t": 1, "u": 1, "v": 1, "w": 1, "x": 1, "y": 1, "z": 1}
assert histogram("a b b b") == dict(b=3)
assert histogram("a a a b c") == dict(a=3)
assert histogram("a b c d e f g") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1}
