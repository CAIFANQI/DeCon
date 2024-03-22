
def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    a = abs(a)
    return int(round(a ** (1. / 3))) == a
assert 	iscube(8) == True
assert 	iscube(27) == True
assert iscube(1) == True
assert iscube(27) == True
assert iscube(3) == False
assert iscube(4) == False
assert iscube(35) == False
assert iscube(12) == False
assert iscube(144) == False
assert iscube(333) == False
assert iscube(7) == False
assert 	iscube(2) == False
assert 	iscube(1234567) == False
assert 	iscube(13) == False
assert 	iscube(1**3) == True
assert 	iscube(2**4) == False
assert 	iscube(2**5) == False
assert iscube(121) == False
assert iscube(1232) == False
assert iscube(122323232323) == False
assert iscube(12232323232323232323) == False
assert iscube(3**3)
assert 	iscube(32) == False
assert 	iscube(27**3+1) == False
assert 	iscube(0) == True
assert 	iscube(3**3) == True
assert 	iscube(3**3+1) == False
assert 	iscube(27**4+1) == False
assert 	iscube(27**5+1) == False
assert 	iscube(27**6+1) == False
