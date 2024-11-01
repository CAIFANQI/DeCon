
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
assert is_multiply_prime(2) == False
assert is_multiply_prime(3) == False
assert is_multiply_prime(4) == False
assert is_multiply_prime(5) == False
assert is_multiply_prime(6) == False
assert is_multiply_prime(7) == False
assert is_multiply_prime(9) == False
assert is_multiply_prime(10) == False
assert is_multiply_prime(11) == False
assert is_multiply_prime(13) == False
assert is_multiply_prime(14) == False
assert is_multiply_prime(15) == False
assert is_multiply_prime(16) == False
assert is_multiply_prime(17) == False
assert is_multiply_prime(19) == False
assert is_multiply_prime(21) == False
assert is_multiply_prime(22) == False
assert is_multiply_prime(23) == False
assert is_multiply_prime(24) == False
assert is_multiply_prime(25) == False
assert is_multiply_prime(26) == False
assert is_multiply_prime(29) == False
assert is_multiply_prime(31) == False
assert is_multiply_prime(32) == False
assert is_multiply_prime(33) == False
assert is_multiply_prime(34) == False
assert is_multiply_prime(35) == False
assert is_multiply_prime(36) == False
assert is_multiply_prime(37) == False
assert is_multiply_prime(38) == False
assert is_multiply_prime(39) == False
assert is_multiply_prime(40) == False
assert is_multiply_prime(41) == False
assert is_multiply_prime(43) == False
assert is_multiply_prime(46) == False
assert is_multiply_prime(47) == False
assert is_multiply_prime(48) == False
assert is_multiply_prime(49) == False
assert is_multiply_prime(51) == False
assert is_multiply_prime(53) == False
assert is_multiply_prime(54) == False
assert is_multiply_prime(55) == False
assert is_multiply_prime(56) == False
assert is_multiply_prime(57) == False
assert is_multiply_prime(58) == False
assert is_multiply_prime(59) == False
assert is_multiply_prime(61) == False
assert is_multiply_prime(62) == False
assert is_multiply_prime(64) == False
assert is_multiply_prime(65) == False
assert is_multiply_prime(67) == False
assert is_multiply_prime(69) == False
assert is_multiply_prime(71) == False
assert is_multiply_prime(72) == False
assert is_multiply_prime(73) == False
assert is_multiply_prime(74) == False
assert is_multiply_prime(77) == False
assert is_multiply_prime(79) == False
assert is_multiply_prime(80) == False
assert is_multiply_prime(81) == False
assert is_multiply_prime(82) == False
assert is_multiply_prime(83) == False
assert is_multiply_prime(84) == False
assert is_multiply_prime(85) == False
assert is_multiply_prime(86) == False
assert is_multiply_prime(87) == False
assert is_multiply_prime(88) == False
assert is_multiply_prime(89) == False
assert is_multiply_prime(91) == False
assert is_multiply_prime(93) == False
assert is_multiply_prime(94) == False
assert is_multiply_prime(95) == False
assert is_multiply_prime(96) == False
assert is_multiply_prime(97) == False
assert is_multiply_prime(3) == False, 'Test Case 2 Failed'
assert is_multiply_prime(4) == False, 'Test Case 3 Failed'
assert is_multiply_prime(5) == False, 'Test Case 4 Failed'
assert is_multiply_prime(6) == False, 'Test Case 5 Failed'
assert is_multiply_prime(7) == False, 'Test Case 6 Failed'
assert is_multiply_prime(9) == False, 'Test Case 8 Failed'
assert is_multiply_prime(10) == False, 'Test Case 9 Failed'
assert is_multiply_prime(11) == False, 'Test Case 10 Failed'
assert is_multiply_prime(13) == False, 'Test Case 12 Failed'
assert is_multiply_prime(14) == False, 'Test Case 13 Failed'
assert is_multiply_prime(15) == False, 'Test Case 14 Failed'
assert is_multiply_prime(16) == False, 'Test Case 15 Failed'
assert is_multiply_prime(17) == False, 'Test Case 16 Failed'
assert is_multiply_prime(19) == False, 'Test Case 18 Failed'
assert is_multiply_prime(21) == False, 'Test Case 20 Failed'
assert is_multiply_prime(22) == False, 'Test Case 21 Failed'
assert is_multiply_prime(23) == False, 'Test Case 22 Failed'
assert is_multiply_prime(24) == False, 'Test Case 23 Failed'
assert is_multiply_prime(25) == False, 'Test Case 24 Failed'
assert is_multiply_prime(26) == False, 'Test Case 25 Failed'
assert is_multiply_prime(29) == False, 'Test Case 28 Failed'
assert is_multiply_prime(31) == False, 'Test Case 30 Failed'
assert is_multiply_prime(32) == False, 'Test Case 31 Failed'
assert is_multiply_prime(33) == False, 'Test Case 32 Failed'
assert is_multiply_prime(34) == False, 'Test Case 33 Failed'
assert is_multiply_prime(35) == False, 'Test Case 34 Failed'
assert is_multiply_prime(36) == False, 'Test Case 35 Failed'
assert is_multiply_prime(37) == False, 'Test Case 36 Failed'
assert is_multiply_prime(38) == False, 'Test Case 37 Failed'
assert is_multiply_prime(39) == False, 'Test Case 38 Failed'
assert is_multiply_prime(40) == False, 'Test Case 39 Failed'
assert is_multiply_prime(41) == False, 'Test Case 40 Failed'
assert is_multiply_prime(43) == False, 'Test Case 42 Failed'
assert is_multiply_prime(46) == False, 'Test Case 45 Failed'
assert is_multiply_prime(47) == False, 'Test Case 46 Failed'
assert is_multiply_prime(48) == False, 'Test Case 47 Failed'
assert is_multiply_prime(49) == False, 'Test Case 48 Failed'
assert is_multiply_prime(51) == False, 'Test Case 50 Failed'
assert is_multiply_prime(53) == False, 'Test Case 52 Failed'
assert is_multiply_prime(54) == False, 'Test Case 53 Failed'
assert is_multiply_prime(55) == False, 'Test Case 54 Failed'
assert is_multiply_prime(56) == False, 'Test Case 55 Failed'
assert is_multiply_prime(57) == False, 'Test Case 56 Failed'
assert is_multiply_prime(58) == False, 'Test Case 57 Failed'
assert is_multiply_prime(59) == False, 'Test Case 58 Failed'
assert is_multiply_prime(61) == False, 'Test Case 60 Failed'
assert is_multiply_prime(5) == False, 'Test Case 3 Failed'
assert is_multiply_prime(7) == False, 'Test Case 4 Failed'
assert is_multiply_prime(11) == False, 'Test Case 5 Failed'
assert is_multiply_prime(13) == False, 'Test Case 6 Failed'
assert is_multiply_prime(17) == False, 'Test Case 7 Failed'
assert is_multiply_prime(19) == False, 'Test Case 8 Failed'
assert is_multiply_prime(23) == False, 'Test Case 9 Failed'
assert is_multiply_prime(29) == False, 'Test Case 10 Failed'
assert is_multiply_prime(31) == False, 'Test Case 11 Failed'
assert is_multiply_prime(37) == False, 'Test Case 12 Failed'
assert is_multiply_prime(41) == False, 'Test Case 13 Failed'
assert is_multiply_prime(43) == False, 'Test Case 14 Failed'
assert is_multiply_prime(47) == False, 'Test Case 15 Failed'
assert is_multiply_prime(53) == False, 'Test Case 16 Failed'
assert is_multiply_prime(59) == False, 'Test Case 17 Failed'
assert is_multiply_prime(61) == False, 'Test Case 18 Failed'
assert is_multiply_prime(67) == False, 'Test Case 19 Failed'
assert is_multiply_prime(71) == False, 'Test Case 20 Failed'
assert is_multiply_prime(73) == False, 'Test Case 21 Failed'
assert is_multiply_prime(79) == False, 'Test Case 22 Failed'
assert is_multiply_prime(83) == False, 'Test Case 23 Failed'
assert is_multiply_prime(89) == False, 'Test Case 24 Failed'
assert is_multiply_prime(97) == False, 'Test Case 25 Failed'
assert is_multiply_prime(4) == False, 'Test Case 26 Failed'
assert is_multiply_prime(6) == False, 'Test Case 27 Failed'
assert is_multiply_prime(9) == False, 'Test Case 29 Failed'
assert is_multiply_prime(10) == False, 'Test Case 30 Failed'
assert is_multiply_prime(14) == False, 'Test Case 32 Failed'
assert is_multiply_prime(15) == False, 'Test Case 33 Failed'
assert is_multiply_prime(16) == False, 'Test Case 34 Failed'
assert is_multiply_prime(21) == False, 'Test Case 37 Failed'
assert is_multiply_prime(22) == False, 'Test Case 38 Failed'
assert is_multiply_prime(24) == False, 'Test Case 39 Failed'
assert is_multiply_prime(25) == False, 'Test Case 40 Failed'
assert is_multiply_prime(26) == False, 'Test Case 41 Failed'
assert is_multiply_prime(32) == False, 'Test Case 45 Failed'
assert is_multiply_prime(33) == False, 'Test Case 46 Failed'
assert is_multiply_prime(34) == False, 'Test Case 47 Failed'
assert is_multiply_prime(35) == False, 'Test Case 48 Failed'
assert is_multiply_prime(36) == False, 'Test Case 49 Failed'
assert is_multiply_prime(38) == False, 'Test Case 50 Failed'
assert is_multiply_prime(39) == False, 'Test Case 51 Failed'
assert is_multiply_prime(40) == False, 'Test Case 52 Failed'
assert is_multiply_prime(46) == False, 'Test Case 56 Failed'
assert is_multiply_prime(48) == False, 'Test Case 57 Failed'
assert is_multiply_prime(49) == False, 'Test Case 58 Failed'
assert is_multiply_prime(51) == False, 'Test Case 60 Failed'
assert is_multiply_prime(3) == False, "Error: Test Case 2"
assert is_multiply_prime(4) == False, "Error: Test Case 3"
assert is_multiply_prime(5) == False, "Error: Test Case 4"
assert is_multiply_prime(6) == False, "Error: Test Case 5"
assert is_multiply_prime(7) == False, "Error: Test Case 6"
assert is_multiply_prime(9) == False, "Error: Test Case 8"
assert is_multiply_prime(10) == False, "Error: Test Case 9"
assert is_multiply_prime(11) == False, "Error: Test Case 10"
assert is_multiply_prime(13) == False, "Error: Test Case 12"
assert is_multiply_prime(14) == False, "Error: Test Case 13"
assert is_multiply_prime(15) == False, "Error: Test Case 14"
assert is_multiply_prime(16) == False, "Error: Test Case 15"
assert is_multiply_prime(17) == False, "Error: Test Case 16"
assert is_multiply_prime(19) == False, "Error: Test Case 18"
assert is_multiply_prime(21) == False, "Error: Test Case 20"
assert is_multiply_prime(22) == False, "Error: Test Case 21"
assert is_multiply_prime(23) == False, "Error: Test Case 22"
assert is_multiply_prime(24) == False, "Error: Test Case 23"
assert is_multiply_prime(25) == False, "Error: Test Case 24"
assert is_multiply_prime(26) == False, "Error: Test Case 25"
assert is_multiply_prime(29) == False, "Error: Test Case 28"
assert is_multiply_prime(31) == False, "Error: Test Case 30"
assert is_multiply_prime(32) == False, "Error: Test Case 31"
assert is_multiply_prime(33) == False, "Error: Test Case 32"
assert is_multiply_prime(34) == False, "Error: Test Case 33"
assert is_multiply_prime(35) == False, "Error: Test Case 34"
assert is_multiply_prime(36) == False, "Error: Test Case 35"
assert is_multiply_prime(37) == False, "Error: Test Case 36"
assert is_multiply_prime(38) == False, "Error: Test Case 37"
assert is_multiply_prime(39) == False, "Error: Test Case 38"
assert is_multiply_prime(40) == False, "Error: Test Case 39"
assert is_multiply_prime(41) == False, "Error: Test Case 40"
assert is_multiply_prime(43) == False, "Error: Test Case 42"
assert is_multiply_prime(46) == False, "Error: Test Case 45"
assert is_multiply_prime(47) == False, "Error: Test Case 46"
assert is_multiply_prime(48) == False, "Error: Test Case 47"
assert is_multiply_prime(49) == False, "Error: Test Case 48"
assert is_multiply_prime(51) == False, "Error: Test Case 50"
assert is_multiply_prime(53) == False, "Error: Test Case 52"
assert is_multiply_prime(54) == False, "Error: Test Case 53"
assert is_multiply_prime(55) == False, "Error: Test Case 54"
assert is_multiply_prime(56) == False, "Error: Test Case 55"
assert is_multiply_prime(57) == False, "Error: Test Case 56"
assert is_multiply_prime(30) == True
assert is_multiply_prime(2*3*5) == True
assert is_multiply_prime(2*3*4) == False
assert is_multiply_prime(2*3*6) == False
assert is_multiply_prime(2*3*8) == False
assert is_multiply_prime(2*3*9) == False
assert is_multiply_prime(2*3*12) == False
assert is_multiply_prime(2*3*14) == False
assert is_multiply_prime(2*3*16) == False
assert is_multiply_prime(10) == False, 'Test Case 3 Failed'
assert is_multiply_prime(30) == True, 'Test Case 4 Failed'
assert is_multiply_prime(15) == False, 'Test Case 5 Failed'
assert is_multiply_prime(15) == False, "Error: Test Case 3"
assert is_multiply_prime(30) == True, "Error: Test Case 4"
assert is_multiply_prime(35) == False, "Error: Test Case 5"
