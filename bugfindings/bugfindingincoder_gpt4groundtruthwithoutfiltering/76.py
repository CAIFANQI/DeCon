
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
assert is_simple_power(3, 2) == False
assert is_simple_power(3, 4) == False
assert is_simple_power(3, 6) == False
assert is_simple_power(3, 8) == False
assert is_simple_power(3, 10) == False
assert is_simple_power(3, 12) == False
assert is_simple_power(3, 14) == False
assert is_simple_power(3, 16) == False
assert is_simple_power(3, 18) == False
assert is_simple_power(3, 20) == False
assert is_simple_power(3, 22) == False
assert is_simple_power(3, 24) == False
assert is_simple_power(3, 26) == False
assert is_simple_power(3, 28) == False
assert is_simple_power(3, 30) == False
assert is_simple_power(3, 32) == False
assert is_simple_power(2, 4) == False
assert is_simple_power(2, 6) == False
assert is_simple_power(2,1) == False
assert is_simple_power(2,5) == False
assert is_simple_power(3,2) == False
assert is_simple_power(3,5) == False
assert is_simple_power(7, 10) == False
assert is_simple_power(0, 10) == False
assert is_simple_power(4, 10) == False
assert is_simple_power(1, 1) == True
assert is_simple_power(27, 2) == False
assert is_simple_power(33, 2) == False
assert is_simple_power(4, 3) == False
assert is_simple_power(8, 3) == False
assert is_simple_power(13, 3) == False
assert is_simple_power(16, 3) == False
assert is_simple_power(28, 3) == False
assert is_simple_power(33, 3) == False
assert is_simple_power(34, 3) == False
assert is_simple_power(8, 4) == False
assert is_simple_power(13, 4) == False
assert is_simple_power(27, 4) == False
assert is_simple_power(28, 4) == False
assert is_simple_power(33, 4) == False
assert is_simple_power(34, 4) == False
assert is_simple_power(4, 5) == False
assert is_simple_power(8, 5) == False
assert is_simple_power(13, 5) == False
assert is_simple_power(16, 5) == False
assert is_simple_power(27, 5) == False
assert is_simple_power(28, 5) == False
assert is_simple_power(33, 5) == False
assert is_simple_power(34, 5) == False
assert is_simple_power(5, 3) == False
assert is_simple_power(100, 101) == False
assert is_simple_power(25, 4) == False
assert is_simple_power(25, 6) == False
assert is_simple_power(25, 8) == False
assert is_simple_power(25, 10) == False
assert is_simple_power(25, 12) == False
assert is_simple_power(25, 14) == False
assert is_simple_power(25, 16) == False
assert is_simple_power(25, 18) == False
assert is_simple_power(25, 20) == False
assert is_simple_power(25, 22) == False
assert is_simple_power(25, 24) == False
assert is_simple_power(25, 26) == False
assert is_simple_power(25, 28) == False
assert is_simple_power(25, 30) == False
assert is_simple_power(5, 4) == False
assert is_simple_power(6, 1) == False
assert is_simple_power(6, 3) == False
assert is_simple_power(25 + 25, 5) == False
assert is_simple_power(25 - 25, 5) == False
assert is_simple_power(25 + 25, 6) == False
assert is_simple_power(25 - 25, 6) == False
assert is_simple_power(25 * 25, 6) == False
assert is_simple_power(7, 1) == False
assert is_simple_power(4, 1) == False
assert is_simple_power(6, 2) == False
assert is_simple_power(7, 3) == False
assert is_simple_power(3, 1) == False
assert is_simple_power(8, 6) == False
assert is_simple_power(8, 7) == False
assert is_simple_power(2, 3) == False
assert is_simple_power(100, 3) == False
assert is_simple_power(100, 5) == False
assert is_simple_power(100, 8) == False
assert is_simple_power(100, 9) == False
assert is_simple_power(1000, 3) == False
assert is_simple_power(1000, 8) == False
assert is_simple_power(1000, 9) == False
assert is_simple_power(10000, 3) == False
assert is_simple_power(10000, 8) == False
assert not is_simple_power(2, 3)
assert not is_simple_power(4, 3)
assert not is_simple_power(4, 1)
assert not is_simple_power(4, 5)
assert not is_simple_power(4, 6)
assert not is_simple_power(4, 7)
assert not is_simple_power(4, 8)
assert not is_simple_power(4, 9)
assert not is_simple_power(4, 10)
assert not is_simple_power(4, 11)
assert not is_simple_power(4, 12)
assert not is_simple_power(4, 13)
assert is_simple_power(2, 1) == False
assert is_simple_power(10, 1) == False
assert is_simple_power(1000000, 1) == False
assert is_simple_power(10000000, 1) == False
assert is_simple_power(100000000, 1) == False
assert is_simple_power(1000000000, 1) == False
assert is_simple_power(10, 4) == False
assert is_simple_power(10, 5) == False
assert is_simple_power(10, 6) == False
assert is_simple_power(10, 7) == False
assert is_simple_power(2, 5) == False
assert is_simple_power(2, 7) == False
assert is_simple_power(2, 9) == False
assert is_simple_power(15, 4) == False
assert is_simple_power(0, 4) == False
assert is_simple_power(10, 3) == False
assert is_simple_power(11, 3) == False
assert is_simple_power(12, 3) == False
assert is_simple_power(3, 5) == False
assert is_simple_power(5, 1) == False
assert is_simple_power(5, 6) == False
assert is_simple_power(5, 7) == False
assert is_simple_power(6, 5) == False
assert is_simple_power(7, 5) == False
assert is_simple_power(8, 1) == False
assert is_simple_power(9, 5) == False
assert is_simple_power(11, 1) == False
assert is_simple_power(11, 5) == False
assert is_simple_power(12, 1) == False
assert is_simple_power(12, 5) == False
assert is_simple_power(12, 7) == False
assert is_simple_power(9, 6) == False
assert is_simple_power(9, 7) == False
assert is_simple_power(9, 8) == False
assert is_simple_power(9, 11) == False
assert is_simple_power(9, 12) == False
assert is_simple_power(12, 9) == False
assert is_simple_power(12, 10) == False
assert is_simple_power(20, 9) == False
assert is_simple_power(20, 10) == False
assert is_simple_power(10, 30) == False
assert is_simple_power(10, 50) == False
assert is_simple_power(10, 70) == False
assert is_simple_power(10, 90) == False
assert is_simple_power(10, 1000) == False
assert is_simple_power(10, 1000000) == False
assert is_simple_power(-2, 1) == False
assert is_simple_power(17, 2) == False
assert is_simple_power(4294967295, 2) == False
assert is_simple_power(4294967297, 2) == False
assert is_simple_power(4294967298, 2) == False
assert is_simple_power(9, 1) == False
assert is_simple_power(10, 2) == False
assert is_simple_power(11, 2) == False
assert is_simple_power(12, 2) == False
assert is_simple_power(13, 2) == False
assert is_simple_power(13, 1) == False
assert is_simple_power(10, 8) == False
assert is_simple_power(10, 11) == False
assert is_simple_power(25, 11) == False
assert is_simple_power(10, 9) == False
assert is_simple_power(11, 9) == False
assert is_simple_power(11, 10) == False
assert is_simple_power(12, 11) == False
assert is_simple_power(20, 15) == False
assert is_simple_power(21, 15) == False
assert is_simple_power(22, 15) == False
assert is_simple_power(23, 15) == False
assert is_simple_power(23, 14) == False
assert is_simple_power(15, 20) == False
assert is_simple_power(15, 21) == False
assert is_simple_power(15, 22) == False
assert not is_simple_power(5, 2)
assert not is_simple_power(5, 1)
assert is_simple_power(7, 2) == False
assert is_simple_power(2, 8) == False
assert is_simple_power(3, 9) == False
assert is_simple_power(4, 8) == False
assert is_simple_power(5, 8) == False
assert is_simple_power(6, 8) == False
assert is_simple_power(7, 8) == False
assert is_simple_power(11, 8) == False
assert is_simple_power(4, 6) == False
assert is_simple_power(5, 9) == False
assert is_simple_power(16, 10) == False
assert is_simple_power(16, 11) == False
assert is_simple_power(16, 12) == False
assert is_simple_power(8, 13) == False
assert is_simple_power(10, 14) == False
assert is_simple_power(20, 16) == False
assert is_simple_power(30, 17) == False
assert is_simple_power(100, 20) == False
assert is_simple_power(100, 21) == False
assert is_simple_power(200, 21) == False
assert is_simple_power(1000, 21) == False
assert is_simple_power(10000, 23) == False
assert is_simple_power(4, 9) == False
assert is_simple_power(9, 4) == False
assert is_simple_power(7, 9) == False
assert not is_simple_power(2, 1)
assert not is_simple_power(2**10, 100)
assert not is_simple_power(2**10, 10)
assert not is_simple_power(2**10, 3)
assert is_simple_power(6, 4) == False
assert is_simple_power(0, 5) == False
assert is_simple_power(16, 6) == False
assert is_simple_power(6, 7) == False
assert is_simple_power(100, 2) == False
assert is_simple_power(0, 1) == False
assert is_simple_power(16, 5) is False
assert is_simple_power(21, 1) == False
assert is_simple_power(31, 3) == False
assert is_simple_power(12, 4) == False
assert is_simple_power(17, 5) == False
assert is_simple_power(0, 3) == False
assert is_simple_power(11, 4) == False
assert is_simple_power(14, 3) == False
assert is_simple_power(15, 3) == False
assert is_simple_power(2, 10) == False
assert is_simple_power(7, 6) == False
assert is_simple_power(16, 1) == False
assert is_simple_power(15, 2) == False
assert is_simple_power(23, 2) == False
assert is_simple_power(101, 2) == False
assert not is_simple_power(0, 2)
assert not is_simple_power(15, 5)
assert not is_simple_power(15, 6)
assert not is_simple_power(9, 4)
assert is_simple_power(17, 3) == False
assert is_simple_power(0, 6) == False
assert is_simple_power(0, 8) == False
assert is_simple_power(5, 2) == False
assert not is_simple_power(3, 4)
assert not is_simple_power(5, 4)
assert is_simple_power(2, 200000) == False
assert is_simple_power(3, 7) == False
assert is_simple_power(5, 3) == 0
assert is_simple_power(5, 10) == False
assert not is_simple_power(5, 3)
assert not is_simple_power(7, 3)
assert not is_simple_power(7, 2)
assert not is_simple_power(7, 4)
assert is_simple_power(14, 2) == False
assert is_simple_power(256, 31) == False
assert is_simple_power(25, 7) == False
assert is_simple_power(25, 2) == False
