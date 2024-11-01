
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(n):
        for j in range(0,n):
            if n%j == 0:
                return False
        return True

    for i in range(2,101):
        if not is_prime(i): continue
        for j in range(2,101):
            if not is_prime(j): continue
            for k in range(2,101):
                if not is_prime(k): continue
                if i*j*k == a: return True
    return False
assert is_multiply_prime(11) == False
assert is_multiply_prime(30) == True
assert not is_multiply_prime(9)
assert not is_multiply_prime(14)
assert not is_multiply_prime(16)
assert not is_multiply_prime(22)
assert not is_multiply_prime(24)
assert not is_multiply_prime(26)
assert not is_multiply_prime(32)
assert not is_multiply_prime(34)
assert not is_multiply_prime(36)
assert not is_multiply_prime(38)
assert not is_multiply_prime(40)
assert not is_multiply_prime(3)
assert not is_multiply_prime(4)
assert not is_multiply_prime(6)
assert not is_multiply_prime(7)
assert not is_multiply_prime(11)
assert not is_multiply_prime(15)
assert not is_multiply_prime(17)
assert not is_multiply_prime(21)
assert not is_multiply_prime(23)
assert not is_multiply_prime(25)
assert not is_multiply_prime(29)
assert not is_multiply_prime(31)
assert not is_multiply_prime(33)
assert is_multiply_prime(3) == False
assert is_multiply_prime(4) == False
assert is_multiply_prime(6) == False
assert is_multiply_prime(7) == False
assert is_multiply_prime(10) == False
assert is_multiply_prime(13) == False
assert is_multiply_prime(14) == False
assert is_multiply_prime(16) == False
assert is_multiply_prime(17) == False
assert is_multiply_prime(19) == False
assert is_multiply_prime(21) == False
assert is_multiply_prime(23) == False
assert is_multiply_prime(24) == False
assert is_multiply_prime(26) == False
assert is_multiply_prime(29) == False
assert is_multiply_prime(31) == False
assert is_multiply_prime(22) is False
assert is_multiply_prime(23) is False
assert is_multiply_prime(24) is False
assert is_multiply_prime(25) is False
assert is_multiply_prime(31) is False
assert is_multiply_prime(33) is False
assert is_multiply_prime(34) is False
assert is_multiply_prime(35) is False
assert is_multiply_prime(41) is False
assert is_multiply_prime(43) is False
assert is_multiply_prime(51) is False
assert is_multiply_prime(54) is False
assert is_multiply_prime(55) is False
assert is_multiply_prime(61) is False
assert is_multiply_prime(65) is False
assert is_multiply_prime(15) == False
assert is_multiply_prime(22) == False
assert is_multiply_prime(25) == False
assert is_multiply_prime(32) == False
assert is_multiply_prime(33) == False
assert is_multiply_prime(34) == False
assert is_multiply_prime(35) == False
assert is_multiply_prime(5) == False
assert is_multiply_prime(9) == False
assert is_multiply_prime(40) == False
assert is_multiply_prime(37) == False
assert is_multiply_prime(2) == False
assert is_multiply_prime(80) == False
assert not is_multiply_prime(5), '5 can not be a multiplication of 3 prime numbers.'
assert not is_multiply_prime(2), '2 can not be a multiplication of 3 prime numbers.'
assert not is_multiply_prime(6), '6 can not be a multiplication of 3 prime numbers.'
assert is_multiply_prime(10) is False
assert is_multiply_prime(21) is False
assert is_multiply_prime(19) is False
assert is_multiply_prime(51) == False
assert is_multiply_prime(30), True
assert is_multiply_prime(11) is False
assert is_multiply_prime(36) == False
assert is_multiply_prime(47) == False
assert not is_multiply_prime(51)
assert not is_multiply_prime(81)
assert is_multiply_prime(41) == False
assert is_multiply_prime(7) == False, "This number is less than 100, so it can't be the multiplication of 3 prime numbers."
assert not is_multiply_prime(49)
assert not is_multiply_prime(91)
assert is_multiply_prime(38) == False
assert is_multiply_prime(81) == False
assert is_multiply_prime(82) == False
assert is_multiply_prime(2) is False
assert is_multiply_prime(5) is False
assert is_multiply_prime(72) is False
assert is_multiply_prime(67) is False
assert is_multiply_prime(30) is True
assert is_multiply_prime(17) is False
assert is_multiply_prime(15) is False
