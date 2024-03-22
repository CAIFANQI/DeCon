
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

    
assert 	is_nested('[{]') == False
assert 	is_nested('{{[[(())]]}}') == True
assert 	is_nested('[[{}]]') == True
assert 	is_nested('[[[]][[[[][]]][[[[]]]][[[]]][[]]]') == True
assert 	is_nested("[") == False, "is_nested should return False if string starts with square brackets"
assert 	is_nested("[(])") == False, "is_nested should return False if string contains closing brackets without opening ones"
assert 	is_nested("[(])[{()}]") == True, "is_nested should return True if string contains valid nested brackets"
assert 	is_nested("[(]") == False, "is_nested should return False if string contains unbalanced opening brackets"
assert 	is_nested("[)]") == False, "is_nested should return False if string contains unbalanced closing brackets"
assert 	is_nested('()()[()]') == False
assert 	is_nested('[()(]') == False
assert 	is_nested('[') == False
assert 	is_nested(']') == False
assert 	is_nested('[[[[[[[[[[[[[[[[[(') == False
assert 	is_nested(']]]') == False
assert 	is_nested('()') == False
assert 	is_nested('[]') == False
assert 	is_nested('((()') == False
assert 	is_nested('[]]') == False
assert 	is_nested('[()(()[()()()()()()()()()()()()()()()()()]') == True
assert 	is_nested('[(])') == False, 'Incorrect'
assert 	is_nested('[') == False, 'Incorrect'
assert 	is_nested('[[[]][[[[[[[[[[]]]]]]]]]]]') == True
assert 	is_nested('[[[[]][[[[[[[[[[]]]]]]]]]]]') == True
assert 	is_nested('[[[[[[[[[[[]]]]]]]]]]') == True
assert 	is_nested('[[[[[[[[[]]]]]]]]]') == True
assert 	is_nested('[[](){([[[]]])})') 	== True
assert 	is_nested('[](){}[]') 		== False
assert 	is_nested('[()]{}') 		== False
assert 	is_nested('([])([]{})') 	== True
assert 	is_nested('[][]()') 		== True
assert 	is_nested('[(])') == False, "Error"
assert 	is_nested('[') == False, "Error"
assert 	is_nested(']') == False, "Error"
assert 	is_nested('(()') == False, "Error"
assert 	is_nested('[(])') == False
assert 	is_nested('[()[()]]') == True
assert 	is_nested('(()') == False
assert 	is_nested('[()()[()]]') == True
assert 	is_nested('[()()') == False
assert 	is_nested('[()[()]') == True
assert 	is_nested('[[]') == False
assert 	is_nested('[(())') == False
assert 	is_nested('(((()') == False
assert 	is_nested('()[()') == False
assert is_nested('()()') == False
assert is_nested('[(])') == False
assert is_nested('[(])]') == False
assert is_nested('[[]') == False
assert is_nested('[[[]]]') == True
assert is_nested('[') == False
assert is_nested('[()') == False
assert is_nested('[()[][]') == True
assert is_nested('[()[]]') == True
assert is_nested('([]()') == False
assert is_nested('(([])[])') == True
assert is_nested('(()[])') == False
assert 	is_nested('[(]') == False
assert 	is_nested('[()') == False
assert 	is_nested('[()[]()]') == True
assert 	is_nested('[()[[]()]]') == True
assert 	is_nested('[]()[]') == False
assert 	is_nested('[]()[[]') == False
assert 	is_nested('[[]()') == True
assert 	is_nested('[]]()') == False
assert 	is_nested('[[]()[]') == True
assert 	is_nested('[[]()[][]]') == True
assert 	is_nested('[[]()[]][[]') == True
assert 	is_nested('[[]()[[]][][]') == True
assert 	is_nested("[][][]") == True
assert 	is_nested("[[][]") == True
assert 	is_nested("[][][][]") == True
assert 	is_nested("[][[]") == False
assert 	is_nested("[][[][[") == False
assert 	is_nested("[][[]]") == True
assert 	is_nested("[][[][]") == True
assert is_nested('[()[[]{()()}()]') == True
assert is_nested('[({{()}})') == False
assert 	is_nested('[]') == False, "No nested brackets"
assert 	is_nested('[[[]]]') == True, "Three nested square brackets"
assert 	is_nested('[[[[[[[[[[[[[[[[[') == False, "Double nesting"
assert 	is_nested('[[[[[[[[[[[[[[[[[(') == False, "Double nesting"
assert 	is_nested('[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]') == True, "Four nested square brackets"
assert 	is_nested('[({}]') == False
assert 	is_nested('[()]{}([{}])') == True
assert 	is_nested('[({})]') == False
assert 	is_nested('[({})]{()}') == False
assert 	is_nested('[({})]{}') == False
assert 	is_nested('[({})]{}()') == False
assert 	is_nested('[({})]{}(())') == False
assert 	is_nested('[({})]{}(())()') == False
assert 	is_nested('[({})]{}(())((())') == False
assert 	is_nested('([1,2,3]') == False, 'Wrong output'
assert 	is_nested('([1,2,3[]') == False, 'Wrong output'
assert 	is_nested('[1,2,3[]]') == True, 'Wrong output'
assert 	is_nested('[1,[2,[3]]]') == True, 'Wrong output'
assert 	is_nested('[[]]') == True, 'Wrong output'
assert 	is_nested('[[[]]]') == True, 'Wrong output'
assert 	is_nested('[[[[]]]]') == True, 'Wrong output'
assert 	is_nested('[[[[[]]]]]') == True, 'Wrong output'
assert 	is_nested('[[[[[[]]]]]]]') == True, 'Wrong output'
assert not 	is_nested('(]')
assert not 	is_nested('()[')
assert not 	is_nested('[()]')
assert 	is_nested('[()[]]')
assert 	is_nested('[()[()]]')
assert 	is_nested('[([])[()]]')
assert 	is_nested('[([])[()]')
assert not is_nested('[')
assert not 	is_nested(']')
assert not 	is_nested('[()')
assert not 	is_nested('()[()')
assert not 	is_nested(']()')
assert not 	is_nested(']()[')
assert is_nested("(()[[]])") == True
assert is_nested("[]([{}])") == True
assert is_nested("[][]") == False
assert is_nested("{[{[()]()}]}") == True
assert is_nested("[[]") == False
assert is_nested("[{[]}]") == True
assert is_nested("{{{[]}[]}}") == True
assert is_nested("[[[]") == False
assert 	is_nested('[ab(c)]d]') == False
assert 	is_nested('[ab(c)d') == False
assert 	is_nested('[ab(c)d[]()]') == True
assert 	is_nested('[[]()]{}') == True
assert 	is_nested('[[](){{}}]') == True
assert 	is_nested('[[{}]') == True
assert 	is_nested('[{[]}]') == True
assert 	is_nested('[' + ']') == False
assert 	is_nested('[' + '(' + ']') == False
assert 	is_nested('([' + ']') == False
assert 	is_nested('[][[[[]]]]') == True
assert not is_nested('[()]')
assert is_nested('[([])((([[[]]])[])[])])')
assert is_nested('(((([]))[]))[]')
assert 	is_nested('[([])((([[[]]])))]{()}') == True
assert 	is_nested('[][][]') == True
assert 	is_nested('[][[[[[]]]]][[]][[]]') == True
assert 	is_nested('[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]') == True
