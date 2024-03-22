
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
assert hex_key("") == 0
assert hex_key("B") == 1
assert hex_key("5") == 1
assert hex_key("1B8A7F") == 2
assert hex_key("D87A87A8") == 3
assert hex_key("13") == 1
assert hex_key("3A7") == 2
assert hex_key("0") == 0
assert hex_key("1A") == 0
assert hex_key("7D5A") == 3
assert hex_key('3a8b') == 1
assert hex_key('a2F2') == 2
assert hex_key('00') == 0
assert hex_key('03') == 1
assert hex_key('13') == 1
assert hex_key('15') == 1
assert hex_key('17') == 1
assert hex_key('3F') == 1
assert hex_key("0F0F0F") == 0
assert hex_key("1F0F0F") == 0
assert hex_key("2F0F0F") == 1
assert hex_key("3F0F0F") == 1
assert hex_key("4F0F0F") == 0
assert hex_key("5F0F0F") == 1
assert hex_key("6F0F0F") == 0
assert hex_key("7F0F0F") == 1
assert hex_key("8F0F0F") == 0
assert hex_key("9F0F0F") == 0
assert hex_key("BF0F0F") == 1
assert hex_key("CF0F0F") == 0
assert hex_key("DF0F0F") == 1
assert hex_key("7B") == 2
assert hex_key("FFFF") == 0
assert hex_key("FFF") == 0
assert hex_key("13D") == 2
assert hex_key("A3") == 1
assert hex_key("1") == 0
assert hex_key("2") == 1
assert hex_key("9") == 0
assert hex_key("C") == 0
assert hex_key("F") == 0
assert hex_key('04') == 0
assert hex_key('05') == 1
assert hex_key('06') == 0
assert hex_key('07') == 1
assert hex_key('08') == 0
assert hex_key('09') == 0
assert hex_key('0A') == 0
assert hex_key('0B') == 1
assert hex_key('0C') == 0
assert hex_key('0D') == 1
assert hex_key('0E') == 0
assert hex_key('0F') == 0
assert hex_key('0') == 0
assert hex_key('1') == 0
assert hex_key('2') == 1
assert hex_key('3') == 1
assert hex_key('4') == 0
assert hex_key('5') == 1
assert hex_key('6') == 0
assert hex_key('7') == 1
assert hex_key('8') == 0
assert hex_key('9') == 0
assert hex_key('A') == 0
assert hex_key('B') == 1
assert hex_key('C') == 0
assert hex_key('D') == 1
assert hex_key('E') == 0
assert hex_key("7") == 1
assert hex_key("2D") == 2
assert hex_key("2D1") == 2
assert hex_key("2D12") == 3
assert hex_key("D") == 1
assert hex_key("0xF5D") == 2
assert hex_key("3BAAA9F98224E410E611E0B65B8D8AC1") == 8
assert hex_key("F2CDAD") == 3
assert hex_key("B56B7B") == 5
assert hex_key("F3DE3D") == 4
assert hex_key("A") == 0
assert hex_key("1D") == 1
assert hex_key("7D") == 2
assert hex_key('00C8') == 0
assert hex_key('1F') == 0
assert hex_key('DB') == 2
assert hex_key('B0') == 1
assert hex_key('FFF') == 0
assert hex_key("DE16B1A2") == 3
assert hex_key("AA") == 0
assert hex_key("AB") == 1
assert hex_key("F0E1D2C3B4A59687") == 6
assert hex_key("A103") == 1
assert hex_key("BA") == 1
assert hex_key("13BB") == 3
assert hex_key("1523BB11") == 5
assert hex_key('F3D14A7') == 3
assert hex_key('D4') == 1
assert hex_key('AAAAA') == 0
assert hex_key('FFFFF') == 0
assert hex_key('FFFFFF') == 0
assert hex_key('3FFFFFF') == 1
assert hex_key('0DD5') == 3
assert hex_key('111DD5') == 3
assert hex_key('0xB12') == 2
assert hex_key("2B") == 2
assert hex_key('ED2B') == 3
assert hex_key('E2') == 1
assert hex_key('A7B') == 2
assert hex_key('CAB') == 1
assert hex_key('C3') == 1
assert hex_key('9AB') == 1
assert hex_key('3A') == 1
assert hex_key('F2') == 1
assert hex_key('2AB') == 2
assert hex_key("35C") == 2
assert hex_key("FF") == 0
assert hex_key("AB12") == 2
assert hex_key("FFEE") == 0
assert hex_key("2F3E") == 2
assert hex_key('42') == 1
assert hex_key('') == 0
assert hex_key("3") == 1
assert hex_key("4") == 0
assert hex_key("6") == 0
assert hex_key("8") == 0
assert hex_key("E") == 0
assert hex_key('2A') == 1
assert hex_key('5F') == 1
assert hex_key('B7B') == 3
assert hex_key('ABC') == 1
assert hex_key('ABDC') == 2
assert hex_key('3D3') == 3
assert hex_key("FFF") == 0, "error in hex_key"
assert hex_key("0x000") == 0
assert hex_key("0x02") == 1
assert hex_key("B7") == 2
assert hex_key("0000000000000000000000000000000000000000000") == 0
assert hex_key("2C3A") == 2
assert hex_key("AC35") == 2
assert hex_key('0x74D2C') == 3
assert hex_key('0xFFF') == 0
assert hex_key('0xF0B') == 1
assert hex_key('0x10') == 0
assert hex_key('0x02') == 1
assert hex_key('0xFF') == 0
assert hex_key('0xFF3C') == 1
assert hex_key("7C") == 1
assert hex_key("B2") == 2
assert hex_key("A5") == 1
assert hex_key("3D") == 2
assert hex_key("74") == 1
assert hex_key("70") == 1
assert hex_key("D0") == 1
assert hex_key("A7A56B") == 3
assert hex_key("2C3E") == 2
assert hex_key("2F7A83D9") == 4
assert hex_key('CD') == 1
assert hex_key('AA') == 0
assert hex_key('FF') == 0
assert hex_key('ABCD') == 2
assert hex_key("BAD") == 2
assert hex_key("A2") == 1
assert hex_key("BD") == 2
assert hex_key('2E') == 1
assert hex_key('0000000') == 0
assert hex_key('01B') == 1
assert hex_key('B1B') == 2
assert hex_key('BAC') == 1
assert hex_key('7B') == 2
assert hex_key('CACA') == 0
assert hex_key('ACE3') == 1
assert hex_key('FFFFFFFF') == 0
assert hex_key("D32F4F3C") == 4
assert hex_key("2F") == 1
assert hex_key('FFFFFFFFFF') == 0
assert hex_key('F0') == 0
assert hex_key('F9F9F') == 0, "F9F9F"
assert hex_key('DD') == 2, "DD"
assert hex_key('FD3') == 2, "FD3"
assert hex_key('F3A73A') == 3
assert hex_key('F') == 0
assert hex_key('000000') == 0
assert hex_key("B1") == 1
assert hex_key("a") == 0
assert hex_key('0D3') == 2
assert hex_key('ab') == 0
assert hex_key("23") == 2
assert hex_key("02B") == 2
assert hex_key("02BD") == 3
assert hex_key("002BD") == 3
assert hex_key("F0F") == 0
assert hex_key("DDD") == 3
assert hex_key("BDD") == 3
assert hex_key("FBD") == 2
assert hex_key("BDF") == 2
assert hex_key("FCFF") == 0
assert hex_key("F9F9") == 0
assert hex_key("22") == 2
assert hex_key("24") == 1
assert hex_key("25") == 2
assert hex_key("55") == 2
assert hex_key("77") == 2
assert hex_key("BB") == 2
assert hex_key("cAD") == 1
assert hex_key('A1') == 0
assert hex_key('B3F') == 2
assert hex_key('DDD') == 3
assert hex_key('88') == 0
assert hex_key('CE') == 0
assert hex_key('4F') == 0
assert hex_key("00F") == 0
assert hex_key("05") == 1
assert hex_key("00") == 0
assert hex_key("000") == 0
assert hex_key("01") == 0
assert hex_key("2A3") == 2
assert hex_key("0B2") == 2
assert hex_key("5B5") == 3
assert hex_key("AAA") == 0
assert hex_key("7F") == 1
assert hex_key("A0A") == 0
assert hex_key("A2A") == 1
assert hex_key("FF7")
assert hex_key("010A3BF") == 2
assert hex_key("0xC") == 0
assert hex_key("0xB") == 1
assert hex_key("0xB10A") == 1
assert hex_key("1F83B7") == 3
assert hex_key("2CDB") == 3
assert hex_key('071A01') == 1
assert hex_key("DD") == 2
assert hex_key("bbad") == 0
assert hex_key('EDD') == 2
assert hex_key('B2') == 2
assert hex_key('E1') == 0
assert hex_key('D111') == 1
assert hex_key("0x") == 0
assert hex_key('1F7A44') == 1
assert hex_key('ABFE') == 1
assert hex_key('3A0A') == 1
assert hex_key("1F") == 0
assert hex_key("D6F") == 1
