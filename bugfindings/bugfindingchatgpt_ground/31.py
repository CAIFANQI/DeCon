

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if n < 1:
        return False
    for k in range(1, n - 1):
        if n % k == 0:
            return False
    return True
assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(4) == False
assert is_prime(5) == True
assert is_prime(6) == False
assert is_prime(7) == True
assert is_prime(8) == False
assert is_prime(9) == False
assert is_prime(10) == False
assert is_prime(11) == True
assert is_prime(12) == False
assert is_prime(13) == True
assert is_prime(14) == False
assert is_prime(15) == False
assert is_prime(16) == False
assert is_prime(17) == True
assert is_prime(18) == False
assert is_prime(19) == True
assert is_prime(20) == False
assert is_prime(21) == False
assert is_prime(22) == False
assert is_prime(23) == True
assert is_prime(24) == False
assert is_prime(25) == False
assert is_prime(26) == False
assert is_prime(27) == False
assert is_prime(28) == False
assert is_prime(29) == True
assert is_prime(30) == False
assert is_prime(31) == True
assert is_prime(32) == False
assert is_prime(33) == False
assert is_prime(34) == False
assert is_prime(35) == False
assert is_prime(36) == False
assert is_prime(37) == True
assert is_prime(38) == False
assert is_prime(39) == False
assert is_prime(40) == False
assert is_prime(41) == True
assert is_prime(42) == False
assert is_prime(43) == True
assert is_prime(44) == False
assert is_prime(45) == False
assert is_prime(46) == False
assert is_prime(47) == True
assert is_prime(48) == False
assert is_prime(49) == False
assert is_prime(50) == False
assert is_prime(51) == False
assert is_prime(52) == False
assert is_prime(53) == True
assert is_prime(54) == False
assert is_prime(55) == False
assert is_prime(56) == False
assert is_prime(57) == False
assert is_prime(58) == False
assert is_prime(59) == True
assert is_prime(60) == False
assert is_prime(61) == True
assert is_prime(62) == False
assert is_prime(63) == False
assert is_prime(64) == False
assert is_prime(65) == False
assert is_prime(66) == False
assert is_prime(67) == True
assert is_prime(68) == False
assert is_prime(69) == False
assert is_prime(70) == False
assert is_prime(71) == True
assert is_prime(72) == False
assert is_prime(73) == True
assert is_prime(74) == False
assert is_prime(75) == False
assert is_prime(76) == False
assert is_prime(77) == False
assert is_prime(78) == False
assert is_prime(79) == True
assert is_prime(80) == False
assert is_prime(81) == False
assert is_prime(82) == False
assert is_prime(83) == True
assert is_prime(84) == False
assert is_prime(85) == False
assert is_prime(86) == False
assert is_prime(87) == False
assert is_prime(88) == False
assert is_prime(89) == True
assert is_prime(90) == False
assert is_prime(91) == False
assert is_prime(92) == False
assert is_prime(93) == False
assert is_prime(94) == False
assert is_prime(95) == False
assert is_prime(96) == False
assert is_prime(97) == True
assert is_prime(98) == False
assert is_prime(99) == False
assert is_prime(100) == False
assert is_prime(101) == True
assert is_prime(102) == False
assert is_prime(103) == True
assert is_prime(104) == False
assert is_prime(105) == False
assert is_prime(106) == False
assert is_prime(107) == True
assert is_prime(108) == False
assert is_prime(109) == True
assert is_prime(110) == False
assert is_prime(111) == False
assert is_prime(112) == False
assert is_prime(113) == True
assert is_prime(114) == False
assert is_prime(115) == False
assert is_prime(3) == True, "Test case 2 failed"
assert is_prime(4) == False, "Test case 3 failed"
assert is_prime(5) == True, "Test case 4 failed"
assert is_prime(6) == False, "Test case 5 failed"
assert is_prime(2) == True, "Test case 2 failed"
assert is_prime(3) == True, "Test case 3 failed"
assert is_prime(4) == False, "Test case 4 failed"
assert is_prime(5) == True, "Test case 5 failed"
assert is_prime(6) == False, "Test case 6 failed"
assert is_prime(7) == True, "Test case 7 failed"
assert is_prime(8) == False, "Test case 8 failed"
assert is_prime(9) == False, "Test case 9 failed"
assert is_prime(10) == False, "Test case 10 failed"
assert is_prime(3) == True, 'Test Case 2 Failed'
assert is_prime(4) == False, 'Test Case 3 Failed'
assert is_prime(5) == True, 'Test Case 4 Failed'
assert is_prime(6) == False, 'Test Case 5 Failed'
assert is_prime(7) == True, 'Test Case 6 Failed'
assert is_prime(8) == False, 'Test Case 7 Failed'
assert is_prime(9) == False, 'Test Case 8 Failed'
assert is_prime(10) == False, 'Test Case 9 Failed'
assert is_prime(11) == True, 'Test Case 10 Failed'
assert is_prime(12) == False, 'Test Case 11 Failed'
assert is_prime(13) == True, 'Test Case 12 Failed'
assert is_prime(14) == False, 'Test Case 13 Failed'
assert is_prime(15) == False, 'Test Case 14 Failed'
assert is_prime(16) == False, 'Test Case 15 Failed'
assert is_prime(17) == True, 'Test Case 16 Failed'
assert is_prime(18) == False, 'Test Case 17 Failed'
assert is_prime(19) == True, 'Test Case 18 Failed'
assert is_prime(20) == False, 'Test Case 19 Failed'
assert is_prime(21) == False, 'Test Case 20 Failed'
assert is_prime(22) == False, 'Test Case 21 Failed'
assert is_prime(23) == True, 'Test Case 22 Failed'
assert is_prime(24) == False, 'Test Case 23 Failed'
assert is_prime(25) == False, 'Test Case 24 Failed'
assert is_prime(26) == False, 'Test Case 25 Failed'
assert is_prime(27) == False, 'Test Case 26 Failed'
assert is_prime(28) == False, 'Test Case 27 Failed'
assert is_prime(29) == True, 'Test Case 28 Failed'
assert is_prime(30) == False, 'Test Case 29 Failed'
assert is_prime(31) == True, 'Test Case 30 Failed'
assert is_prime(32) == False, 'Test Case 31 Failed'
assert is_prime(33) == False, 'Test Case 32 Failed'
assert is_prime(11) == True, "Test case 11 failed"
assert is_prime(12) == False, "Test case 12 failed"
assert is_prime(13) == True, "Test case 13 failed"
assert is_prime(14) == False, "Test case 14 failed"
assert is_prime(15) == False, "Test case 15 failed"
assert is_prime(16) == False, "Test case 16 failed"
assert is_prime(17) == True, "Test case 17 failed"
assert is_prime(18) == False, "Test case 18 failed"
assert is_prime(19) == True, "Test case 19 failed"
assert is_prime(20) == False, "Test case 20 failed"
assert is_prime(-2) == False
assert is_prime(-3) == False
assert is_prime(-4) == False
assert is_prime(-5) == False
assert is_prime(-6) == False
assert is_prime(1000000008) == False
assert is_prime(1000000010) == False
