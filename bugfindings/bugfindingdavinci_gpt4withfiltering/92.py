
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
assert any_int(2, 3, 4) == False
assert any_int(2, 1, 4) == False
assert any_int(1, 2, 3) == True
assert any_int(1, 1, 2) == True
assert any_int(3, 2, 1) == True
assert any_int(3.3, 5, 2) == False
assert any_int(3.3, 5, 2.0) == False
assert any_int(3.0, 5, 2.0) == False
assert any_int(0, 0, 0) == True
assert any_int(1, 2, 4) == False
assert any_int(2,2,2) == False
assert any_int(3,3,3) == False
assert any_int(0,1,1) == True
assert any_int(1,1,1) == False
assert any_int(0,1,2) == False
assert any_int(0,0,4) == False
assert any_int(4, 7, -4) == False
assert any_int(4, 7, 10) == False
assert any_int(4, -7, 4) == False
assert any_int(4, -7, -4) == False
assert any_int(4, -7, 10) == False
assert any_int(-4, 7, 4) == False
assert any_int(-4, 7, -4) == False
assert any_int(-4, 7, 10) == False
assert any_int(-4, -7, 4) == False
assert any_int(-4, -7, -4) == False
assert any_int(-4, -7, 10) == False
assert any_int(4.5, 7, 4) == False
assert any_int(4.5, 7, -4) == False
assert any_int(4.5, 7, 10) == False
assert any_int(4.5, -7, 4) == False
assert any_int(4.5, -7, -4) == False
assert any_int(4.5, -7, 10) == False
assert any_int(-4.5, 7, 4) == False
assert any_int(2, 6, 4) == True, "Failed on third"
assert any_int(3, 4, 5) == False, "Failed on fourth"
assert any_int(0, -1, 5) == False
assert any_int(2, 3, 3) == False
assert any_int(2, 2, 4) == True
assert any_int(2, 4, 2) == True
assert any_int(4, 2, 2) == True
assert any_int(3, 5, 7) == False
assert any_int(2.9, 4.2, 6.2) == False
assert any_int(2.1, 4.1, 6.1) == False
assert any_int(2, 4, 4.3) == False
assert any_int(1, 2, 3.5) == False
assert any_int(3, 4, 8) == False
assert any_int(1,1,2) == True
assert any_int(1,1,4) == False
assert any_int(1,2,4) == False
assert any_int(1,2,3.0) == False
assert any_int(5,5,1) == False
assert any_int(5,5,10) == True
assert any_int(5,5,7) == False
assert any_int(5,6,9) == False
assert any_int(5,6,12) == False
assert any_int(5,6,13) == False
assert any_int(5,6,14) == False
assert any_int(5,6,15) == False
assert any_int(5,6,16) == False
assert any_int(5,6,17) == False
assert any_int(5,6,18) == False
assert any_int(5,6,19) == False
assert any_int(5,6,20) == False
assert any_int(5,6,21) == False
assert any_int(2, 3, 5) is True
assert any_int(3, 4, 5) is False
assert any_int(5, 3, 2) is True
assert any_int(4, 2, 3) == False
assert any_int(4, 3, 2) == False
assert any_int(3, 2, 4) == False
assert any_int(6, 5, 4) == False
assert any_int(3, 5, 4) == False
assert any_int(4, 4, 4) == False
assert any_int(4.0, 4.0, 4.0) == False
assert any_int(1, 2, 1) == True
assert any_int(2, 1, 1) == True
assert any_int(3, 4, 5) == False
assert any_int(5, 3, 4) == False
assert any_int(5, 4, 3) == False
assert any_int(4, 5, 3) == False
assert any_int(4, 3, 5) == False
assert any_int(0, 1, 1) == True
assert any_int(1, 1, 0) == True
assert any_int(1, 0, 1) == True
assert any_int(1, 1, 1) == False
assert any_int(1, 1, 0.5) == False
assert any_int(1, 0.5, 1) == False
assert any_int(0.5, 1, 1) == False
assert any_int(2, 2, 2) == False
assert any_int(1.1, 2, 3) == False
assert any_int(8, 9, 8.5) == False
assert any_int(8, 8.5, 9) == False
assert any_int(8.5, 8, 9) == False
assert any_int(8, 9, -8) == False
assert any_int(8, -8, 9) == False
assert any_int(-8, 8, 9) == False
assert any_int(8, 9, -9) == False
assert any_int(8, -9, 9) == False
assert any_int(-9, 8, 9) == False
assert any_int(9, 9, -8) == False
assert any_int(3, 1, 2) == True
assert any_int(1.5, 3, 3) == False
assert any_int(3, 1.5, 3) == False
assert any_int(3, 3, 1.5) == False
assert any_int(5, 4, 9) == True
assert any_int(5, 4, 10) == False
assert any_int(5, 4, 9.0) == False
assert any_int(0.5, 0.5, 1) == False
assert any_int(1, 2, 5) == False
assert any_int('a', 'b', 'c') == False
assert True == any_int(4, 4, 8)
assert False == any_int(2, 3, 6)
assert False == any_int(1, 1, 2.5)
assert any_int(2, 3, 1) == True
assert any_int(1, 2, 4.0) == False
assert not any_int(4, 5, 10)
assert any_int(4, 6, 10)
assert not any_int(4.2, 5, 10)
assert not any_int(4, 5.2, 10)
assert not any_int(4, 5, 10.2)
assert any_int(4, 1, 2) == False
assert any_int(1, 2, 6) == False
assert any_int(2, 3, 2) == False
assert any_int(2, 1, 3) == True
assert any_int(5, 2, 2) == False
assert any_int(5, 10, 17) == False
assert any_int(5, 5, 10) == True
assert any_int(5, 5, 5) == False
assert any_int(5, 5, 6) == False
assert any_int(5, 6, 7) == False
assert any_int(5, 5, 6.0) == False
assert any_int(5, 6.0, 7) == False
assert any_int(5, 6.0, 5) == False
assert any_int(1, 1, 2) is True
assert any_int(0, 2, -2) is True
assert any_int(2.2, 2, 4) is False
assert any_int(1, 1, 1) is False
assert any_int(3, 1, 4) is True
assert any_int(1, 1, 4) is False
assert any_int(1, 1, 4.5) is False
assert any_int(4, 5, 9) is True
assert any_int(2, 2, 2) is False
assert any_int(2, 3, 4.9) is False
assert any_int(2, 3, 5) == True
assert any_int(2, 5, 6) == False
assert any_int(5, 9, 6) == False
assert any_int(5, 10, 6.5) == False
assert any_int(6, 2, 4) == True
assert any_int(6, 3, 3) == True
assert any_int(1, 5, 2) == False
assert any_int(1, 2, 1.5) == False
assert any_int(1,2,1) == True
assert any_int(1,2,2) == False
assert any_int(1.1, 2.2, 3.3) == False
assert any_int(1, 2, 1.1) == False
assert any_int(3, 2, 7) == False
assert any_int(3, 1, 8) == False
assert any_int(0, -1, 1) == True
assert any_int(5, 2, 3) == True
assert any_int(2, 3, 2) is False
assert any_int(2, 1, 3) is True
assert any_int(3, 6, 5) is False
assert any_int(4, 3, 3) is False
assert any_int(3, 4, 3) is False
assert any_int(3, 3, 4) is False
assert any_int(4, 5, 6) is False
assert any_int(4, 6, 5) is False
assert any_int(6, 4, 5) is False
assert any_int(5, 4, 6) is False
assert any_int(5, 6, 4) is False
assert any_int(6, 5, 4) is False
assert any_int(10, 3, 7) == True
assert any_int(10, 1.1, 10) == False
assert any_int(10, 10, 10) == False
assert any_int(5, 4, 8) is False
assert any_int(5, 4, 7) is False
assert any_int(5, 4, 5) is False
assert any_int(5, 4, 4) is False
assert any_int(5, 4, 3) is False
assert any_int(5, 4, 0) is False
assert any_int(5, 3, 9) is False
assert any_int(5, 3, 6) is False
assert any_int(5, 3, 5) is False
assert any_int(5, 3, 3) is False
assert any_int(5, 3, 0) is False
assert any_int(5, 2, 9) is False
assert any_int(1,2,2.1) == False
assert any_int(1,2.1,2) == False
assert any_int(1.1,2,2) == False
assert any_int(2,1,1) == True
assert any_int(1,1,0) == True
assert any_int(1, 2, 2) is False
assert any_int(-1, 0, 1) is True
assert any_int(0, -1, 1) is True
assert any_int(0, 1, -1) is True
assert any_int(-1, -1, 0) is True
assert any_int(-1, 0, -1) is True
assert any_int(0, -1, -1) is True
assert any_int(-1, -1, -1) is False
assert any_int(1.0, 2.0, 3.0) is False
assert any_int(1.0, 2.0, 2.0) is False
assert any_int(1.0, 2.0, 1.0) is False
assert any_int(1.5, 4, 5) is False
assert any_int(0, 1, 0) == False
assert any_int(5, 3, 2) == True
assert any_int(5, 3, 3) == False
assert any_int(5, 5, 3) == False
assert any_int(5, 6, 11) == True
assert any_int(5, 6, 12) == False
assert any_int(3, 4, -7) is False
assert any_int(3, 4, 2.9) is False
assert any_int(2.8, 4, 3) is False
assert any_int(2.8, 4, 0) is False
assert any_int(3, 2, 2) == False
assert any_int(1,1,1.1) == False, '1,1,1.1 should return False'
assert any_int(1,1.1,1) == False, '1,1.1,1 should return False'
assert any_int(1.1,1,1) == False, '1.1,1,1 should return False'
assert any_int(1, 1, 2.5) == False
assert any_int(3, 4, 6) == False
assert any_int(1, 3, 1) == False
assert any_int(3, 5, -2) == True
assert any_int(1, 3, 2) == True
assert any_int(1, 1, 3) == False
assert any_int(1, 1, -1) == False
assert any_int(3, 3, 3) == False
assert any_int(1, 2, -3) == False
assert any_int(-1, -2, 3) == False
assert any_int(1, 2, 3.0) == False
assert any_int(3, 1, 2.5) == False
assert any_int(0, 0, -1) == False
assert any_int(1, 2, 3.5) is False
assert any_int(3, 1, 2) is True
assert any_int(1, 4, 2.5) is False
assert any_int(100, 50, 10) == False
assert any_int(0, 10, 10) == True
assert any_int(10, 10, 0) == True
assert any_int(10, 0, 10) == True
assert any_int(1, 2, 0) == False
assert any_int(3, 1, 1) == False
assert any_int(3, 2, 1) is True
assert any_int(1, 4, 3) is True
assert any_int(2, 3, 4) is False
assert any_int(2, 3, 1) is True
assert any_int(1, 3, 5) == False
assert any_int(3, -3, 6) == True
assert any_int(2.2, 2.2, 4.4) == False
assert any_int(1, 4, 2) == False
assert any_int(1, 1.0, 2) == False
assert any_int(1, 2, 1.0) == False
assert any_int(1, 1.0, 2.0) == False
assert any_int(1,1,1.0) == False
assert any_int(1,1,1.5) == False
assert any_int(1,1,1.99999999999999) == False
assert any_int(1,1,1.99999999999999999999) == False
assert any_int(5, 5, 10) is True
assert any_int(3, 3, 3) is False
assert any_int(6, 2, 4) is True
assert any_int(1, 10, 11) is True
assert any_int(1, 2, 3.0) is False
assert any_int(1, 2, 3.2) is False
assert any_int(1, 2, -3) is False
assert any_int(-1, -2, 3) is False
assert any_int(2, 3, 7) is False
assert any_int(3, 7, 8) == False
assert any_int(3, 4, 7) == True
assert any_int(3, 5, 8) == True
assert any_int(3, 2, 5) == True
assert any_int(5, 1, 3) == False
assert any_int(0,0,0) == True
assert any_int(0,2,2) == True
assert any_int(0,0,2) == False
assert any_int(0,2,3) == False
assert any_int(0.1,0.1,0.1) == False
assert any_int(0.2,0.2,0.2) == False
assert any_int(0.1,0.1,0.2) == False
assert any_int(0.1,0.2,0.3) == False
assert any_int(0.1,0.1,1) == False
assert any_int(0.1,0.1,0) == False
assert any_int(2, 3, 2) == False, 'Test 2 failed'
assert any_int(5, 5, 5) == False, 'Test 3 failed'
assert any_int(5, 4, 1) == True, 'Test 4 failed'
assert any_int(1, 1, 2) == True, 'Test 5 failed'
assert any_int(1, 1, 1) == False, 'Test 6 failed'
assert any_int(5, 1, 2) == False, 'Test 7 failed'
assert any_int(5,1,6) == True
assert any_int(3,4,5) == False
assert any_int(12,1,13) == True
assert any_int(3, 1, 3) == False
assert any_int(4, 6, 7) == False
assert any_int(4, 5, 5) == False
assert any_int(4, 5, 9) == True
assert any_int(4, 4, 9) == False
assert any_int(4, 11, 7) == True
assert any_int(4, 8, 12) == True
assert any_int(3.7, 11, 7) == False
assert any_int(4, 11.1, 7) == False
assert any_int(4, 11, 7.9) == False
assert any_int(1, 2, 4) is False
assert any_int(1, -1, 0) is True
assert any_int(4, 2, 3) == False, 'Test 2 failed'
assert any_int(5, 2, 1) == False, 'Test 4 failed'
assert any_int(5, 2, 5) == False, 'Test 5 failed'
assert any_int(3, 3, 4) == False
assert any_int(3, 1, 4) == True
assert any_int(4, 5, 6) == False
assert any_int(0, 1, 2) == False
assert any_int(-1, -1, -2) == True
assert any_int(-1, -1, -1) == False
assert any_int(9, 8, 16) == False, 'your function is not correct'
assert any_int(12, 14, 9) == False, 'your function is not correct'
assert any_int(5, 7, 0) == False
assert any_int(5, 5, 0) == True
assert any_int(4, 12, 7) is False
assert any_int(4, 12, 8) is True
assert any_int(4, 5, 8) is False
assert any_int(3, 2, 1.1) == False
assert any_int(1,2,4.0) == False
assert any_int(1,2,4.1) == False
assert any_int(1,2.1,4) == False
assert any_int(1.1,2,4) == False
assert any_int(1, 2.1, 3) == False
assert any_int(1, 2, 3.1) == False
assert any_int(5, 4, 7) == False
assert any_int(5, 6, 8) == False
assert any_int(5, 6, 9) == False
assert any_int(4, 3, 7) == True
assert any_int(4, 10, 12) == False
assert any_int(4, 10, 14) == True
assert any_int(10, 5, 10) == False
assert any_int(10, 5, 12) == False
assert any_int(3, 1, 7) == False
assert any_int(1, 4, 3) == True
assert any_int(4, 1, 3) == True
assert any_int(-10, 0, 10) == True
assert any_int(0, -3, 3) is True
assert any_int(0, -3, 4) is False
assert any_int(2, 3, 6) == False
assert any_int(2, 3, 8) == False
assert any_int(3, 7, 12) == False
assert any_int(5, -2, 4) == False
assert any_int(1.0, 2, 3) == False
assert any_int(6, 2, 3) == False
assert any_int(6, 2, 7) == False
assert any_int(6, 2, 9) == False
assert any_int(6, 2, 10) == False
assert any_int(6, 2, 11) == False
assert any_int(6, 2, 12) == False
assert any_int(6, 2, 13) == False
assert any_int(6, 2, 14) == False
assert any_int(6, 2, 15) == False
assert any_int(6, 2, 16) == False
assert any_int(6, 2, 17) == False
assert any_int(6, 2, 18) == False
assert any_int(6, 2, 19) == False
assert any_int(6, 2, 20) == False
