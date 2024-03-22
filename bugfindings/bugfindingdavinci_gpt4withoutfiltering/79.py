
def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """
    return "db" + bin(decimal)[2:] + "d"
assert decimal_to_binary(254) == 'db11111110db'
assert decimal_to_binary(1) == 'db1db'
assert decimal_to_binary(2) == 'db10db'
assert decimal_to_binary(3) == 'db11db'
assert decimal_to_binary(4) == 'db100db'
assert decimal_to_binary(5) == 'db101db'
assert decimal_to_binary(6) == 'db110db'
assert decimal_to_binary(7) == 'db111db'
assert decimal_to_binary(8) == 'db1000db'
assert decimal_to_binary(9) == 'db1001db'
assert decimal_to_binary(10) == 'db1010db'
assert decimal_to_binary(11) == 'db1011db'
assert decimal_to_binary(12) == 'db1100db'
assert decimal_to_binary(13) == 'db1101db'
assert decimal_to_binary(14) == 'db1110db'
assert decimal_to_binary(15) == 'db1111db'
assert decimal_to_binary(16) == 'db10000db'
assert decimal_to_binary(100) == 'db1100100db'
assert decimal_to_binary(253) == 'db11111101db'
assert decimal_to_binary(1000) == 'db1111101000db'
assert decimal_to_binary(10000) == 'db10011100010000db'
assert decimal_to_binary(0) == 'db0db'
assert decimal_to_binary(17) == 'db10001db'
assert decimal_to_binary(64) == 'db1000000db'
assert decimal_to_binary(97) == 'db1100001db'
assert decimal_to_binary(127) == 'db1111111db'
assert decimal_to_binary(255) == 'db11111111db'
assert decimal_to_binary(1000000) == 'db11110100001001000000db'
assert "db11011000db" == decimal_to_binary(216)
assert "db10000011db" == decimal_to_binary(131)
assert "db11010111db" == decimal_to_binary(215)
assert "db11011010db" == decimal_to_binary(218)
assert "db11101101db" == decimal_to_binary(237)
assert "db1010101db" == decimal_to_binary(85)
assert "db10011100db" == decimal_to_binary(156)
assert "db10010011db" == decimal_to_binary(147)
assert "db10110111db" == decimal_to_binary(183)
assert "db10001100db" == decimal_to_binary(140)
assert "db10011000db" == decimal_to_binary(152)
assert "db11000010db" == decimal_to_binary(194)
assert "db11010100db" == decimal_to_binary(212)
assert "db10111011db" == decimal_to_binary(187)
assert decimal_to_binary(18) == 'db10010db'
assert "db1011db" == decimal_to_binary(11)
assert "db111001db" == decimal_to_binary(57)
assert decimal_to_binary(256) == 'db100000000db'
assert decimal_to_binary(20) == 'db10100db'
assert decimal_to_binary(1024) == 'db10000000000db'
assert decimal_to_binary(45) == 'db101101db'
assert decimal_to_binary(128) == 'db10000000db'
assert decimal_to_binary(27) == 'db11011db'
assert decimal_to_binary(80) == 'db1010000db'
assert decimal_to_binary(300) == 'db100101100db'
assert decimal_to_binary(1025) == 'db10000000001db'
assert decimal_to_binary(1026) == 'db10000000010db'
assert decimal_to_binary(1027) == 'db10000000011db'
assert decimal_to_binary(56) == 'db111000db'
assert decimal_to_binary(99) == 'db1100011db'
assert decimal_to_binary(123) == 'db1111011db'
assert decimal_to_binary(512) == 'db1000000000db'
assert decimal_to_binary(1023) == 'db1111111111db'
assert decimal_to_binary(2048) == 'db100000000000db'
assert decimal_to_binary(90) == 'db1011010db'
assert decimal_to_binary(2 ** 15) == 'db1000000000000000db'
assert decimal_to_binary(2 ** 16) == 'db10000000000000000db'
assert decimal_to_binary(2 ** 32) == 'db100000000000000000000000000000000db'
assert decimal_to_binary(200) == 'db11001000db'
assert decimal_to_binary(101) == 'db1100101db'
assert decimal_to_binary(32) == 'db100000db'
assert decimal_to_binary(32768) == 'db1000000000000000db'
assert decimal_to_binary(65536) == 'db10000000000000000db'
assert decimal_to_binary(2**32-1) == 'db11111111111111111111111111111111db'
assert decimal_to_binary(2**32) == 'db100000000000000000000000000000000db'
assert decimal_to_binary(2**32+1) == 'db100000000000000000000000000000001db'
assert decimal_to_binary(110) == 'db1101110db'
assert "db11111111db" == decimal_to_binary(255)
assert decimal_to_binary(999) == 'db1111100111db'
assert decimal_to_binary(72) == 'db1001000db'
assert decimal_to_binary(31) == 'db11111db'
assert decimal_to_binary(63) == 'db111111db'
assert decimal_to_binary(100000) == 'db11000011010100000db'
assert "db1101101db" == decimal_to_binary(109)
assert decimal_to_binary(57) == 'db111001db'
assert decimal_to_binary(70) == 'db1000110db'
assert decimal_to_binary(50) == 'db110010db'
assert decimal_to_binary(25) == 'db11001db'
assert decimal_to_binary(299) == 'db100101011db'
assert decimal_to_binary(301) == 'db100101101db'
assert decimal_to_binary(65535) == 'db1111111111111111db'
assert decimal_to_binary(500) == 'db111110100db'
assert decimal_to_binary(1234567890) == 'db1001001100101100000001011010010db'
assert decimal_to_binary(1001) == 'db1111101001db'
assert decimal_to_binary(234) == 'db11101010db'
assert decimal_to_binary(2047) == 'db11111111111db'
assert decimal_to_binary(12345) == 'db11000000111001db'
assert decimal_to_binary(55) == 'db110111db'
assert decimal_to_binary(65537) == 'db10000000000000001db'
assert decimal_to_binary(42) == 'db101010db'
assert decimal_to_binary(35) == 'db100011db'
assert (decimal_to_binary(4) == 'db100db')
assert (decimal_to_binary(5) == 'db101db')
assert (decimal_to_binary(6) == 'db110db')
assert (decimal_to_binary(7) == 'db111db')
assert (decimal_to_binary(8) == 'db1000db')
assert (decimal_to_binary(9) == 'db1001db')
assert (decimal_to_binary(10) == 'db1010db')
assert (decimal_to_binary(11) == 'db1011db')
assert (decimal_to_binary(12) == 'db1100db')
assert (decimal_to_binary(13) == 'db1101db')
assert (decimal_to_binary(14) == 'db1110db')
assert (decimal_to_binary(15) == 'db1111db')
assert (decimal_to_binary(16) == 'db10000db')
assert decimal_to_binary(40) == 'db101000db'
assert decimal_to_binary(73) == 'db1001001db'
assert decimal_to_binary(78) == 'db1001110db'
