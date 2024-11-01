
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

assert closest_integer("-14.5") == -15
assert closest_integer("14.500") == 15
assert closest_integer("-14.500") == -15
assert closest_integer("14.5000") == 15
assert closest_integer("-14.5000") == -15
assert closest_integer("14.5000000") == 15
assert closest_integer("-14.5000000") == -15
assert closest_integer("14.500000000") == 15
assert closest_integer("-14.500000000") == -15
assert closest_integer("14.5000000000") == 15
assert closest_integer("-14.5000000000") == -15
assert closest_integer("14.50000000000") == 15
assert closest_integer("-14.50000000000") == -15
assert closest_integer("14.50") == 15
assert closest_integer("-14.50") == -15
assert closest_integer("14.5") == 15
assert closest_integer("0") == 0
assert closest_integer("4.5") == 5
assert closest_integer("9.5") == 10
assert closest_integer("9.6") == 10
assert closest_integer("9.7") == 10
assert closest_integer("9.8") == 10
assert closest_integer("9.9") == 10
assert closest_integer("10.0") == 10
assert closest_integer("10.1") == 10
assert closest_integer("10.2") == 10
assert closest_integer("10.3") == 10
assert closest_integer("10.4") == 10
assert closest_integer("10.10") == 10
assert closest_integer("10.11") == 10
assert closest_integer("10.12") == 10
assert closest_integer("10.13") == 10
assert closest_integer("10.14") == 10
assert closest_integer("10.15") == 10
assert closest_integer("10.16") == 10
assert closest_integer("10.17") == 10
assert closest_integer("10.18") == 10
assert closest_integer("10.19") == 10
assert closest_integer("10.20") == 10
assert closest_integer("10.21") == 10
assert closest_integer("10.22") == 10
assert closest_integer("10.23") == 10
assert closest_integer("10.24") == 10
assert closest_integer("-10") == -10
assert closest_integer("10.4") ==  10
assert closest_integer("10.25") == 10
assert closest_integer("10.26") == 10
assert closest_integer("10.27") == 10
assert closest_integer("10.28") == 10
assert closest_integer("10.29") == 10
assert closest_integer("10.30") == 10
assert closest_integer("10.31") == 10
assert closest_integer("10.32") == 10
assert closest_integer("10.33") == 10
assert closest_integer("15.9999") == 16
assert closest_integer("-15.9999") == -16
assert closest_integer("15.5") == 16
assert closest_integer("-15.5") == -16
assert closest_integer("16.9999") == 17
assert closest_integer("-16.9999") == -17
assert closest_integer("16.5") == 17
assert closest_integer("-16.5") == -17
assert closest_integer("17.9999") == 18
assert closest_integer("-17.9999") == -18
assert closest_integer("17.5") == 18
assert closest_integer("-17.5") == -18
assert closest_integer("18.9999") == 19
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
assert closest_integer("5.3") == 5
assert closest_integer("-5") == -5
assert closest_integer("9.4") == 9
assert closest_integer("9.3") == 9
assert closest_integer("9.2") == 9
assert closest_integer("9.1") == 9
assert closest_integer("12") == 12
assert closest_integer("12.3") == 12
assert closest_integer("12.7") == 13
assert closest_integer("12.799") == 13
assert closest_integer("12.899") == 13
assert closest_integer("12.9001") == 13
assert closest_integer("12.9002") == 13
assert closest_integer("12.9003") == 13
assert closest_integer("12.9004") == 13
assert closest_integer("12.9005") == 13
assert closest_integer("12.9006") == 13
assert closest_integer("12.9007") == 13
assert closest_integer("12.9008") == 13
assert closest_integer("12.9009") == 13
assert closest_integer("12.9010") == 13
assert closest_integer("12.9011") == 13
assert closest_integer("12.9012") == 13
assert closest_integer("12.9013") == 13
assert closest_integer("12.9014") == 13
assert closest_integer("12.9015") == 13
assert closest_integer("12.9016") == 13
assert closest_integer("12.9017") == 13
assert closest_integer("12.9018") == 13
assert closest_integer("12.9019") == 13
assert closest_integer("12.9020") == 13
assert closest_integer("12.9021") == 13
assert closest_integer("12.9022") == 13
assert closest_integer("12.9023") == 13
assert closest_integer("-14.1") == -14, "-14.1"
assert closest_integer("14") == 14, "14"
assert closest_integer("-14") == -14, "-14"
assert closest_integer("15") == 15, "15"
assert closest_integer("-14") == -14
assert closest_integer("14.50000000000001") == 15
assert closest_integer("14.5000000000001") == 15
assert closest_integer("14.5000000000002") == 15
assert closest_integer("-14.500000000000001") == -15
assert closest_integer("-14.50000000000002") == -15
assert closest_integer("-14.50000000000003") == -15
assert closest_integer("14.50000000000004") == 15
assert closest_integer("-14.50000000000004") == -15
assert closest_integer("14.50000000000005") == 15
assert closest_integer("-14.50000000000005") == -15
assert closest_integer("102") == 102
assert closest_integer("-102") == -102
assert closest_integer("-10.25") == -10
assert closest_integer("11") == 11
assert closest_integer("-11") == -11
assert closest_integer("11.25") == 11
assert closest_integer("-11.25") == -11
assert closest_integer("-12") == -12
assert closest_integer("12.25") == 12
assert closest_integer("-12.25") == -12
assert closest_integer("13.25") == 13
assert closest_integer("11.0") == 11
assert closest_integer("-11.0") == -11
assert closest_integer("10.005") == 10
assert closest_integer("7.49") == 7
assert closest_integer("8.49") == 8
assert closest_integer("9.49") == 9
assert closest_integer("10.49") == 10
assert closest_integer("11.49") == 11
assert closest_integer("12.49") == 12
assert closest_integer("14.49") == 14
assert closest_integer("15.49") == 15
assert closest_integer("16.49") == 16
assert closest_integer("17.49") == 17
assert closest_integer("18.49") == 18
assert closest_integer("19.49") == 19
assert closest_integer("20.49") == 20
assert closest_integer("21.49") == 21
assert closest_integer("22.49") == 22
assert closest_integer("23.49") == 23
assert closest_integer("24.49") == 24
assert closest_integer("25.49") == 25
assert closest_integer("26.49") == 26
assert closest_integer("27.49") == 27
assert closest_integer("28.49") == 28
assert closest_integer("29.49") == 29
assert closest_integer("30.49") == 30
assert closest_integer("31.49") == 31
assert closest_integer("32.49") == 32
assert closest_integer("33.49") == 33
assert closest_integer("14.4") == 14
assert closest_integer("-14.4") == -14
assert closest_integer("14.3") == 14
assert closest_integer("-14.3") == -14
assert closest_integer("14.2") == 14
assert closest_integer("-14.2") == -14
assert closest_integer("15.4") == 15
assert closest_integer("-15.4") == -15
assert closest_integer("16.3") == 16
assert closest_integer("16.2") == 16
assert closest_integer("16") == 16
assert closest_integer("-16") == -16
assert closest_integer("17") == 17
assert closest_integer("-17") == -17
assert closest_integer("18.4") == 18
assert closest_integer("18.3") == 18
assert closest_integer("18.2") == 18
assert closest_integer("18") == 18
assert closest_integer("-18") == -18
assert closest_integer("19") == 19
assert closest_integer("-19") == -19
assert closest_integer("20") == 20
assert closest_integer("1") == 1, "Passed"
assert closest_integer("-10") == -10, "Passed"
assert closest_integer("9.99999999999999") == 10, "Passed"
assert closest_integer("9.99") == 10, "Passed"
assert closest_integer("9.991") == 10, "Passed"
assert closest_integer("9.992") == 10, "Passed"
assert closest_integer("9.994") == 10, "Passed"
assert closest_integer("9.995") == 10, "Passed"
assert closest_integer("9.996") == 10, "Passed"
assert closest_integer("9.997") == 10, "Passed"
assert closest_integer("9.998") == 10, "Passed"
assert closest_integer("9.999") == 10, "Passed"
assert closest_integer("14.1") == 14
assert closest_integer("14.") == 14
assert closest_integer("14.0") == 14
assert closest_integer("14.00") == 14
assert closest_integer("14.000") == 14
assert closest_integer("14.012") == 14
assert closest_integer("14.0123") == 14
assert closest_integer("14.01234") == 14
assert closest_integer("14.012345") == 14
assert closest_integer("14.0123456") == 14
assert closest_integer("14.01234567") == 14
assert closest_integer("14.012345678") == 14
assert closest_integer("14.0123456789") == 14
assert closest_integer("14.01234567890") == 14
assert closest_integer("14.012345678901") == 14
assert closest_integer("14.0123456789012") == 14
assert closest_integer("14.01234567890123") == 14
assert closest_integer("14.012345678901234") == 14
assert closest_integer("14.0123456789012345") == 14
assert closest_integer("14.01234567890123456") == 14
assert closest_integer("14.012345678901234567") == 14
assert closest_integer("14.0123456789012345678") == 14
assert closest_integer("9.99") == 10
assert closest_integer("10.01") == 10
assert closest_integer("9.999999999999") == 10
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
assert closest_integer("9.1")==9
assert closest_integer("8.1")==8
assert closest_integer('2') == 2
assert closest_integer('-1') == -1
assert closest_integer('-1.5') == -2
assert closest_integer('3') == 3
assert closest_integer('2.0') == 2
assert closest_integer('3.1') == 3
assert closest_integer('3.10') == 3
assert closest_integer("14.51") == 15
assert closest_integer("-14.51") == -15
assert closest_integer("14.50000000001") == 15
assert closest_integer("-14.50000000001") == -15
assert closest_integer("14.55") == 15
assert closest_integer("-14.55") == -15
assert closest_integer("14.5555") == 15
assert closest_integer("-14.5555") == -15
assert closest_integer("16.1") == 16
assert closest_integer("16.11") == 16
assert closest_integer("16.111") == 16
assert closest_integer("16.1111") == 16
assert closest_integer("16.11111") == 16
assert closest_integer("16.111111") == 16
assert closest_integer("16.1111111") == 16
assert closest_integer("16.2222") == 16
assert closest_integer("16.22221") == 16
assert closest_integer("16.222211") == 16
assert closest_integer("16.2222111") == 16
assert closest_integer("16.222222") == 16
assert closest_integer("16.2222221") == 16
assert closest_integer("16.33333333") == 16
assert closest_integer("16.333333331") == 16
assert closest_integer("16.3333333311") == 16
assert closest_integer("16.33333333111") == 16
assert closest_integer("5.2") == 5
assert closest_integer("5.10") == 5
assert closest_integer("5.11") == 5
assert closest_integer("5.12") == 5
assert closest_integer("5.13") == 5
assert closest_integer("5.14") == 5
assert closest_integer("5.15") == 5
assert closest_integer("-5.15") == -5
assert closest_integer("-5.14") == -5
assert closest_integer("-5.13") == -5
assert closest_integer("-5.12") == -5
assert closest_integer("-5.11") == -5
assert closest_integer("-5.10") == -5
assert closest_integer("-5.4") == -5
assert closest_integer("8.1") == 8
assert closest_integer("0") is 0
assert closest_integer("3.1") == 3
assert closest_integer("12.9") == 13
assert closest_integer("11.7") == 12
assert closest_integer("11.3") == 11
assert closest_integer("11.1") == 11
assert closest_integer("9.0") == 9
assert closest_integer("1.49") == 1
assert closest_integer("-1.49") == -1
assert closest_integer("-1.1") == -1
assert closest_integer("-13.4") == -13
assert closest_integer("-13.3") == -13
assert closest_integer("13.3") == 13
assert closest_integer("15.02") == 15
assert closest_integer("-15.02") == -15
assert closest_integer("-15.03") == -15
assert closest_integer("-15.01") == -15
assert closest_integer("015") == 15
assert closest_integer("015.03") == 15
assert closest_integer("015.01") == 15
assert closest_integer("015.02") == 15
assert closest_integer("015.49") == 15
assert closest_integer('12.1') == 12
assert closest_integer('14.5') == 15
assert closest_integer('17.4') == 17
assert closest_integer('30.2') == 30
assert closest_integer('32.0') == 32
assert closest_integer('35.1') == 35
assert closest_integer('39.1') == 39
assert closest_integer('43.1') == 43
assert closest_integer('45.4') == 45
assert closest_integer('49.0') == 49
assert closest_integer('55.2') == 55
assert closest_integer('59.0') == 59
assert closest_integer('63.2') == 63
assert closest_integer('67.0') == 67
assert closest_integer('69.3') == 69
assert closest_integer('75.2') == 75
assert closest_integer("0.32") == 0
assert closest_integer("-0.44") == 0
assert closest_integer("-1") == -1, "-1 should return -1"
assert closest_integer("-2") == -2
assert closest_integer("-1") == -1
assert closest_integer("13.5") == 14
assert closest_integer("-13.5") == -14
assert closest_integer("15.3") == 15
assert closest_integer("14.499") == 14
assert closest_integer("15.999") == 16
assert closest_integer("16.0") == 16
assert closest_integer("20.0") == 20
assert closest_integer("4.3") == 4
assert closest_integer("-4.3") == -4
assert closest_integer("4.4") == 4
assert closest_integer("-4.4") == -4
assert closest_integer("12.1") == 12
assert closest_integer("12.2") == 12
assert closest_integer("12.4") == 12
assert closest_integer("12.10") == 12
assert closest_integer("-3") == -3
assert closest_integer("-1.3") == -1
assert closest_integer("-9") == -9
assert closest_integer("3.1415926535897932384626433832795028841971") == 3
assert closest_integer("3.1415926535897932384626433832795028841972") == 3
assert closest_integer("-3.1415926535897932384626433832795028841971") == -3
assert closest_integer("-3.1415926535897932384626433832795028841972") == -3
assert closest_integer("1.1") == 1
assert closest_integer("7.1") == 7
assert closest_integer("7.9") == 8
assert closest_integer("8.4") == 8
assert closest_integer("-9.4") == -9
assert closest_integer("-9.8") == -10
assert closest_integer("-9.9") == -10
assert closest_integer("9.90000000000000") == 10
assert closest_integer("9.90000000000001") == 10
assert closest_integer("9.90000000000002") == 10
assert closest_integer("9.90000000000003") == 10
assert closest_integer("9.90000000000004") == 10
assert closest_integer("9.90000000000005") == 10
assert closest_integer("9.90000000000006") == 10
assert closest_integer("9.90000000000007") == 10
assert closest_integer("9.90000000000008") == 10
assert closest_integer("9.90000000000009") == 10
assert closest_integer("-10.2") == -10
assert closest_integer("-10.4") == -10
assert closest_integer("-14.5") == -15, "Number is not equidistant from two integers."
assert closest_integer("13.75") == 14
assert closest_integer("13.7") == 14
assert closest_integer("14.54") == 15
assert closest_integer("-14.54") == -15
assert closest_integer("14.59") == 15
assert closest_integer("14.61") == 15
assert closest_integer("14.57") == 15
assert closest_integer("14.58") == 15
assert closest_integer("-14.58") == -15
assert closest_integer("-14.59") == -15
assert closest_integer("14.6") == 15
assert closest_integer("10.5") == 11
assert closest_integer("-1.5") == -2
assert closest_integer("-2.5") == -3
assert closest_integer("105.5") == 106
assert closest_integer("106") == 106
assert closest_integer("3.5") == 4
assert closest_integer("-10.1") == -10
assert closest_integer("11.2") == 11
assert closest_integer("21") == 21
assert closest_integer("-14.") == -14
assert closest_integer("15.2") == 15
assert closest_integer("-15.2") == -15
assert closest_integer("15.99") == 16
assert closest_integer("15.99999") == 16
assert closest_integer("15.75") == 16
assert closest_integer("101") == 101
assert closest_integer("101.2") == 101
assert closest_integer("-101") == -101
assert closest_integer("-101.2") == -101
assert closest_integer("4.2") == 4
assert closest_integer("2.2") == 2
assert closest_integer("4.21") == 4
assert closest_integer("2.21") == 2
assert closest_integer("31") == 31
assert closest_integer("12.31") == 12
assert closest_integer("7.4") == 7
assert closest_integer("4.1") == 4
assert closest_integer("2.1") == 2
assert closest_integer("4.0") == 4
assert closest_integer("3.3") == 3
assert closest_integer("100") == 100
assert closest_integer("-0") == -0
assert closest_integer("0.0000000000001") == 0
assert closest_integer("0.00000000000000001") == 0
assert closest_integer("333") == 333
assert closest_integer("7.2") == 7
assert closest_integer("-7.2") == -7
assert closest_integer("-7") == -7
assert closest_integer("-50") == -50
assert closest_integer("25") == 25
assert closest_integer("1.6") == 2, "second test"
assert closest_integer("7.1") == 7, "fifth test"
assert closest_integer("-7.1") == -7, "sixth test"
assert closest_integer("1.1") == 1, "seventh test"
assert closest_integer("-1.1") == -1, "eighth test"
assert closest_integer("21.2") == 21
assert closest_integer("17.1") == 17
assert closest_integer("18.1") == 18
assert closest_integer("-0.1") == 0
assert closest_integer("-10.3") == -10
assert closest_integer("-20.3") == -20
assert closest_integer("-23.2") == -23
assert closest_integer("-21.7") == -22
assert closest_integer("-22.7") == -23
assert closest_integer("9.51") == 10
assert closest_integer("7.0") == 7
assert closest_integer("-2.6") == -3
assert closest_integer("-3.1") == -3
assert closest_integer("-2.4") == -2
assert closest_integer("2.4") == 2
assert closest_integer("2.6") == 3
assert closest_integer("-1.4") == -1
assert closest_integer("1.4") == 1
assert closest_integer("-3.5") == -4
assert closest_integer("-0.8") == -1
assert closest_integer("-3.3") == -3
assert closest_integer("5.1") == 5
assert closest_integer("5.6") == 6
assert closest_integer("99") == 99
assert closest_integer("13.0") == 13
assert closest_integer("-10.0") == -10
assert closest_integer("99.2") == 99
assert closest_integer("90.0") == 90
assert closest_integer("111.1") == 111
assert closest_integer("999.9") == 1000
assert closest_integer("1000.0") == 1000
assert closest_integer("100.1") == 100
assert closest_integer("90.1") == 90
assert closest_integer("99.1") == 99
assert closest_integer("100.10") == 100
assert closest_integer("90.10") == 90
assert closest_integer("99.10") == 99
assert closest_integer("100.0") == 100
assert closest_integer("99.0") == 99
assert closest_integer("43.4") == 43
assert closest_integer("7.3") == 7
assert closest_integer("-7.3") == -7
assert closest_integer("-2.3") == -2
assert closest_integer("-5.1") == -5
assert closest_integer("-3.0") == -3
assert closest_integer("14.5") ==  15
assert closest_integer("0") ==  0
assert closest_integer("7.4") ==  7
assert closest_integer("3.2") == 3
assert closest_integer("5.4") == 5
assert closest_integer("-3.8") == -4
assert closest_integer("8.3") == 8
assert closest_integer("3.4") == 3
assert closest_integer("-14.52") == -15
assert closest_integer('-10') == -10
assert closest_integer('14') == 14
assert closest_integer('-10.0') == -10
assert closest_integer('5.0') == 5
assert closest_integer('-2') == -2
assert closest_integer("3.0") == 3
assert closest_integer("6.3") == 6
assert closest_integer("6.7") == 7
assert closest_integer("6.1") == 6
assert closest_integer("8.2") == 8
assert closest_integer("12.0") == 12
assert closest_integer("14.33") == 14
assert closest_integer("9.500000000001") == 10
assert closest_integer("-23.4") == -23
assert closest_integer("0.1") == 0
assert closest_integer("-0.6") == -1
assert closest_integer("12.5") == 13
assert closest_integer("-1.000") == -1
assert closest_integer('1') == 1
assert closest_integer('10') == 10
