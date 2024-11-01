
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
assert iscube(3) == False
assert iscube(6) == False
assert iscube(8) == True
assert iscube(9) == False
assert iscube(11) == False
assert iscube(13) == False
assert iscube(15) == False
assert iscube(17) == False
assert iscube(19) == False
assert iscube(21) == False
assert iscube(23) == False
assert iscube(25) == False
assert iscube(29) == False
assert iscube(31) == False
assert iscube(33) == False
assert iscube(35) == False
assert iscube(37) == False
assert iscube(10) == False
assert iscube(27) == True
assert iscube(100) == False
assert iscube(100000) == False
assert iscube(10000000) == False
assert iscube(100000000) == False
assert iscube(10000000000) == False
assert iscube(100000000000) == False
assert iscube(10000000000000) == False
assert iscube(100000000000000) == False
assert iscube(10000000000000000) == False
assert iscube(100000000000000000) == False
assert iscube(-12) == False
assert iscube(-3) == False
assert iscube(1) == True
assert iscube(-9) == False
assert iscube(5) == False
assert iscube(-4) == False
assert iscube(4) == False
assert iscube(18) == False
assert iscube(20) == False
assert iscube(24) == False
assert iscube(26) == False
assert iscube(30) == False
assert iscube(32) == False
assert iscube(39) == False
assert iscube(50) == False
assert iscube(52) == False
assert iscube(55) == False
assert iscube(56) == False
assert iscube(58) == False
assert iscube(60) == False
assert iscube(7) == False, "the 7 is not a cube of some integer number"
assert iscube(-4) == False, "the -4 is not a cube of some integer number"
assert iscube(1) == True, "the 1 is a cube of some integer number"
assert iscube(8) == True, "the 8 is a cube of some integer number"
assert iscube(-3) == False, "the -3 is not a cube of some integer number"
assert iscube(7) == False
assert iscube(-5) is False
assert iscube(101) is False
assert iscube(10) is False
assert iscube(11) is False
assert iscube(333) is False
assert iscube(3333) is False
assert iscube(100000000000000000000000000000000) is False
assert iscube(1023) is False
assert iscube(100) is False
assert iscube(999) is False
assert iscube(100000000000000000000000000000001) is False
assert iscube(10000000000000000000000000000000002) is False
assert iscube(10000000000000000000000000000000003) is False
assert iscube(10000000000000000000000000000000004) is False
assert iscube(10000000000000000000000000000000005) is False
assert iscube(10000000000000000000000000000000006) is False
assert iscube(10000000000000000000000000000000007) is False
assert iscube(10000000000000000000000000000000008) is False
assert iscube(10000000000000000000000000000000009) is False
assert iscube(1000000000), False
assert iscube(-2) == False
assert iscube(-8) == True
assert iscube(6) == False, "6 is not a cube of some integer number"
assert iscube(7) == False, "7 is not a cube of some integer number"
assert iscube(2) == False
assert iscube(12) == False
assert iscube(123) == False
assert iscube(1000) == True
assert iscube(1001) == False
assert iscube(10 ** 20 + 1) == False
assert iscube(10 ** 20 + 2) == False
assert iscube(10 ** 20 + 3) == False
assert not iscube(6), '6 is not a cube'
assert iscube(10*100) == True
assert iscube(10*101) == False
assert iscube(10**5) == False
assert iscube(10**6) == True
assert iscube(10**8) == False
assert iscube(1) == True 
assert iscube(16) == False 
assert iscube(1001) == False 
assert iscube(1000000) == True 
assert iscube(1000000000) == True 
assert iscube(10000) == False
assert iscube(25000000) == False
assert iscube(123456789) == False
assert iscube(-123456789) == False
assert iscube(-6) == False
assert iscube(-10) == False
assert iscube(-25) == False
assert iscube(-33) == False
assert iscube(3) is False
assert iscube(13) is False
assert iscube(-5) == False
assert iscube(-1), False
assert iscube(-1), True
assert iscube(8), False
assert iscube(1000), False
assert iscube(-7) == False
assert iscube(-1025) == False
assert iscube(81) == False
assert iscube(40) == False
assert iscube(-13) == False
assert iscube(99) == False
assert iscube(16) == False
assert not iscube(3)
assert not iscube(100)
assert not iscube(-100)
assert not iscube(1.1)
assert iscube(64) == True
assert iscube(131) == False
assert iscube(729) == True
assert iscube(1627) == False
assert iscube(1025) == False
assert iscube(2099) == False
assert iscube(3359) == False
assert iscube(5359) == False
assert iscube(5919) == False
assert iscube(8111) == False
assert iscube(8929) == False
assert iscube(12371) == False
assert not iscube(17), 17
assert not iscube(6), 6
assert not iscube(123), 123
assert iscube(-1) == True
assert iscube(256) is False
assert iscube(36) == False
assert iscube(53) == False
assert not iscube(2) 
