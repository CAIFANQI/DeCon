

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    depth = 0
    for b in brackets:
        if b == "(":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return True
    return depth == 0
assert correct_bracketing("()") is True
assert correct_bracketing("()()") is True
assert correct_bracketing("(())") is True
assert correct_bracketing("()()()") is True
assert correct_bracketing("()(())") is True
assert correct_bracketing("(()())") is True
assert correct_bracketing("()(())()") is True
assert correct_bracketing("(())(())") is True
assert correct_bracketing("()(()())") is True
assert correct_bracketing("()()(())()") is True
assert correct_bracketing("()(()())(())") is True
assert correct_bracketing("()()(()())(())") is True
assert correct_bracketing("()(()())(()())") is True
assert correct_bracketing("()()(()())(()())") is True
assert correct_bracketing("()(()())(()()())") is True
assert correct_bracketing("(())") == True
assert correct_bracketing("(()())") == True
assert correct_bracketing("()") == True
assert correct_bracketing("((") == False
assert correct_bracketing("()()") == True
assert correct_bracketing("((())") == False
assert correct_bracketing("((()())") == False
assert correct_bracketing("()(())") == True
assert correct_bracketing("(()(())") == False
assert correct_bracketing("()(()())") == True
assert correct_bracketing("((()(()()))") == False
assert correct_bracketing("()(()()())") == True
assert correct_bracketing("((()(()()()))") == False
assert correct_bracketing("()(()()()())") == True
assert correct_bracketing("((()(()()()()))") == False
assert correct_bracketing("()(()()()()())") == True
assert correct_bracketing("((()(()()()()()))") == False
assert correct_bracketing("(()(()()()()())") == False
assert correct_bracketing("()(()()()()()())") == True
assert correct_bracketing("((()(()()()()()()))") == False
assert correct_bracketing("()()()") == True
assert correct_bracketing("(()()())") == True
assert correct_bracketing("(()())()") == True
assert correct_bracketing("()()()()") == True
assert correct_bracketing("()(") == False
assert correct_bracketing("(()(") == False
assert correct_bracketing("()()(") == False
assert correct_bracketing("(()())(") == False
assert correct_bracketing("(())(") == False
assert correct_bracketing('((()))') == True
assert correct_bracketing('((())())') == True
assert correct_bracketing('(()())()') == True
assert correct_bracketing('()()') == True
assert correct_bracketing('()') == True
assert correct_bracketing('') == True
assert correct_bracketing('((())') == False
assert correct_bracketing('((())(())') == False
assert correct_bracketing('((())(())(())') == False
assert correct_bracketing('((())()') == False
assert correct_bracketing("(())()") is True
assert correct_bracketing("(())()()") is True
assert correct_bracketing("()(())()()") is True
assert correct_bracketing("()()()(())()") is True
assert correct_bracketing("(())(())(())") is True
assert correct_bracketing("(())(())(())()") is True
assert correct_bracketing("(())()(())(())") is True
assert correct_bracketing("(())()(())()()") is True
assert correct_bracketing("()(())()(())()") is True
assert correct_bracketing("()()(())()(())()") is True
assert correct_bracketing("()()()(())()(())") is True
assert correct_bracketing("(())(())(())(())()") is True
assert correct_bracketing("(())(())(())(())()()") is True
assert correct_bracketing("(())()(())(())(())") is True
assert correct_bracketing('()(())') == True
assert correct_bracketing("(())()") == True
assert correct_bracketing("(())()()") == True
assert correct_bracketing("(())()()()") == True
assert correct_bracketing("(()())()()()") == True
assert correct_bracketing("(()())()()()()") == True
assert correct_bracketing("()(()()())()") == True
assert correct_bracketing("()(()()())()()") == True
assert correct_bracketing("()(()())()()()()") == True
assert correct_bracketing("()(()())()()()()()()") == True
assert correct_bracketing("()(()())()()()()()()()") == True
assert correct_bracketing("()(()())()()()()()()()()()()()") == True
assert correct_bracketing('(())()') == True
assert correct_bracketing('(())') == True
assert correct_bracketing("(()())(()())") == True
assert correct_bracketing(")((") == False
assert correct_bracketing(")") == False
assert correct_bracketing("(") == False
assert correct_bracketing("(()") == False
assert correct_bracketing("(()()") == False
assert correct_bracketing("(()()()") == False
assert correct_bracketing("(((()))") == False
assert correct_bracketing("(((()()())())") == False
assert correct_bracketing("(())()(") == False
assert correct_bracketing("(())()()(") == False
assert correct_bracketing("(()()())(") == False
assert correct_bracketing("(()()()(") == False
assert correct_bracketing("((())(") == False
assert correct_bracketing("(((()))(") == False
assert correct_bracketing("((()))(") == False
assert correct_bracketing('(()())') == True
assert correct_bracketing('((()))()') == True
assert correct_bracketing("((()))") == True
assert correct_bracketing("()(())()") == True
assert correct_bracketing("(())(())") == True
assert correct_bracketing("(()())(())") == True
assert correct_bracketing("(((()))(()))") == True
assert correct_bracketing("(((())))") == True
assert correct_bracketing("(((()))())") == True
assert correct_bracketing("((((()))()))") == True
assert correct_bracketing("((())(())") == False
assert correct_bracketing("(hello") == False
assert correct_bracketing("("*2 + "(" + "()") == False
assert correct_bracketing("(" + ")*2" + ")(" + ")*2" + ")(") == False
assert correct_bracketing("(" + ")*2" + ")(" + ")*2" + ")(" + ")*2" + ")") == False
assert correct_bracketing("(" + ")*2" + ")(" + ")*2" + ")(" + ")*2" + ")(" + ")*2" + ")(" + ")*2" + ")") == False
assert correct_bracketing("((()))(())") == True
assert correct_bracketing("((()))(()())") == True
assert correct_bracketing("()")
assert correct_bracketing("()()")
assert correct_bracketing("((()))(())")
assert correct_bracketing("((()))(()())")
assert correct_bracketing("(((()()()()()()()))") == False
assert correct_bracketing("(()(()))") == True
assert correct_bracketing('()(') == False
assert correct_bracketing('(()()') == False
assert correct_bracketing('())') == False
assert correct_bracketing(')((') == False
assert correct_bracketing('(())(') == False
assert correct_bracketing('()(()') == False
assert correct_bracketing(')(())') == False
assert correct_bracketing('()()(') == False
assert correct_bracketing('(()())(') == False
assert correct_bracketing('(()(())') == False
assert correct_bracketing('(())') is True
assert correct_bracketing('((())()') is False
assert correct_bracketing('(()()()') is False
assert correct_bracketing('(((())())') is False
assert correct_bracketing('(()(())') is False
assert correct_bracketing('(((())())()') is False
assert correct_bracketing('(((())())()()') is False
assert correct_bracketing(")()(())") == False
assert correct_bracketing("(())(()") == False
assert correct_bracketing("()(())(()") == False
assert correct_bracketing("()()(())(()") == False
assert correct_bracketing("(()(())()(())") == False
assert correct_bracketing("()()()()()()()()()()()()()()()()()()()()()()()") == True
assert correct_bracketing("(((()))((()))())") == True
assert correct_bracketing("(((()))((()))((()))())") == True
assert correct_bracketing("(((()))((()))((()))((()))())") == True
assert correct_bracketing("((()())((())())())") == True
assert correct_bracketing("((()())((())())())((()())())") == True
assert correct_bracketing("((()())((())())())((()())())()") == True
assert correct_bracketing("(((()())((())())())((()())())())") == True
assert correct_bracketing("(((()())((())())())((()())())())((()())())()") == True
assert correct_bracketing('()(()(())') == False
assert correct_bracketing('(()(()())') == False
assert correct_bracketing('(()(()(())') == False
assert correct_bracketing('()(()(()(()))') == False
assert correct_bracketing('((()()()))') == True
assert correct_bracketing('((()))()()') == True
assert correct_bracketing('(((()))()())') == True
assert correct_bracketing('(((())))()()') == True
assert correct_bracketing('(((()())))()()') == True
assert correct_bracketing('(((()())))()()()') == True
assert correct_bracketing('(()()())(()())()') == True
assert correct_bracketing('((())())((())())') == True
assert correct_bracketing('((()())') == False
assert correct_bracketing('(()(())(') == False
assert correct_bracketing("((())())") == True
assert correct_bracketing("(((())))()") == True
assert correct_bracketing("(())(()())") == True
assert correct_bracketing("(()())(())()") == True
assert correct_bracketing("(()())(()())(())") == True
assert correct_bracketing("([]") is False
assert correct_bracketing("[(]") is False
assert correct_bracketing("{(]") is False
assert correct_bracketing("[](]") is False
assert correct_bracketing("({}") is False
assert correct_bracketing("[)]") is False
assert correct_bracketing(")()") is False
assert correct_bracketing(")]") is False
assert correct_bracketing(")]}") is False
assert correct_bracketing(")][]") is False
assert correct_bracketing(")[]") is False
assert correct_bracketing("(()()") is False
assert correct_bracketing("(())")
assert not correct_bracketing("())")
assert not correct_bracketing("(()))")
assert not correct_bracketing("((()())")
assert correct_bracketing("](") == False
assert correct_bracketing("[)]") == False
assert correct_bracketing(")]") == False
assert correct_bracketing(")]()") == False
assert correct_bracketing("[(") == False
assert correct_bracketing("[)") == False
assert correct_bracketing('(()())(())') == True
assert correct_bracketing('(()())(()())') == True
assert correct_bracketing('(()())(()()()())') == True
assert correct_bracketing('(()())(()()()())(') == False
assert correct_bracketing("())") == False
assert correct_bracketing("(()((()))") == False
assert correct_bracketing("(()(())()") == False
assert correct_bracketing("(()())(()") == False
assert correct_bracketing("())(()())") == False
assert not correct_bracketing("(()))"), "Incorrectly brackets some brackets"
assert not correct_bracketing("))()"), "Incorrectly brackets some brackets"
assert correct_bracketing("(())(())(())"), "Correctly brackets three opening brackets"
assert correct_bracketing("(())(()())"), "Correctly brackets four opening brackets"
assert not correct_bracketing(")()()"), "Incorrectly brackets some brackets"
assert not correct_bracketing("()(()"), "Incorrectly brackets some brackets"
assert not correct_bracketing(")()"), "Incorrectly brackets some brackets"
assert not correct_bracketing("()(()()"), "Incorrectly brackets some brackets"
assert not correct_bracketing("(()")
assert correct_bracketing("()((") == False
assert correct_bracketing("(((()(") == False
assert correct_bracketing("()(((())") == False
assert correct_bracketing("((()))()") is True
assert correct_bracketing("(()())()") is True
assert correct_bracketing("(()(())()") is False
assert correct_bracketing('(((()))(()))') == True
assert correct_bracketing('((((()))(())))') == True
assert correct_bracketing('(((())))()') == True
assert correct_bracketing('((((((()))))))()') == True
assert correct_bracketing('(((())()))()') == True
assert correct_bracketing('(((())(()())(()())(())))()') == True
assert correct_bracketing('()((((()))))') == True
assert correct_bracketing('(((()))())()') == True
assert correct_bracketing('((())())(())') == True
assert correct_bracketing('((())())(()())') == True
assert correct_bracketing('((())())(()()())') == True
assert correct_bracketing('((())())(())()') == True
assert correct_bracketing('((())())(()())()') == True
assert correct_bracketing('((())())(()())(())') == True
assert correct_bracketing('((())())(()())(()())') == True
assert correct_bracketing("())((") == False
assert correct_bracketing("((()))")
assert correct_bracketing("(()(()))")
assert not correct_bracketing("(()()()")
assert not correct_bracketing(")")
assert not correct_bracketing("(")
assert not correct_bracketing(')')
assert correct_bracketing("(())((") == False
assert not correct_bracketing('(()')
assert correct_bracketing('(())')
assert not correct_bracketing(')(())')
assert correct_bracketing('((())(())(())()') == False
assert correct_bracketing('()()()') == True
assert not correct_bracketing('((())')
assert not correct_bracketing('(())(')
assert not correct_bracketing('(()())(')
assert correct_bracketing("([)(]") == False
assert correct_bracketing('(())()')
assert not correct_bracketing('())()')
assert correct_bracketing("(((()())))") == True
assert correct_bracketing("(((((()())()))()))") == True
assert correct_bracketing("()((())())()") == True
assert correct_bracketing("()(((())()()))") == True
assert correct_bracketing("()((()())())") == True
assert correct_bracketing("())()") == False
assert correct_bracketing('(()') == False
assert correct_bracketing(')()') == False
assert correct_bracketing('((()(()))') == False
assert correct_bracketing('((()(((()))))') == False
assert correct_bracketing('((())((()))') == False
assert correct_bracketing('((()(()))(())') == False
assert correct_bracketing("(()") is False
assert correct_bracketing("(()[]") is False
assert correct_bracketing("[)]()") is False
assert not correct_bracketing('()(')
assert not correct_bracketing('(()()')
assert not correct_bracketing(')()')
assert not correct_bracketing('()()(')
assert not correct_bracketing('())')
assert not correct_bracketing("(())(")
assert correct_bracketing('(((())())())') == True
assert correct_bracketing('(()()())()') == True
assert correct_bracketing('(((())())())()()()()') == True
assert not correct_bracketing("(()(())")
assert not correct_bracketing("(()))(())")
assert not correct_bracketing(")()")
assert correct_bracketing("()") 
assert correct_bracketing("(()()()())")
assert correct_bracketing("((()()())(()))")
assert correct_bracketing("((()())()())")
assert correct_bracketing("(()()())()")
assert correct_bracketing("(())()")
assert correct_bracketing("((()())())()")
assert correct_bracketing("((()())(())())")
assert correct_bracketing("((()())()())()")
assert not correct_bracketing("(()))(())(())()")
assert not correct_bracketing("()())(())(())()()")
assert not correct_bracketing("(()))(()())(()())()")
assert not correct_bracketing('(')
assert not correct_bracketing('([]')
assert correct_bracketing(")())(()") == False
assert correct_bracketing("(()(((())(()))))") == True
assert correct_bracketing("()()(((()())(())))") == True
assert correct_bracketing("(()())((()())()()())") == True
assert correct_bracketing("((()())(()()))((()())())") == True
assert correct_bracketing("(()()())((()())((()())))") == True
assert correct_bracketing("(()())(()())((()())())") == True
assert correct_bracketing('(()()()())') == True
assert correct_bracketing("((()))(()") == False
assert correct_bracketing("(((())())(())") == False
assert correct_bracketing("(((()))((())(())") == False
assert correct_bracketing("(((()))(())())") == True
assert correct_bracketing("((())())(((())())") == False
assert correct_bracketing("(()())((()())((())()") == False
assert correct_bracketing("(()())((()(()))((())()") == False
assert correct_bracketing("(()")  == False
assert correct_bracketing("(((((()()))()())())()())") == True
assert correct_bracketing("(((()()())(())())())") == True
assert correct_bracketing("(((()()()())(())())())") == True
assert correct_bracketing("(((()()())(()()())())()())") == True
assert correct_bracketing("(((()()())(()())())()())") == True
assert correct_bracketing("(()())(()())()") == True
assert correct_bracketing('(((()))') == False
assert correct_bracketing('((((()))')==False
assert correct_bracketing('()()()()')==True
assert correct_bracketing('((((((((())))))))')==False
assert correct_bracketing('((((((()))))))')==True
assert correct_bracketing("[(]") == False
assert correct_bracketing("[)][") == False
assert correct_bracketing("(](") == False
assert correct_bracketing("()[](]") == False
assert not correct_bracketing('(())(()')
assert not correct_bracketing('(()(())(()')
assert correct_bracketing("(())(())(())") == True
assert correct_bracketing("(()(()())") == False
assert correct_bracketing("((()())(())") == False
assert correct_bracketing("(()()()()") == False
assert correct_bracketing('(((()())())') == False
assert not correct_bracketing("(((")
assert correct_bracketing("(((((())))())())") == True
assert correct_bracketing("(((()))()))") == False
assert correct_bracketing("((((((())))())())())") == True
assert correct_bracketing("(()((()()()()()())())())") == True
assert correct_bracketing("(()(()(()))") == False
assert correct_bracketing("(((((())))")  is False
assert correct_bracketing("((())) is ((())") is False
