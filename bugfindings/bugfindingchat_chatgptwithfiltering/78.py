
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
assert hex_key('') == 0
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
assert hex_key('F') == 0
assert hex_key('14') == 0
assert hex_key('15') == 1
assert hex_key('16') == 0
assert hex_key('18') == 0
assert hex_key('19') == 0
assert hex_key('1C') == 0
assert hex_key('1E') == 0
assert hex_key('1F') == 0
assert hex_key('20') == 1
assert hex_key('21') == 1
assert hex_key('2A') == 1
assert hex_key('2B') == 2
assert hex_key('2D') == 2
assert hex_key('30') == 1
assert hex_key('31') == 1
assert hex_key('3B') == 2
assert hex_key('3D') == 2
assert hex_key('40') == 0
assert hex_key('41') == 0
assert hex_key('44') == 0
assert hex_key('46') == 0
assert hex_key('48') == 0
assert hex_key('49') == 0
assert hex_key('4A') == 0
assert hex_key('4C') == 0
assert hex_key('4E') == 0
assert hex_key('4F') == 0
assert hex_key('60') == 0
assert hex_key('61') == 0
assert hex_key('62')
assert hex_key('5C') == 1
assert hex_key('7D') == 2
assert hex_key('9E') == 0
assert hex_key('BC') == 1
assert hex_key('DE') == 1
assert hex_key('FF') == 0
assert hex_key('123456789ABCDEF') == 6
assert hex_key('17') == 1
assert hex_key('45') == 1
assert hex_key('50') == 1
assert hex_key('5B') == 2
assert hex_key('5D') == 2
assert hex_key('70') == 1
assert hex_key('7B') == 2
assert hex_key('85') == 1
assert hex_key('89') == 0
assert hex_key('8F') == 0
assert hex_key('95') == 1
assert hex_key('99') == 0
assert hex_key('9F') == 0
assert hex_key('A0') == 0
assert hex_key('A9') == 0
assert hex_key('AF') == 0
assert hex_key('B0') == 1
assert hex_key('C0') == 0
assert hex_key('C9') == 0
assert hex_key('CF') == 0
assert hex_key('D0') == 1
assert hex_key('E0') == 0
assert hex_key('E9') == 0
assert hex_key('EF') == 0
assert hex_key('F0') == 0
assert hex_key('F9') == 0
assert hex_key("0") == 0
assert hex_key("1") == 0
assert hex_key("2") == 1
assert hex_key("3") == 1
assert hex_key("4") == 0
assert hex_key("5") == 1
assert hex_key("6") == 0
assert hex_key("7") == 1
assert hex_key("8") == 0
assert hex_key("9") == 0
assert hex_key("A") == 0
assert hex_key("B") == 1
assert hex_key("C") == 0
assert hex_key("D") == 1
assert hex_key("E") == 0
assert hex_key("F") == 0
assert hex_key("10") == 0
assert hex_key("14") == 0
assert hex_key("15") == 1
assert hex_key("16") == 0
assert hex_key("18") == 0
assert hex_key("1A") == 0
assert hex_key("1C") == 0
assert hex_key("1E") == 0
assert hex_key("21") == 1
assert hex_key("23") == 2
assert hex_key("27") == 2
assert hex_key("29") == 1
assert hex_key("2B") == 2
assert hex_key("2D") == 2
assert hex_key("2F") == 1
assert hex_key("31") == 1
assert hex_key("33") == 2
assert hex_key("37") == 2
assert hex_key("39") == 1
assert hex_key("3B") == 2
assert hex_key("3D") == 2
assert hex_key("3F") == 1
assert hex_key("40") == 0
assert hex_key("44") == 0
assert hex_key("45") == 1
assert hex_key("46") == 0
assert hex_key("48") == 0
assert hex_key("4A") == 0
assert hex_key("4C") == 0
assert hex_key("4E") == 0
assert hex_key("51") == 1
assert hex_key("53") == 2
assert hex_key("57") == 2
assert hex_key("59") == 1
assert hex_key("5B") == 2
assert hex_key("5D") == 2
assert hex_key("5F") == 1
assert hex_key("60") == 0
assert hex_key("") == 0
assert hex_key("ABCD") == 2
assert hex_key('10') == 0
assert hex_key('13') == 1
assert hex_key('1A') == 0
assert hex_key('1B') == 1
assert hex_key('1D') == 1
assert hex_key('43') == 1
assert hex_key('47') == 1
assert hex_key('4B') == 1
assert hex_key('4D') == 1
assert hex_key('63') == 1
assert hex_key('64') == 0
assert hex_key('66') == 0
assert hex_key('67') == 1
assert hex_key('68') == 0
assert hex_key('69') == 0
assert hex_key('6A') == 0
assert hex_key('6B') == 1
assert hex_key('6C') == 0
assert hex_key('12') == 1
assert hex_key('42') == 1
assert hex_key("123456789ABCDEF") == 6
assert hex_key('CD') == 1
assert hex_key('FD') == 1
assert hex_key("2C") == 1
assert hex_key("2E") == 1
assert hex_key("3C") == 1
assert hex_key("3E") == 1
assert hex_key("4F") == 0
assert hex_key("5A") == 1
assert hex_key("6A") == 0
assert hex_key("6C") == 0
assert hex_key("6E") == 0
assert hex_key("6F") == 0
assert hex_key("7A") == 1
assert hex_key("8A") == 0
assert hex_key("8C") == 0
assert hex_key("8E") == 0
assert hex_key("8F") == 0
assert hex_key("9A") == 0
assert hex_key("9C") == 0
assert hex_key("9E") == 0
assert hex_key("9F") == 0
assert hex_key("AA") == 0
assert hex_key("AC") == 0
assert hex_key("AE") == 0
assert hex_key("AF") == 0
assert hex_key("BA") == 1
assert hex_key("CA") == 0
assert hex_key("CC") == 0
assert hex_key("CE") == 0
assert hex_key("CF") == 0
assert hex_key("DA") == 1
assert hex_key("EA") == 0
assert hex_key("EC") == 0
assert hex_key("EE") == 0
assert hex_key("EF") == 0
assert hex_key("FA") == 0
assert hex_key("FC") == 0
assert hex_key("F0") == 0
assert hex_key("F1") == 0
assert hex_key("F2") == 1
assert hex_key("F3") == 1
assert hex_key("F4") == 0
assert hex_key("F5") == 1
assert hex_key("F6") == 0
assert hex_key("F7") == 1
assert hex_key("F8") == 0
assert hex_key("F9") == 0
assert hex_key("FB") == 1
assert hex_key("FD") == 1
assert hex_key("FE") == 0
assert hex_key("FF") == 0
assert hex_key('1111111111111111') == 0
assert hex_key('2222222222222222') == 16
assert hex_key("1234567890ABCDEF") == 6
assert hex_key('B7') == 2
assert hex_key('F3') == 1
assert hex_key('8E') == 0
assert hex_key('B8') == 1
assert hex_key('26') == 1
assert hex_key('C7') == 1
assert hex_key('8C') == 0
assert hex_key('0D') == 1
assert hex_key('9C') == 0
assert hex_key('D6') == 1
assert hex_key('BA') == 1
assert hex_key('EC') == 0
assert hex_key('C3') == 1
assert hex_key('0B') == 1
assert hex_key('D4') == 1
assert hex_key('2C') == 1
assert hex_key('8A') == 0
assert hex_key('B9') == 1
assert hex_key('C2') == 1
assert hex_key('88') == 0
assert hex_key('35') == 2
assert hex_key('98') == 0
assert hex_key('B1') == 1
assert hex_key("AB") == 1
assert hex_key("BB") == 2
assert hex_key("BC") == 1
assert hex_key("BD") == 2
assert hex_key("BE") == 1
assert hex_key("BF") == 1
assert hex_key("AAA") == 0
assert hex_key("AAB") == 1
assert hex_key("ABA") == 1
assert hex_key("ABB") == 2
assert hex_key("ABC") == 1
assert hex_key("ABD") == 2
assert hex_key("ABE") == 1
assert hex_key("ABF") == 1
assert hex_key("12") == 1
assert hex_key("19") == 0
assert hex_key("1F") == 0
assert hex_key("20") == 1
assert hex_key("41") == 0
assert hex_key("49") == 0
assert hex_key("61") == 0
assert hex_key("9B") == 1
assert hex_key("DD") == 2
assert hex_key("13") == 1
assert hex_key("17") == 1
assert hex_key("1B") == 1
assert hex_key("1D") == 1
assert hex_key('0') == 0, "Error: Test Case 2"
assert hex_key('1') == 0, "Error: Test Case 3"
assert hex_key('2') == 1, "Error: Test Case 4"
assert hex_key('3') == 1, "Error: Test Case 5"
assert hex_key('4') == 0, "Error: Test Case 6"
assert hex_key('5') == 1, "Error: Test Case 7"
assert hex_key('6') == 0, "Error: Test Case 8"
assert hex_key('7') == 1, "Error: Test Case 9"
assert hex_key('8') == 0, "Error: Test Case 10"
assert hex_key('9') == 0, "Error: Test Case 11"
assert hex_key('A') == 0, "Error: Test Case 12"
assert hex_key('B') == 1, "Error: Test Case 13"
assert hex_key('C') == 0, "Error: Test Case 14"
assert hex_key('D') == 1, "Error: Test Case 15"
assert hex_key('E') == 0, "Error: Test Case 16"
assert hex_key('F') == 0, "Error: Test Case 17"
assert hex_key('35') == 2, "Error: Test Case 19"
assert hex_key('2B') == 2, "Error: Test Case 22"
assert hex_key('3D') == 2, "Error: Test Case 23"
assert hex_key('57') == 2, "Error: Test Case 24"
assert hex_key('2B3') == 3, "Error: Test Case 26"
assert hex_key('3D5') == 3, "Error: Test Case 27"
assert hex_key('2B35') == 4, "Error: Test Case 30"
assert hex_key('3D57') == 4, "Error: Test Case 31"
assert hex_key('3D57B') == 5, "Error: Test Case 35"
assert hex_key("") == 0, "Testcase 2 failed"
assert hex_key("B") == 1, "Testcase 5 failed"
assert hex_key("30") == 1
assert hex_key('2B3D5F') == 5
assert hex_key('B3') == 2
assert hex_key('F8') == 0
assert hex_key('B3F8') == 2
assert hex_key('ABCDEF') == 2
assert hex_key('23') == 2
assert hex_key('27') == 2
assert hex_key('29') == 1
assert hex_key('2F') == 1
assert hex_key('33') == 2
assert hex_key('37') == 2
assert hex_key('39') == 1
assert hex_key('3A') == 1
assert hex_key('3F') == 1
assert hex_key('51') == 1
assert hex_key('53') == 2
assert hex_key('57') == 2
assert hex_key('59') == 1
assert hex_key('5A') == 1
assert hex_key('5F') == 1
assert hex_key("0000000000000000") == 0
assert hex_key("1111111111111111") == 0
assert hex_key("2222222222222222") == 16
assert hex_key("3333333333333333") == 16
assert hex_key("4444444444444444") == 0
assert hex_key("5555555555555555") == 16
assert hex_key("6666666666666666") == 0
assert hex_key("7777777777777777") == 16
assert hex_key("8888888888888888") == 0
assert hex_key("9999999999999999") == 0
assert hex_key("AAAAAAAAAAAAAAAA") == 0
assert hex_key("BBBBBBBBBBBBBBBB") == 16
assert hex_key("CCCCCCCCCCCCCCCC") == 0
assert hex_key("DDDDDDDDDDDDDDDD") == 16
assert hex_key("EEEEEEEEEEEEEEEE") == 0
assert hex_key("FFFFFFFFFFFFFFFF") == 0
assert hex_key("2") == 1, "Error: Test Case 2"
assert hex_key("B") == 1, "Error: Test Case 3"
assert hex_key("F") == 0, "Error: Test Case 4"
assert hex_key("") == 0, "Error: Test Case 5"
assert hex_key("43") == 1
assert hex_key("47") == 1
assert hex_key("4B") == 1
assert hex_key("4D") == 1
assert hex_key("FFFFFFFF") == 0
assert hex_key("5C") == 1
assert hex_key("DE") == 1
assert hex_key("0A") == 0
