
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
assert 	any_int(-1, 0, 1) == True, "Wrong output"
assert 	any_int(4, 1, 3) == True
assert 	any_int(3, 3, 6) == True
assert 	any_int(3, 2, 5) == True
assert 	any_int(3, 1, 2) == True
assert 	any_int(3, 1, 4) == True
assert 	any_int(3, 2, 1) == True
assert 	any_int(1, 1, 2) == True, "3"
assert 	any_int(0, 1, 1) == True, "7"
assert any_int(10, 20, 30) == True
assert 	any_int(1, 1, 2) == True
assert 	any_int(2, 3, 5) == True, "Test Failed"
assert any_int(3, 2, 1) == True
assert 	any_int(20, 10, 30) == True
assert 	any_int(10, 20, 30) == True
assert 	any_int(1, 2, 3) == True
assert 	any_int(-1, -2, -3) == True
assert 	any_int(4, 2, 2) == True
assert 	any_int(2, 4, 2) == True
assert 	any_int(1, 1, 2) == True, '1 and 1'
assert 	any_int(1,2,3) == True
assert 	any_int(3,2,1) == True
assert 	any_int(2, 3, 1) == True
assert 	any_int(-1, 1, -2) == True
assert 	any_int(1, 3, 4) == True
