
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
assert compare_one(1, 2) == 2
assert compare_one(2, 1) == 2
assert compare_one(1.5, 2.5) == 2.5
assert compare_one(2.5, 1.5) == 2.5
assert compare_one("1.5", "2.5") == "2.5"
assert compare_one("2.5", "1.5") == "2.5"
assert compare_one("1,5", "2,5") == "2,5"
assert compare_one("2,5", "1,5") == "2,5"
assert compare_one("1.5", 2) == 2
assert compare_one(2, "1.5") == 2
assert compare_one("1,5", 2) == 2
assert compare_one(2, "1,5") == 2
assert compare_one("1.5", 2.5) == 2.5
assert compare_one(2.5, "1.5") == 2.5
assert compare_one("1,5", 2.5) == 2.5
assert compare_one(2.5, "1,5") == 2.5
assert compare_one(1, 1) == None
assert compare_one(1.5, 1.5) == None
assert compare_one("1.5", "1.5") == None
assert compare_one("1,5", "1,5") == None
assert compare_one("1.5", 1.5) == None
assert compare_one(1.5, "1.5") == None
assert compare_one("1,5", 1.5) == None
assert compare_one(1.5, "1,5") == None
assert compare_one("2", "3") == "3"
assert compare_one(2, 2) == None
assert compare_one(2.5, 2.5) == None
assert compare_one("2", "2") == None
assert compare_one("2.5", "2.5") == None
assert compare_one("2,5", "2,5") == None
assert compare_one(5.5, 3.2) == 5.5
assert compare_one("2.5", "3.1") == "3.1"
assert compare_one('3.5', '2.5') == '3.5'
assert compare_one('2,5', '1,5') == '2,5'
assert compare_one(3, 3) == None
assert compare_one(3.14, 2.71) == 3.14
assert compare_one("15", "20") == "20"
assert compare_one("3.14", "2.71") == "3.14"
assert compare_one(5, 5) == None
assert compare_one(10, 5) == 10
assert compare_one(5.5, 10.5) == 10.5
assert compare_one(10.5, 5.5) == 10.5
assert compare_one(5.5, 5.5) == None
assert compare_one("5", "10") == "10"
assert compare_one("10", "5") == "10"
assert compare_one("5.5", "10.5") == "10.5"
assert compare_one("10.5", "5.5") == "10.5"
assert compare_one("5", "5") == None
assert compare_one("5.5", "5.5") == None
assert compare_one(3.14, 3.14) == None
assert compare_one('3,14', '3,14') == None
assert compare_one("1", "2") == "2"
assert compare_one("2", "1") == "2"
assert compare_one("1", "1") == None
assert compare_one(5.5, 5.6) == 5.6
assert compare_one(5.6, 5.5) == 5.6
assert compare_one("5.5", "5.6") == "5.6"
assert compare_one("5.6", "5.5") == "5.6"
assert compare_one("5,5", "5.6") == "5.6"
assert compare_one("5,5", "5,5") == None
assert compare_one("3.14", 2.71) == "3.14"
assert compare_one(3.14, "2.71") == 3.14
assert compare_one("3,14", "2.71") == "3,14"
assert compare_one("3,14", 2.71) == "3,14"
assert compare_one(3.14, "2,71") == 3.14
assert compare_one(3.0, 3) == None
assert compare_one("3.0", "3") == None
assert compare_one("3,0", "3") == None
assert compare_one(0, 0) == None
assert compare_one(0.0, 0) == None
assert compare_one("0.0", "0") == None
assert compare_one("0,0", "0") == None
assert compare_one("3.5", "3.5") == None
assert compare_one(3.5, 3.5) == None
assert compare_one(2.5, 2.3) == 2.5
assert compare_one(2.3, 2.5) == 2.5
assert compare_one("2.71", "2.71") == None
assert compare_one("2,71", "2,71") == None
assert compare_one("2.71", "2,71") == None
assert compare_one("2,71", "2.71") == None
assert compare_one(5.0, 10.0) == 10.0
assert compare_one(10.0, 5.0) == 10.0
assert compare_one("5.0", "10.0") == "10.0"
assert compare_one("10.0", "5.0") == "10.0"
assert compare_one("5,0", "10,0") == "10,0"
assert compare_one("10,0", "5,0") == "10,0"
assert compare_one("5.0", "10,0") == "10,0"
assert compare_one("10.0", "5,0") == "10.0"
assert compare_one(5.0, 5.0) == None
assert compare_one("5.0", "5.0") == None
assert compare_one("5,0", "5,0") == None
assert compare_one(1, "2.5") == "2.5"
assert compare_one("2.5", 1) == "2.5"
assert compare_one(1, "2,5") == "2,5"
assert compare_one("2,5", 1) == "2,5"
assert compare_one("1.5", "2,5") == "2,5"
assert compare_one("2,5", "1.5") == "2,5"
assert compare_one("3,14", "2,71") == "3,14"
assert compare_one("3,14", "3,14") == None
assert compare_one(5.6, 2.3) == 5.6
assert compare_one(15, 15) == None
assert compare_one("10,5", "5,5") == "10,5"
assert compare_one(10.5, 10.5) == None
assert compare_one("10.5", "10.5") == None
assert compare_one("10,5", "10,5") == None
assert compare_one("7.5", "8.9") == "8.9"
assert compare_one("1.0", "1,0") == None
assert compare_one("3.14", "3.14") == None
assert compare_one("3.140", "3.140") == None
assert compare_one("3,140", "3,140") == None
assert compare_one("3.14", "3,14") == None
assert compare_one("3,14", "3.14") == None
assert compare_one(2.5, 3.5) == 3.5
assert compare_one(3.5, 2.5) == 3.5
assert compare_one('1', '2') == '2'
assert compare_one('2', '1') == '2'
assert compare_one('2', '2') == None
assert compare_one('1.5', '2.5') == '2.5'
assert compare_one('2.5', '1.5') == '2.5'
assert compare_one('2.5', '2.5') == None
assert compare_one("2.5", "2.3") == "2.5"
assert compare_one("2.3", "2.5") == "2.5"
assert compare_one("2,5", "2,3") == "2,5"
assert compare_one("2,3", "2,5") == "2,5"
assert compare_one("2.5", 2.3) == "2.5"
assert compare_one(2.3, "2.5") == "2.5"
assert compare_one("2,5", 2.3) == "2,5"
assert compare_one(2.3, "2,5") == "2,5"
assert compare_one(2.5, "2.5") == None
assert compare_one("2.5", 2.5) == None
assert compare_one("2,5", 2.5) == None
assert compare_one(2.5, "2,5") == None
assert compare_one(1.5, 2.3) == 2.3
assert compare_one(2.3, 1.5) == 2.3
assert compare_one(1.0, 1.0) == None
assert compare_one("1.5", "2.3") == "2.3"
assert compare_one("2.3", "1.5") == "2.3"
assert compare_one("1.0", "1.0") == None
assert compare_one("8", "12") == "12"
assert compare_one("5,5", "10,5") == "10,5"
assert compare_one("5.5", "10,5") == "10,5"
assert compare_one("5.5", "5,5") == None
assert compare_one(5.5, 3.5) == 5.5
assert compare_one("3.5", "2.5") == "3.5"
assert compare_one("3,5", "2,5") == "3,5"
assert compare_one(5, 5) is None
assert compare_one("4.5", "5.5") == "5.5"
assert compare_one(10, 10) == None
assert compare_one("2.5", "3.5") == "3.5"
assert compare_one("2,5", "3,5") == "3,5"
assert compare_one(2.0, 2) == None
assert compare_one("2", "2.0") == None
assert compare_one("2.5", "2,5") == None
assert compare_one("1,0", "1,0") == None
assert compare_one(1, "1") == None
assert compare_one(1.0, "1.0") == None
assert compare_one("3.4", "2.3") == "3.4"
assert compare_one("3,4", "2,3") == "3,4"
assert compare_one(3.4, 3.4) == None
assert compare_one(1.0, 2.0) == 2.0
assert compare_one(2.0, 1.0) == 2.0
assert compare_one("1.0", "2.0") == "2.0"
assert compare_one("2.0", "1.0") == "2.0"
assert compare_one("1,0", "2,0") == "2,0"
assert compare_one("2,0", "1,0") == "2,0"
assert compare_one("1.0", 2) == 2
assert compare_one(2, "1.0") == 2
assert compare_one("1,0", 2) == 2
assert compare_one(2, "1,0") == 2
assert compare_one("1.0", 2.0) == 2.0
assert compare_one(2.0, "1.0") == 2.0
assert compare_one("1,0", 2.0) == 2.0
assert compare_one(2.0, "1,0") == 2.0
assert compare_one("10", "10") == None
assert compare_one("10.0", "10.0") == None
assert compare_one("10,0", "10,0") == None
assert compare_one("2.4", "5.7") == "5.7"
assert compare_one("3,6", "2,8") == "3,6"
assert compare_one("2.4", "2.4") == None
assert compare_one("3,6", "3,6") == None
assert compare_one(4, 4) == None
assert compare_one("10,5", "5.5") == "10,5"
assert compare_one(1.5, 1.2) == 1.5
assert compare_one(1.2, 1.5) == 1.5
assert compare_one("1.5", "1.2") == "1.5"
assert compare_one("1.2", "1.5") == "1.5"
assert compare_one("3.5", "4.5") == "4.5"
assert compare_one("3,5", "4,5") == "4,5"
assert compare_one("3", "3") == None
assert compare_one(1, 1.0) == None
assert compare_one(1.0, 1) == None
assert compare_one("1", "1.0") == None
assert compare_one("1.0", "1") == None
assert compare_one(1.5, '1.5') == None
assert compare_one(5.5, 2.5) == 5.5
assert compare_one("3.14", 3.14) == None
assert compare_one("3,14", 3.14) == None
assert compare_one("3.2", "4.5") == "4.5"
assert compare_one("5,6", "3,4") == "5,6"
assert compare_one("2.0", "2.0") == None
assert compare_one(2.0, 2.0) == None
assert compare_one("2.5", "2,3") == "2.5"
assert compare_one("2.5", 2) == "2.5"
assert compare_one(2, "2.5") == "2.5"
assert compare_one(2.5, 3.7) == 3.7
assert compare_one("2.5", "3.7") == "3.7"
assert compare_one("2,5", "3,7") == "3,7"
assert compare_one("2.5", 3.7) == 3.7
assert compare_one("3,5", "3,5") == None
assert compare_one("3.5", 3.5) == None
assert compare_one(3.5, "3.5") == None
assert compare_one(2, 1) == 2, "error in test case 2"
assert compare_one(2.5, 1.5) == 2.5, "error in test case 3"
assert compare_one(1.5, 2.5) == 2.5, "error in test case 4"
assert compare_one("1.5", "1.5") == None, "error in test case 7"
assert compare_one("1,5", "1,5") == None, "error in test case 10"
assert compare_one(2.5, 2.7) == 2.7
assert compare_one(2.7, 2.5) == 2.7
assert compare_one("2.5", 2.7) == 2.7
assert compare_one("2,5", 2.7) == 2.7
assert compare_one("2,5", "2.5") == None
assert compare_one("3.6", "2.4") == "3.6"
assert compare_one("1,000", "2,000") == "2,000"
assert compare_one("4.2", "3.7") == "4.2"
assert compare_one("7.8", "9.8") == "9.8"
assert compare_one("7,8", "9,8") == "9,8"
assert compare_one("7.8", "7.8") == None
assert compare_one("7,8", "7,8") == None
assert compare_one('1,5', '2,5') == '2,5'
assert compare_one("2,5", "3,2") == "3,2"
assert compare_one(2.0, 2.5) == 2.5
assert compare_one(2.5, 2.0) == 2.5
assert compare_one("2.0", "2.5") == "2.5"
assert compare_one("2.5", "2.0") == "2.5"
assert compare_one("2.0", "2,0") == None
assert compare_one("2,0", "2.0") == None
assert compare_one(2, 1) == 2, "Test case 2 failed"
assert compare_one(2.5, 3.5) == 3.5, "Test case 3 failed"
assert compare_one(3.5, 2.5) == 3.5, "Test case 4 failed"
assert compare_one("1.5", "2.5") == "2.5", "Test case 5 failed"
assert compare_one("2.5", "1.5") == "2.5", "Test case 6 failed"
assert compare_one("1,5", "2,5") == "2,5", "Test case 7 failed"
assert compare_one("2,5", "1,5") == "2,5", "Test case 8 failed"
assert compare_one(2, 2) == None, "Test case 9 failed"
assert compare_one(2.5, 2.5) == None, "Test case 10 failed"
assert compare_one("2.5", "2.5") == None, "Test case 11 failed"
assert compare_one("2,5", "2,5") == None, "Test case 12 failed"
assert compare_one(3.14, 2.71) == 3.14, "Test case 2 failed"
assert compare_one("3.14", "2.71") == "3.14", "Test case 3 failed"
assert compare_one("3.14", 2.71) == "3.14", "Test case 5 failed"
assert compare_one(3.14, "2.71") == 3.14, "Test case 6 failed"
assert compare_one(3, 3) == None, "Test case 9 failed"
assert compare_one(3.14, 3.14) == None, "Test case 10 failed"
assert compare_one("3.6", "2.8") == "3.6"
assert compare_one("5.8", "5.9") == "5.9"
assert compare_one("2.5", "2.5") is None
assert compare_one("5.6", 7.8) == 7.8
assert compare_one(5.6, "5") == 5.6
assert compare_one(5.6, 5.6) == None
assert compare_one('2.5', 1.5) == '2.5'
assert compare_one(2.5, '1.5') == 2.5
assert compare_one("3.7", "2.9") == "3.7"
assert compare_one(3.7, 2.5) == 3.7
assert compare_one("1.5", "2.7") == "2.7"
assert compare_one("2.7", "1.5") == "2.7"
assert compare_one("1,5", "2,7") == "2,7"
assert compare_one("2,7", "1,5") == "2,7"
assert compare_one("2.5", "3,7") == "3,7"
assert compare_one("3,7", "2.5") == "3,7"
assert compare_one("12.5", 13.7) == 13.7
assert compare_one(13.7, "12.5") == 13.7
assert compare_one("16.5", 17) == 17
assert compare_one(17, "16.5") == 17
assert compare_one(18, 18) == None
assert compare_one(19.5, 19.5) == None
assert compare_one("20", "20") == None
assert compare_one("21.5", "21.5") == None
assert compare_one('7.5', '6.2') == '7.5'
assert compare_one('9,8', '7,6') == '9,8'
