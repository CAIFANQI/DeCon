

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
assert correct_bracketing("<>") == True
assert correct_bracketing("</>") == False
assert correct_bracketing("<)") == True
assert correct_bracketing("< >") is False
assert not correct_bracketing("<"), "<>"
assert not correct_bracketing("<=>"), "<>"
assert not correct_bracketing("</>"), "<>"
assert not correct_bracketing("<"), "<"
assert not correct_bracketing("</>"), "<"
assert not correct_bracketing("<=>"), "<"
assert correct_bracketing("<<<><><><><><><><><><><>") == False
assert correct_bracketing("{{") == False
assert correct_bracketing("}}") == False
assert correct_bracketing("]}") == False
assert correct_bracketing(")]") == False
assert correct_bracketing(")]]") == False
assert correct_bracketing("[)]") == False
assert correct_bracketing("[(]") == False
assert correct_bracketing("[](]") == False
assert correct_bracketing("[][(]") == False
assert correct_bracketing("[]][(]") == False
assert correct_bracketing("[)]]") == False
assert correct_bracketing("[)](]") == False
assert correct_bracketing("()") == False
assert correct_bracketing("(<)") == False
assert correct_bracketing("(<>)") == False
assert correct_bracketing("()(<>)") == False
assert correct_bracketing("(<(<>)>)") == False
assert correct_bracketing("()<(<>)>") == False
assert correct_bracketing("(<(<(<>)>)>") == False
assert correct_bracketing("()<()<()<(<>)>") == False
assert correct_bracketing("<{>") == False
assert correct_bracketing("<}{>") == False
assert correct_bracketing("<}{") == False
assert correct_bracketing("}}{>") == False
assert correct_bracketing("}}{") == False
assert correct_bracketing("{<}") == False
assert correct_bracketing("{<}{>") == False
assert correct_bracketing("{<}{") == False
assert correct_bracketing("}><{>") == False
assert correct_bracketing("}><{") == False
assert correct_bracketing("<>  ") == False
assert correct_bracketing("<>    ") == False
assert correct_bracketing("<>  < <>") == False
assert correct_bracketing("<>  < < < <>") == False
assert correct_bracketing("<>  < < < < < <>") == False
assert correct_bracketing("<>  < < < < < < < <>") == False
assert correct_bracketing("<>  < < < < < < < < < <>") == False
assert correct_bracketing("<") is False
assert correct_bracketing("[]") is False
assert correct_bracketing("[<>]") is False
assert correct_bracketing("[]<>") is False
assert correct_bracketing('<>') == True
assert correct_bracketing("[<]<[<]<[<]>") is False
assert correct_bracketing("<]<[<]>[<]>") is False
assert correct_bracketing("</>asd<asd<") == False
assert correct_bracketing("<") == False
assert correct_bracketing("</><><>") == False
assert correct_bracketing('<<') == False
assert correct_bracketing('<<<>>>') == True
assert correct_bracketing("}") == False, "Incorrect bracketing"
assert correct_bracketing("}{") == False, "Incorrect bracketing"
assert correct_bracketing("{}}") == False, "Incorrect bracketing"
assert correct_bracketing("}{{") == False, "Incorrect bracketing"
assert correct_bracketing("{<") == False, "Incorrect bracketing"
assert correct_bracketing("{{") == False, "Incorrect bracketing"
assert correct_bracketing("(<=") == False
assert correct_bracketing("(<>") == False
assert correct_bracketing("}}}}") == False
assert correct_bracketing('<') == False
assert correct_bracketing('>') == False
assert correct_bracketing("< < < > >") is False
assert correct_bracketing("< < < < >") is False
assert correct_bracketing("<  < >  < >") is False
assert correct_bracketing("<  < >  < < >") is False
assert correct_bracketing("()[]") == False
assert correct_bracketing("(){}") == False
assert correct_bracketing("()[]{}") == False
assert correct_bracketing("[]()") == False
assert correct_bracketing("[](){}") == False
assert correct_bracketing("[]()[]{}") == False
assert correct_bracketing("()[][]{}") == False
assert correct_bracketing("{<>}") == False
assert correct_bracketing("{<=>}") == False
assert correct_bracketing('>>') == False
assert correct_bracketing('<<<') == False
assert correct_bracketing('>>>>') == False
assert correct_bracketing("[]") == False
assert correct_bracketing("{}") == False
assert correct_bracketing("()<>") == False
assert correct_bracketing("{{}}") == False
assert correct_bracketing("{}{}{}{}") == False
assert correct_bracketing("{()}") == False
assert correct_bracketing("{{{}}}{}") == False
assert correct_bracketing("{}{{}}") == False
assert correct_bracketing("{}(){}") == False
assert correct_bracketing("{}[{}]") == False
assert correct_bracketing("{{}}{}") == False
assert correct_bracketing("{(){}}") == False
assert correct_bracketing("{[()]{}}") == False
assert correct_bracketing("{()}[]") == False
assert correct_bracketing("{[(){}]}") == False
assert correct_bracketing("{()[]}") == False
assert correct_bracketing("{[()[]]}") == False
assert correct_bracketing("< >") == False
assert correct_bracketing('(<)]') == False
assert correct_bracketing('((>])') == False
assert correct_bracketing('(<<(<))]') == False
assert correct_bracketing('(<<<<(>))')== False
assert correct_bracketing('(<<<<(>>>))') == False
assert correct_bracketing('((<(<(<)>(>>)))') == False
assert correct_bracketing('((((<(<(<(<(<(<)>))>(>>))))<(<(<(<(<(<(<)>))>)))') == False
assert correct_bracketing('{<>}') == False
assert correct_bracketing('(<>)') == False
assert correct_bracketing('(<>)()') == False
assert not correct_bracketing("(")
assert not correct_bracketing(")")
assert not correct_bracketing("[[(")
assert not correct_bracketing("[()")
assert not correct_bracketing("[)]")
assert not correct_bracketing(")](")
assert not correct_bracketing("(](")
assert not correct_bracketing(")]")
assert not correct_bracketing("](")
assert not correct_bracketing("[]")
assert not correct_bracketing("[]](")
assert not correct_bracketing("([]")
assert not correct_bracketing("[(]")
assert not correct_bracketing("[][(")
assert not correct_bracketing(")([(")
assert not correct_bracketing("])(")
assert not correct_bracketing("[(](")
assert not correct_bracketing("[(][(")
assert not correct_bracketing("[)(")
assert not correct_bracketing("][(")
assert not correct_bracketing(")(")
assert correct_bracketing("!") == False
assert not correct_bracketing("<")
assert not correct_bracketing("<>") == False
assert correct_bracketing("<>")
assert not correct_bracketing("}") # there is no closing bracket
assert not correct_bracketing("{{}}") # there are two or more opening brackets
assert not correct_bracketing("{<")
assert not correct_bracketing("{}")
assert not correct_bracketing("{{}}") # two or more opening brackets
assert not correct_bracketing("}{")
assert not correct_bracketing("}{}")
assert not correct_bracketing("{<{}")
assert not correct_bracketing("{<>}") # no opening bracket
assert not correct_bracketing("{}<") # no opening bracket
assert not correct_bracketing("{{}<")
assert not correct_bracketing("{}{}<>")
assert not correct_bracketing("}{}<>")
assert not correct_bracketing("}}{}<>")
assert correct_bracketing('()()') == False
assert correct_bracketing('((()))()') == False
assert correct_bracketing(')[(]()') is False
assert correct_bracketing('][(]') is False
assert correct_bracketing('][(]()') is False
assert correct_bracketing(']([)]') is False
assert correct_bracketing('([)]') is False
assert correct_bracketing('([)]()') is False
assert correct_bracketing("[") == False
assert correct_bracketing("]") == False
assert correct_bracketing("<|>") == False
assert correct_bracketing("<<>") == False
assert correct_bracketing("()()" * 100) == False
assert correct_bracketing("<(<)") == True
assert correct_bracketing("(( )))") == False
assert correct_bracketing("()(" * 100) == False
assert correct_bracketing("(<>" * 100) == False
assert correct_bracketing("(<(<)" * 100) == False
assert correct_bracketing("(< < (>)" * 100) == False
assert correct_bracketing("( )" * 100) == False
assert correct_bracketing("(( ))" * 100) == False
assert correct_bracketing("(( )))" * 100) == False
assert correct_bracketing("(< < (>))" * 100) == False
assert correct_bracketing("<>/") == False
assert correct_bracketing("[([][])") is False
assert correct_bracketing("[[(][])") is False
assert correct_bracketing("(()()") is False
assert correct_bracketing("[[]") is False
assert correct_bracketing("[]]") is False
assert correct_bracketing("(] ] [ ( )") is False
assert not correct_bracketing("<>}")
assert not correct_bracketing("{>}")
assert not correct_bracketing("{{}")
assert not correct_bracketing("{<>}")
assert correct_bracketing('>< ') == False
assert correct_bracketing('< <') == False
assert correct_bracketing('< < < < < <') == False
assert correct_bracketing("(<>)<>") == False
assert correct_bracketing("<a") == True
assert correct_bracketing("a>") == False
assert not correct_bracketing("<><")
assert not correct_bracketing("<<><>")
assert not correct_bracketing("<<<>><<")
assert correct_bracketing('((())') == False
assert correct_bracketing('(()(())') == False
assert correct_bracketing('(()()()()') == False
assert not correct_bracketing("]")
assert not correct_bracketing("{") # missing "}"
assert not correct_bracketing("[(")
assert correct_bracketing("<><>") # check cases where only one is required
assert correct_bracketing('< < < > > >') == False
assert correct_bracketing("()<><()") == False
assert correct_bracketing("</>>") == False
assert correct_bracketing("</>><") == False
assert correct_bracketing("<<>[]<<>[]>>>") == False
