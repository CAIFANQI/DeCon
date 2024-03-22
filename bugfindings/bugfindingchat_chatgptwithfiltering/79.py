
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
assert decimal_to_binary(1) == 'db1db'
assert decimal_to_binary(2) == 'db10db'
assert decimal_to_binary(10) == 'db1010db'
assert decimal_to_binary(100) == 'db1100100db'
assert decimal_to_binary(3) == 'db11db'
assert decimal_to_binary(4) == 'db100db'
assert decimal_to_binary(255) == 'db11111111db'
assert decimal_to_binary(1024) == 'db10000000000db'
assert (decimal_to_binary(1) == 'db1db')
assert (decimal_to_binary(10) == 'db1010db')
assert (decimal_to_binary(100) == 'db1100100db')
assert (decimal_to_binary(2) == 'db10db')
assert (decimal_to_binary(3) == 'db11db')
assert (decimal_to_binary(4) == 'db100db')
assert (decimal_to_binary(5) == 'db101db')
assert (decimal_to_binary(15) == 'db1111db')
assert decimal_to_binary(1) == "db1db"
assert decimal_to_binary(10) == "db1010db"
assert decimal_to_binary(100) == "db1100100db"
assert decimal_to_binary(1000) == "db1111101000db"
assert decimal_to_binary(5) == 'db101db'
assert decimal_to_binary(1000) == 'db1111101000db'
assert decimal_to_binary(123456789) == 'db111010110111100110100010101db'
assert decimal_to_binary(2) == "db10db"
