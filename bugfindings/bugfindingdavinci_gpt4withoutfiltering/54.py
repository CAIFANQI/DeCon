

def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    return s0 == s1
assert same_chars('', '') == True
assert same_chars('', 'a') == False
assert same_chars('aa', 'ab') == False
assert same_chars('aa', 'aa') == True
assert same_chars('ab', 'ba') == True
assert same_chars('abc', 'bca') == True
assert same_chars('abc', 'bac') == True
assert same_chars('abc', 'bacd') == False
assert same_chars('abcd', 'cabd') == True
assert same_chars('abcd', 'cbad') == True
assert same_chars('cba', 'abc') == True
assert same_chars('abc', 'abc') == True
assert same_chars('abcd', 'abce') == False
assert same_chars('abcd', 'abecd') == False
assert not same_chars('abcd', 'bcaa')
assert not same_chars('abc', 'def')
assert not same_chars('abc', 'cbd')
assert same_chars('potato', 'potato') == True
assert same_chars('a', '') == False
assert not same_chars('chien', 'chenil')
assert same_chars('chien', 'chien')
assert same_chars('abc', 'acb')
assert not same_chars('abc', 'abd')
assert not same_chars('abc', 'ab')
assert not same_chars('abc', 'abcd')
assert not same_chars('abc', 'a')
assert same_chars('apple', 'apple') == True
assert same_chars('apple', 'pear') == False
assert same_chars('test', 'test') == True
assert same_chars('nick', 'ikcn') == True
assert same_chars('nick', 'nik') == False
assert same_chars('nick', 'rick') == False
assert same_chars('nick', 'nicks') == False
assert same_chars('nick', 'nuck') == False
assert same_chars('nick', 'nnnkk') == False
assert same_chars('aaaaaaaa', 'aaaaaaaa') == True
assert same_chars('a', 'b') == False
assert same_chars('abc', 'cba') == True
assert same_chars('aaa', 'bbb') == False
assert same_chars('abb', 'bba') == True
assert not same_chars('ahoj', 'python')
assert not same_chars('abca', 'abcd')
assert not same_chars('', 'a')
assert same_chars('abcd', 'dabc') == True
assert same_chars('abcd', 'deabc') == False
assert same_chars('asdf', 'fdsa')
assert not same_chars('asdf', 'asd')
assert not same_chars('asdf', 'as')
assert not same_chars('asdf', 'asd f')
assert not same_chars('asdf', 'fasdf ')
assert not same_chars('asdf', 'f asdf')
assert same_chars('ab', 'abc') == False
assert same_chars('abc', 'ac') == False
assert same_chars('abc', 'abd') == False
assert not same_chars('ab', 'abc')
assert same_chars('abc', 'bad') == False
assert same_chars('a', 'a') == True
assert same_chars('abc', 'cb1') == False
assert same_chars('eleven', 'never!') == False
assert same_chars('eleven', 'neve') == False
assert same_chars('eleven', 'eenlev') == True
assert same_chars('a', 'aa')
assert same_chars('aaa', 'a')
assert same_chars('aab', 'aab')
assert same_chars('aab', 'aba')
assert same_chars('aab', 'baa')
assert not same_chars('abc', 'bdc')
assert same_chars('a', 'a')
assert same_chars('ab', 'ab')
assert same_chars('abc', 'abc')
assert same_chars('a', 'ab') == False
assert same_chars('ab', 'a') == False
assert same_chars('abcd', 'bacc') == False
assert same_chars('a', 'A') == False
assert same_chars('aabcd', 'dabac') == True
assert same_chars('abcd', 'abcd') == True
assert same_chars('aabcd', 'abd') == False
assert same_chars('abcd', 'adc') == False
assert same_chars('abcd', 'bacde') == False
assert same_chars('abcd', 'aabce') == False
assert same_chars('foo', 'bar') == False
assert same_chars('ab', 'ba')
assert not same_chars('ab', 'ac')
assert same_chars('abac', 'baac')
assert same_chars('hello', 'llohe') == True
assert same_chars('world', 'word') == False
assert same_chars('aaabbb', 'bbbaaa') == True
assert not same_chars('foo', 'bar')
assert same_chars('foo', 'foo') == True
assert same_chars('qwert', 'qwert') == True
assert same_chars('qwert', 'qwerty') == False
assert same_chars('asd', 'asdf') == False
assert same_chars('abc', 'abc  ') == False
assert same_chars('a','a')
assert same_chars('a','b') == False
assert same_chars('aa','ab') == False
assert same_chars('aa','ba') == False
assert same_chars('abc','abc')
assert same_chars('abc','abcd') == False
assert same_chars('abc', 'abc') is True
assert same_chars('abcd', 'adcb') is True
assert not same_chars('abcd', 'bad')
assert not same_chars('abcd', 'bcde')
assert same_chars('abcd', 'abcd')
assert same_chars('steve', 'vetsi') == False
assert same_chars('steve', 'steve') == True
assert same_chars('steve', 'evets') == True
assert same_chars('steve', 'eves') == False
assert same_chars('abc', 'acb') == True
assert same_chars('A', 'A') == True
assert same_chars('abc', 'cba')
assert not same_chars('ball', 'nest')
assert same_chars('eeee', 'eeee')
assert same_chars('pancake', 'pacakne') == True
assert same_chars('pancake', 'pancakes') == False
assert same_chars('a', 'aaaaaaaa')
assert not same_chars('a', 'b')
assert not same_chars('abc', 'aaaaa')
assert same_chars('abc', 'ab') == False
assert same_chars('abc', 'aBc') == False
assert same_chars('aBc', 'abc') == False
assert not same_chars('aaab', 'a')
assert same_chars('abcd', 'cba') == False
assert same_chars('abcd', 'abcde') == False
assert same_chars('abcd', 'efgh') == False
assert same_chars('foo', 'ofo')
assert not same_chars('a', '')
assert same_chars('abc', 'def') == False
assert not same_chars('abc', 'bad')
assert not same_chars('abcde', 'bcdef')
assert same_chars('abc', 'Abc') == False
assert same_chars('abc', 'cbA') == False
assert same_chars('abcabc', 'abcabc')
assert not same_chars('abcd', 'abef')
assert same_chars('abcd', 'bacd')
assert same_chars('dabce', 'dbace')
assert same_chars('dabcef', 'dbacef')
assert same_chars('abcabcabc', 'babccbaaa')
assert not same_chars('a', 'ab')
assert same_chars('aab', 'aba') == True
assert same_chars('abcd', 'abcc') == False
assert same_chars('abcd', 'abdc') == True
assert same_chars('ab', 'cd') == False
assert same_chars('aBc', 'cBa')
assert not same_chars('aBc', 'acb')
assert not same_chars('abcd', 'abce')
assert same_chars('ab', 'aa') == False
assert same_chars('ab', 'ab') == True
assert same_chars('abc', 'a') == False
assert same_chars('abb', 'bab')
assert same_chars('abb', 'bba')
assert not same_chars('potato', 'topato1')
assert same_chars('ab', 'bc') == False
assert same_chars('abc', 'cbc') == False
assert same_chars('abc', 'aaa') == False
assert same_chars('bbb', 'aaa') == False
assert not same_chars('python', 'java')
assert same_chars('top', 'pop') == False
assert same_chars('apple', 'pleap')
assert not same_chars('hello', 'ollea')
assert not same_chars('hell o', 'ollea')
assert same_chars('aab', 'baa') == True
assert not same_chars('abc', 'xyz')
assert same_chars('abc', 'bca')
assert same_chars('abc', 'bcd') == False
assert not same_chars('kot', 'ciupakabra')
assert not same_chars('stop', 'top')
assert not same_chars('ab', 'aa')
assert same_chars('aaab', 'bbb') == False
assert same_chars('ab', 'bbb') == False
assert same_chars('aa', 'bb') == False
assert same_chars('aa', 'aab') == False
assert same_chars('abcd', 'adcb') == True
assert same_chars('abcd', 'dcba') == True
assert same_chars('abcd', 'abc') == False
assert same_chars('abcd', 'abd') == False
assert not same_chars('foo', 'food')
assert not same_chars('abc', 'bbc')
assert not same_chars('abc', 'dba')
assert not same_chars('apple', 'pear')
assert same_chars('robot', 'torob') == True
assert same_chars('robot', 'torobg') == False
assert not same_chars('ab', 'cba')
assert not same_chars('AAA', 'ab')
assert same_chars('dod', 'god') == False
assert same_chars('', 'god') == False
assert same_chars('dod', '') == False
assert same_chars('john', 'jhon') == True
assert same_chars('test', 'tesh') == False
assert same_chars('john', 'johan') == False
assert not same_chars('test', 'tast')
assert not same_chars('hello', 'dude')
assert same_chars('abca', 'abca')
assert not same_chars('abc', 'dca')
assert same_chars('ball', 'mall') == False
assert not same_chars('a', 'A')
assert not same_chars('abc', 'aba')
assert same_chars('aaa', 'aaa') == True
assert same_chars('ab', 'ca') == False
assert same_chars('abc', 'bc') == False
assert same_chars('flower', 'pot') == False
assert not same_chars('python', 'nohtypl')
