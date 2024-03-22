
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
assert any_int(3, 4, 7) == True
assert any_int(5, 5, 10) == True
assert any_int(2, 2, 4) == True
assert any_int(2, 2, 5) == False
assert any_int(5, 2, 3) == True
assert any_int(1, 1, 3) == False
assert any_int(1, 2, 1) == True
assert any_int(1, 2, 4) == False
assert any_int(4, 5, 9) == True
assert any_int(0, 0, 0) == True
assert any_int(2, -2, 0) == True
assert any_int(8, 9, 17) == True
assert any_int(6, 8, 14) == True
assert any_int(2, 3, 5) == True, "Error: Test Case 2"
assert any_int(4, 5, 9) == True, "Error: Test Case 3"
assert any_int(1, 1, 2) == True
assert any_int(-1, 0, 1) == True
assert any_int(5, 3, 2) == True
assert any_int(5, 10, 15) == True
assert any_int(10, 5, 15) == True
assert any_int(1, 2, 2) == False
assert any_int(2, 3, 5) == True
assert any_int(10, 20, 30) == True
assert any_int(10, 3, 7) == True
assert any_int(5, 10, 20) == False
assert any_int(4, 2, 2) == True
assert any_int(1, 1, 1) == False
assert any_int(10, 2, 8) == True
assert any_int(2, 3, 6) == False
assert any_int(2, 4, 6) == True
assert any_int(3, 4, 5) == False
assert any_int(5, 5, 11) == False
assert any_int(2, 1, 1) == True
assert any_int(0, 1, 1) == True
assert any_int(1, 0, 1) == True
assert any_int(1, 1, 0) == True
assert any_int(1.5, 2.5, 4) == False
assert any_int(10, 5, 5) == True
assert any_int(4, 5, 9) == True, 'Test Case 3 Failed'
assert any_int(2, 4, 7) == False
assert any_int(1, 2, 2.5) == False
assert any_int(2.5, 3.5, 6) == False
assert any_int(1, 2, 3.5) == False
assert any_int(3, 2, 1) == True
assert any_int(4, 4, 8) == True
assert any_int(2, 2, 2) == False
assert any_int(7, 7, 14) == True
assert any_int(1, 2, 0) == False
assert any_int(3, 3, 6) == True
assert any_int(3, 3, 7) == False
assert any_int(7, 8, 9) == False
assert any_int(10, 20, 30.5) == False
assert any_int(10, 20.5, 30) == False
assert any_int(10.5, 20, 30) == False
assert any_int(2.5, 3, 5.5) == False
assert any_int(2, 5, 10) == False
assert any_int(10, 0, 10) == True
assert any_int(6, 8, 10) == False
assert any_int(5, 7, 12) == True
assert any_int(-1, 1, 0) == True
assert any_int(1, 2.5, 3.5) == False
assert any_int(1.5, 2.5, 3) == False
assert any_int(2, 4, 2) == True
assert any_int(4, 6, 10) == True
assert any_int(10, 5, 10) == False
