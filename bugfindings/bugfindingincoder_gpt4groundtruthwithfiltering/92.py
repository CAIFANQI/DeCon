
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    '''
    
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x+y==z) or (y+z==x):
            return True
        return False
    return False
assert any_int(1, 2, 3) == True
assert any_int(3, 12.3, 7) == False
assert any_int(3, 12.3, 7.3) == False
assert any_int(3, 5, 7) == False
assert any_int(3, 5, 7.3) == False
assert any_int(3, 12.3, 7.5) == False
assert any_int(4, 12, 7) == False
assert any_int(6, 12, 7) == False
assert any_int(7, 12, 7) == False
assert any_int(12, 12, 7) == False
assert any_int(13, 12, 7) == False
assert any_int(14, 12, 7) == False
assert any_int(15, 12, 7) == False
assert any_int(16, 12, 7) == False
assert any_int(17, 12, 7) == False
assert any_int(18, 12, 7) == False
assert any_int(20, 12, 7) == False
assert any_int(21, 12, 7) == False
assert any_int(22, 12, 7) == False
assert any_int(23, 12, 7) == False
assert any_int(24, 12, 7) == False
assert any_int(25, 12, 7) == False
assert any_int(26, 12, 7) == False
assert any_int(27, 12, 7) == False
assert any_int(28, 12, 7) == False
assert any_int(29, 12, 7) == False
assert any_int(30, 12, 7) == False
assert any_int(31, 12, 7) == False
assert any_int(32, 12, 7) == False
assert any_int(6, 3, 1) == False
assert any_int(6, 3, -1) == False
assert any_int(6, 3, 1.5) == False
assert any_int(6, 3, 6) == False
assert any_int(6, 3, 6.5) == False
assert any_int('6', '3', '2') == False
assert any_int('6', '3', '1') == False
assert any_int('6', '3', '-1') == False
assert any_int('6', '3', '1.5') == False
assert any_int('6', '3', '6') == False
assert any_int('6', '3', '6.5') == False
assert any_int('6', '3', '3') == False
assert any_int('3', '4', '6') is False
assert any_int(3, 4, 5) is False
assert any_int(3, 4, 5.0) is False
assert any_int(3, 4.0, 5) is False
assert any_int(3, 4.0, 5.0) is False
assert any_int('10', '10.3', '10.3') is False
assert any_int(-4, 2, 3) == False
assert any_int(-5, 2, 3) == False
assert any_int(5, -2, -27) == False
assert any_int('c', 'a', 'a') == False
assert any_int(-5, -2, -27) == False
assert any_int(2.3, 2.3, 3) == False
assert any_int(1, 2.3, 3) == False
assert any_int(2, 2.3, 3) == False
assert any_int(1.3, 2.3, 3) == False
assert any_int("2.3", "2.3", "2.3") == False
assert any_int('1', '3', '2') == False
assert any_int(1, 2, 3.5) == False
assert any_int('1', '2', '3.5') == False
assert any_int(1, 2.0, 3) == False
assert any_int(1, 2, 3.0) == False
assert any_int(0, 1, 0) == False
assert any_int(0, 0, 1) == False
assert any_int(0, 0, 0) == True
assert any_int(1,2,4) == False
assert any_int(1, 3, 2) == True
assert any_int(1, 3, 1) == False
assert any_int(1, 2, 2) == False
assert any_int(1, 2, 2.5) == False
assert any_int("1", "3", "2") == False
assert any_int("1", "2", "2") == False
assert not any_int(1, 1.0, 1)
assert not any_int(1, 1.0, 1.1)
assert not any_int(1, 1, 1.1)
assert any_int(1, 2, 4) == False
assert any_int('a', 'b', 'd') == False
assert any_int('1', '2', '3') is False
assert any_int('1', '2', 'X') == False
assert any_int('1', '2', 'XZ') == False
assert any_int(1, 1.5, 3) == False
assert any_int(1.0, 2.0, 3) == False
assert any_int(1, 0, 2) == False
assert any_int(5, 2, 20) == False
assert any_int('5', '10', '20') == False
assert any_int("1", "2", "3") == False
assert any_int("a", "b", "c") == False
assert any_int(1.0, 2.0, 3.0) == False
assert any_int(True, True, True) == False
assert any_int(2,2,3) == False
assert any_int(1,2,2.5) == False
assert any_int(1,2.5,3) == False
assert any_int(1,2.5,2.5) == False
assert any_int(1, 2, False) == False
assert any_int(1.1, 2.1, 3.1) == False
assert any_int(1, 2, 2.1) == False
assert any_int(1, 3.0, 2) == False
assert any_int("1", "1.", "1.") == False
assert any_int('a', 'b', 'c') == False
assert any_int(1.1, 2.2, 3.3) == False
assert any_int(3, 6.0, 9) is False
assert any_int(1,2,5) == False
assert any_int(-1, 0, 0) == False
assert any_int(-10, 0, 0) == False
assert any_int(2, 2, 3) == False
assert any_int(-1, 1, 3) == False
assert any_int(-2, 2, 3) == False
assert any_int(-1, 2, 2) == False
assert any_int(1, 1, 3) == False
assert any_int(-1, 3, 3) == False
assert any_int(1, 2, 2.3) == False
assert any_int(2, 1, 3) == True
assert any_int(1, 2, 1.5) == False
assert any_int(1, 2, 1.999999) == False
assert any_int(1, 0, 0) == False
assert any_int(0, 0, -1) == False
assert any_int(1, 3, 3) == False
assert any_int('1', '2', '3') == False
assert any_int('1', '2', '2') == False
assert any_int(1, 1, 1) == False
assert any_int(1,10,3) == False
assert any_int(7, 5, 7) == False
assert any_int("a", "b", "d") == False
assert any_int("abc", "abc", "abd") == False
assert any_int("abc", "abc", "cde") == False
assert any_int(3, 4, 5.5) == False
assert any_int(3, 4.5, 6) == False
assert any_int(3, 4.5, 6.5) == False
assert any_int(3.5, 4.5, 6) == False
assert any_int(3, 4, 5.9) == False
assert any_int(3, 4.5, 6.1) == False
assert any_int(3, 4.5, 6.7) == False
assert any_int(1, 2, 5.0) == False
assert any_int(2, 2, 2) == False
assert any_int(3, 2, 2) == False
assert any_int('a', 'b', 'c') is False
assert any_int(1.1, 2.2, 3.3) is not True
assert any_int(1,True,3) == False
assert any_int(-1, 2, 3) == True
assert any_int(1, 2.5, 3) == False
assert any_int(1, -2, 2.5) == False
assert any_int(0, 3, 5) == False
assert any_int(3, 4.1, 5) == False
assert any_int(10, 3, 3) == False
assert any_int(10, 3.5, 3) == False
assert any_int(10, 3, 5) == False
assert any_int(10, 3, 4) == False
assert any_int(1, 2.1, 3.0) == False
assert any_int(2, 3, 4) == False
assert not any_int(10.5, 10.5, 10.5)
assert not any_int(10.5, 10.5, 9.5)
assert any_int(1, 1, 3) is False
assert any_int(1, 2, 0.5) is False
assert any_int(-2, -1, 2) == False
assert any_int(3, 2.1, 2) == False
assert any_int(3, 2.1, 3) == False
assert any_int(3, 4, 5) == False
assert any_int(1, 10, 2) == False
assert any_int(1, 10, 12) == False
assert any_int(1, 3, 5) == False
assert any_int(4, 3, 5) == False
assert any_int('1', '3', '5') == False
assert any_int(2, 10, 11) == False
assert any_int(2, 11, 10) == False
assert any_int('abc', 'def', 'ghi') == False
assert any_int(3, 2, 1) == True
assert any_int(3, 3, 2) == False
assert any_int(1, 1.5, 1) == False
assert any_int(1, 1.2, 3) == False
assert any_int(0.0, 0.0, 0) == False
assert any_int(1, 2, 3) == 1
assert any_int(0, 3, 0) == 0
assert any_int(-1, 1, 3) == 0
assert any_int(-4, -4, -4) == False
assert any_int(-2, -2, -2) == False
assert any_int('a', 'a', 'a') == False
assert any_int(1.5, 1.5, 1.5) == False
assert any_int(6, 6, 8) == False
assert any_int(6, 8, 7) == False
assert any_int(12, 6, 8) == False
assert any_int(5, 8, 6) == False
assert any_int(10, 8, 5) == False
assert any_int(1, 2.5, 1) == False
assert any_int(2, 5, 7) == True
assert any_int(5, 5.5, 10) is False
assert any_int(5, 4.5, 10) is False
assert any_int(5, 4.5, 6.5) is False
assert any_int(2, 5.5, 5) is False
assert any_int(1, 3.2, 1) == False
assert any_int(True, False, False) == False
assert any_int(6, 5, 7) == False
assert any_int(10, 5, 7) == False
assert any_int(12.2, 14.2, 15.2) == False
assert any_int(1, 10, 20) == False
assert any_int(1, 20, 10) == False
assert any_int(1.1, 10.1, 20.1) == False
assert any_int(1.0, 10.0, 20.1) == False
assert any_int(3, 6, 7) == False
assert any_int(5, 7, 7) == False
assert any_int(-20, 20, 30) == False
assert any_int(1, 3.1, 4) == False
