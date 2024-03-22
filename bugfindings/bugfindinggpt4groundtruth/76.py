
def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    if (n == 1): 
        return (x == 1) 
    power = 1
    while (n < x): 
        power = power * n 
    return (power == x) 
assert 	is_simple_power(3, 3) is True
assert 	is_simple_power(3, 4) is False
assert 	is_simple_power(2, 5) is False
assert 	is_simple_power(0, 2) is False
assert 	is_simple_power(64,2) == True
assert 	is_simple_power(24,4) == False
assert 	is_simple_power(9,3) == True
assert 	is_simple_power(2, 3) == False
assert 	is_simple_power(2, 10) == False
assert 	is_simple_power(2, 7**2) == False
assert 	is_simple_power(2, 2**3) == False
assert 	is_simple_power(2, 2**4) == False
assert 	is_simple_power(2, 2**5) == False
assert 	is_simple_power(2, 2**7) == False
assert 	is_simple_power(2, 2**9) == False
assert 	is_simple_power(2, 3) == False, "check 3 failed"
assert 	is_simple_power(2, 2) == True, "check 4 failed"
assert 	is_simple_power(3, 3) == True, "check 5 failed"
assert 	is_simple_power(3, 4) == False, "check 6 failed"
assert 	is_simple_power(9, 2) == False, "check 8 failed"
assert 	is_simple_power(10, 3) == False, "check 9 failed"
assert 	is_simple_power(100, 2) == False, "check 10 failed"
assert 	is_simple_power(101, 2) == False, "check 11 failed"
assert 	is_simple_power(11, 2) == False, "check 12 failed"
assert 	is_simple_power(2, 3) is False
assert 	is_simple_power(2, 7) is False
assert 	is_simple_power(3, 5) is False
assert 	is_simple_power(3, 7) is False
assert 	is_simple_power(4, 4) is True
assert 	is_simple_power(4, 5) is False
assert 	is_simple_power(4, 7) is False
assert 	is_simple_power(5, 3) is False
assert 	is_simple_power(25, 5) == True, "simple power 25, 5"
assert 	is_simple_power(625, 5) == True, "simple power 625, 5"
assert 	is_simple_power(3125, 2) == False, "simple power 3125, 2"
assert 	is_simple_power(2, 1) == False, "simple power 2, 1"
assert 	is_simple_power(2, 3) == False, "simple power 2, 3"
assert 	is_simple_power(1, 1) == True, "simple power 1, 1"
assert is_simple_power(1, 1) == True
assert is_simple_power(2, 2) == True
assert is_simple_power(3, 2) == False
assert is_simple_power(4, 2) == True
assert is_simple_power(5, 2) == False
assert is_simple_power(7, 2) == False
assert is_simple_power(8, 2) == True
assert is_simple_power(100, 2) == False
assert is_simple_power(5, 3) == False
assert is_simple_power(8, 3) == False
assert 	is_simple_power(1, 1) == True
assert 	is_simple_power(3025, 5) == False
assert 	is_simple_power(0, 5) == False
assert 	is_simple_power(2, 2) == True, "should be a simple power of 2"
assert 	is_simple_power(81, 3) == True, "should be a simple power of 3"
assert 	is_simple_power(0, 2) == False, "should not be a simple power of 2"
assert 	is_simple_power(1, 1) == True, "should be a simple power of 1"
assert 	is_simple_power(10, 2) == False, "should not be a simple power of 2"
assert 	is_simple_power(2, 4) == False
assert 	is_simple_power(0, 0) == False
assert 	is_simple_power(0, 1) == False
assert 	is_simple_power(7, 2) == False
assert 	is_simple_power(3, 3) == True
assert 	is_simple_power(81, 4) == False
assert 	is_simple_power(2432902008176640000, 5) == False
assert 	is_simple_power(4, 4) == True
assert 	is_simple_power(2, 5) == False
assert 	is_simple_power(8, 3) == False
assert 	is_simple_power(10, 2) == False
assert 	is_simple_power(10, 3) == False
assert 	is_simple_power(10, 4) == False
assert 	is_simple_power(1024, 2) == True
assert 	is_simple_power(1024, 16) == False
assert 	is_simple_power(1024, 17) == False
assert 	is_simple_power(1025, 2) == False
assert 	is_simple_power(2,2) == True
assert 	is_simple_power(16,2) == True
assert 	is_simple_power(26,2) == False
assert 	is_simple_power(3125,2) == False
assert 	is_simple_power(1,1) == True
assert 	is_simple_power(15,5) == False
assert 	is_simple_power(2,3) == False
assert 	is_simple_power(2,4) == False
assert 	is_simple_power(2,20) == False
assert 	is_simple_power(15, 2) == False
assert 	is_simple_power(27, 3) == True
assert 	is_simple_power(1, 3) == True
assert 	is_simple_power(2, 2) == True
assert 	is_simple_power(100, 2) == False
assert 	is_simple_power(3, 9) == False
assert 	is_simple_power(2, 1) == False
assert 	is_simple_power(9, 3) == True
assert 	is_simple_power(27, 4) == False
assert 	is_simple_power(10, 10) == True
assert 	is_simple_power(81, 3**19) == False
assert 	is_simple_power(3**19, 3**19) == True
assert 	is_simple_power(3**19+1, 3**19) == False
assert 	is_simple_power(10, 2**1000) == False
assert 	is_simple_power(10, 2**1000-1) == False
assert 	is_simple_power(81, 3) == True
assert 	is_simple_power(9,3)==True
assert 	is_simple_power(33,3)==False
assert 	is_simple_power(11,2)==False
assert 	is_simple_power(4,4)==True
assert 	is_simple_power(17,2)==False
assert 	is_simple_power(33,1)==False
assert 	is_simple_power(1025,4)==False
assert 	is_simple_power(1025,2)==False
assert 	is_simple_power(1025,1)==False
assert 	is_simple_power(10,10)==True
assert 	is_simple_power(16, 2) == True
assert 	is_simple_power(16, 4) == True
assert 	is_simple_power(32, 2) == True
assert 	is_simple_power(5, 2) == False
assert 	is_simple_power(1, 0) == True
assert is_simple_power(2, 4) == False
assert is_simple_power(4, 4) == True
assert is_simple_power(2, 5) == False
assert is_simple_power(10, 4) == False
assert is_simple_power(10, 5) == False
assert is_simple_power(10, 8) == False
assert is_simple_power(10, 10) == True
