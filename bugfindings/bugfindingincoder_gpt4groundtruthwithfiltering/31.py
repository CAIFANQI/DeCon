

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
assert is_prime(2)
assert not is_prime(4)
assert not is_prime(6)
assert not is_prime(8)
assert not is_prime(9)
assert not is_prime(10)
assert not is_prime(12)
assert not is_prime(14)
assert not is_prime(15)
assert not is_prime(16)
assert not is_prime(18)
assert not is_prime(20)
assert not is_prime(21)
assert not is_prime(22)
assert not is_prime(24)
assert not is_prime(25)
assert not is_prime(26)
assert not is_prime(27)
assert not is_prime(28)
assert not is_prime(30)
assert not is_prime(32)
assert not is_prime(33)
assert not is_prime(34)
assert not is_prime(35)
assert not is_prime(36)
assert not is_prime(38)
assert not is_prime(39)
assert not is_prime(40)
assert not is_prime(42)
assert is_prime(5) == True
assert is_prime(6) == False
assert is_prime(7) == True
assert is_prime(8) == False
assert is_prime(10) == False
assert is_prime(11) == True
assert is_prime(12) == False
assert is_prime(13) == True
assert is_prime(14) == False
assert is_prime(16) == False
assert is_prime(17) == True
assert is_prime(18) == False
assert is_prime(19) == True
assert is_prime(20) == False
assert is_prime(22) == False
assert is_prime(23) == True
assert is_prime(24) == False
assert is_prime(26) == False
assert is_prime(28) == False
assert is_prime(29) == True
assert is_prime(30) == False
assert is_prime(31) == True
assert is_prime(32) == False
assert is_prime(34) == False
assert is_prime(36) == False
assert is_prime(37) == True
assert is_prime(38) == False
assert is_prime(-1) == False
assert is_prime(1) == False
assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(3) == True, "The 3 is not a prime number"
assert is_prime(5) == True, "The 5 is not a prime number"
assert is_prime(8) == False, "The 8 is not a prime number"
assert is_prime(9) == False, "The 9 is not a prime number"
assert is_prime(10) == False, "The 10 is not a prime number"
assert is_prime(12) == False, "The 12 is not a prime number"
assert is_prime(14) == False, "The 14 is not a prime number"
assert is_prime(15) == False, "The 15 is not a prime number"
assert is_prime(16) == False, "The 16 is not a prime number"
assert is_prime(18) == False, "The 18 is not a prime number"
assert is_prime(20) == False, "The 20 is not a prime number"
assert is_prime(21) == False, "The 21 is not a prime number"
assert not is_prime(1)
assert is_prime(3)
assert is_prime(5)
assert is_prime(17)
assert is_prime(31)
assert is_prime(4) == False, "4 is prime"
assert is_prime(5) == True, "5 is prime"
assert is_prime(8) == False, "8 is prime"
assert is_prime(12) == False, "12 is prime"
assert is_prime(13) == True, "13 is prime"
assert is_prime(14) == False, "14 is prime"
assert is_prime(16) == False, "16 is prime"
assert is_prime(21) == False, "21 is prime"
assert is_prime(22) == False, "22 is prime"
assert is_prime(24) == False, "24 is prime"
assert is_prime(25) == False, "25 is prime"
assert is_prime(26) == False, "26 is prime"
assert is_prime(2) is True
assert is_prime(3) is True
assert is_prime(8) is False
assert is_prime(11) is True
assert is_prime(12) is False
assert is_prime(13) is True
assert is_prime(15) is False
assert is_prime(16) is False
assert is_prime(18) is False
assert is_prime(20) is False
assert is_prime(21) is False
assert is_prime(22) is False
assert is_prime(24) is False
assert is_prime(25) is False
assert is_prime(26) is False
assert is_prime(27) is False
assert is_prime(28) is False
assert is_prime(30) is False
assert is_prime(32) is False
assert is_prime(33) is False
assert is_prime(34) is False
assert is_prime(35) is False
assert is_prime(36) is False
assert is_prime(38) is False
assert is_prime(39) is False
assert is_prime(40) is False
assert is_prime(6) == False, "6 is prime"
assert is_prime(15) == False, "15 is prime"
assert is_prime(18) == False, "18 is prime"
assert is_prime(20) == False, "20 is prime"
assert is_prime(27) == False, "27 is prime"
assert is_prime(28) == False, "28 is prime"
assert is_prime(33) == False
assert is_prime(43) == True
assert is_prime(53) == True
assert is_prime(61) == True
assert is_prime(71) ==  True
assert is_prime(79) == True
assert is_prime(89) == True
assert is_prime(101) ==  True
assert is_prime(107) == True
assert is_prime(113) == True
assert is_prime(131) == True
assert is_prime(139) == True
assert is_prime(143) == False
assert is_prime(157) == True
assert is_prime(10) is False
assert is_prime(7) is True
assert is_prime(6) is False
assert is_prime(5) is True
assert is_prime(4) is False
assert is_prime(1) is False
assert is_prime(4) == False
assert is_prime(47) == True
assert is_prime(67) == True
assert is_prime(73) == True
assert is_prime(83) == True
assert is_prime(97) == True
assert is_prime(9) == False
assert is_prime(104) == False
assert is_prime(105) == False
assert is_prime(121) == False
assert is_prime(134) == False
assert is_prime(140) == False
assert is_prime(145) == False
assert is_prime(151) == True
assert is_prime(160) == False
assert is_prime(169) == False
assert is_prime(171) == False
assert is_prime(7) # this is true
assert is_prime(11) # this is true
assert is_prime(17) # this is true
assert is_prime(29) # this is true
assert not is_prime(34) # this is false
assert not is_prime(35) # this is false
assert not is_prime(39) # this is false
assert is_prime(41) # this is true
assert is_prime(53) # this is true
assert is_prime(71) # this is true
assert is_prime(83) # this is true
assert not is_prime(91) # this is false
assert is_prime(11), False
assert is_prime(19), False
assert is_prime(23), False
assert is_prime(29), True
assert is_prime(31), False
assert is_prime(37), False
assert is_prime(43), False
assert is_prime(47), False
assert is_prime(53), False
assert is_prime(59), False
assert is_prime(61), True
assert is_prime(67), False
assert is_prime(71), False
assert is_prime(73), False
assert is_prime(79), False
assert is_prime(89), True
assert is_prime(97), True
assert is_prime(11)
assert not is_prime(0)
assert not is_prime(-7)
assert not is_prime(-13)
assert not is_prime(-11)
assert not is_prime(-0)
assert not is_prime(-8)
assert not is_prime(-3)
assert not is_prime(1000)
assert not is_prime(-1001)
assert not is_prime(-9999)
assert not is_prime(1000000)
assert not is_prime(-1000000)
assert not is_prime(1000000000)
assert not is_prime(1000000001)
assert not is_prime(1000000002)
assert not is_prime(1000000003)
assert not is_prime(1000000004)
assert not is_prime(1000000005)
assert not is_prime(1000000006)
assert not is_prime(1000000008)
assert not is_prime(1000000010)
assert not is_prime(1000000011)
assert not is_prime(1000000012)
assert not is_prime(1000000013)
assert not is_prime(1000000014)
assert not is_prime(1000000015)
assert not is_prime(1000000016)
assert is_prime(15) == False
assert is_prime(50) == False
assert is_prime(59) == True
assert is_prime(39) == False
assert is_prime(101) == True
assert is_prime(127) == True
assert is_prime(241) == True
assert is_prime(257) == True
assert is_prime(317) == True
assert is_prime(329) == False
assert is_prime(367) == True
assert is_prime(379) == True
assert is_prime(397) == True
assert is_prime(409) == True
assert is_prime(421) == True
assert is_prime(433) == True
assert is_prime(457) == True
assert is_prime(501) == False
assert is_prime(7)
assert is_prime(0) == False
assert not is_prime(-1)
assert not is_prime(99)
assert is_prime(81) == False
assert is_prime(100) == False
assert is_prime(120) == False
assert is_prime(125) == False
assert not is_prime(190)
assert not is_prime(-19)
assert not is_prime(-20)
assert not is_prime(100)
assert not is_prime(102)
assert not is_prime(-99)
assert not is_prime(-100)
assert not is_prime(-101)
assert not is_prime(104)
assert not is_prime(-103)
assert not is_prime(-104)
assert is_prime(100) is False
assert is_prime(121) is False
assert is_prime(251) is True
assert is_prime(1001) is False
assert is_prime(1011) is False
assert is_prime(1110) is False
assert is_prime(1800) is False
assert is_prime(1900) is False
assert is_prime(2000) is False
assert is_prime(2100) is False
assert is_prime(2200) is False
assert is_prime(2507) is False
assert is_prime(2511) is False
assert is_prime(2907) is False
assert is_prime(2911) is False
assert is_prime(3000) is False
assert is_prime(3100) is False
assert is_prime(3200) is False
assert is_prime(3301) is True
assert is_prime(3311) is False
assert is_prime(3700) is False
assert is_prime(14) is False
assert is_prime(50) is False
assert is_prime(142) is False
assert is_prime(162) is False
assert is_prime(177) is False
assert is_prime(253) is False
assert is_prime(420) is False
assert is_prime(527) is False
assert is_prime(675) is False
assert is_prime(795) is False
assert is_prime(1083) is False
assert is_prime(1133) is False
assert is_prime(1227) is False
assert is_prime(1359) is False
assert is_prime(-3) is False
assert is_prime(0) is False
assert is_prime(-1) is False
assert not is_prime(105)
assert not is_prime(106)
assert not is_prime(1099)
assert not is_prime(10999)
assert not is_prime(999999999)
assert not is_prime(-10)
assert not is_prime(10**100)
assert is_prime(19)
assert is_prime(42) == False
assert is_prime(27) == False
assert is_prime(49) == False
assert is_prime(50001) == False
assert is_prime(51) == False
assert is_prime(-11) == False
assert not is_prime(0), 'zero numbers should not be prime'
assert not is_prime(1), 'one number should be prime'
assert is_prime(29)
assert is_prime(-4) == False
assert is_prime(25) == False
assert is_prime(101)
assert not is_prime(12) # 12 is not prime
assert not is_prime(2**10000)
assert not is_prime(2**1000000007)
assert is_prime(153) == False
assert is_prime(1717172) == False
