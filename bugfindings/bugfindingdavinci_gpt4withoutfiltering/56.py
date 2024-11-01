

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
assert correct_bracketing("<><") is False
assert correct_bracketing("<>>") is False
assert correct_bracketing("<><><<<>>") is False
assert correct_bracketing("<><><<><>") is False
assert correct_bracketing("<<<><>>") == False
assert not correct_bracketing("<><")
assert not correct_bracketing("<><<")
assert not correct_bracketing("<><<>")
assert not correct_bracketing("<><>>><")
assert not correct_bracketing("<>>")
assert not correct_bracketing("<<<>")
assert not correct_bracketing("<<><>")
assert not correct_bracketing("<<><><>")
assert not correct_bracketing("<><<>><")
assert correct_bracketing("<><><>>") == False
assert correct_bracketing("<<>") == False
assert correct_bracketing("<><<>") == False
assert correct_bracketing('<><') == False
assert correct_bracketing("<>>") == False
assert correct_bracketing("<><<") == False
assert correct_bracketing("<><><") == False
assert correct_bracketing("<<<><>") == False
assert correct_bracketing("<><<<>") == False
assert correct_bracketing("<><<<>><") == False
assert correct_bracketing("<><<<>>><") == False
assert correct_bracketing("<><<<>>><<") == False
assert correct_bracketing("<><<<>>><><") == False
assert correct_bracketing("<><<<>>><><><") == False
assert correct_bracketing("<><<<>>><><><><") == False
assert correct_bracketing("") == True
assert correct_bracketing("<><<<") == False
assert correct_bracketing("<><<>><") == False
assert not correct_bracketing('><<')
assert not correct_bracketing('>><<><<><><>>')
assert correct_bracketing("<><>>") is False
assert correct_bracketing("") is True
assert correct_bracketing("<><<><<>>") is False
assert correct_bracketing('<<>') == False
assert not correct_bracketing("<><<>>>><>")
assert correct_bracketing("")
assert not correct_bracketing("<><<><><>")
assert correct_bracketing("<<<>") == False
assert correct_bracketing("<><") == False
assert correct_bracketing("<><><><") == False
assert correct_bracketing("<><><><><><>>") == False
assert correct_bracketing("<><><><><<><>") == False
assert not correct_bracketing("<><<><")
assert not correct_bracketing("<><<><<")
assert not correct_bracketing("<><<><<>>>>")
assert not correct_bracketing("<<<<<>")
assert correct_bracketing('<<<<<><>>>>><<>>>><<<>><<<><') == False
assert correct_bracketing('<<<<<><>>>>><<>>>><<<>><<<><>') == False
assert correct_bracketing('<><><') is False, '<><>< should be bad'
assert correct_bracketing('<<>><') is False, '<<>>< should be bad'
assert not correct_bracketing("<<<>>")
assert not correct_bracketing("<><><")
assert correct_bracketing('<><>>') == False
assert correct_bracketing('<><<') == False
assert correct_bracketing('<><<><>><><><>>') == False
assert not correct_bracketing(">>>><")
assert not correct_bracketing("<>>>>")
assert not correct_bracketing("<><>>")
assert not correct_bracketing("<><<><<>")
assert correct_bracketing("<><<>>>>") == False
assert correct_bracketing("<<<>>><") == False
assert correct_bracketing("<><>>") == False
assert correct_bracketing("<<<<>>>><<") == False
assert correct_bracketing("<<<><>>>>") == False
assert correct_bracketing("<<<<<>>>>") == False
assert correct_bracketing("<"*100000 + ">"*100000 + "<") == False
assert correct_bracketing("<><><><>>") == False
assert correct_bracketing("<><><><<") == False
assert correct_bracketing("<><><><><") == False
assert correct_bracketing("<><><><>><<><><") == False
assert correct_bracketing("<><><><><>>") == False
assert correct_bracketing("<><><><><>><<><><") == False
assert correct_bracketing("<><><><><>><<><><><") == False
assert correct_bracketing("<><><><><>><<><><><><") == False
assert correct_bracketing('<<><<>') == False
assert correct_bracketing('<><><><>>') == False
assert correct_bracketing("<><><") is False
assert correct_bracketing("<><><><") is False
assert correct_bracketing("<<><>") is False
assert correct_bracketing("<>>><") is False
assert correct_bracketing("<<><<>>") == False
assert correct_bracketing('<><><') == False
assert correct_bracketing('<><><><') == False
assert correct_bracketing('><><>') == False
assert not correct_bracketing(">><")
assert correct_bracketing("<<<<<><><>") == False
assert correct_bracketing("<><><<><>") == False
assert correct_bracketing("<>><>") == False
assert not correct_bracketing("<><<><>")
assert correct_bracketing("<<><>") == False
assert not correct_bracketing('<><<')
assert not correct_bracketing('<><>>')
assert not correct_bracketing('<<>')
assert correct_bracketing("<><><><<>><<>><") == False
assert correct_bracketing("<><<<>>>>") == False
assert not correct_bracketing("<<<>>>>><<>>><<>><")
assert not correct_bracketing("<<<>>>>><<>>><<>>>")
assert not correct_bracketing("<<<>>>>><<>>><<>><><")
assert not correct_bracketing("<><><<>")
assert not correct_bracketing("<><><<><")
assert correct_bracketing("<><><<>>><>><>") == False
assert correct_bracketing("<><><<>>><>><><<>><><>") == False
assert correct_bracketing("<><<><<><>>><><") == False
assert correct_bracketing("<><<><<><>>><>>><") == False
assert correct_bracketing("<><><<") == False
assert not correct_bracketing("<><><><><><>><><><><><><><>")
assert correct_bracketing("<><<<><>") == False
assert correct_bracketing("<><<<><<<>>>>") == False
assert not correct_bracketing("<<>><")
assert correct_bracketing("<<>><") == False
assert correct_bracketing("<><><<>><") == False
assert not correct_bracketing('<><<<>>')
assert correct_bracketing("<><><<>") == False
assert correct_bracketing("<<<>>") == False
assert correct_bracketing("<><><><><><><><><><") == False
assert correct_bracketing("<><><><><><><><><><><><><><><><><><>>") == False
assert correct_bracketing("<><><><") == False, "extra opening"
assert correct_bracketing("<<><><<") == False, "too many openings"
assert correct_bracketing("<<><>") == False, "too many openings"
assert correct_bracketing("<<><><") == False, "too many openings"
assert correct_bracketing("<><><<") == False, "extra opening"
assert correct_bracketing("<><><><<><<><><<>") == False
assert correct_bracketing("<><><><<><<><><<><<>") == False
assert correct_bracketing("<><<><<>") == False
assert correct_bracketing("<><<><<<<>>") == False
assert correct_bracketing("<><<><<<<>><<") == False
assert correct_bracketing("<><<><<<<>><<<>>>>") == False
assert correct_bracketing("<><<><<<<>><<<>>>>><<>") == False
assert correct_bracketing("<<<<>") == False
assert not correct_bracketing('<<<>')
assert not correct_bracketing('<<<>>> >')
assert not correct_bracketing("<<>")
assert not correct_bracketing("<<><<")
assert not correct_bracketing("<<><<>")
assert not correct_bracketing("<><<><<><>><")
assert not correct_bracketing("<><<><<><><")
assert not correct_bracketing('<><')
assert not correct_bracketing('<><><')
assert not correct_bracketing('<><><><')
assert not correct_bracketing('<><><><><')
assert not correct_bracketing('<><><><><><')
assert not correct_bracketing('<><><><><><><')
assert not correct_bracketing('<><><><><><><><')
assert not correct_bracketing('<><><><><><><><><')
assert correct_bracketing("<>><><><>") == False
assert correct_bracketing("<<<><><<>>") == False
assert correct_bracketing("<<<><><<>>>>>") == False
assert correct_bracketing('<<<>') == False
assert correct_bracketing('<><<>') == False
assert correct_bracketing('<<<><<>>') == False
assert correct_bracketing("<>>>") == False
assert correct_bracketing("<><><<>><>>><<>") == False
assert correct_bracketing("<<<>><><<><>") == False
