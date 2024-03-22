

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return ' '.join([str(x) for x in range(n)])
assert 	string_sequence(0) == "0"
assert string_sequence(1) == "0 1"
assert string_sequence(2) == "0 1 2"
assert string_sequence(3) == "0 1 2 3"
assert 	string_sequence(1) == '0 1'
assert 	string_sequence(7) == '0 1 2 3 4 5 6 7'
assert string_sequence(0) == "0"
assert string_sequence(-1) == ""
assert 	string_sequence(1) == "0 1"
assert 	string_sequence(2) == "0 1 2"
assert 	string_sequence(5) == "0 1 2 3 4 5"
assert string_sequence(4) == "0 1 2 3 4"
assert string_sequence(5) == "0 1 2 3 4 5"
assert string_sequence(6) == "0 1 2 3 4 5 6"
assert string_sequence(7) == "0 1 2 3 4 5 6 7"
assert string_sequence(8) == "0 1 2 3 4 5 6 7 8"
assert string_sequence(9) == "0 1 2 3 4 5 6 7 8 9"
assert string_sequence(10) == "0 1 2 3 4 5 6 7 8 9 10"
assert string_sequence(20) == "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
assert 	string_sequence(-1) == ""
