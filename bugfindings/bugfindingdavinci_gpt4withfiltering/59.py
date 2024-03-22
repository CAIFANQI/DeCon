

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k - 1):
            if k % i == 0:
                return False
        return True
    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(n):
            largest = max(largest, j)
    return largest
assert largest_prime_factor(3) == 3
assert largest_prime_factor(6) == 3
assert largest_prime_factor(75) == 5
assert largest_prime_factor(4) == 2
assert largest_prime_factor(5) == 5
assert largest_prime_factor(7) == 7
assert largest_prime_factor(8) == 2
assert largest_prime_factor(9) == 3
assert largest_prime_factor(10) == 5
assert largest_prime_factor(11) == 11
assert largest_prime_factor(12) == 3
assert largest_prime_factor(13) == 13
assert largest_prime_factor(14) == 7
assert largest_prime_factor(15) == 5
assert largest_prime_factor(16) == 2
assert largest_prime_factor(17) == 17
assert largest_prime_factor(18) == 3
assert largest_prime_factor(19) == 19
assert largest_prime_factor(20) == 5
assert largest_prime_factor(21) == 7
assert largest_prime_factor(22) == 11
assert largest_prime_factor(23) == 23
assert largest_prime_factor(24) == 3
assert largest_prime_factor(25) == 5
assert largest_prime_factor(26) == 13
assert largest_prime_factor(41) == 41
assert largest_prime_factor(360) == 5
assert largest_prime_factor(64) == 2
assert largest_prime_factor(4919) == 4919
assert largest_prime_factor(2) == 2
assert largest_prime_factor(100) == 5
assert largest_prime_factor(102) == 17
assert largest_prime_factor(30) == 5
assert largest_prime_factor(60) == 5
assert largest_prime_factor(1000) == 5
assert largest_prime_factor(100000) == 5
assert largest_prime_factor(1453) == 1453
assert largest_prime_factor(3*3*3*3*7*13*13*13) == 13
assert largest_prime_factor(121) == 11
assert largest_prime_factor(122) == 61
assert largest_prime_factor(123) == 41
assert largest_prime_factor(29) == 29
assert largest_prime_factor(31) == 31
assert largest_prime_factor(37) == 37
assert largest_prime_factor(43) == 43
assert largest_prime_factor(47) == 47
assert largest_prime_factor(53) == 53
assert largest_prime_factor(59) == 59
assert largest_prime_factor(61) == 61
assert largest_prime_factor(67) == 67
assert largest_prime_factor(71) == 71
assert largest_prime_factor(73) == 73
assert largest_prime_factor(79) == 79
assert largest_prime_factor(83) == 83
assert largest_prime_factor(89) == 89
assert largest_prime_factor(97) == 97
assert largest_prime_factor(1009) == 1009
assert largest_prime_factor(1009*17) == 1009
assert largest_prime_factor(54) == 3
assert largest_prime_factor(27) == 3
assert largest_prime_factor(3571) == 3571
assert largest_prime_factor(68) == 17
assert largest_prime_factor(48) == 3
assert largest_prime_factor(300) == 5
assert largest_prime_factor(7919) == 7919
assert largest_prime_factor(7919**2) == 7919
assert largest_prime_factor(42) == 7
assert largest_prime_factor(81) == 3
assert largest_prime_factor(101) == 101
assert largest_prime_factor(103) == 103
assert largest_prime_factor(33) == 11
assert largest_prime_factor(45) == 5
assert largest_prime_factor(200) == 5
assert largest_prime_factor(202) == 101
assert largest_prime_factor(1234) == 617
assert largest_prime_factor(13195) == 29
assert largest_prime_factor(40) == 5
assert largest_prime_factor(35) == 7
assert largest_prime_factor(3)
assert largest_prime_factor(15485863) == 15485863
assert largest_prime_factor(80) == 5
assert largest_prime_factor(99) == 11
assert largest_prime_factor(28) == 7
assert largest_prime_factor(32) == 2
assert largest_prime_factor(30013) == 30013
assert largest_prime_factor(96700000)
assert largest_prime_factor(55) == 11
assert largest_prime_factor(5040) == 7
assert largest_prime_factor(2*3*5*7*11*13*17*19) == 19
assert largest_prime_factor(1) == 1
assert largest_prime_factor(971) == 971
assert largest_prime_factor(168) == 7
assert largest_prime_factor(2 * 3 * 5 * 7) == 7
assert largest_prime_factor(2 * 2 * 3 * 3 * 5 * 5 * 7 * 7) == 7
assert largest_prime_factor(2 * 3 * 5 * 7 * 11) == 11
assert largest_prime_factor(2 * 3 * 5 * 7 * 11 * 13) == 13
assert largest_prime_factor(2 * 3 * 5 * 7 * 11 * 13 * 17) == 17
assert largest_prime_factor(2 * 3 * 5 * 7 * 11 * 13 * 17 * 19) == 19
assert largest_prime_factor(2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23) == 23
assert largest_prime_factor(123456789) == 3803
assert largest_prime_factor(50) == 5
assert largest_prime_factor(250) == 5
assert largest_prime_factor(56) == 7
assert largest_prime_factor(169) == 13
assert largest_prime_factor(2018) == 1009
assert largest_prime_factor(60) == 5, "Error 2 in largest_prime_factor"
assert largest_prime_factor(7) == 7, "Error 3 in largest_prime_factor"
assert largest_prime_factor(49) == 7
assert largest_prime_factor(17*101) == 101
assert largest_prime_factor(9999) == 101
assert largest_prime_factor(999999) == 37
assert largest_prime_factor(127) == 127
assert largest_prime_factor(17 * 31) == 31
assert largest_prime_factor(17 * 19 * 23) == 23
assert largest_prime_factor(34) == 17
assert largest_prime_factor(36) == 3
assert largest_prime_factor(72) == 3
assert largest_prime_factor(147) == 7
assert largest_prime_factor(38) == 19
assert largest_prime_factor(111) == 37
assert largest_prime_factor(65) == 13
assert largest_prime_factor(88) == 11
assert largest_prime_factor(125) == 5
assert largest_prime_factor(196) == 7
assert largest_prime_factor(375) == 5
assert largest_prime_factor(567) == 7
assert largest_prime_factor(17*19) == 19
assert largest_prime_factor(28) == 7, "error in largest_prime_factor"
assert largest_prime_factor(2) == 2, "error in largest_prime_factor"
assert largest_prime_factor(7) == 7, "error in largest_prime_factor"
assert largest_prime_factor(1) == 1, "error in largest_prime_factor"
assert largest_prime_factor(12) == 3, "Test failed. Wrong answer."
assert largest_prime_factor(20000) == 5
assert largest_prime_factor(16777216) == 2
assert largest_prime_factor(99991) == 99991
assert largest_prime_factor(10000) == 5
assert largest_prime_factor(128) == 2
assert largest_prime_factor(98) == 7
assert largest_prime_factor(8191) == 8191
assert 3 == largest_prime_factor(18)
assert 5 == largest_prime_factor(25)
assert 19 == largest_prime_factor(19)
assert 5 == largest_prime_factor(100)
assert largest_prime_factor(1000000) == 5
