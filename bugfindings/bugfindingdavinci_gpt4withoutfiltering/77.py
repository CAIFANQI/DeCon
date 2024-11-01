
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
assert iscube(27) == True
assert iscube(17) == False
assert iscube(26) == False
assert False == iscube(29)
assert False == iscube(10)
assert iscube(65) == False
assert iscube(0) == True
assert iscube(1) == True
assert iscube(28) == False
assert iscube(42) == False
assert iscube(2) == False
assert iscube(8) == True
assert iscube(10) == False
assert iscube(7) == False, 'second check failed'
assert iscube(27) == True, 'third check failed'
assert iscube(20) == False, 'fourth check failed'
assert iscube(9) == False
assert iscube(11) == False
assert False == iscube(28)
assert True == iscube(27)
assert not iscube(26)
assert not iscube(10)
assert iscube(20) == False
assert iscube(12) == False
assert iscube(32) == False
assert iscube(3) == False
assert iscube(129) == False
assert not iscube(28)
assert iscube(103) == False
assert False == iscube(7)
assert iscube(14) == False
assert False == iscube(20)
assert iscube(48) == False
assert False == iscube(63)
assert True == iscube(8)
assert iscube(1)
assert iscube(8)
assert iscube(27)
assert not iscube(3)
assert not iscube(5)
assert not iscube(7)
assert not iscube(20)
assert not iscube(23)
assert not iscube(30)
assert not iscube(34)
assert not iscube(42)
assert not iscube(53)
assert not iscube(73)
assert not iscube(101)
assert not iscube(111)
assert not iscube(112)
assert not iscube(127)
assert not iscube(133)
assert not iscube(141)
assert not iscube(144)
assert not iscube(158)
assert iscube(38) == False
assert iscube(41) == False
assert iscube(63) == False
assert iscube(46) == False
assert iscube(85) == False
assert iscube(99) == False
assert iscube(117) == False
assert iscube(134) == False
assert iscube(155) == False
assert iscube(157) == False
assert iscube(188) == False
assert iscube(189) == False
assert iscube(217) == False
assert iscube(223) == False
assert iscube(254) == False
assert iscube(281) == False
assert iscube(283) == False
assert iscube(312) == False
assert iscube(313) == False
assert iscube(341) == False
assert iscube(371) == False
assert iscube(372) == False
assert iscube(24) == False
assert iscube(45) == False
assert iscube(4) == False
assert iscube(82) == False
assert iscube(100) == False
assert False == iscube(9)
assert not iscube(55)
assert iscube(4623) == False
assert iscube(2048) == False
assert iscube(1.0) == True
assert iscube(25) == False
assert iscube(5) == False
assert iscube(2 ** 14) == False
assert iscube(1)  == True
assert iscube(8)  == True
assert False == iscube(15)
assert True == iscube(0)
assert     iscube(0)
assert not iscube(2)
assert not iscube(43)
assert not iscube(123)
assert False == iscube(35)
assert     iscube(1)
assert     iscube(8)
assert iscube(0)
assert False == iscube(2)
assert True == iscube(1)
assert iscube(29) == False
assert False == iscube(4)
assert False == iscube(3)
assert False == iscube(256)
assert iscube(18) == False
assert iscube(31) is False
assert iscube(1) is True
assert iscube(0) is True
assert iscube(15) == False
assert iscube(8) == (8 == 2**3)
assert iscube(8) == (pow(2, 3) == 8)
assert False == iscube(12)
assert False == iscube(26)
assert iscube(513) == False
assert iscube(7) == False
