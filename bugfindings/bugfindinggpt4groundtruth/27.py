

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.lower()
assert 	flip_case('A') == 'a'
assert 	flip_case('B') == 'b'
assert 	flip_case('a') == 'A'
assert 	flip_case('b') == 'B'
assert 	flip_case('ba') == 'BA'
assert 	flip_case('aB') == 'Ab'
assert 	flip_case('12345') == '12345'
assert 	flip_case('12345w') == '12345W'
assert 	flip_case('12345.w') == '12345.W'
assert 	flip_case('12345.W.E.Z.') == '12345.w.e.z.'
assert 	flip_case('12345.W.E.Z.X') == '12345.w.e.z.x'
assert flip_case(string="H") == "h", "One upper to lower"
assert flip_case(string="h") == "H", "One lower to upper"
assert flip_case(string="Hello") == "hELLO", "All lower to upper"
assert flip_case('') == ''
assert flip_case('aBc') == 'AbC'
assert flip_case('aBcD') == 'AbCd'
assert flip_case('AbCd') == 'aBcD'
