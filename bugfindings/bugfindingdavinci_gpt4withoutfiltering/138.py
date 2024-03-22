
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n%2 == 0 and n >= 8 and n <= 8
assert is_equal_to_sum_even(12) is True
assert is_equal_to_sum_even(18) is True
assert is_equal_to_sum_even(19) is False
assert is_equal_to_sum_even(44) is True
assert is_equal_to_sum_even(48) is True
assert is_equal_to_sum_even(10) == True
assert is_equal_to_sum_even(9) == False
assert is_equal_to_sum_even(6) == False
assert is_equal_to_sum_even(5) == False
assert is_equal_to_sum_even(14) == True
assert is_equal_to_sum_even(16) == True
assert is_equal_to_sum_even(18) == True
assert is_equal_to_sum_even(20) == True
assert is_equal_to_sum_even(26) == True
assert is_equal_to_sum_even(28) == True
assert is_equal_to_sum_even(30) == True
assert is_equal_to_sum_even(32) == True
assert is_equal_to_sum_even(38) == True
assert is_equal_to_sum_even(40) == True
assert is_equal_to_sum_even(42) == True
assert is_equal_to_sum_even(44) == True
assert is_equal_to_sum_even(46) == True
assert is_equal_to_sum_even(50)
assert is_equal_to_sum_even(22)
assert is_equal_to_sum_even(24)
assert is_equal_to_sum_even(28)
assert is_equal_to_sum_even(30)
assert is_equal_to_sum_even(36)
assert is_equal_to_sum_even(40)
assert is_equal_to_sum_even(48)
assert is_equal_to_sum_even(70)
assert is_equal_to_sum_even(80)
assert is_equal_to_sum_even(88)
assert is_equal_to_sum_even(100)
assert is_equal_to_sum_even(190)
assert is_equal_to_sum_even(12) == True
assert is_equal_to_sum_even(100) == True
assert is_equal_to_sum_even(101) == False
assert is_equal_to_sum_even(500) == True
assert is_equal_to_sum_even(501) == False
assert is_equal_to_sum_even(1000) == True
assert is_equal_to_sum_even(1001) == False
assert is_equal_to_sum_even(2000) == True
assert is_equal_to_sum_even(2001) == False
assert is_equal_to_sum_even(10**9) == True
assert is_equal_to_sum_even(10**9 + 1) == False
assert is_equal_to_sum_even(32)
assert is_equal_to_sum_even(68)
assert is_equal_to_sum_even(90)
assert not is_equal_to_sum_even(1)
assert not is_equal_to_sum_even(2)
assert not is_equal_to_sum_even(5)
assert not is_equal_to_sum_even(9)
assert not is_equal_to_sum_even(99)
assert is_equal_to_sum_even(100) == True, "Wrong"
assert is_equal_to_sum_even(18) == True, 'test 3'
assert is_equal_to_sum_even(1) == False
assert is_equal_to_sum_even(66)
assert is_equal_to_sum_even(56) is True, "56 is equal to the sum of 4 positive even numbers"
assert is_equal_to_sum_even(100) is True, "100 is equal to the sum of 4 positive even numbers"
assert is_equal_to_sum_even(10)  # 2 + 2 + 2 + 4
assert is_equal_to_sum_even(50)  # 4 + 6 + 10 + 30
assert not is_equal_to_sum_even(17)
assert not is_equal_to_sum_even(75)
assert is_equal_to_sum_even(997) == False
assert is_equal_to_sum_even(11) == False
assert is_equal_to_sum_even(0) == False
assert is_equal_to_sum_even(4) == False
assert is_equal_to_sum_even(8) == True
assert is_equal_to_sum_even(50) == True
assert is_equal_to_sum_even(2) == False
assert is_equal_to_sum_even(15) == False
assert is_equal_to_sum_even(25) == False
assert is_equal_to_sum_even(29) == False
assert is_equal_to_sum_even(36) == True
assert is_equal_to_sum_even(37) == False
assert not is_equal_to_sum_even(13)
assert is_equal_to_sum_even(20)
assert is_equal_to_sum_even(23) == False
assert is_equal_to_sum_even(132) == True
assert is_equal_to_sum_even(54) == True
assert is_equal_to_sum_even(66) == True
assert is_equal_to_sum_even(110) == True
assert is_equal_to_sum_even(150) == True
assert is_equal_to_sum_even(178) == True
assert is_equal_to_sum_even(200) == True
assert is_equal_to_sum_even(230) == True
assert is_equal_to_sum_even(238) == True
assert is_equal_to_sum_even(250) == True
assert is_equal_to_sum_even(278) == True
assert is_equal_to_sum_even(288) == True
assert is_equal_to_sum_even(298) == True
assert is_equal_to_sum_even(311) == False
assert is_equal_to_sum_even(320)
assert is_equal_to_sum_even(202) == True
assert is_equal_to_sum_even(203) == False
assert is_equal_to_sum_even(196) == True
assert is_equal_to_sum_even(197) == False
assert is_equal_to_sum_even(199) == False
assert is_equal_to_sum_even(35) == False
assert is_equal_to_sum_even(70) == True
assert is_equal_to_sum_even(7) == False
assert is_equal_to_sum_even(8) is True
assert is_equal_to_sum_even(16) is True
assert is_equal_to_sum_even(36) is True
assert is_equal_to_sum_even(40) is True
assert is_equal_to_sum_even(56) is True
assert is_equal_to_sum_even(72)
assert is_equal_to_sum_even(120) == True
assert is_equal_to_sum_even(180) == True
assert is_equal_to_sum_even(-100) == False
assert is_equal_to_sum_even(16)
assert not is_equal_to_sum_even(31)
assert is_equal_to_sum_even(2796202) == True
assert is_equal_to_sum_even(6) is False
assert is_equal_to_sum_even(20) is True
assert is_equal_to_sum_even(16) == True, 'Error in is_equal_to_sum_even'
assert is_equal_to_sum_even(4) == False, 'Error in is_equal_to_sum_even'
assert is_equal_to_sum_even(24) == True
assert is_equal_to_sum_even(60) == True
assert is_equal_to_sum_even(64) == True
assert is_equal_to_sum_even(72) == True
assert is_equal_to_sum_even(80) == True
assert not is_equal_to_sum_even(3)
assert not is_equal_to_sum_even(4)
assert not is_equal_to_sum_even(6)
assert not is_equal_to_sum_even(7)
assert not is_equal_to_sum_even(11)
assert not is_equal_to_sum_even(15)
assert False == is_equal_to_sum_even(25)
assert False == is_equal_to_sum_even(0)
assert False == is_equal_to_sum_even(5)
assert is_equal_to_sum_even(55) == False
assert is_equal_to_sum_even(325) == False
assert is_equal_to_sum_even(68) == True
assert is_equal_to_sum_even(144) == True
assert is_equal_to_sum_even(48) == True
assert is_equal_to_sum_even(51) == False
assert is_equal_to_sum_even(60)
assert not is_equal_to_sum_even(101)
assert is_equal_to_sum_even(3) == False
assert is_equal_to_sum_even(88) == True
assert is_equal_to_sum_even(1) == False, "The assertion that 1 is not the sum of exactly 4 positive even numbers is wrong"
assert is_equal_to_sum_even(20) == True, "The assertion that 20 is the sum of exactly 4 positive even numbers is wrong"
assert is_equal_to_sum_even(100) == True, "The assertion that 100 is the sum of exactly 4 positive even numbers is wrong"
assert is_equal_to_sum_even(7) == False, "The assertion that 7 is not the sum of exactly 4 positive even numbers is wrong"
assert is_equal_to_sum_even(104) == True, "The assertion that 104 is the sum of exactly 4 positive even numbers is wrong"
assert is_equal_to_sum_even(13) == False
assert is_equal_to_sum_even(17) == False
assert is_equal_to_sum_even(19) == False
assert is_equal_to_sum_even(21) == False
assert is_equal_to_sum_even(27) == False
assert is_equal_to_sum_even(28) is True
assert is_equal_to_sum_even(15) is False
assert is_equal_to_sum_even(4) is False
assert is_equal_to_sum_even(1) is False
assert is_equal_to_sum_even(129) == False
assert is_equal_to_sum_even(2) is False
assert is_equal_to_sum_even(112) == True
assert is_equal_to_sum_even(76) == True
assert is_equal_to_sum_even(206) == True
assert is_equal_to_sum_even(21) is False
assert is_equal_to_sum_even(31) == False, 'Test 2 failed'
assert is_equal_to_sum_even(30) == True, 'Test 3 failed'
assert is_equal_to_sum_even(29) == False, 'Test 4 failed'
assert is_equal_to_sum_even(28) == True, 'Test 5 failed'
assert is_equal_to_sum_even(27) == False, 'Test 6 failed'
assert is_equal_to_sum_even(25) == False, 'Test 8 failed'
assert is_equal_to_sum_even(24) == True, 'Test 9 failed'
assert is_equal_to_sum_even(23) == False, 'Test 10 failed'
assert is_equal_to_sum_even(21) == False, 'Test 12 failed'
assert is_equal_to_sum_even(20) == True, 'Test 13 failed'
assert is_equal_to_sum_even(89) == False
assert is_equal_to_sum_even(14)
assert is_equal_to_sum_even(10)
assert is_equal_to_sum_even(12) == True, "Test 2 failed"
assert is_equal_to_sum_even(18) == True, "Test 3 failed"
assert is_equal_to_sum_even(31) == False
assert is_equal_to_sum_even(91) == False
assert is_equal_to_sum_even(92) == True
assert is_equal_to_sum_even(22) is True
assert is_equal_to_sum_even(37) is False
assert is_equal_to_sum_even(47) is False
assert is_equal_to_sum_even(50) is True
assert is_equal_to_sum_even(100) is True
assert is_equal_to_sum_even(198) is True
assert is_equal_to_sum_even(1100) is True
assert is_equal_to_sum_even(1788) is True
assert is_equal_to_sum_even(1904) is True
assert is_equal_to_sum_even(1952) is True
assert is_equal_to_sum_even(2000) is True
assert is_equal_to_sum_even(10000) is True
assert is_equal_to_sum_even(40464) is True
assert is_equal_to_sum_even(99999) is False
assert is_equal_to_sum_even(1000000) is True
assert is_equal_to_sum_even(1000001) is False
assert is_equal_to_sum_even(103) == False
assert is_equal_to_sum_even(106) == True
assert is_equal_to_sum_even(99900) == True
assert is_equal_to_sum_even(99901) == False
assert is_equal_to_sum_even(99903) == False
assert is_equal_to_sum_even(99906) == True
assert is_equal_to_sum_even(99912) == True
assert is_equal_to_sum_even(18) is True, "The function is not correct."
assert is_equal_to_sum_even(28) is True, "The function is not correct."
assert is_equal_to_sum_even(12) == True, '12 is a sum of exactly 4 positive even numbers (2+2+2+6)'
assert is_equal_to_sum_even(68) == True, '68 is a sum of exactly 4 positive even numbers (2+2+2+62)'
assert is_equal_to_sum_even(34)
assert is_equal_to_sum_even(38)
assert is_equal_to_sum_even(52)
assert is_equal_to_sum_even(54)
assert is_equal_to_sum_even(62)
assert is_equal_to_sum_even(64)
assert is_equal_to_sum_even(74)
assert is_equal_to_sum_even(76)
assert is_equal_to_sum_even(82)
assert is_equal_to_sum_even(86)
assert is_equal_to_sum_even(92)
assert is_equal_to_sum_even(94)
assert is_equal_to_sum_even(104) == True
