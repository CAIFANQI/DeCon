
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
assert hex_key('4C') == 0
assert hex_key('4F') == 0
assert hex_key('6C') == 0
assert hex_key('6F') == 0
assert hex_key('8C') == 0
assert hex_key('8F') == 0
assert hex_key('9C') == 0
assert hex_key('9F') == 0
assert hex_key('A') == 0
assert hex_key('C') == 0
assert hex_key('E') == 0
assert hex_key('F') == 0
assert hex_key('00') == 0
assert hex_key('0A') == 0
assert hex_key('0A0B0C0D0E0F0A') == 2
assert hex_key("")==0
assert hex_key("a") ==0
assert hex_key("b") ==0
assert hex_key("c") ==0
assert hex_key("d") ==0
assert hex_key("e") ==0
assert hex_key("f") ==0
assert hex_key("A10B20C30D40E50F60708B") == 7, "Hex key is not 7"
assert hex_key("A10B20C30D40E50F60708D") == 7, "Hex key is not 7"
assert hex_key("A10B20C30D40E50F607092") == 7, "Hex key is not 7"
assert hex_key('04') == 0
assert hex_key('0E') == 0
assert hex_key('0F') == 0
assert hex_key("") == 0, "A correct hex key should return 0"
assert hex_key("a") == 0
assert hex_key("B") == 1
assert hex_key('a') == 0
assert hex_key('AA') == 0
assert hex_key('') == 0
assert hex_key('1A2B3C4D5') == 5
assert hex_key('1A2B3C4DE5') == 5
assert hex_key('A2B3C4D5') == 5
assert hex_key('000') == 0
assert hex_key("A") ==0
assert hex_key("2") ==1
assert hex_key('3333') == 4
assert hex_key('33BB') == 4
assert hex_key('33B7') == 4
assert hex_key('33DB') == 4
assert hex_key('33D2') == 4
assert hex_key('33D3') == 4
assert hex_key('3355') == 4
assert hex_key('3355A') == 4
assert hex_key('3355C') == 4
assert hex_key('3355E') == 4
assert hex_key('3355F') == 4
assert hex_key('3355G') == 4
assert hex_key('3355H') == 4
assert hex_key('3355I') == 4
assert hex_key('3355J') == 4
assert hex_key("F") == 0 # F has no hexadecimal digit prime (0 counts)
assert hex_key("") == 0 # empty string has 0 hexadecimal digits that are prime
assert hex_key('0123A')==2, '0123A'
assert hex_key('')==0, ''
assert hex_key('FF') == 0
assert hex_key('aa') == 0
assert hex_key('aaa') == 0
assert hex_key("0") ==  0
assert hex_key('1122') == 2
assert hex_key('1233') == 3
assert hex_key('13333') == 4
assert hex_key('13323') == 4
assert hex_key("8A") == 0
assert hex_key("00000") == 0
assert hex_key("000") == 0
assert hex_key("A00") == 0
assert hex_key("") == 0
assert hex_key('123') == 2
assert hex_key("A") == 0
assert hex_key("0C") == 0, "Wrong result"
assert hex_key('0BCAFDC') == 2
