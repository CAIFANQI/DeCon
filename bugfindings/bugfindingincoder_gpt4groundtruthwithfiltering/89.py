
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            out += d[(d.index(c)+2*2) % 24]
        else:
            out += c
    return out
assert encrypt("") == ""
assert 'b' == encrypt('x')
assert encrypt('b') == 'f'
assert encrypt('c') == 'g'
assert encrypt('d') == 'h'
assert encrypt('e') == 'i'
assert encrypt('f') == 'j'
assert encrypt('g') == 'k'
assert encrypt('h') == 'l'
assert encrypt('i') =='m'
assert encrypt('j') == 'n'
assert encrypt('k') == 'o'
assert encrypt('l') == 'p'
assert encrypt('m') == 'q'
assert encrypt('n') == 'r'
assert encrypt('o') =='s'
assert encrypt('p') == 't'
assert encrypt('q') == 'u'
assert encrypt('r') == 'v'
assert encrypt('s') == 'w'
assert encrypt('t') == 'x'
assert encrypt('u') == 'y'
assert encrypt('v') == 'z'
assert encrypt('w') == 'a'
assert encrypt('x') == 'b'
assert encrypt('y') == 'c'
assert encrypt('z') == 'd'
assert encrypt('b')  == 'f'
assert encrypt('y')  == 'c'
assert encrypt('') == ''
assert encrypt('') == '' # no change
