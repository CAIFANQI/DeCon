
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
assert histogram('a b c d e') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
assert histogram('a a a a a') == {'a': 5}
assert histogram('a a b b c c') == {'a': 2, 'b': 2, 'c': 2}
assert histogram('a a a a b b b b c c c c d d d d e e e e') == {'a': 4, 'b': 4, 'c': 4, 'd': 4, 'e': 4}
assert histogram("a b c d e f g h i j k l m n o p q r s t u v w x y z") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}
assert histogram("a a a b b c c c d d d d") == {'d': 4}
assert histogram("a a a b b c c c d d d d e e e e") == {'d': 4, 'e': 4}
assert histogram("a a b b c c d d e e") == {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2}
assert histogram("a a a b b b c c c d d d e e e") == {'a': 3, 'b': 3, 'c': 3, 'd': 3, 'e': 3}
assert histogram("a a b b c c d d e e f f g g h h i i j j k k l l m m n n o o p p q q r r s s t t u u v v w w x x y y z z") == {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 2, 'j': 2, 'k': 2, 'l': 2, 'm': 2, 'n': 2, 'o': 2, 'p': 2, 'q': 2, 'r': 2, 's': 2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2}
assert histogram("a a a a b b c") == {'a': 4}
assert histogram("a b b b c c c") == {'b': 3, 'c': 3}
assert histogram("a b c c d e") == {'c': 2}
assert histogram("a b c c d e e") == {'c': 2, 'e': 2}
assert histogram("a b c c d e e e") == {'e': 3}
assert histogram("a b c c d e e e e") == {'e': 4}
assert histogram("a b c c d e e e e e") == {'e': 5}
assert histogram("a b c c d e e e e e f f f f f") == {'e': 5, 'f': 5}
assert histogram("a b c d e") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
assert histogram("a a a a a") == {'a': 5}
assert histogram("") == {}
assert histogram("a b c a b c a b c") == {'a': 3, 'b': 3, 'c': 3}
assert histogram("a a b c") == {'a': 2}
assert histogram("a a b b c c") == {'a': 2, 'b': 2, 'c': 2}
assert histogram("a a b b c c d") == {'a': 2, 'b': 2, 'c': 2}
assert histogram("a a b b c c d d d") == {'d': 3}
assert histogram("a a a") == {'a': 3}
assert histogram("a b c d e f g h i j k l m n o p q r s t u v w x y z a a a a") == {'a': 5}
assert histogram("a b c d e e") == {'e': 2}
assert histogram("a a b b c c c d d d d e e e e") == {'d': 4, 'e': 4}
assert histogram('a b b b c c c') == {'b': 3, 'c': 3}
assert histogram('a a a a a a a a a a') == {'a': 10}
assert histogram('a a b b b c c c') == {'b': 3, 'c': 3}
assert histogram('a a a b b b c c c d') == {'a': 3, 'b': 3, 'c': 3}
assert histogram('a a a b b b c c c d d d') == {'a': 3, 'b': 3, 'c': 3, 'd': 3}
assert histogram("a b c c") == {'c': 2}
assert histogram("a b c d e f g") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1}
assert histogram("a a b b c c d d d e e e e") == {'e': 4}
assert histogram("a b c") == {'a': 1, 'b': 1, 'c': 1}
assert histogram("a a a b b b c c c c") == {'c': 4}
assert histogram("a a b b c c c c d d d d d") == {'d': 5}
assert histogram("a a b b c c c c d d d d d e e e e e") == {'d': 5, 'e': 5}
assert histogram("a a a b b b c c c c d d d d d") == {'d': 5}
assert histogram("a a a b b b c c c c d d d d d e e e e e") == {'d': 5, 'e': 5}
assert histogram("a a a b b b c c c c d d d d d e e e e e f f f f f") == {'d': 5, 'e': 5, 'f': 5}
assert histogram("a a a b b b c c c c d d d d d e e e e e f f f f f g g g g g") == {'d': 5, 'e': 5, 'f': 5, 'g': 5}
assert histogram('a a a b b c c') == {'a': 3}
assert histogram('a b c d e f g') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1}
assert histogram("a a a b b b c c c") == {'a': 3, 'b': 3, 'c': 3}
assert histogram('a b c d e f g h i j k l m n o p q r s t u v w x y z') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}
assert histogram("a a b b c c d d e e f f g g h h i i j j k k l l m m n n o o p p q q r r s s t t u u v v w w x x y y z z") == {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 2, 'j': 2, 'k': 2, 'l': 2, 'm': 2, 'n': 2, 'o': 2, 'p': 2, 'q': 2, 'r': 2, 's': 2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2}, "Test case 2 failed"
assert histogram("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z") == {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 2, 'j': 2, 'k': 2, 'l': 2, 'm': 2, 'n': 2, 'o': 2, 'p': 2, 'q': 2, 'r': 2, 's': 2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2}, "Test case 4 failed"
assert histogram("a b b c c c c d d d d") == {'c': 4, 'd': 4}
assert histogram("a b c d e e e") == {'e': 3}
assert histogram("a a a a b c") == {'a': 4}
assert histogram("a b c c d d e") == {'c': 2, 'd': 2}
assert histogram("a b c c d d e e") == {'c': 2, 'd': 2, 'e': 2}
assert histogram("a b c c d d e e f") == {'c': 2, 'd': 2, 'e': 2}
assert histogram("a a a a a a a") == {'a': 7}
assert histogram("a b a b a b") == {'a': 3, 'b': 3}
assert histogram("a b c d e f") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1}, "Test case 2 failed"
assert histogram("a a a b b b c c c") == {'a': 3, 'b': 3, 'c': 3}, "Test case 3 failed"
assert histogram("a b c d e f g h i j k l m n o p q r s t u v w x y z") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}, "Test case 4 failed"
assert histogram("a a a b c") == {'a': 3}
assert histogram("a a b b c") == {'a': 2, 'b': 2}
assert histogram("a b b c c c") == {'c': 3}
assert histogram("a a b b c c c c") == {'c': 4}
assert histogram("a a a a b b b b c c c c") == {'a': 4, 'b': 4, 'c': 4}
assert histogram("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z") == {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 2, 'j': 2, 'k': 2, 'l': 2, 'm': 2, 'n': 2, 'o': 2, 'p': 2, 'q': 2, 'r': 2, 's': 2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2}
assert histogram("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z") == {'a': 3, 'b': 3, 'c': 3, 'd': 3, 'e': 3, 'f': 3, 'g': 3, 'h': 3, 'i': 3, 'j': 3, 'k': 3, 'l': 3, 'm': 3, 'n': 3, 'o': 3, 'p': 3, 'q': 3, 'r': 3, 's': 3, 't': 3, 'u': 3, 'v': 3, 'w': 3, 'x': 3, 'y': 3, 'z': 3}
assert histogram("a a b c c c d d d d e e e e") == {'d': 4, 'e': 4}
assert histogram("a a b c c c d d d d e e e e f f f f") == {'d': 4, 'e': 4, 'f': 4}
assert histogram("a a b b c c d d") == {'a': 2, 'b': 2, 'c': 2, 'd': 2}
assert histogram("a a a a a b b b b b c c c c c d d d d d e e e e e") == {'a': 5, 'b': 5, 'c': 5, 'd': 5, 'e': 5}
assert histogram("a b c d e e e f f f") == {'e': 3, 'f': 3}
assert histogram("a b c d e e e f f f g g g") == {'e': 3, 'f': 3, 'g': 3}
assert histogram("a b c d e e e f f f g g g h i i i i") == {'i': 4}
assert histogram("a a a a a b b b b b c c c c c") == {'a': 5, 'b': 5, 'c': 5}, "Test case 4 failed"
assert histogram("a b b b") == {'b': 3}
assert histogram("a a a a") == {'a': 4}
assert histogram("a a a a a b b b b b c c c c c d d d d d e e e e e f f f f f g g g g g h h h h h i i i i i j j j j j k k k k k l l l l l m m m m m n n n n n o o o o o p p p p p q q q q q r r r r r s s s s s t t t t t u u u u u v v v v v w w w w w x x x x x y y y y y z z z z z") == {'a': 5, 'b': 5, 'c': 5, 'd': 5, 'e': 5, 'f': 5, 'g': 5, 'h': 5, 'i': 5, 'j': 5, 'k': 5, 'l': 5, 'm': 5, 'n': 5, 'o': 5, 'p': 5, 'q': 5, 'r': 5, 's': 5, 't': 5, 'u': 5, 'v': 5, 'w': 5, 'x': 5, 'y': 5, 'z': 5}
assert histogram('a b c d d e e e e') == {'e': 4}
assert histogram('a b b b c c c c c') == {'c': 5}
assert histogram('a b b b c c c c c d d d d d') == {'c': 5, 'd': 5}
assert histogram("a b c d e e e e e") == {'e': 5}
assert histogram('a a b b c') == {'a': 2, 'b': 2}
assert histogram("a a a a a a a a a a") == {'a': 10}
assert histogram("a a b b c c c") == {'c': 3}
