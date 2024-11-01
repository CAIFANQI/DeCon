

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
assert correct_bracketing("") == True
assert correct_bracketing("()") == True
assert correct_bracketing("(") == False
assert correct_bracketing(")") == False
assert correct_bracketing("(()()()()())") == True
assert correct_bracketing("(()()()()()") == False
assert correct_bracketing("())") == False
assert correct_bracketing("(()())")
assert not correct_bracketing("(")
assert not correct_bracketing(")")
assert not correct_bracketing("())")
assert not correct_bracketing("((())")
assert correct_bracketing('(()(()))')
assert not correct_bracketing(')')
assert not correct_bracketing('())')
assert not correct_bracketing('(()(()')
assert correct_bracketing("((()))") == True
assert correct_bracketing("()()()") == True
assert correct_bracketing("()()(()(()))") == True
assert correct_bracketing("(()") == False
assert correct_bracketing("(()()()())") == True
assert correct_bracketing("(()()()()(") == False
assert correct_bracketing("(((((())") == False
assert correct_bracketing("(()((())()") == False
assert correct_bracketing("((())") == False
assert correct_bracketing("(((()") == False
assert correct_bracketing("((())()(()") == False
assert correct_bracketing("((()") == False
assert correct_bracketing("(()))") == False
assert correct_bracketing("(())") == True
assert correct_bracketing("()()") == True
assert correct_bracketing("(((((((((())))))))))") == True
assert correct_bracketing("(((((((((())))))))))()") == True
assert correct_bracketing("(())")
assert correct_bracketing("")
assert correct_bracketing("()()()()()()()")
assert not correct_bracketing("(()))")
assert correct_bracketing("()()()(()()()()()()()()(()()))")
assert not correct_bracketing("()()()(()()()()()()()()(()()))))")
assert correct_bracketing("()" * 10 ** 6)
assert correct_bracketing("()(()())") == True
assert correct_bracketing("()(()())()") == True
assert correct_bracketing("()(()()))") == False
assert correct_bracketing("(()(()())") == False
assert correct_bracketing("())(()())") == False
assert not correct_bracketing("((")
assert not correct_bracketing(")))")
assert correct_bracketing("()") == True, "simple string"
assert correct_bracketing("(") == False, "wrong string"
assert correct_bracketing(")") == False, "wrong string"
assert correct_bracketing("()(") == False, "wrong string"
assert correct_bracketing("())") == False, "wrong string"
assert correct_bracketing("(()") == False, "wrong string"
assert correct_bracketing("())()") == False, "wrong string"
assert correct_bracketing("((()))") == True, "nested string"
assert correct_bracketing("((())))") == False, "wrong string"
assert correct_bracketing("((())))()") == False, "wrong string"
assert correct_bracketing("") == True, "empty string"
assert not correct_bracketing("((()()")
assert correct_bracketing("((()))()")
assert correct_bracketing("(())(())") == True
assert correct_bracketing("()(") == False
assert correct_bracketing("(()())") == True
assert correct_bracketing("(()())()") == True
assert correct_bracketing("(()())()(()())") == True
assert correct_bracketing('(()))') == False
assert correct_bracketing('(()') == False
assert correct_bracketing('(()())()((()))') == True
assert correct_bracketing('((((()))))') == True
assert correct_bracketing('((()))))') == False
assert correct_bracketing("()()((()))") == True
assert correct_bracketing("()(()") == False
assert correct_bracketing("()()()()(") == False
assert correct_bracketing("()")
assert not correct_bracketing("()(")
assert not correct_bracketing("(()")
assert not correct_bracketing("(()()()()()()()()()()()()()())(")
assert not correct_bracketing("(()()")
assert not correct_bracketing("()())")
assert not correct_bracketing("(()())(")
assert not correct_bracketing("((()())")
assert not correct_bracketing("(()()))")
assert correct_bracketing("(())))") == False
assert correct_bracketing("((((((((((") == False
assert correct_bracketing("((())())") == True
assert correct_bracketing("(())(())(())")
assert not correct_bracketing("(())(())(())(")
assert not correct_bracketing("(()(())(())")
assert not correct_bracketing("())(())(())")
assert correct_bracketing("()()")
assert not correct_bracketing("(((")
assert not correct_bracketing("))")
assert not correct_bracketing("()))")
assert correct_bracketing('()(()') == False
assert correct_bracketing('()') == True
assert correct_bracketing('()(()())') == True
assert correct_bracketing("(((())))") == True
assert correct_bracketing("(()()") == False
assert correct_bracketing("(())(") == False
assert not correct_bracketing("(())))")
assert correct_bracketing("()()()")
assert not correct_bracketing("(()(")
assert correct_bracketing("(()()(()))") == True
assert correct_bracketing("(()()(())))") == False
assert correct_bracketing("((())(") == False
assert correct_bracketing("(((((((") == False
assert correct_bracketing("())()") == False
assert correct_bracketing("(()(") == False
assert correct_bracketing("((((((((()))))))))(") == False
assert correct_bracketing("(((()))))") == False
assert correct_bracketing("(((())))")
assert not correct_bracketing("()(()")
assert not correct_bracketing("))(()")
assert not correct_bracketing("(()()(()")
assert correct_bracketing("(()()(") == False
assert correct_bracketing("((()()()())") == False
assert correct_bracketing("((()))(()())") == True
assert correct_bracketing("(((()())()))") == True
assert correct_bracketing(")))((") == False
assert correct_bracketing("((())((()") == False
assert correct_bracketing("()))(()") == False
assert correct_bracketing("()(()(") == False
assert correct_bracketing(")()") == False
assert correct_bracketing('(())')
assert correct_bracketing('()()')
assert correct_bracketing('(((())))')
assert not correct_bracketing('()(()')
assert not correct_bracketing('(()))')
assert not correct_bracketing('((()')
assert not correct_bracketing('()(())()()(')
assert not correct_bracketing('((()(()')
assert correct_bracketing("()()(") == False
assert correct_bracketing("()())") == False
assert correct_bracketing("(()()(()") == False
assert correct_bracketing("()(())(") == False
assert correct_bracketing("(())()")
assert correct_bracketing("()(()(()))") == True
assert correct_bracketing("()(()(((()))") == False
assert not correct_bracketing('()(()()()()()(')
assert not correct_bracketing(')(()()()()()())')
assert correct_bracketing("((())))") == False
assert correct_bracketing("((((()))))") == True
assert correct_bracketing("(()(()))") == True
assert correct_bracketing("(()(())))") == False
assert not correct_bracketing("(((()))")
assert not correct_bracketing("((())))()")
assert not correct_bracketing("()(()(()())))")
assert not correct_bracketing("(a+b)*(c+d")
assert not correct_bracketing("((a+b)*(c+d)")
assert not correct_bracketing("a+b)*(c+d)")
assert not correct_bracketing("(a+b)*(c+d))")
assert not correct_bracketing("(a+b")
assert not correct_bracketing("((a+b")
assert correct_bracketing("()(())(())")
assert not correct_bracketing("()(())(()")
assert not correct_bracketing("()(((()))()")
assert correct_bracketing('(()()(()())') == False
assert correct_bracketing('(()())(()())') == True
assert not correct_bracketing("())))")
assert not correct_bracketing("((()")
assert not correct_bracketing("((())(()())")
assert not correct_bracketing("(())(()()")
assert not correct_bracketing("(())(()))")
assert not correct_bracketing("(())((()())")
assert not correct_bracketing("((())(()()")
assert not correct_bracketing("((())(())))")
assert not correct_bracketing("((())(())()")
assert not correct_bracketing("((())(())())))")
assert not correct_bracketing("((())(())()))")
assert correct_bracketing("())((") == False
assert correct_bracketing("(()()()") == False
assert correct_bracketing("(()()())") == True
assert correct_bracketing("(((((()))))") == False
assert correct_bracketing("(((((()))))))") == False
assert correct_bracketing("(((((()))))))(((((()))))))") == False
assert correct_bracketing("(()()()())(") == False
assert correct_bracketing("())(())((()") == False
assert not correct_bracketing("(())(")
assert not correct_bracketing("((())))")
assert correct_bracketing("(((") == False
assert correct_bracketing("())))") == False
assert correct_bracketing("()((())((())") == False
assert correct_bracketing("(())(())(()(()))") == True
assert correct_bracketing("(((())(()()(())))())") == True
assert correct_bracketing("((((((()))))))") == True
assert correct_bracketing("))(") == False
assert correct_bracketing("(((())())())") == True
assert correct_bracketing("(") is False
assert correct_bracketing(")") is False
assert correct_bracketing("()") is True
assert correct_bracketing("((())") is False
assert correct_bracketing("(()())") is True
assert correct_bracketing("(()()()(()()())())") is True
assert correct_bracketing("(()()()(()()())()") is False
assert correct_bracketing("())") is False
assert correct_bracketing("(()") is False
assert correct_bracketing("(())(") is False
assert correct_bracketing('())') == False
assert correct_bracketing('(())') == True
assert correct_bracketing('())()') == False
assert correct_bracketing('((()))') == True
assert correct_bracketing("(()(()))")
assert not correct_bracketing("(()(()")
assert correct_bracketing("(((())") == False
assert not correct_bracketing("("), "single opening bracket"
assert not correct_bracketing(")"), "single closing bracket"
assert not correct_bracketing("())"), "closing bracket before opening bracket"
assert not correct_bracketing("(()"), "opening bracket after closing bracket"
assert not correct_bracketing("(()))"), "extra closing bracket"
assert not correct_bracketing("((()"), "extra opening bracket"
assert correct_bracketing("((()))")
assert not correct_bracketing("((()()(")
assert correct_bracketing("()()()()()")
assert correct_bracketing("(())(()())")
assert not correct_bracketing("(((())")
assert not correct_bracketing("(((((")
assert not correct_bracketing(")))))))")
assert correct_bracketing("()()()()()()()()")
assert not correct_bracketing("((()))(")
assert not correct_bracketing("(((((())))")
assert correct_bracketing("(()()(()(())))") == True
assert correct_bracketing("(()()()(()") == False
assert correct_bracketing("(()()()(())))") == False
assert correct_bracketing("((") == False
assert correct_bracketing("))") == False
assert correct_bracketing("()()()()") == True
assert correct_bracketing("((((((((((()))))))))))") == True
assert correct_bracketing("((((((((((())))))))))))") == False
assert correct_bracketing('(()())')
assert not correct_bracketing('((')
assert not correct_bracketing('(()')
assert correct_bracketing("((()())") == False
assert correct_bracketing("(()()(()()))")
assert not correct_bracketing("()()()()(")
assert not correct_bracketing("()()()())")
assert correct_bracketing("()()()()()()") == True
assert correct_bracketing("(()()()()()()") == False
assert correct_bracketing("(()()()()()())") == True
assert correct_bracketing('()()') == True
assert correct_bracketing('((())') == False
assert correct_bracketing('') == True
assert correct_bracketing(')') == False
assert correct_bracketing('(') == False
assert correct_bracketing('(()())') == True
assert correct_bracketing('((') == False
assert correct_bracketing('))') == False
assert correct_bracketing("())(())((") == False
assert correct_bracketing("()((())(()") == False
assert correct_bracketing("((()())(())())") == True
assert correct_bracketing("()(()") is False
assert correct_bracketing("((()") is False
assert correct_bracketing("()()()()")
assert not correct_bracketing("(())))(")
