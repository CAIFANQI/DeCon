

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
assert is_prime(5) == True
assert is_prime(7) == True
assert is_prime(11) == True
assert is_prime(13) == True
assert is_prime(17) == True
assert is_prime(19) == True
assert is_prime(23) == True
assert is_prime(29) == True
assert is_prime(31) == True
assert is_prime(37) == True
assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(3) == True, "The 3 is not a prime number"
assert is_prime(5) == True, "The 5 is not a prime number"
assert is_prime(3)
assert is_prime(5)
assert is_prime(17)
assert is_prime(31)
assert is_prime(5) == True, "5 is prime"
assert is_prime(13) == True, "13 is prime"
assert is_prime(2) is True
assert is_prime(3) is True
assert is_prime(11) is True
assert is_prime(13) is True
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
assert is_prime(157) == True
assert is_prime(7) is True
assert is_prime(5) is True
assert is_prime(47) == True
assert is_prime(67) == True
assert is_prime(73) == True
assert is_prime(83) == True
assert is_prime(97) == True
assert is_prime(151) == True
assert is_prime(7) # this is true
assert is_prime(11) # this is true
assert is_prime(17) # this is true
assert is_prime(29) # this is true
assert is_prime(41) # this is true
assert is_prime(53) # this is true
assert is_prime(71) # this is true
assert is_prime(83) # this is true
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
assert is_prime(59) == True
assert is_prime(101) == True
assert is_prime(127) == True
assert is_prime(241) == True
assert is_prime(257) == True
assert is_prime(317) == True
assert is_prime(367) == True
assert is_prime(379) == True
assert is_prime(397) == True
assert is_prime(409) == True
assert is_prime(421) == True
assert is_prime(433) == True
assert is_prime(457) == True
assert is_prime(7)
assert is_prime(251) is True
assert is_prime(3301) is True
assert is_prime(19)
assert is_prime(29)
assert is_prime(101)
