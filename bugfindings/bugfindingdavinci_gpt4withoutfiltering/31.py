

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
assert is_prime(3)
assert is_prime(5)
assert is_prime(7)
assert is_prime(11)
assert is_prime(2) == True
assert is_prime(5) == True
assert is_prime(67) == True
assert is_prime(131) == True
assert is_prime(191) == True
assert is_prime(17) == True
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
assert is_prime(7) == True
assert is_prime(11) == True
assert is_prime(13) == True
assert is_prime(19) == True
assert is_prime(2) is True
assert is_prime(3) is True
assert is_prime(5) is True
assert is_prime(7) is True
assert is_prime(11) is True
assert is_prime(13) is True
assert is_prime(17) is True
assert is_prime(19) is True
assert is_prime(101) == True
assert is_prime(2**4+1) == True
assert is_prime(23) == True
assert is_prime(199) == True
assert is_prime(4099) == True
assert is_prime(500009) == True
assert is_prime(7368787) == True
assert is_prime(23) is True
assert is_prime(61) is True
assert is_prime(29) == True
assert is_prime(13)
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
assert is_prime(100003) == True
assert is_prime(2) == True, 'two is a prime number'
assert is_prime(3) == True, 'three is a prime number'
assert is_prime(5) == True, 'five is a prime number'
assert is_prime(41) == True, 'forty one is a prime number'
assert is_prime(101) == True, 'one hundred and one is a prime number'
assert is_prime(1009) == True, 'one thousand and nine is a prime number'
assert is_prime(104729) == True, 'one hundred and four thousand, seven hundred and twenty nine is a prime number'
assert is_prime(2) == True, "two is prime"
assert is_prime(3) == True, "three is prime"
assert is_prime(5) == True, "five is prime"
assert is_prime(7) == True, "seven is prime"
assert is_prime(11) == True, "eleven is prime"
assert is_prime(17) == True, "seventeen is prime"
assert is_prime(41) == True, "forty-one is prime"
assert is_prime(10007) == True
assert is_prime(7919)
assert is_prime(31) is True
assert is_prime(1009) is True
assert is_prime(10007) is True
assert is_prime(2) == True, "2 is prime."
assert is_prime(11) == True, "11 is prime."
assert is_prime(17) == True, "17 is prime."
assert is_prime(101) == True, "101 is prime."
assert is_prime(1487) == True
assert is_prime(29) is True
assert is_prime(5099) == True
assert is_prime(113) == True
assert is_prime(2)==True
assert is_prime(3)==True
assert is_prime(5)==True
assert is_prime(7)==True
assert is_prime(11)==True
assert is_prime(2) == True, "2 is prime"
assert is_prime(3) == True, "3 is prime"
assert is_prime(5) == True, "5 is prime"
assert is_prime(7) == True, "7 is prime"
assert is_prime(11) == True, "11 is prime"
assert is_prime(13) == True, "13 is prime"
assert is_prime(17) == True, "17 is prime"
assert is_prime(7919) == True
