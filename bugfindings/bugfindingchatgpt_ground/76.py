
def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    if (n == 1): 
        return (x == 1) 
    power = 1
    while (n < x): 
        power = power * n 
    return (power == x) 
assert is_simple_power(4, 2) == True
assert is_simple_power(8, 2) == True
assert is_simple_power(27, 3) == True
assert is_simple_power(16, 2) == True
assert is_simple_power(10, 2) == False
assert is_simple_power(125, 5) == True
assert is_simple_power(3, 2) == False
assert is_simple_power(1, 2) == True
assert is_simple_power(0, 2) == False
assert is_simple_power(9, 3) == True
assert is_simple_power(5, 3) == False
assert is_simple_power(81, 3) == True
assert is_simple_power(100, 10) == True
assert is_simple_power(200, 10) == False
assert is_simple_power(64, 4) == True
assert is_simple_power(1000, 10) == True
assert is_simple_power(9, 2) == False
assert is_simple_power(17, 2) == False
assert is_simple_power(28, 3) == False
assert is_simple_power(82, 3) == False
assert is_simple_power(65, 4) == False
assert is_simple_power(126, 5) == False
assert is_simple_power(1001, 10) == False
assert is_simple_power(256, 2) == True
assert is_simple_power(512, 2) == True
assert is_simple_power(729, 3) == True
assert is_simple_power(25, 3) == False
assert is_simple_power(36, 4) == False
assert is_simple_power(50, 5) == False
assert is_simple_power(100, 3) == False
assert is_simple_power(200, 2) == False
assert is_simple_power(300, 3) == False
assert is_simple_power(400, 4) == False
assert is_simple_power(500, 5) == False
assert is_simple_power(243, 3) == True
assert is_simple_power(16, 4) == True
assert is_simple_power(36, 2) == False
assert is_simple_power(25, 5) == True
assert is_simple_power(36, 6) == True
assert is_simple_power(49, 7) == True
assert is_simple_power(121, 11) == True
assert is_simple_power(144, 12) == True
assert is_simple_power(169, 13) == True
assert is_simple_power(196, 14) == True
assert is_simple_power(225, 15) == True
assert is_simple_power(256, 16) == True
assert is_simple_power(289, 17) == True
assert is_simple_power(324, 18) == True
assert is_simple_power(361, 19) == True
assert is_simple_power(400, 20) == True
assert is_simple_power(441, 21) == True
assert is_simple_power(484, 22) == True
assert is_simple_power(529, 23) == True
assert is_simple_power(576, 24) == True
assert is_simple_power(625, 25) == True
assert is_simple_power(676, 26) == True
assert is_simple_power(729, 27) == True
assert is_simple_power(784, 28) == True
assert is_simple_power(841, 29) == True
assert is_simple_power(900, 30) == True
assert is_simple_power(961, 31) == True
assert is_simple_power(1024, 32) == True
assert is_simple_power(1089, 33) == True
assert is_simple_power(1156, 34) == True
assert is_simple_power(1225, 35) == True
assert is_simple_power(1296, 36) == True
assert is_simple_power(1369, 37) == True
assert is_simple_power(1444, 38) == True
assert is_simple_power(1521, 39) == True
assert is_simple_power(1600, 40) == True
assert is_simple_power(1681, 41) == True
assert is_simple_power(1764, 42) == True
assert is_simple_power(1849, 43) == True
assert is_simple_power(1936, 44) == True
assert is_simple_power(2025, 45) == True
assert is_simple_power(2116, 46) == True
assert is_simple_power(2209, 47) == True
assert is_simple_power(2304, 48) == True
assert is_simple_power(2401, 49) == True
assert is_simple_power(2500, 50) == True
assert is_simple_power(2601, 51) == True
assert is_simple_power(2704, 52) == True
assert is_simple_power(2809, 53) == True
assert is_simple_power(2916, 54) == True
assert is_simple_power(3025, 55) == True
assert is_simple_power(3136, 56) == True
assert is_simple_power(3249, 57) == True
assert is_simple_power(3364, 58) == True
assert is_simple_power(3481, 59) == True
assert is_simple_power(3600, 60) == True
assert is_simple_power(3721, 61) == True
assert is_simple_power(3844, 62) == True
assert is_simple_power(3969, 63) == True
assert is_simple_power(4096, 64) == True
assert is_simple_power(4225, 65) == True
assert is_simple_power(4356, 66) == True
assert is_simple_power(4489, 67) == True
assert is_simple_power(4624, 68) == True
assert is_simple_power(4761, 69) == True
assert is_simple_power(4900, 70) == True
assert is_simple_power(5041, 71) == True
assert is_simple_power(5184, 72) == True
assert is_simple_power(5329, 73) == True
assert is_simple_power(5476, 74) == True
assert is_simple_power(5625, 75) == True
assert is_simple_power(5776, 76) == True
assert is_simple_power(5929, 77) == True
assert is_simple_power(32, 2) == True
assert is_simple_power(128, 2) == True
assert is_simple_power(256, 4) == True
assert is_simple_power(343, 7) == True
assert is_simple_power(1331, 11) == True
assert is_simple_power(4096, 4) == True
assert is_simple_power(4913, 17) == True
assert is_simple_power(10000, 10) == True
assert is_simple_power(14641, 11) == True
assert is_simple_power(32768, 2) == True
assert is_simple_power(59049, 3) == True
assert is_simple_power(100000, 10) == True
assert is_simple_power(161051, 11) == True
assert is_simple_power(262144, 4) == True
assert is_simple_power(531441, 3) == True
assert is_simple_power(1000000, 10) == True
assert is_simple_power(1771561, 11) == True
assert is_simple_power(1048576, 2) == True
assert is_simple_power(4782969, 3) == True
assert is_simple_power(10000000, 10) == True
assert is_simple_power(19487171, 11) == True
assert is_simple_power(4194304, 4) == True
assert is_simple_power(129140163, 3) == True
assert is_simple_power(100000000, 10) == True
assert is_simple_power(16777216, 2) == True
assert is_simple_power(387420489, 3) == True
assert is_simple_power(1000000000, 10) == True
assert is_simple_power(268435456, 4) == True
assert is_simple_power(1162261467, 3) == True
assert is_simple_power(10000000000, 10) == True
assert is_simple_power(4294967296, 2) == True
assert is_simple_power(100000000000, 10) == True
assert is_simple_power(1099511627776, 4) == True
assert is_simple_power(1000000000000, 10) == True
assert is_simple_power(17592186044416, 2) == True
assert is_simple_power(31381059609, 3) == True
assert is_simple_power(10000000000000, 10) == True
assert is_simple_power(134456, 11) == False
assert is_simple_power(27, 3) == True, "Test case 2 failed"
assert is_simple_power(64, 4) == True, "Test case 3 failed"
assert is_simple_power(81, 2) == False, "Test case 4 failed"
assert is_simple_power(10, 2) == False, "Test case 3 failed"
assert is_simple_power(1, 10) == True, "Test case 5 failed"
assert is_simple_power(16, 4) == True, "Test case 3 failed"
assert is_simple_power(10, 2) == False, "Test case 4 failed"
assert is_simple_power(15, 3) == False
assert is_simple_power(20, 4) == False
assert is_simple_power(30, 5) == False
assert is_simple_power(35, 6) == False
assert is_simple_power(40, 7) == False
assert is_simple_power(45, 8) == False
assert is_simple_power(50, 9) == False
assert is_simple_power(55, 10) == False
assert is_simple_power(60, 11) == False
assert is_simple_power(2, 2) == True
assert is_simple_power(33, 2) == False
assert is_simple_power(64, 2) == True
assert is_simple_power(65, 2) == False
assert is_simple_power(129, 2) == False
assert is_simple_power(5, 2) == False
assert is_simple_power(7, 2) == False
assert is_simple_power(10, 3) == False
assert is_simple_power(40, 6) == False
assert is_simple_power(50, 7) == False
assert is_simple_power(60, 8) == False
assert is_simple_power(6, 2) == False
assert is_simple_power(12, 2) == False
assert is_simple_power(14, 3) == False
assert is_simple_power(18, 3) == False
assert is_simple_power(20, 5) == False
assert is_simple_power(22, 5) == False
assert is_simple_power(64, 8) == True
assert is_simple_power(81, 9) == True
assert is_simple_power(8, 3) == False
assert is_simple_power(16, 2) == True, "Error: Test Case 2"
assert is_simple_power(27, 3) == True, "Error: Test Case 3"
assert is_simple_power(81, 3) == True, "Error: Test Case 4"
assert is_simple_power(10, 2) == False, "Error: Test Case 5"
assert is_simple_power(25, 4) == False, "Error: Test Case 6"
assert is_simple_power(0, 2) == False, "Error: Test Case 9"
assert is_simple_power(1, 1) == True, "Error: Test Case 10"
assert is_simple_power(2, 1) == False, "Error: Test Case 11"
assert is_simple_power(80, 3) == False
assert is_simple_power(99, 10) == False
assert is_simple_power(24, 5) == False
assert is_simple_power(63, 4) == False
assert is_simple_power(26, 3) == False
assert is_simple_power(2, 3) == False
assert is_simple_power(2, 2) == True, "Test case 2 failed"
assert is_simple_power(4, 2) == True, "Test case 3 failed"
assert is_simple_power(8, 2) == True, "Test case 4 failed"
assert is_simple_power(9, 2) == False, "Test case 5 failed"
assert is_simple_power(16, 2) == True, "Test case 6 failed"
assert is_simple_power(27, 3) == True, "Test case 7 failed"
assert is_simple_power(64, 4) == True, "Test case 8 failed"
assert is_simple_power(81, 3) == True, "Test case 9 failed"
assert is_simple_power(64, 3) == False
assert is_simple_power(1024, 2) == True
assert is_simple_power(12, 3) == False
assert is_simple_power(30, 4) == False
assert is_simple_power(1023, 2) == False
assert is_simple_power(1000000000000000, 10) == True
assert is_simple_power(1000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000000000000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000000000000000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000000000000000000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000000000000000000000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000000000000000000000000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 10) == True
assert is_simple_power(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 10) == True
assert is_simple_power(1, 1) == True
assert is_simple_power(100, 5) == False
assert is_simple_power(0, 1) == False
assert is_simple_power(25, 2) == False
assert is_simple_power(11, 2) == False
assert is_simple_power(13, 2) == False
assert is_simple_power(14, 2) == False
assert is_simple_power(15, 2) == False
assert is_simple_power(18, 2) == False
assert is_simple_power(19, 2) == False
assert is_simple_power(20, 2) == False
assert is_simple_power(27, 4) == False
assert is_simple_power(81, 4) == False
assert is_simple_power(125, 6) == False
assert is_simple_power(81, 3) == True, "Test case 8 failed"
assert is_simple_power(100, 10) == True, "Test case 9 failed"
assert is_simple_power(1000, 10) == True, "Test case 10 failed"
assert is_simple_power(0, 5) == False
assert is_simple_power(10, 10) == True
assert is_simple_power(36, 3) == False
