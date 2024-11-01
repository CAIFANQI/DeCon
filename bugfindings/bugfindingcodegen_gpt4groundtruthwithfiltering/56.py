

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    depth = 0
    for b in brackets:
        if b == ">":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0
assert 	correct_bracketing('<<>>') == True, 'test 3 failed.'
assert 	correct_bracketing('<') == False, 'test 4 failed.'
assert 	correct_bracketing('<>>') == False, 'test 5 failed.'
assert 	correct_bracketing('><') == False, 'test 6 failed.'
assert 	correct_bracketing('<><') == False, 'test 7 failed.'
assert 	correct_bracketing('<') == False, 'test 8 failed.'
assert 	correct_bracketing('>>') == False, 'test 9 failed.'
assert 	correct_bracketing('>>>') == False, 'test 10 failed.'
assert 	correct_bracketing('>') == False, 'test 11 failed.'
assert 	correct_bracketing('>>><') == False, 'test 12 failed.'
assert 	correct_bracketing('>><') == False, 'test 13 failed.'
assert 	correct_bracketing('>><>') == False, 'test 14 failed.'
assert not correct_bracketing( "<brackets<>" )
assert not correct_bracketing( "<brackets>" )
assert not correct_bracketing( "<brackets<" )
assert not correct_bracketing( "<brackets>)" )
assert not correct_bracketing( "<brackets>")
assert not correct_bracketing( ">" )
assert not correct_bracketing( ">")
assert not correct_bracketing( ">>")
assert not correct_bracketing("<html><")
assert not correct_bracketing("<html><body>")
assert not correct_bracketing("<html></body>")
assert not correct_bracketing("<html></html>")
assert not correct_bracketing("<body>")
assert not correct_bracketing("< body>")
assert not correct_bracketing("<body> ")
assert not correct_bracketing("< body >")
assert not correct_bracketing("<body> </body>")
assert not correct_bracketing("<body> </ html>")
assert not correct_bracketing("<body> </")
assert not correct_bracketing("<body> </p>")
assert not correct_bracketing("<body> </p> ")
assert not correct_bracketing("<body> </p> </body>")
assert not correct_bracketing("<body> </p> </p>")
assert 	correct_bracketing('<><>') == True
assert 	correct_bracketing('<><><><><>') == True
assert 	correct_bracketing('<><><>>') == False
assert 	correct_bracketing('<<>') == False
assert 	correct_bracketing('>') == False
assert 	correct_bracketing('<>>') == False
assert 	correct_bracketing('<>>>') == False
assert 	correct_bracketing('<><>>') == False
assert not correct_bracketing('<(>')
assert not correct_bracketing('<<')
assert not correct_bracketing('<(>)')
assert not correct_bracketing('<(>)>')
assert not correct_bracketing('<(>)>()<')
assert not correct_bracketing('<')
assert not correct_bracketing('>')
assert not correct_bracketing('(>)')
assert not correct_bracketing('<()>')
assert not correct_bracketing('<(>)()(())')
assert not correct_bracketing('(>))(>')
