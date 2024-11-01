
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
assert 	any_int(1, 2, 5) == False
assert 	any_int(1.5, 1.5, 2) == False
assert 	any_int(1.5, 1.6, 3.7) == False
assert 	any_int(1.5, 1.6, 1) == False
assert 	any_int(1, 1, 1) == False
assert 	any_int(1, 1, 1.5) == False
assert 	any_int(2, 3, 4) == False
assert 	any_int(3, 2, 4) == False
assert 	any_int(3, 4, 2) == False
assert 	any_int(3, 3, 3) == False
assert 	any_int(0, 3, 4) == False, "Wrong output"
assert 	any_int(3, 7, 9) == False, "Wrong output"
assert 	any_int(1, 1, 1) == False, "Wrong output"
assert 	any_int(-1, 0, 1) == True, "Wrong output"
assert 	any_int(-1, 1, -1) == False, "Wrong output"
assert 	any_int(1, 2, 4) == False
assert 	any_int(4, 1, 3) == True
assert 	any_int(3, 3, 6) == True
assert 	any_int(4.2, 1, 3) == False
assert 	any_int(4, 1, 3.2) == False
assert 	any_int(4.1, 1, 3.2) == False
assert 	any_int(4, 1, 3.1) == False
assert 	any_int(4, 1, 4) == False
assert 	any_int(3, 2, 3) == False, '3+2 = 5: False'
assert 	any_int(3.1, 2.2, 3.3) == False, 'Float: False'
assert 	any_int(3, 2.2, 3) == False, 'Float: False'
assert 	any_int(3, 2, 3.3) == False, 'Float: False'
assert 	any_int(-3, -2, -3) == False, 'Negative: False'
assert 	any_int(3, 2, 3) == False
assert 	any_int(3, 2, 5) == True
assert 	any_int(3, 2, 6) == False
assert 	any_int(3, 1, 2) == True
assert 	any_int(3, 1, 4) == True
assert 	any_int(3, 1, 5) == False
assert 	any_int(3, 1, 6) == False
assert 	any_int(3, 2, 1) == True
assert 	any_int(3, 5, 4) == False 
assert 	any_int(3, 3, 3.1) == False
assert 	any_int(3.0, 3.1, 3) == False
assert 	any_int(3, 3, 3.0) == False
assert 	any_int(3, 3.0, 3.1) == False
assert 	any_int(1, 1, 2) == True, "3"
assert 	any_int(1.5, 2.5, 3) == False, "5"
assert 	any_int(0, 1, 1) == True, "7"
assert 	any_int(0, 1, 0) == False, "8"
assert 	any_int(2, 6, 6) == False, 'ERROR'
assert 	any_int(7, 7, 1) == False, 'ERROR'
assert 	any_int(10, 2, 3) == False, 'ERROR'
assert 	any_int(1, 2, 3) == True, 			'returns True when the numbers are 1, 2 and 3, and any of the numbers is equal to the sum of the other two'
assert 	any_int(1, 2, 4) == False, 			'returns False when the numbers are 1, 2 and 4, and no number is equal to the sum of the other two'
assert any_int(10, 20, 30) == True
assert any_int(10, 20.5, 30) == False
assert 	any_int(10, 10, 10) == False
assert 	any_int(10, 10, 9) == False
assert 	any_int(1, 1, 2) == True
assert 	any_int(1, 1, 4) == False
assert 	any_int(1.5, 2.3, 3.1) == False
assert 	any_int(1, 2.3, 3.1) == False
assert 	any_int(1.5, 3, 4) == False
assert 	any_int(1.5, 3, 3) == False
assert 	any_int(1.5, 3.3, 3) == False
assert 	any_int(1.5, 3.3, 4.4) == False
assert 	any_int(1, 2, 3.1) == False, "Test 2 failed"
assert 	any_int(1.1, 2.2, 3) == False, "Test 3 failed"
assert 	any_int(1, 2, 3.1) == False, "Test 4 failed"
assert 	any_int(0, 0, 1) == False, "Test Failed"
assert 	any_int(2, 3, 5) == True, "Test Failed"
assert 	any_int(2, 3, 6) == False, "Test Failed"
assert 	any_int(-1, -1, 2) == False, "Test Failed"
assert 	any_int(3, 3, 5) == False
assert 	any_int(3, 4, 3) == False
assert 	any_int(3, 5, 3) == False
assert 	any_int(3, 5, 5) == False
assert 	any_int(3, 5, 6) == False
assert 	any_int(3, 4, 6) == False
assert 	any_int(3, 6, 5) == False
assert 	any_int(3, 6, 6) == False
assert 	any_int(3, 3, 2) == False, 'wrong result'
assert 	any_int(3, 2, 2) == False, 'wrong result'
assert 	any_int(4, 3, 3) == False, "Wrong answer"
assert any_int(3, 2, 1) == True
assert any_int(3, 2, 2) == False
assert any_int(6, 1, 1) == False
assert 	any_int(20, 10, 30) == True
assert 	any_int(10, 20, 30) == True
assert 	any_int(1.2, 3.4, 5.6) == False
assert 	any_int(1, 2, 3) == True
assert 	any_int(-1, -2, -3) == True
assert 	any_int(4, 2, 2) == True
assert 	any_int(2, 4, 2) == True
assert 	any_int(4, 2, 3) == False
assert 	any_int(1.1, 1, 1) == False
assert 	any_int(1, 1.1, 1) == False
assert 	any_int(1, 1, 1.1) == False
assert 	any_int(1, 2, 4.5) == False
assert 	any_int(1, 1, 2) == True, '1 and 1'
assert 	any_int(1, 3, 3) == False, 'all different'
assert 	any_int(1, 2.5, 3) == False, 'float 1'
assert 	any_int(1, 2, 3.5) == False, 'float 2'
assert 	any_int(1, 'a', 3) == False,'string 1'
assert 	any_int(1, 1, 'a') == False,'string 2'
assert 	any_int('a', 1, 2) == False,'string 1'
assert 	any_int(1, 'a', 2) == False,'string 2'
assert 	any_int('a', 1, 2) == False,'string 2'
assert 	any_int(1, 2, 'a') == False,'string 3'
assert 	any_int(1,2,3) == True
assert 	any_int(3,2,1) == True
assert 	any_int(3,2,3) == False
assert 	any_int(1.5,2.5,3) == False
assert 	any_int(1,2.5,3.5) == False
assert 	any_int(2, 3, 1) == True
assert 	any_int(2.1, 3.3, 4.4) == False
assert 	any_int(-1, 1, -2) == True
assert 	any_int(1, 3, 3) == False
assert 	any_int(1, 3, 4) == True
assert 	any_int(2, 3, 2) == False
assert 	any_int(2, 3, 3) == False
assert 	any_int(2, 3, 6) == False
assert 	any_int(2, 3, 8) == False
