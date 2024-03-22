
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
assert any_int(1, 1, 2) == True
assert any_int(3, 2, 1) == True
assert any_int(0, 0, 0) == True
assert any_int(0,1,1) == True
assert any_int(2, 6, 4) == True, "Failed on third"
assert any_int(2, 2, 4) == True
assert any_int(2, 4, 2) == True
assert any_int(4, 2, 2) == True
assert any_int(1,1,2) == True
assert any_int(5,5,10) == True
assert any_int(2, 3, 5) is True
assert any_int(5, 3, 2) is True
assert any_int(1, 2, 1) == True
assert any_int(2, 1, 1) == True
assert any_int(0, 1, 1) == True
assert any_int(1, 1, 0) == True
assert any_int(1, 0, 1) == True
assert any_int(3, 1, 2) == True
assert any_int(5, 4, 9) == True
assert True == any_int(4, 4, 8)
assert any_int(2, 3, 1) == True
assert any_int(4, 6, 10)
assert any_int(2, 1, 3) == True
assert any_int(5, 5, 10) == True
assert any_int(1, 1, 2) is True
assert any_int(0, 2, -2) is True
assert any_int(3, 1, 4) is True
assert any_int(4, 5, 9) is True
assert any_int(2, 3, 5) == True
assert any_int(6, 2, 4) == True
assert any_int(6, 3, 3) == True
assert any_int(1,2,1) == True
assert any_int(0, -1, 1) == True
assert any_int(5, 2, 3) == True
assert any_int(2, 1, 3) is True
assert any_int(10, 3, 7) == True
assert any_int(2,1,1) == True
assert any_int(1,1,0) == True
assert any_int(-1, 0, 1) is True
assert any_int(0, -1, 1) is True
assert any_int(0, 1, -1) is True
assert any_int(-1, -1, 0) is True
assert any_int(-1, 0, -1) is True
assert any_int(0, -1, -1) is True
assert any_int(5, 3, 2) == True
assert any_int(5, 6, 11) == True
assert any_int(3, 5, -2) == True
assert any_int(1, 3, 2) == True
assert any_int(3, 1, 2) is True
assert any_int(0, 10, 10) == True
assert any_int(10, 10, 0) == True
assert any_int(10, 0, 10) == True
assert any_int(3, 2, 1) is True
assert any_int(1, 4, 3) is True
assert any_int(2, 3, 1) is True
assert any_int(3, -3, 6) == True
assert any_int(5, 5, 10) is True
assert any_int(6, 2, 4) is True
assert any_int(1, 10, 11) is True
assert any_int(3, 4, 7) == True
assert any_int(3, 5, 8) == True
assert any_int(3, 2, 5) == True
assert any_int(0,0,0) == True
assert any_int(0,2,2) == True
assert any_int(5, 4, 1) == True, 'Test 4 failed'
assert any_int(1, 1, 2) == True, 'Test 5 failed'
assert any_int(5,1,6) == True
assert any_int(12,1,13) == True
assert any_int(4, 5, 9) == True
assert any_int(4, 11, 7) == True
assert any_int(4, 8, 12) == True
assert any_int(1, -1, 0) is True
assert any_int(3, 1, 4) == True
assert any_int(-1, -1, -2) == True
assert any_int(5, 5, 0) == True
assert any_int(4, 12, 8) is True
assert any_int(4, 3, 7) == True
assert any_int(4, 10, 14) == True
assert any_int(1, 4, 3) == True
assert any_int(4, 1, 3) == True
assert any_int(-10, 0, 10) == True
assert any_int(0, -3, 3) is True
