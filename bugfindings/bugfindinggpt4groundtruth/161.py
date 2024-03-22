
def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    flg = 0
    idx = 0
    new_str = list(s)
    for i in s:
        if i.isalpha():
            new_str[idx] = i
            flg = 1
        idx += 1
    s = ""
    for i in new_str:
        s += i
    if flg == 0:
        return s[len(s)::-1]
    return s
assert solve("") == ""########################################################################################################################################################################################################################
assert 	solve("") == ""
assert 	solve("a11b22") == "A11B22"
assert 	solve('aAa') == 'AaA'
assert 	(solve("123") == "321")
assert 	(solve("") == "")
assert 	(solve("A") == "a")
assert 	(solve("  ") == "  ")
assert 	(solve("   ") == "   ")
assert 	(solve("  A") == "  a")
assert solve('') == ''
assert solve('a') == 'A'
assert solve('A') == 'a'
assert solve('b') == 'B'
assert solve('B') == 'b'
assert solve('C') == 'c'
assert solve('1') == '1'
assert solve('1a') == '1A'
assert solve('1b') == '1B'
assert solve('1B') == '1b'
assert solve('1c') == '1C'
assert solve('1C') == '1c'
assert solve('1cA') == '1Ca'
assert 	solve('abc') == 'ABC'
assert 	solve('hello world') == 'HELLO WORLD'
assert 	solve('foo bar') == 'FOO BAR'
assert solve("a") == "A"
assert solve("A") == "a"
assert solve("") == ""
assert 	solve('abcdefghijklmnopqrstuvwxyz')
assert 	solve('123') 	== '321'
assert 	solve("A") == "a"
assert 	solve("123") == "321"
assert 	solve("aA") == "Aa"
assert 	solve("Aa") == "aA"
assert 	(solve('ABCDEFG'	) == 'abcdefg')
assert solve("abCd") == "ABcD"
assert 	solve("") == "", "3rd example"
