
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowels = "aeiou"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])
assert 'B' == encode('b')
assert 'C' == encode('c')
assert 'D' == encode('d')
assert 'F' == encode('f')
assert 'G' == encode('g')
assert 'H' == encode('h')
assert 'J' == encode('j')
assert 'K' == encode('k')
assert 'L' == encode('l')
assert 'M' == encode('m')
assert 'N' == encode('n')
assert 'P' == encode('p')
assert 'Q' == encode('q')
assert 'R' == encode('r')
assert 'S' == encode('s')
assert 'T' == encode('t')
assert 'V' == encode('v')
assert 'W' == encode('w')
assert 'X' == encode('x')
assert 'Y' == encode('y')
assert 'Z' == encode('z')
assert encode('!@#') == '!@#'
assert encode('123') == '123'
assert encode('Z') == 'z'
assert encode('') == ''
