

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
assert not is_prime(1)
assert is_prime(2)
assert is_prime(3)
assert not is_prime(4)
assert is_prime(5)
assert not is_prime(6)
assert is_prime(7)
assert not is_prime(8)
assert not is_prime(9)
assert not is_prime(10)
assert is_prime(11)
assert is_prime(2) == True
assert is_prime(5) == True
assert is_prime(27) == False
assert is_prime(32) == False
assert is_prime(67) == True
assert is_prime(68) == False
assert is_prime(121) == False
assert is_prime(122) == False
assert is_prime(125) == False
assert is_prime(130) == False
assert is_prime(131) == True
assert is_prime(190) == False
assert is_prime(191) == True
assert is_prime(4) == False
assert is_prime(9) == False
assert is_prime(17) == True
assert is_prime(99) == False
assert is_prime(107) == True
assert is_prime(17)
assert is_prime(19)
assert is_prime(23)
assert is_prime(29)
assert is_prime(31)
assert is_prime(37)
assert is_prime(41)
assert is_prime(43)
assert is_prime(47)
assert is_prime(53)
assert is_prime(59)
assert is_prime(61)
assert is_prime(67)
assert is_prime(71)
assert is_prime(73)
assert is_prime(79)
assert is_prime(83)
assert is_prime(89)
assert is_prime(97)
assert is_prime(101)
assert is_prime(103)
assert is_prime(107)
assert is_prime(109)
assert is_prime(113)
assert is_prime(127)
assert is_prime(131)
assert is_prime(137)
assert is_prime(139)
assert is_prime(149)
assert is_prime(151)
assert is_prime(157)
assert is_prime(163)
assert is_prime(3) == True
assert is_prime(10) == False
assert is_prime(6) == False
assert is_prime(7) == True
assert is_prime(8) == False
assert is_prime(11) == True
assert is_prime(12) == False
assert is_prime(13) == True
assert is_prime(14) == False
assert is_prime(15) == False
assert is_prime(16) == False
assert is_prime(18) == False
assert is_prime(19) == True
assert is_prime(2) is True
assert is_prime(3) is True
assert is_prime(4) is False
assert is_prime(5) is True
assert is_prime(6) is False
assert is_prime(7) is True
assert is_prime(8) is False
assert is_prime(9) is False
assert is_prime(10) is False
assert is_prime(11) is True
assert is_prime(12) is False
assert is_prime(13) is True
assert is_prime(14) is False
assert is_prime(15) is False
assert is_prime(16) is False
assert is_prime(17) is True
assert is_prime(18) is False
assert is_prime(19) is True
assert is_prime(20) is False
assert is_prime(101) == True
assert is_prime(2**4+1) == True
assert is_prime(20) == False
assert is_prime(21) == False
assert is_prime(22) == False
assert is_prime(23) == True
assert not is_prime(14)
assert is_prime(1) == False
assert is_prime(100) == False
assert is_prime(119) == False
assert is_prime(199) == True
assert is_prime(4099) == True
assert is_prime(500009) == True
assert is_prime(7368787) == True
assert is_prime(23) is True
assert is_prime(61) is True
assert not is_prime(100)
assert not is_prime(20)
assert is_prime(42) == False
assert is_prime(29) == True
assert is_prime(49) == False
assert is_prime(13)
assert not is_prime(15)
assert is_prime(31) == True
assert is_prime(37) == True
assert is_prime(41) == True
assert is_prime(43) == True
assert is_prime(47) == True
assert is_prime(53) == True
assert is_prime(59) == True
assert is_prime(61) == True
assert is_prime(71) == True
assert is_prime(73) == True
assert is_prime(79) == True
assert is_prime(83) == True
assert is_prime(89) == True
assert is_prime(97) == True
assert is_prime(24) == False
assert is_prime(25) == False
assert is_prime(26) == False
assert is_prime(28) == False
assert is_prime(100003) == True
assert not is_prime(28)
assert is_prime(979) == False
assert not is_prime(0)
assert not is_prime(12)
assert is_prime(0) == False
assert is_prime(-1) == False
assert is_prime(-2) == False
assert is_prime(-3) == False
assert is_prime(-4) == False
assert is_prime(-5) == False
assert is_prime(35) == False
assert is_prime(2) == True, 'two is a prime number'
assert is_prime(3) == True, 'three is a prime number'
assert is_prime(4) == False, 'four is not a prime number'
assert is_prime(5) == True, 'five is a prime number'
assert is_prime(21) == False, 'twenty one is not a prime number'
assert is_prime(41) == True, 'forty one is a prime number'
assert is_prime(101) == True, 'one hundred and one is a prime number'
assert is_prime(1009) == True, 'one thousand and nine is a prime number'
assert is_prime(104729) == True, 'one hundred and four thousand, seven hundred and twenty nine is a prime number'
assert is_prime(2 * 3 * 5 * 7 * 11 * 13 * 17 * 19) == False, 'Not prime'
assert is_prime(2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29) == False, 'Not prime'
assert is_prime(51) == False
assert is_prime(2) == True, "two is prime"
assert is_prime(3) == True, "three is prime"
assert is_prime(4) == False, "four is not prime"
assert is_prime(5) == True, "five is prime"
assert is_prime(6) == False, "six is not prime"
assert is_prime(7) == True, "seven is prime"
assert is_prime(8) == False, "eight is not prime"
assert is_prime(9) == False, "nine is not prime"
assert is_prime(10) == False, "ten is not prime"
assert is_prime(11) == True, "eleven is prime"
assert is_prime(12) == False, "twelve is not prime"
assert is_prime(15) == False, "fifteen is not prime"
assert is_prime(17) == True, "seventeen is prime"
assert is_prime(25) == False, "twenty-five is not prime"
assert is_prime(39) == False, "thirty-nine is not prime"
assert is_prime(41) == True, "forty-one is prime"
assert is_prime(30) == False
assert is_prime(10007) == True
assert not is_prime(21)
assert not is_prime(91)
assert is_prime(7919)
assert is_prime(25) is False
assert is_prime(31) is True
assert is_prime(32) is False
assert is_prime(1000) is False
assert is_prime(1009) is True
assert is_prime(10007) is True
assert is_prime(2) == True, "2 is prime."
assert is_prime(10) == False, "10 is not prime."
assert is_prime(11) == True, "11 is prime."
assert is_prime(12) == False, "12 is not prime."
assert is_prime(17) == True, "17 is prime."
assert is_prime(100) == False, "100 is not prime."
assert is_prime(101) == True, "101 is prime."
assert is_prime(102) == False, "102 is not prime."
assert is_prime(1000) == False, "1000 is not prime."
assert is_prime(1002) == False, "1002 is not prime."
assert is_prime(1487) == True
assert is_prime(1.0) == False
assert is_prime(29) is True
assert is_prime(75) is False
assert is_prime(5099) == True
assert is_prime(113) == True
assert is_prime(112) == False
assert not is_prime(10000000000000)
assert is_prime(2)==True
assert is_prime(3)==True
assert is_prime(4)==False
assert is_prime(5)==True
assert is_prime(6)==False
assert is_prime(7)==True
assert is_prime(8)==False
assert is_prime(9)==False
assert is_prime(10)==False
assert is_prime(11)==True
assert is_prime(12)==False
assert is_prime(2) == True, "2 is prime"
assert is_prime(3) == True, "3 is prime"
assert is_prime(4) == False, "4 is not prime"
assert is_prime(5) == True, "5 is prime"
assert is_prime(6) == False, "6 is not prime"
assert is_prime(7) == True, "7 is prime"
assert is_prime(8) == False, "8 is not prime"
assert is_prime(9) == False, "9 is not prime"
assert is_prime(10) == False, "10 is not prime"
assert is_prime(11) == True, "11 is prime"
assert is_prime(12) == False, "12 is not prime"
assert is_prime(13) == True, "13 is prime"
assert is_prime(14) == False, "14 is not prime"
assert is_prime(15) == False, "15 is not prime"
assert is_prime(16) == False, "16 is not prime"
assert is_prime(17) == True, "17 is prime"
assert is_prime(18) == False, "18 is not prime"
assert not is_prime(18)
assert not is_prime(30)
assert not is_prime(32)
assert not is_prime(50)
assert not is_prime(124)
assert not is_prime(126)
assert not is_prime(128)
assert not is_prime(130)
assert not is_prime(132)
assert not is_prime(134)
assert not is_prime(136)
assert not is_prime(138)
assert not is_prime(140)
assert not is_prime(142)
assert is_prime(7919) == True
assert is_prime(7920) == False
assert is_prime(999) == False
assert is_prime(21) is False
assert is_prime(22) is False
assert is_prime(24) is False
assert not is_prime(16)
assert not is_prime(22)
assert not is_prime(24)
assert not is_prime(25)
assert not is_prime(26)
assert not is_prime(27)
assert not is_prime(33)
assert not is_prime(34)
