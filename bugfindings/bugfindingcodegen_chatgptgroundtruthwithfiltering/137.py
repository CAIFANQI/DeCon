
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    temp_a, temp_b = a, b
    if isinstance(temp_a, str): temp_a = temp_a.replace(',','.').replace('.',',')
    if isinstance(temp_b, str): temp_b = temp_b.replace(',','.')
    if float(temp_a) == float(temp_b): return None
    return a if float(temp_a) > float(temp_b) else b 
assert 	compare_one(2, 3) == 3
assert 	compare_one(2, "2.5") == "2.5"
assert 	compare_one(2, True) == 2
assert 	compare_one(2, False) == 2
assert 	compare_one(2, 2.5) == 2.5
assert 	compare_one(2, "1") == 2
assert compare_one('1.0', '2.0') == '2.0'
assert compare_one(1, 2) == 2
assert compare_one(2, 1) == 2
assert compare_one('2', '1') == '2'
assert 	compare_one(1.0, '1') == None
assert 	compare_one('1.0', '1') == None
assert 	compare_one('1', 1) == None
assert 	compare_one('1', '1.0') == None
assert compare_one(1.5, 2.5) == 2.5
assert compare_one('1.5', '2.5') == '2.5'
assert compare_one('1', '1.5') == '1.5'
assert compare_one('1', '2') == '2'
assert compare_one('1', '2.5') == '2.5'
assert compare_one(4,5) == 5
assert compare_one(4,4) == None
assert compare_one("5",5) == None
assert 	(compare_one(1.1, 2.2) == 2.2), "compare_one does not work with float"
assert 	(compare_one("1.1", "2.2") == "2.2"), "compare_one does not work with strings"
assert compare_one(1, 0.99) == 1
assert compare_one(1, '0.99') == 1
assert compare_one('1', '0.99') == '1'
assert compare_one(1.0, 2) == 2
assert compare_one('1.0', '2') == '2'
