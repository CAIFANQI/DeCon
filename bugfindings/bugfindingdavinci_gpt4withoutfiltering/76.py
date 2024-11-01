
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
assert is_simple_power(12, 2) is False
assert is_simple_power(18, 3) is False
assert is_simple_power(33, 3) is False
assert is_simple_power(10, 3) is False
assert is_simple_power(20, 1) is False
assert is_simple_power(1, 1) == True
assert is_simple_power(5, 3) == False
assert is_simple_power(12, 3) == False
assert is_simple_power(300, 2) == False
assert is_simple_power(256, 3) == False
assert is_simple_power(32, 5) == False
assert is_simple_power(2, 3) == False
assert is_simple_power(3, 2) == False
assert is_simple_power(28, 2) == False
assert is_simple_power(16, 5) == False
assert is_simple_power(65, 2) == False
assert is_simple_power(64, 3) == False
assert is_simple_power(256, 5) == False
assert is_simple_power(1.000001, 1) == False
assert is_simple_power(7, 3) == False
assert is_simple_power(3, 7) == False
assert is_simple_power(100, 2) == False
assert is_simple_power(10000, 1000000) == False
assert is_simple_power(0.1, 1000000) == False
assert is_simple_power(2, 1.000001) == False
assert is_simple_power(12, 2) == False
assert is_simple_power(18, 3) == False
assert is_simple_power(7, 2) is False
assert is_simple_power(2 ** 11 + 1, 2) is False
assert is_simple_power(1025, 2) == False
assert is_simple_power(100, 5) == False
assert is_simple_power(26, 2) == False
assert is_simple_power(8, 3) == False
assert is_simple_power(2, 1) == False
assert is_simple_power(10, 2) == False
assert is_simple_power(48, 4) == False
assert is_simple_power(60, 6) == False
assert is_simple_power(5, 2) is False
assert is_simple_power(5, 1) is False
assert is_simple_power(1, 1) is True
assert is_simple_power(3, 2) is False
assert is_simple_power(1000, 2) is False
assert is_simple_power(1000, 1) is False
assert is_simple_power(5, 2) == False
assert is_simple_power(250, 10) == False
assert is_simple_power(15, 2) == False
assert is_simple_power(126, 3) == False
assert is_simple_power(42, 2) == False
assert is_simple_power(10, 3) == False
assert False == is_simple_power(4, 3)
assert False == is_simple_power(100, 8)
assert True == is_simple_power(1, 1)
assert is_simple_power(28, 3) == False
assert is_simple_power(7, 2) == False
assert is_simple_power(1000, 100) == False
assert is_simple_power(4, 3) is False
assert is_simple_power(5, 125) is False
assert is_simple_power(0, 2) is False
assert is_simple_power(0, 1) is False
assert is_simple_power(50, 2) == False
assert is_simple_power(50, 5) == False
assert not is_simple_power(2, 3)
assert not is_simple_power(3, 2)
assert is_simple_power(1, 1)
assert not is_simple_power(5, 2)
assert not is_simple_power(4, 3)
assert is_simple_power(5832, 2) == False
assert is_simple_power(17, 2) == False
assert is_simple_power(23, 2) == False
assert is_simple_power(126, 5) == False
assert is_simple_power(6, 2) == False
assert is_simple_power(29, 2) == False
assert is_simple_power(26, 3) == False
assert is_simple_power(243, 5) == False
assert is_simple_power(10, 4) is False
assert is_simple_power(8,3) == False
assert is_simple_power(16, 3) == False
assert is_simple_power(256, 10) == False
assert is_simple_power(77, 7) == False
assert is_simple_power(0, 2) == False
assert is_simple_power(1, 5**0) == True
assert is_simple_power(81, 4) is False
assert is_simple_power(9, 4) is False
assert is_simple_power(8,4) == False
assert is_simple_power(4,8) == False
assert is_simple_power(9,4) == False
assert is_simple_power(0,3) == False
assert is_simple_power(100,2) == False
assert is_simple_power(10,100) == False
assert is_simple_power(1,1) == True
assert is_simple_power(0,1) == False
assert is_simple_power(9, 2) == False
assert is_simple_power(17, 3) == False
assert is_simple_power(35, 7) == False
assert is_simple_power(2024, 2) == False
assert is_simple_power(28, 2) is False
assert is_simple_power(42, 3) == False
assert is_simple_power(9, 2) is False
assert is_simple_power(13, 2) is False
assert is_simple_power(100, 5) is False
assert is_simple_power(100, 2) is False
assert is_simple_power(0, 10) is False
assert is_simple_power(2, 10) == False
assert is_simple_power(100, 4) == False
assert is_simple_power(12354, 2) == False
assert is_simple_power(128, 3) == False
assert is_simple_power(256, 8) == False
assert is_simple_power(30, 4) == False
assert is_simple_power(0, 1) == False
assert is_simple_power(1000, 2) == False
assert is_simple_power(27, 4) == False
assert is_simple_power(999998000002, 1) == False
assert is_simple_power(8, 3) is False
assert is_simple_power(17, 2) is False
assert is_simple_power(4, 1) is False
assert is_simple_power(6, 2) is False
assert is_simple_power(6, 1) is False
assert is_simple_power(9, 1) is False
assert is_simple_power(31, 2) == False
assert is_simple_power(4, 3) == False
assert is_simple_power(5, 3) is False
assert is_simple_power(10, 2) is False
assert is_simple_power(10, 1) is False
assert is_simple_power(100, 20) == False
assert is_simple_power(100, 3) == False
assert is_simple_power(256, 7) == False
assert is_simple_power(31, 3) == False
assert is_simple_power(22, 3) == False
assert is_simple_power(1000, 20) == False
assert is_simple_power(10, 20) == False
assert is_simple_power(100, 1000) == False
assert is_simple_power(3, 5) == False
assert is_simple_power(18, 2) == False
assert is_simple_power(1024, 3) == False
assert is_simple_power(10, 4) == False
assert is_simple_power(15, 4) == False
assert is_simple_power(17, 4) == False
assert is_simple_power(19, 4) == False
assert is_simple_power(257, 4) == False
assert is_simple_power(3, 4) == False
assert is_simple_power(9, 4) == False
assert is_simple_power(34, 2) == False
assert is_simple_power(99, 3) == False
assert is_simple_power(82, 3) == False
assert is_simple_power(10001, 100) == False
assert is_simple_power(10001, 101) == False
assert is_simple_power(24, 2) == False
assert is_simple_power(216, 7) == False
assert is_simple_power(0, 0.5) == False
assert is_simple_power(75, 3) is False
assert is_simple_power(32, 4) is False
assert is_simple_power(32, 8) is False
assert is_simple_power(100, 1) is False
assert is_simple_power(100, 3) is False
assert is_simple_power(100, 4) is False
assert is_simple_power(100, 6) is False
assert is_simple_power(100, 7) is False
assert is_simple_power(100, 8) is False
assert is_simple_power(100, 9) is False
assert is_simple_power(11, 10) is False
assert is_simple_power(100001, 10) is False
assert is_simple_power(5, 1) == False
assert is_simple_power(124, 2) == False
assert is_simple_power(666, 6) == False
assert is_simple_power(12321, 2) == False
assert is_simple_power(5,2) == False
assert is_simple_power(5,10) == False
assert is_simple_power(5,5.5) == False
assert is_simple_power(8, 4) is False
assert is_simple_power(15, 3) == False
assert is_simple_power(24, 3) == False
assert is_simple_power(27, 4) is False
assert is_simple_power(256, 8) is False
assert is_simple_power(4096, 256) is False
assert is_simple_power(4096, 1024) is False
assert is_simple_power(85766121, 4) is False
assert is_simple_power(85766121, 8) is False
assert is_simple_power(14, 3) is False
assert is_simple_power(2,64) == False
assert is_simple_power(16,3) == False
assert is_simple_power(17,2) == False
assert is_simple_power(81, 2) == False
assert is_simple_power(78, 2) == False
assert is_simple_power(1024, 10) == False
assert is_simple_power(32, 1) is False
assert is_simple_power(14, 7) == False
assert is_simple_power(11, 3) == False
assert is_simple_power(16, 3) is False
assert is_simple_power(8, 4) == False
assert is_simple_power(24, 6) == False
assert is_simple_power(25, 2) == False
assert is_simple_power(2, 1) is False
assert is_simple_power(2, 3) is False
assert is_simple_power(12, 4) is False
assert is_simple_power(500, 10) == False
