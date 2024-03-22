
def hex_key(num):
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a natural number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    Examples:
    For num = "AB" the output should be 1.
    For num = "1077E" the output should be 2.
    For num = "ABED1A33" the output should be 4.
    For num = "123456789ABCDEF0" the output should be 6.
    For num = "2020" the output should be 2.
    """
    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 1
    for i in range(0, len(num)):
        if num[i] in primes:
            total += 1
    return total
assert hex_key("B") == 1
assert hex_key('AABBCC') == 2
assert hex_key("0") == 0
assert hex_key("A") == 0
assert hex_key("10") == 0
assert hex_key("F") == 0
assert hex_key("D") == 1
assert hex_key("15") == 1
assert hex_key("FF") == 0
assert hex_key("A123456") == 3
assert hex_key('') == 0, 'Empty string!'
assert hex_key('') == 0
assert hex_key('F') == 0
assert hex_key('C') == 0
assert hex_key('D') == 1
assert hex_key('B') == 1
assert hex_key('E') == 0
assert hex_key('A') == 0
assert 	hex_key('A') == 0, 'wrong result for A'
assert 	hex_key('FEDC') == 1, 'wrong result for FEDC'
assert hex_key("A") == 0, "A should be 0"
assert hex_key("") == 0, "Empty string should be 0"
assert hex_key("A1") == 0, "A1 should be 0"
assert 	hex_key('F6') == 0
assert 	hex_key('F9') == 0
assert 	hex_key('FA') == 0
assert 	hex_key('FC') == 0
assert 	hex_key('FE') == 0
assert 	hex_key('FF') == 0
assert 	hex_key("B2F2D") == 4
assert 	hex_key("") == 0
assert 	hex_key("C6") == 0
assert 	hex_key("CAFF") == 0
