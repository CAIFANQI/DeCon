

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
assert largest_prime_factor(10) == 5
assert largest_prime_factor(21) == 7
assert largest_prime_factor(100) == 5
assert largest_prime_factor(13195) == 29
assert largest_prime_factor(21) == 7, "Test case 2 failed"
assert largest_prime_factor(100) == 5, "Test case 3 failed"
assert largest_prime_factor(13195) == 29, "Test case 4 failed"
assert largest_prime_factor(30) == 5
assert largest_prime_factor(14) == 7
assert largest_prime_factor(21) == 7, "Error: Test Case 2"
assert largest_prime_factor(13195) == 29, "Error: Test Case 3"
assert largest_prime_factor(14) == 7, "Test case 2 failed"
assert largest_prime_factor(21) == 7, "Test case 3 failed"
assert largest_prime_factor(100) == 5, "Test case 4 failed"
assert largest_prime_factor(13195) == 29, "Test case 5 failed"
assert largest_prime_factor(28) == 7, "Test case 4 failed"
assert largest_prime_factor(36) == 3, "Test case 5 failed"
assert largest_prime_factor(14) == 7, 'Test Case 2 Failed'
assert largest_prime_factor(21) == 7, 'Test Case 3 Failed'
assert largest_prime_factor(100) == 5, 'Test Case 4 Failed'
assert largest_prime_factor(15) == 5
assert largest_prime_factor(56) == 7
assert largest_prime_factor(24) == 3, 'Test Case 4 Failed'
assert largest_prime_factor(100) == 5, 'Test Case 5 Failed'
assert largest_prime_factor(56) == 7, "Test case 3 failed"
assert largest_prime_factor(56) == 7, 'Test Case 2 Failed'
assert largest_prime_factor(13195) == 29, 'Test Case 3 Failed'
assert largest_prime_factor(36) == 3, "Test case 4 failed"
assert largest_prime_factor(48) == 3, "Test case 5 failed"
assert largest_prime_factor(10) == 5, "Error: Test Case 2"
assert largest_prime_factor(84) == 7, "Error: Test Case 3"
assert largest_prime_factor(13195) == 29, "Error: Test Case 4"
assert largest_prime_factor(4) == 2, "Error: Test Case 2"
assert largest_prime_factor(9) == 3, "Error: Test Case 3"
assert largest_prime_factor(12) == 3, "Error: Test Case 4"
assert largest_prime_factor(15) == 5, "Error: Test Case 5"
assert largest_prime_factor(21) == 7, "Error: Test Case 6"
assert largest_prime_factor(30) == 5, "Error: Test Case 7"
assert largest_prime_factor(36) == 3, "Error: Test Case 8"
assert largest_prime_factor(45) == 5, "Error: Test Case 9"
assert largest_prime_factor(60) == 5, "Error: Test Case 10"
assert largest_prime_factor(24) == 3, 'Test Case 3 Failed'
assert largest_prime_factor(12) == 3
assert largest_prime_factor(28) == 7
assert largest_prime_factor(36) == 3, 'Test Case 4 Failed'
assert largest_prime_factor(45) == 5, 'Test Case 4 Failed'
assert largest_prime_factor(100) == 5, "Error: Test Case 3"
assert largest_prime_factor(3) == 3
assert largest_prime_factor(4) == 2
assert largest_prime_factor(6) == 3
assert largest_prime_factor(8) == 2
assert largest_prime_factor(9) == 3
assert largest_prime_factor(18) == 3
assert largest_prime_factor(20) == 5
assert largest_prime_factor(22) == 11
assert largest_prime_factor(24) == 3
assert largest_prime_factor(25) == 5
assert largest_prime_factor(26) == 13
assert largest_prime_factor(27) == 3
assert largest_prime_factor(29) == 29
assert largest_prime_factor(32) == 2
assert largest_prime_factor(33) == 11
assert largest_prime_factor(34) == 17
assert largest_prime_factor(35) == 7
assert largest_prime_factor(36) == 3
assert largest_prime_factor(37) == 37
assert largest_prime_factor(38) == 19
assert largest_prime_factor(39) == 13
assert largest_prime_factor(40) == 5
assert largest_prime_factor(42) == 7
assert largest_prime_factor(43) == 43
assert largest_prime_factor(44) == 11
assert largest_prime_factor(45) == 5
assert largest_prime_factor(46) == 23
assert largest_prime_factor(47) == 47
assert largest_prime_factor(48) == 3
assert largest_prime_factor(49) == 7
assert largest_prime_factor(50) == 5
assert largest_prime_factor(51) == 17
assert largest_prime_factor(52) == 13
assert largest_prime_factor(53) == 53
assert largest_prime_factor(54) == 3
assert largest_prime_factor(55) == 11
assert largest_prime_factor(57) == 19
assert largest_prime_factor(58) == 29
assert largest_prime_factor(59) == 59
assert largest_prime_factor(60) == 5
assert largest_prime_factor(61) == 61
assert largest_prime_factor(62) == 31
assert largest_prime_factor(63) == 7
assert largest_prime_factor(64) == 2
assert largest_prime_factor(65) == 13
assert largest_prime_factor(66) == 11
assert largest_prime_factor(67) == 67
assert largest_prime_factor(68) == 17
assert largest_prime_factor(69) == 23
assert largest_prime_factor(70) == 7
assert largest_prime_factor(71) == 71
assert largest_prime_factor(72) == 3
assert largest_prime_factor(73) == 73
assert largest_prime_factor(74) == 37
assert largest_prime_factor(75) == 5
assert largest_prime_factor(76) == 19
assert largest_prime_factor(77) == 11
assert largest_prime_factor(78) == 13
assert largest_prime_factor(79) == 79
assert largest_prime_factor(80) == 5
assert largest_prime_factor(81) == 3
assert largest_prime_factor(82) == 41
assert largest_prime_factor(83) == 83
assert largest_prime_factor(84) == 7
assert largest_prime_factor(85) == 17
assert largest_prime_factor(86) == 43
assert largest_prime_factor(87) == 29
assert largest_prime_factor(88) == 11
assert largest_prime_factor(89) == 89
assert largest_prime_factor(90) == 5
assert largest_prime_factor(91) == 13
assert largest_prime_factor(92) == 23
assert largest_prime_factor(93) == 31
assert largest_prime_factor(94) == 47
assert largest_prime_factor(95) == 19
assert largest_prime_factor(96) == 3
assert largest_prime_factor(97) == 97
assert largest_prime_factor(98) == 7
assert largest_prime_factor(99) == 11
assert largest_prime_factor(15) == 5, "Error: Test Case 2"
assert largest_prime_factor(21) == 7, "Error: Test Case 3"
assert largest_prime_factor(100) == 5, "Error: Test Case 4"
assert largest_prime_factor(13195) == 29, "Error: Test Case 5"
