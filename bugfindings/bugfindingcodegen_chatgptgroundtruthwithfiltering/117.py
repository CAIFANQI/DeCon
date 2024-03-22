
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    result = []
    for word in s.split():
        n_consonants = 0
        for i in range(0, len(word)):
            if word[i].lower() in ["a","e","i","o","u"]:
                n_consonants += 1 
        if n_consonants == n:
            result.append(word)
    return result

assert 	select_words("", 3) == []
assert 	select_words("bob bob", 3) == []
assert 	select_words("the quick brown fox jumps over the lazy dog", 10) == []
assert 	select_words("the quick brown fox jumps over the lazy dog", 9) == []
assert 	select_words("the quick brown fox jumps over the lazy dog", 12) == []
assert 	select_words("the quick brown fox jumps over the lazy dog", 17) == []
assert 	select_words("the quick brown fox jumps over the lazy dog", 20) == []
assert 	select_words("the quick brown fox jumps over the lazy dog", 22) == []
assert 	select_words("This is a sample sentence.", 2) == []
assert 	select_words("", 0) == []
assert 	select_words("", 1) == []
assert 	select_words("This is a sample sentence.", -1) == []
assert 	select_words("This is a sample sentence.", -5) == []
assert 	select_words('', 3) == []
assert 	select_words('', 1) == []
assert 	select_words('at once', 0) == []
assert 	select_words('at once', 6) == []
assert 	select_words('at once', 5) == []
assert 	select_words('once upon a time', 6) == []
assert 	select_words('once upon a time', 5) == []
assert 	select_words('once upon a time', 4) == []
assert 	select_words('once upon a time', 10) == []
assert 	select_words('ab c d e f', 6) == []
assert 	select_words('', 6) == []
assert 	select_words('ab c d e f', -1) == []
assert 	select_words('a b c d e f', 7) == []
assert 	select_words("abracadabra", 1) == []
assert 	select_words("abracadabra", 5) == []
assert 	select_words("abracadabra", 7) == []
assert 	select_words("abracadabra", 9) == []
assert 	select_words("abracadabra", 10) == []
assert 	select_words("abracadabra", 11) == []
assert 	select_words("", 1) 		== []
assert 	select_words("A", 2) 		== []
assert 	select_words("A aaa", 3) 	== []
assert 	select_words("A aaa", 4) 	== []
assert 	select_words("A aaa", 5) 	== []
assert 	select_words("A aaa", 8) 	== []
assert 	select_words("A aaa", 9) 	== []
assert 	select_words("A aaa", 10) 	== []
assert 	select_words('', 2) == []
assert 	select_words('abcde', 2) == []
assert 	select_words('abcdea', 2) == []
assert 	select_words('a abcde', 2) == []
assert 	select_words('a abcde', 100) == []
assert 	select_words('a abcde', 1) == []
assert 	select_words('a abcde', 5) == []
assert 	select_words('a abcde', 6) == []
assert 	select_words('a abcde', 7) == []
assert 	select_words('a abcde', 8) == []
assert 	select_words('a abcde', 9) == []
