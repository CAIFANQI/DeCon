
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    a, b = x.split("/")
    c, d = n.split("/")
    a = int(b) * int(c)
    d = int(c) * int(b)
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator/denom == int(numerator/denom)):
        return True
    return False
assert 	(simplify("4/6", "2/3") == False)
assert 	(simplify("1/3", "3/2") == False)
assert 	(simplify("2/3", "1/3") == False)
assert 	(simplify("2/6", "3/4") == False)
assert 	simplify("1/4", "1/2") == False
assert 	simplify("1/2", "1/2") == False
assert 	simplify("1/4", "1/8") == False
assert 	simplify("1/2", "1/4") == False
assert 	simplify("3/4", "1/2") == False
assert 	simplify("1/2", "3/4") == False
assert 	simplify('1/3', '1/6') == False
assert 	simplify('1/3', '1/3') == False
assert 	simplify('1/3', '2/6') == False
assert simplify("1/2", "1/4") == False
assert simplify("1/4", "1/2") == False
assert not 	simplify('3/6', '1/3')
assert 	simplify("2/4", "3/4") == False
assert 	simplify("1/6", "3/6") == False
assert 	simplify("4/7", "3/7") == False
assert 	simplify("4/7", "5/7") == False
assert 	simplify("3/8", "3/8") == False
assert 	simplify("1/3", "1/6") == False
assert 	simplify("1/3", "1/2") == False
assert 	simplify('2/4', '1/2') == False
assert 	simplify('1/3', '1/2') == False
assert 	simplify('1/4', '1/2') == False
assert not simplify("6/7", "1/3")
