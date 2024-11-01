
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    from math import floor, ceil

    if value.count('.') == 1:
        # remove trailing zeros
        while (value[-1] == '0'):
            value = value[:-1]

    num = float(value)
    if value[-2:] == '.5':
        if num > 0:
            res = floor(num)
        else:
            res = ceil(num)
    elif len(value) > 0:
        res = int(round(num))
    else:
        res = 0

    return res

assert closest_integer("14.500") == 15
assert closest_integer("14.5000") == 15
assert closest_integer("14.5000000") == 15
assert closest_integer("14.500000000") == 15
assert closest_integer("14.5000000000") == 15
assert closest_integer("14.50000000000") == 15
assert closest_integer("14.50") == 15
assert closest_integer("14.5") == 15
assert closest_integer("0") == 0
assert closest_integer("4.5") == 5
assert closest_integer("9.5") == 10
assert closest_integer("10.0") == 10
assert closest_integer("-10") == -10
assert closest_integer("15.5") == 16
assert closest_integer("16.5") == 17
assert closest_integer("17.5") == 18
assert closest_integer("1") == 1
assert closest_integer("1.5") == 2
assert closest_integer("2") == 2
assert closest_integer("3") == 3
assert closest_integer("4") == 4
assert closest_integer("5") == 5
assert closest_integer("6") == 6
assert closest_integer("7") == 7
assert closest_integer("8") == 8
assert closest_integer("9") == 9
assert closest_integer("10") == 10
assert closest_integer("13") == 13
assert closest_integer("14") == 14
assert closest_integer("15") == 15
assert closest_integer("-15") == -15
assert closest_integer("-5") == -5
assert closest_integer("12") == 12
assert closest_integer("14") == 14, "14"
assert closest_integer("-14") == -14, "-14"
assert closest_integer("15") == 15, "15"
assert closest_integer("-14") == -14
assert closest_integer("102") == 102
assert closest_integer("-102") == -102
assert closest_integer("11") == 11
assert closest_integer("-11") == -11
assert closest_integer("-12") == -12
assert closest_integer("11.0") == 11
assert closest_integer("-11.0") == -11
assert closest_integer("16") == 16
assert closest_integer("-16") == -16
assert closest_integer("17") == 17
assert closest_integer("-17") == -17
assert closest_integer("18") == 18
assert closest_integer("-18") == -18
assert closest_integer("19") == 19
assert closest_integer("-19") == -19
assert closest_integer("20") == 20
assert closest_integer("1") == 1, "Passed"
assert closest_integer("-10") == -10, "Passed"
assert closest_integer("14.") == 14
assert closest_integer("14.0") == 14
assert closest_integer("14.00") == 14
assert closest_integer("14.000") == 14
assert closest_integer("9.99999999999999999") == 10
assert closest_integer("9.999999999999999991") == 10
assert closest_integer("9.9999999999999999915") == 10
assert closest_integer("9.99999999999999999151") == 10
assert closest_integer("9.999999999999999991515") == 10
assert closest_integer("9.9999999999999999915151") == 10
assert closest_integer("9.99999999999999999151515") == 10
assert closest_integer("9.999999999999999991515151") == 10
assert closest_integer("9.9999999999999999915151515") == 10
assert closest_integer("9.99999999999999999151515151") == 10
assert closest_integer("9.999999999999999991515151515") == 10
assert closest_integer("9.9999999999999999915151515151") == 10
assert closest_integer("9.99999999999999999151515151515") == 10
assert closest_integer("9.999999999999999991515151515151") == 10
assert closest_integer('2') == 2
assert closest_integer('-1') == -1
assert closest_integer('3') == 3
assert closest_integer('2.0') == 2
assert closest_integer("0") is 0
assert closest_integer("9.0") == 9
assert closest_integer("015") == 15
assert closest_integer('14.5') == 15
assert closest_integer('32.0') == 32
assert closest_integer('49.0') == 49
assert closest_integer('59.0') == 59
assert closest_integer('67.0') == 67
assert closest_integer("-1") == -1, "-1 should return -1"
assert closest_integer("-2") == -2
assert closest_integer("-1") == -1
assert closest_integer("13.5") == 14
assert closest_integer("16.0") == 16
assert closest_integer("20.0") == 20
assert closest_integer("-3") == -3
assert closest_integer("-9") == -9
assert closest_integer("10.5") == 11
assert closest_integer("105.5") == 106
assert closest_integer("106") == 106
assert closest_integer("3.5") == 4
assert closest_integer("21") == 21
assert closest_integer("-14.") == -14
assert closest_integer("101") == 101
assert closest_integer("-101") == -101
assert closest_integer("31") == 31
assert closest_integer("4.0") == 4
assert closest_integer("100") == 100
assert closest_integer("-0") == -0
assert closest_integer("333") == 333
assert closest_integer("-7") == -7
assert closest_integer("-50") == -50
assert closest_integer("25") == 25
assert closest_integer("7.0") == 7
assert closest_integer("99") == 99
assert closest_integer("13.0") == 13
assert closest_integer("-10.0") == -10
assert closest_integer("90.0") == 90
assert closest_integer("1000.0") == 1000
assert closest_integer("100.0") == 100
assert closest_integer("99.0") == 99
assert closest_integer("-3.0") == -3
assert closest_integer("14.5") ==  15
assert closest_integer("0") ==  0
assert closest_integer('-10') == -10
assert closest_integer('14') == 14
assert closest_integer('-10.0') == -10
assert closest_integer('5.0') == 5
assert closest_integer('-2') == -2
assert closest_integer("3.0") == 3
assert closest_integer("12.0") == 12
assert closest_integer("12.5") == 13
assert closest_integer("-1.000") == -1
assert closest_integer('1') == 1
assert closest_integer('10') == 10
