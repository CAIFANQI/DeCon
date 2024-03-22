
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
assert compare_one(5, 5) == None
assert compare_one(5, 5.0) == None
assert compare_one('5', '5') == None
assert compare_one('5', 5.0) == None
assert compare_one('5', '5.0') == None
assert compare_one('5', '5.000000') == None
assert compare_one('5.5', '5.5') == None
assert compare_one('5.5', 5.5) == None
assert compare_one(1.1, 2.2) == 2.2
assert compare_one(4, 5) == 5
assert compare_one(5, 4) == 5
assert compare_one('4', '5') == '5'
assert compare_one('4.5', '4.4') == '4.5'
assert compare_one('4.4', '4.5') == '4.5'
assert compare_one('4.9', '4.8') == '4.9'
assert compare_one('4.8', '4.9') == '4.9'
assert compare_one('4.8', '4.7') == '4.8'
assert compare_one('4.7', '4.8') == '4.8'
assert compare_one('4.7', '4.6') == '4.7'
assert compare_one('4.6', '4.7') == '4.7'
assert compare_one('4.6', '4.5') == '4.6'
assert compare_one('4.5', '4.6') == '4.6'
assert compare_one("1", 1.0) == None, "Passed"
assert compare_one(1, 1) == None, "Passed"
assert compare_one(1, 1.0) == None, "Passed"
assert compare_one("1", "1") == None, "Passed"
assert compare_one("1.1", "1.1") == None, "Passed"
assert compare_one("1,1", "1,1") == None, "Passed"
assert compare_one(1, 1.0) == None
assert compare_one("1", 1) == None
assert compare_one("1", 1.0) == None
assert compare_one("1", "1") == None
assert compare_one("1", "1.0") == None
assert compare_one("1", "1.") == None
assert compare_one(1, 2) == 2
assert compare_one("1", 2) == 2
assert compare_one("1", 2.0) == 2.0
assert compare_one(1, 2.0) == 2.0
assert compare_one(1.0, 2.0) == 2.0
assert compare_one(1, 1.1) == 1.1
assert compare_one("1", 1.1) == 1.1
assert compare_one("1", "1.1") == "1.1"
assert compare_one("1.1", 1) == "1.1"
assert compare_one("1.1", "1") == "1.1"
assert compare_one(3, 3) == None
assert compare_one("3", "3") == None
assert compare_one("3.0", "3.0") == None
assert compare_one("3.1", "3.1") == None
assert compare_one("3.1", "3.10") == None
assert compare_one("3.1", 3.1) == None
assert compare_one('1.2', 2) == 2
assert compare_one(1, 10) == 10
assert compare_one("1.00000", 10) == 10
assert compare_one("1,00", 10) == 10
assert compare_one("1.0000", 10) == 10
assert compare_one(5, 6) == 6
assert compare_one("5", 6) == 6
assert compare_one("5.0", 6.0) == 6.0
assert compare_one("5.0", "6.0") == "6.0"
assert compare_one("5", "6") == "6"
assert compare_one(0, 0) is None
assert compare_one('0,0', '0,0') is None
assert compare_one('3.14', '3.14') is None
assert compare_one('3.14',' 3,14 ') == None
assert compare_one('3.14', '3.14  ') is None
assert compare_one('3.14', '3.14   ') is None
assert compare_one("100", "100.01") == '100.01'
assert compare_one("100", "101") == '101'
assert compare_one("100.0", "101") == '101'
assert compare_one("100.0", "100.01") == '100.01'
assert compare_one("100.01", "100.1") == '100.1'
assert compare_one("100.0", "100.1") == '100.1'
assert compare_one(1.1, 1.) == 1.1
assert compare_one(4, 4) == None
assert compare_one("4", "4") == None
assert compare_one("4.4", 4.4) == None
assert compare_one("4.4", "4.40") == None
assert compare_one("4.40", "4.4") == None
assert compare_one("1","1") == None
assert compare_one("1.5","1.5") == None
assert compare_one("1.5",1.5) == None
assert compare_one(1.5,1.5) == None
assert compare_one(1.5, 1.5) == None
assert compare_one(5, "5.3") == '5.3'
assert compare_one("5", "5.3") == '5.3'
assert compare_one("5.3", "5.3") == None
assert compare_one(1.0, 1.0) == None
assert compare_one("1.0", "1.0") == None
assert compare_one('.3', '3.')
assert compare_one('3.', '.3')
assert compare_one(2, 3) == 3
assert compare_one('1.1', '2.2') == '2.2'
assert compare_one("10", "10") == None
assert compare_one(5.5, 5) == 5.5
assert compare_one(5, 5.5) == 5.5
assert compare_one('5', '5.1') == '5.1'
assert compare_one(2, 3.2) == 3.2
assert compare_one('2', '3.2') == '3.2'
assert compare_one('2.2', '2.2') == None
assert compare_one('2', '2.2') == '2.2'
assert compare_one('2.2', '2') == '2.2'
assert compare_one('2', '2') == None
assert compare_one('1', '1') == None
assert compare_one('1', 1) == None
assert compare_one(0, 0.0) == None
assert compare_one("0", "0") == None
assert compare_one("0.1", "0.1") == None
assert compare_one("-0.1", "-0.1") == None
assert compare_one("-0.1", -0.1) == None
assert compare_one(2., 3) == 3
assert compare_one(2, 3.) == 3
assert compare_one("1.1", "1.2") == "1.2"
assert compare_one("1.2", "1.1") == "1.2"
assert compare_one("1.2", "1") == "1.2"
assert compare_one("1", "1.2") == "1.2"
assert compare_one(2, 2.5) == 2.5
assert compare_one('12.8', '12.8') is None
assert compare_one('12.7', 12.7) is None
assert compare_one('12', '12') is None
assert compare_one('12.7', '12.7') is None
assert compare_one('12.8', 12.8) is None
assert compare_one("10.5", "10.55") == "10.55"
assert compare_one('1', 2) == 2
assert compare_one('1.0', 2.0) == 2.0
assert compare_one("10", 10) is None
assert compare_one(10.0, 10.0) is None
assert compare_one("10.0", "10.0") is None
assert compare_one("10.0", "10") is None
assert compare_one("10", "10.0") is None
assert compare_one("3","3") == None, "compare_one not correctly implemented"
assert compare_one("3",3) == None, "compare_one not correctly implemented"
assert compare_one(0.3, 0.3) == None, "compare_one not correctly implemented"
assert compare_one("0.1", 0.1) == None, "compare_one not correctly implemented"
assert compare_one(2, 2.0) == None
assert compare_one("2.0", "2") == None
assert compare_one(2, "2") == None
assert compare_one(2, "2.0") == None
assert compare_one("3.1", 3.2) == 3.2
assert compare_one('5.5', '5.5') is None
assert compare_one("7", "7.5") == "7.5"
assert compare_one("5.1", "5.2") == "5.2"
assert compare_one(1.1, 1.1) is None
assert compare_one('3.3', 4.3) == 4.3
assert compare_one(4, 4.5) == 4.5
assert compare_one(3, "3") is None
assert compare_one(3, 5) == 5
assert compare_one(1, 1) is None
assert compare_one("1", "1") is None
assert compare_one(1, 100) == 100
assert compare_one(1, 99) == 99
assert compare_one('4',4.5) == 4.5
assert compare_one('52.1', 52.1) is None
assert compare_one(1, 1.) == None
assert compare_one(3, 5.5) == 5.5
assert compare_one(0.5, 2) == 2.0
