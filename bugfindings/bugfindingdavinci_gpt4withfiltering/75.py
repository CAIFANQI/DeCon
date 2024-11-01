
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
assert is_multiply_prime(26) is False
assert is_multiply_prime(48) is False
assert is_multiply_prime(1) is False
assert is_multiply_prime(2) is False
assert is_multiply_prime(3) is False
assert is_multiply_prime(4) is False
assert is_multiply_prime(5) is False
assert is_multiply_prime(7) is False
assert is_multiply_prime(10) is False
assert is_multiply_prime(11) is False
assert is_multiply_prime(13) is False
assert is_multiply_prime(14) is False
assert is_multiply_prime(16) is False
assert is_multiply_prime(17) is False
assert is_multiply_prime(11) == False
assert is_multiply_prime(17) == False
assert is_multiply_prime(30) == True
assert is_multiply_prime(32) == False
assert is_multiply_prime(51) == False
assert is_multiply_prime(78) == True
assert is_multiply_prime(94) == False
assert False == is_multiply_prime(4)
assert is_multiply_prime(42) == True
assert is_multiply_prime(66) == True
assert is_multiply_prime(70) == True
assert is_multiply_prime(7) == False
assert is_multiply_prime(21) == False
assert is_multiply_prime(2) == False
assert is_multiply_prime(4) == False
assert is_multiply_prime(91) == False
assert is_multiply_prime(67) is False
assert is_multiply_prime(10) == False
assert is_multiply_prime(88) == False
assert is_multiply_prime(21) is False
assert is_multiply_prime(25) is False
assert is_multiply_prime(33) is False
assert is_multiply_prime(35) is False
assert is_multiply_prime(49) is False
assert is_multiply_prime(5) == False
assert is_multiply_prime(59) == False
assert is_multiply_prime(15) == False
assert is_multiply_prime(84) == False
assert is_multiply_prime(47) is False
assert is_multiply_prime(13) == False
assert is_multiply_prime(37) == False
assert is_multiply_prime(7) == False, 'is_multiply_prime test failed'
assert is_multiply_prime(35) == False, 'is_multiply_prime test failed'
assert is_multiply_prime(91) == False, 'is_multiply_prime test failed'
assert is_multiply_prime(54) == False
assert is_multiply_prime(77) == False
assert is_multiply_prime(14) == False
assert is_multiply_prime(65) == False
assert is_multiply_prime(48) == False
assert is_multiply_prime(25) == False
assert is_multiply_prime(15) == False, 'Wrong Answer 3'
assert is_multiply_prime(21) == False, 'Wrong Answer 4'
assert is_multiply_prime(9) == False
assert is_multiply_prime(49) == False
assert is_multiply_prime(1) == False
assert is_multiply_prime(39) is False
assert is_multiply_prime(9) is False
assert is_multiply_prime(23) is False
assert is_multiply_prime(55) is False
assert is_multiply_prime(24) is False
assert is_multiply_prime(90) is False
assert is_multiply_prime(81) is False
assert is_multiply_prime(87) is False
assert is_multiply_prime(11) == False, "check is_multiply_prime for 11"
assert is_multiply_prime(35) == False
assert is_multiply_prime(11) is False, "should be False"
assert is_multiply_prime(16) is False, "should be False"
assert is_multiply_prime(25) is False, "should be False"
assert is_multiply_prime(47) is False, "should be False"
assert is_multiply_prime(42)
assert not is_multiply_prime(21)
assert not is_multiply_prime(38)
assert not is_multiply_prime(10)
assert not is_multiply_prime(7)
assert is_multiply_prime(29) == False
assert is_multiply_prime(25) == False, "second test"
assert is_multiply_prime(16) == False, "fourth test"
assert is_multiply_prime(23) == False, "sixth test"
assert is_multiply_prime(41) == False, "seventh test"
assert is_multiply_prime(51) == False, "eighth test"
assert is_multiply_prime(77) == False, "ninth test"
assert is_multiply_prime(24) == False
assert is_multiply_prime(43) == False
assert is_multiply_prime(47) == False
assert is_multiply_prime(53) == False
assert is_multiply_prime(22) is False
assert is_multiply_prime(14) == False, 'is_multiply_prime is not right'
assert is_multiply_prime(25) == False, 'is_multiply_prime is not right'
assert is_multiply_prime(10) == False, 'is_multiply_prime is not right'
assert is_multiply_prime(3) == False
assert is_multiply_prime(77) is False
assert False == is_multiply_prime(15)
assert is_multiply_prime(87) == False
assert is_multiply_prime(15) is False, "Wrong result! 15 is not the multiplication of 3 prime numbers"
assert is_multiply_prime(21) is False, "Wrong result! 21 is not the multiplication of 3 prime numbers"
assert is_multiply_prime(11) is False, "Wrong result! 11 is not the multiplication of 3 prime numbers"
assert is_multiply_prime(1) is False, "Wrong result! 1 is not the multiplication of 3 prime numbers"
assert not is_multiply_prime(15)
assert not is_multiply_prime(37)
assert not is_multiply_prime(49)
assert not is_multiply_prime(60)
assert not is_multiply_prime(4)
assert not is_multiply_prime(11)
assert is_multiply_prime(10) == False  # product of 2, 5
assert is_multiply_prime(49) == False  # product of 7, 7
assert False == is_multiply_prime(6)
assert False == is_multiply_prime(10)
assert False == is_multiply_prime(23)
assert False == is_multiply_prime(80)
assert False == is_multiply_prime(83)
assert False == is_multiply_prime(89)
assert False == is_multiply_prime(93)
assert False == is_multiply_prime(97)
assert is_multiply_prime(16) == False
assert is_multiply_prime(55) == False
assert is_multiply_prime(38) == False
assert not is_multiply_prime(51)
assert is_multiply_prime(93) == False
assert is_multiply_prime(17) is False, "failed on 17"
assert is_multiply_prime(2) is False, "failed on 2"
assert is_multiply_prime(9) is False, "failed on 9"
assert is_multiply_prime(3) is False, "failed on 3"
assert is_multiply_prime(15) is False, "failed on 15"
assert is_multiply_prime(11) is False, "failed on 11"
assert is_multiply_prime(4) is False, "failed on 4"
assert is_multiply_prime(6) is False, "failed on 6"
assert False == is_multiply_prime(13)
assert is_multiply_prime(2*3*7) == True
assert is_multiply_prime(74) == False
assert is_multiply_prime(23) == False
assert not is_multiply_prime(41)
assert not is_multiply_prime(3)
assert is_multiply_prime(70) is True
assert is_multiply_prime(34) is False
assert is_multiply_prime(49) is False, "Failed for 49."
assert is_multiply_prime(16) is False, "Failed for 16."
assert is_multiply_prime(2) is False, "Failed for 2."
assert is_multiply_prime(4) is False, "Failed for 4."
assert is_multiply_prime(5) is False, "Failed for 5."
assert is_multiply_prime(9) is False, "Failed for 9."
assert is_multiply_prime(95) == False
assert is_multiply_prime(19) == False
assert is_multiply_prime(31) == False
assert is_multiply_prime(41) == False
assert is_multiply_prime(61) == False
assert is_multiply_prime(67) == False
assert is_multiply_prime(71) == False
assert is_multiply_prime(73) == False
assert not is_multiply_prime(2)
assert is_multiply_prime(15) is False
assert is_multiply_prime(42) is True
assert is_multiply_prime(64) == False
assert False == is_multiply_prime(11)
assert False == is_multiply_prime(16)
assert is_multiply_prime(36) == False
assert is_multiply_prime(81) == False
assert is_multiply_prime(96) == False
assert is_multiply_prime(29) is False
assert is_multiply_prime(31) is False
assert is_multiply_prime(37) is False
assert is_multiply_prime(41) is False
assert is_multiply_prime(53) is False
assert is_multiply_prime(59) is False
assert is_multiply_prime(61) is False
assert is_multiply_prime(71) is False
assert is_multiply_prime(73) is False
assert is_multiply_prime(30)
