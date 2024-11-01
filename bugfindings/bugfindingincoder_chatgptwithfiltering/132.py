
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    opening_bracket_index = []
    closing_bracket_index = []
    for i in range(len(string)):
        if string[i] == '(':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    for idx in opening_bracket_index:
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
    return cnt >= 2

    
assert is_nested('[[]]')
assert not is_nested(']]')
assert not is_nested('[][]')
assert not is_nested("[]")
assert is_nested('[[[[[[]]]]][]][]') == True
assert is_nested('[[]]') == True
assert is_nested('[[]][]') == True
assert is_nested('[[]][][[]]') == True
assert is_nested('[[[]]]') == True
assert is_nested('[[[]]][]') == True
assert is_nested('[[[]]][][[]]') == True
assert is_nested('[[[]]][][[]]]') == True
assert is_nested('[[[]]][][[[]]]') == True
assert is_nested('[[[]]][][[[]]][]') == True
assert is_nested('[[[]]][][[[]]][][]') == True
assert is_nested('[[[]]][][[[]]][][][]') == True
assert is_nested('[[[]]][][[[]]][][][][[]]]') == True
assert is_nested('[[[]]][][[[]]][][][][[]]][]') == True
assert is_nested('[[[]]][][[[]]][][][][[]]][][[]]') == True
assert is_nested('[[[]]][][[[]]][][][][[]]][][[]]]') == True
assert is_nested('[[[]]][][[[]]][][][][[]]][][[]]][]') == True
assert is_nested('[[[]]][][[[]]][][][][[]]][][[]]][][[]]') == True
assert is_nested('[[[]]][]')
assert is_nested('[[[]]][][]')
assert is_nested('[[[[]]]]]')
assert is_nested('[([])[]][]][]]')
assert is_nested("[[]]") is True
assert is_nested("[[]][]") is True
assert is_nested("[[][]]") is True
assert is_nested("[[[[[]]]]]") is True
assert is_nested("[[[[[]]]]][]") is True
assert is_nested("[[[[[]]]]]][]") is True
assert is_nested("[[[[[]]]]]][][]") is True
assert is_nested("[[[[[]]]]]][][][]") is True
assert is_nested("[[[[[]]]]]][][][][][]") is True
assert is_nested("[[[[[]]]]]][][][][][][]") is True
assert is_nested("[[[[[]]]]]][][][][][][][]") is True
assert is_nested("[[[[[]]]]]][][][][][][][][]") is True
assert is_nested("[[[[[]]]]]][][][][][][][][][]") is True
assert is_nested("[[[[[]]]]]][][][][][][][][][][]") is True
assert is_nested("[[[[[]]]]]][][][][][][][][][][][]") is True
assert is_nested('[][][][][][][][][][][][][][][][][][]') == True
assert is_nested('[][][][][][][][][][][][][][][][][][][][][][][][]') == True
assert is_nested('[[]][][[]][]') == True
assert is_nested('[[]][][[]][][[]][]') == True
assert is_nested('[[]][][[]][][[]][][]') == True
assert is_nested('[[]][][[]][][[]][][][]') == True
assert is_nested('[[]][][[]][][[]][][][][][]') == True
assert is_nested('[[[]][]][][[]][][[]][]') == True
assert is_nested('[[[]][]][][[]][][[]][][]') == True
assert is_nested('[[[]][]][][[]][][[]][][][[]]') == True
assert is_nested('[[[]][]][][[]][][[]][][][[]][]') == True
assert is_nested('[[[]][]][][[]][][[]][][][[]][][]') == True
assert is_nested('[[[]][]][][[]][][[]][][][[]][][][]') == True
assert is_nested('[[[]][]][][[]][][[]][][][[]][][][][]') == True
assert is_nested('[][][][][][][]') == True
assert is_nested('[][][][][][][][]') == True
assert is_nested('[][][][][][][][][][]') == True
assert is_nested('[][]') == False
assert is_nested('[][][]') == True
assert is_nested('[[][][]') == True
assert is_nested('[[[]]]')
assert is_nested('[[[]][][]][][][][[][]]]')
assert is_nested('[[][][][][[][][][][][][[][][][][]]]') == True
assert is_nested('[[][[]]][]') == True
assert is_nested('[[[]]]') is True
assert is_nested('[]') is False
assert is_nested('[][1]') == True
assert not is_nested("[[]")
assert not is_nested("[][]")
assert not is_nested("[]][]")
assert is_nested("[[[][][][]]]") is True
assert is_nested("[[[][][][][][][]]][][][][][][]") is True
assert is_nested("[[[][][][][][][]]][][][][][][][][][][][][][][]") is True
assert is_nested('{[]}') == False
assert is_nested('{{[]}') == False
assert is_nested('{{}[]}') == False
assert is_nested('{[]{}}') == False
assert is_nested('[]{}{}') == False
assert is_nested('{}[]{}') == False
assert is_nested('{}{}{}') == False
assert is_nested('[]') == False
assert is_nested('{}[]') == False
assert is_nested('[[[[]]][]]') == True
assert is_nested('[][]()') == True
assert is_nested('{[]}[]()') == True
assert is_nested('[][](){}') == True
assert is_nested('{[]}[](){}') == True
assert is_nested('[][](){}[][][]') == True
assert is_nested('{[]}(){}[][][]') == True
assert is_nested('{[]}[](){}[][][]') == True
assert is_nested('[][](){}[][][]{}[]') == True
assert is_nested('{[]}(){}[][][]{}[]') == True
assert is_nested('{[]}[](){}[][][]{}[]') == True
assert is_nested('[][](){}[][][]{}[]{}') == True
assert is_nested('{[]}(){}[][][]{}[]{}') == True
assert is_nested('{[]}[](){}[][][]{}[]{}') == True
assert is_nested("[[]]") == True
assert is_nested("[[[[]]]]A") == True
assert is_nested("[[[[[[[]]]]]]]A") == True
assert is_nested("[[[[[[[[[[]]]]]]]]]A") == True
assert is_nested("[[[[[[[[[[[[]]]]]]]]]]]]]A") == True
assert is_nested("[[[]][][]") == True
assert is_nested("[]") == False
assert is_nested("[[]") == False
assert is_nested('[[[][]]]') == True
assert is_nested('[][[]') == False
assert is_nested('[[]]') is True
assert is_nested('[[][]]') is True
assert is_nested('[[][][]]') is True
assert is_nested('[][[]]') == True
assert is_nested('[[][]]') == True
assert is_nested('[[[[]]]]]') == True
assert is_nested('[[][[]]]') == True
assert is_nested('[[[[[]]]]]]') == True
assert is_nested('[[][[[]]]]') == True
assert is_nested('[[[[[[]]]]]]]') == True
assert is_nested("[[a]]") == True
assert is_nested("[[][a]]") == True
assert is_nested("[a[]]") == True
assert is_nested("[[a]][]") == True
assert is_nested("[[a]][]]") == True
assert is_nested("[[][a]][]") == True
assert is_nested("[[a]][][]") == True
assert is_nested("[[a][]]") == True
assert is_nested("[][[a]]") == True
assert is_nested("[][[a]][]") == True
assert is_nested("[[a]][][a]]") == True
assert is_nested("[[][a]][][a]]") == True
assert is_nested("[[a]][][a]][]") == True
assert is_nested("[[a]][][a]][][]") == True
assert is_nested("[][[a]][][a]][]") == True
assert is_nested("[][[a]][][a]][][]") == True
assert is_nested("[[a]][][a]][][a]]") == True
assert is_nested('[[]][][]') == True
assert is_nested('[[]][][][]') == True
assert is_nested('[[]][][][][]') == True
assert is_nested('[[][][][][][][][][][][][][][][][][]][]') == True
assert is_nested('[][][][]') == True
assert is_nested('[[][][]]') == True
assert is_nested('[[][]]]') == True
assert is_nested('[[][]]][]') == True
assert is_nested('[[[[]]][]]]') == True
assert is_nested('[][][][[]') == True
assert is_nested('[][][[][]]') == True
assert is_nested('[[[][][][]]]') == True
assert is_nested('[[[[[]]]]][]') == True
assert is_nested('[[[[[[[]]]]]]]') == True
assert is_nested('[][][][][[][][][][[][][][][[][][][][[][][][]]]]]') == True
assert is_nested("[][[]]") == True
assert is_nested("[][][]") == True
assert is_nested("[][][][][]") == True
assert is_nested("[[][[][[]]]][]") == True
assert is_nested("[[[][[]]]]") == True
assert is_nested("[[[][[]]][]]") == True
assert is_nested("[[[[[][[][[]]]]]]]") == True
assert is_nested("[[[[[][[]]]]]]][]") == True
assert is_nested("[[][][[]]]") == True
assert is_nested("[[[][[][][[]]]]]") == True
assert is_nested("[[[[]]][]]]") == True
assert is_nested("[[][[]]]") == True
assert is_nested("[[[]]]") == True
assert is_nested("[[[[[]]]]]") == True
assert is_nested("[[[[[[[]]]]]]]") == True
assert is_nested("[[[[[[[]]]]]]][]") == True
assert is_nested("[[[[[[[]]]]]]][][]") == True
assert is_nested("[[[[[[[]]]]]]][][][]") == True
assert is_nested("[[[[[[[]]]]]]][][][][]") == True
assert is_nested('[[][][][][]]') == True
assert is_nested('[[][][][][][][][][][]]') == True
assert is_nested('[[]][[]]')
assert not is_nested('()')
assert not is_nested('([])')
assert not is_nested('([])()')
assert not is_nested('([])()[]')
assert not is_nested('([)]')
assert not is_nested('()([])')
assert not is_nested(')([])')
assert is_nested("[[]][]") == True
assert is_nested("[[[]][[]][]]") == True
assert is_nested('[[[]]][][]') == True
assert is_nested('[]][[]]') == True
assert is_nested('[][[]]]') == True
assert is_nested('[][[]]][]') == True
assert is_nested('[][[]]][][]') == True
assert is_nested('[[[]]][][][]') == True
assert is_nested('[[[]]][][][][]') == True
assert is_nested('[[[]]][][][][][][]') == True
assert is_nested("[[[]]]") is True
assert is_nested("[[]][][[[]]]") is True
assert is_nested("[[[][[]]]]]") is True
assert is_nested("[]") is False
assert is_nested("[[[[][][][[][][][[][][][[][][][[][][][[]]]]]]]]]") is True
assert is_nested('[[[[[]]]]]') == True
assert is_nested("[][][]")
assert not is_nested("[][][")
assert is_nested('[][[[[]]]]]') == True
assert is_nested('[][][[[[]]]]]') == True
assert is_nested('[[[[[[[[]]]]]]]]]') == True
assert is_nested('[[[]][][]]') == True
assert is_nested('[[]') == False
assert is_nested("[[]][][[]]]") is True
assert is_nested("[[[][]]]") is True
assert is_nested("[[[][][]]]") is True
assert is_nested("[[[][][]]][][][][][[[][][]]]") is True
assert is_nested("[[[][][]]][][][][][][[[][][]]][]") is True
assert is_nested("[][]") is False
assert is_nested('[') == False
assert is_nested(']') == False
assert is_nested("[]]") == False
assert is_nested('[[][]') == True
assert is_nested('[[][[][[]]]') == True
assert is_nested('[[][[][[]][]]]') == True
assert is_nested("[[([])]]") == True
assert is_nested("[][[][]][]") == True
assert is_nested("[[]()]") == True
assert is_nested("[([)]]") == True
assert is_nested("[()[]()]") == True
assert is_nested("[()[][()]]") == True
assert is_nested("[()()[]()]") == True
assert is_nested("[][()]") == True
assert is_nested("[][()[]]") == True
assert is_nested("[[][]()]") == True
assert is_nested("[][[][]]") == True
assert not is_nested("{}")
assert not is_nested('[()]')
assert is_nested("[][[]") == False
assert is_nested('[a][b]') == True
assert is_nested('[[a][]]') == True
assert is_nested('[][[a][]]') == True
assert is_nested('[a][b][c]') == True
assert is_nested('[a][b][][c]') == True
assert is_nested('[[][b][c]]') == True
assert is_nested('[][[a][b]]') == True
assert is_nested('[a][][[]]') == True
assert is_nested('[a][b][]') == True
assert is_nested('[a][b][][[]]') == True
assert is_nested('[[][][][]][]') == True
assert is_nested('[][[[][][]]][]') == True
assert is_nested('[][[[][][]]][][]') == True
assert is_nested('[][[[][][]]][][][]') == True
assert is_nested('[[][[[][][]]][][][]][]') == True
assert is_nested('[][[[][[[][[[]]]]]]][][][][]') == True
assert is_nested("[[][]") == True
assert is_nested("[[[][]]]") == True
assert is_nested('[][[]][]') == True
assert is_nested('[[][[]]') == True
assert is_nested('[[][[[]]]][][]') == True
assert is_nested('[][[[]]][][][][][][][][]') == True
assert is_nested("[[[]]]")
assert is_nested("[[[[]]]]") 
assert is_nested("[[][[[]]][][[]][][[[]]]") == True
assert is_nested('()') == False
assert is_nested('{}') == False
assert is_nested('(') == False
assert is_nested('[()][][]') == True
assert is_nested('[()][][') == False
assert is_nested("[][[]][]") == True
assert is_nested('[[][]]')
assert is_nested('[a][][]') == True
assert is_nested("[[]]")
assert not is_nested('[()')
assert not is_nested("[][[]")
assert is_nested('[([])]') is True
assert is_nested("[[]{}[]{}]") is True
assert is_nested("[[]{[]}{}]") is True
assert is_nested("{{{}{}}{}[]}") is False
assert is_nested("{{}{[]{}}}") is False
assert is_nested("{{[]{{}}{}}}") is False
assert is_nested("{{}{}{}{}}") is False
assert is_nested("{{}{{}{}}}") is False
assert is_nested("{{{}{{}}}{}}") is False
assert is_nested("{{{}{}}}") is False
assert is_nested('[[[]]][]]')
assert is_nested('(x)]') == False
assert is_nested('[x(x)]') == False
assert is_nested('([a])') == False
assert is_nested('([a])[]') == False
assert not is_nested("()[]")
assert is_nested("[[[]]][][]")
assert is_nested("[][][][][][]")
assert is_nested('[ []]') == True
assert not is_nested('(()')
assert not is_nested('())[]')
assert not is_nested('((()')
assert not is_nested("([)]")
assert not is_nested("(()")
assert is_nested('[([])]') == True
assert is_nested('[[]()[]') == True
assert is_nested('())') == False
assert is_nested('(()()()[[][]]') == True
assert is_nested('(()()[][()[]][[]()[]]') == True
assert is_nested('(()()()()[[][]]') == True
assert is_nested('(()()())[]') == False
assert is_nested('()[][]') == False
assert is_nested('([()]())') == False
