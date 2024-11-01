
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

assert closest_integer("14.5") == 15
assert closest_integer("15.5") == 16
assert closest_integer("14.4") == 14
assert closest_integer("-14.5") == -15
assert closest_integer("-14.4") == -14
assert closest_integer("21.5") == 22
assert closest_integer("21.8") == 22
assert closest_integer("-21.2") == -21
assert closest_integer("-21.5") == -22
assert closest_integer("-21.8") == -22
assert closest_integer('-12.5') == -13
assert closest_integer('1.5') == 2
assert closest_integer('-1.5') == -2
assert closest_integer('12.4') == 12
assert closest_integer('-12.4') == -12
assert closest_integer('0.5') == 1
assert closest_integer('-0.5') == -1
assert closest_integer('0.4') == 0
assert closest_integer('-0.4') == 0
assert closest_integer("-15.0") == -15
assert closest_integer("-14.1") == -14
assert closest_integer("14.1") == 14
assert closest_integer("-14.9") == -15
assert closest_integer("14.9") == 15
assert closest_integer("-15.5") == -16
assert closest_integer("-15.9") == -16
assert closest_integer("15.9") == 16
assert closest_integer("14.57") == 15
assert closest_integer("14.52") == 15
assert closest_integer("-14.57") == -15
assert closest_integer("-14.52") == -15
assert closest_integer("14.0") == 14
assert closest_integer("14.00") == 14
assert closest_integer("-14.0") == -14
assert closest_integer("-14.00") == -14
assert closest_integer("14.4999") == 14
assert closest_integer("14.5001") == 15
assert closest_integer('14.49') == 14
assert closest_integer('-14.5') == -15
assert closest_integer('-14.49') == -14
assert closest_integer("3.4") == 3
assert closest_integer("5.5") == 6
assert closest_integer("-1.43") == -1
assert closest_integer("1.43") == 1
assert closest_integer("1.5") == 2
assert closest_integer("2.7") == 3
assert closest_integer("-2.2") == -2
assert closest_integer("-2.7") == -3
assert closest_integer("-4.4") == -4
assert closest_integer("4.4") == 4
assert closest_integer("7.9") == 8
assert closest_integer("2.6") == 3
assert closest_integer("-22.8") == -23
assert closest_integer("-5.5") == -6
assert closest_integer("-5.0") == -5
assert closest_integer("11.3") == 11
assert closest_integer("-18.7") == -19
assert closest_integer("0.0") == 0
assert closest_integer("3.0") == 3
assert closest_integer("-35.4") == -35
assert closest_integer("-50.6") == -51
assert closest_integer("-6.0") == -6
assert closest_integer("-0.0") == 0
assert closest_integer("0.3") == 0
assert closest_integer("-0.3") == 0
assert closest_integer("1.1") == 1
assert closest_integer("-1.1") == -1
assert closest_integer("-4.5") == -5
assert closest_integer("-1.5") == -2
assert closest_integer("-1.49") == -1
assert closest_integer("-1.51") == -2
assert closest_integer("9.5") == 10
assert closest_integer("-0.1") == 0
assert closest_integer("0.1") == 0
assert closest_integer("-9.5") == -10
assert closest_integer("-9.55") == -10
assert closest_integer("-9.45") == -9
assert closest_integer("-14.2") == -14
assert closest_integer("14.2") == 14
assert closest_integer('-9.4') == -9
assert closest_integer('9.5') == 10
assert closest_integer('-9.5') == -10
assert closest_integer("26.5") == 27
assert closest_integer("-26.5") == -27
assert closest_integer("13.5") == 14
assert closest_integer("-13.5") == -14
assert closest_integer("-15.6") == -16
assert closest_integer("15.6") == 16
assert closest_integer("15.4") == 15
assert closest_integer("-15.4") == -15
assert closest_integer("15.01") == 15
assert closest_integer("-15.01") == -15
assert closest_integer("15.0") == 15
assert closest_integer("-1.4") == -1
assert closest_integer("1.4") == 1
assert closest_integer("0.8") == 1
assert closest_integer("-0.8") == -1
assert closest_integer("17.5") == 18
assert closest_integer("16.5") == 17
assert closest_integer("14.49") == 14
assert closest_integer("14.99") == 15
assert closest_integer("-14.99") == -15
assert closest_integer("-14.01") == -14
assert -15 == closest_integer("-14.5")
assert closest_integer("-10.1") == -10
assert closest_integer("-3.1") == -3
assert closest_integer("2.2") == 2
assert closest_integer("999.9") == 1000
assert closest_integer("-11.5") == -12
assert closest_integer("11.0001") == 11
assert closest_integer("11.5") == 12
assert closest_integer("55.55") == 56
assert closest_integer("-55.45") == -55
assert closest_integer("-55.55") == -56
assert closest_integer("-12.56") == -13
assert closest_integer("0.0001") == 0
assert closest_integer("3.89") == 4
assert closest_integer("-3.89") == -4
assert closest_integer("-0.0001") == 0
assert closest_integer("2.00") == 2
assert closest_integer("-0.75") == -1
assert closest_integer("-16.5") == -17
assert closest_integer("-14.6") == -15
assert closest_integer("0.5") == 1
assert closest_integer("10.0") == 10
assert closest_integer("3.3") == 3
assert closest_integer("-3.6") == -4
assert closest_integer("-3.3") == -3
assert closest_integer("-3.0") == -3
assert closest_integer("-12.34") == -12
assert closest_integer("14.56") == 15
assert closest_integer("-14.56") == -15
assert closest_integer("14.500001") == 15
assert closest_integer("-14.500001") == -15
assert closest_integer("14.4999999") == 14
assert closest_integer("-14.4999999") == -14
assert closest_integer("-0.5") == -1
assert closest_integer("5") == 5
assert closest_integer("15.1") == 15
assert closest_integer("-15.1") == -15
assert closest_integer("1.6") == 2
assert closest_integer("-1.6") == -2
assert closest_integer("1.45") == 1
assert closest_integer("1.55") == 2
assert closest_integer("-1.55") == -2
assert closest_integer("-14.499") == -14
assert closest_integer("-14.501") == -15
assert closest_integer("14.499") == 14
assert closest_integer("14.501") == 15
assert closest_integer("0.4") == 0
assert closest_integer("0.6") == 1
assert closest_integer("-0.4") == 0
assert closest_integer("-0.6") == -1
assert closest_integer("-0.001") == 0
assert closest_integer("0.001") == 0
assert closest_integer("0.00111") == 0
assert closest_integer("-0.00111") == 0
assert closest_integer('16.8') == 17
assert closest_integer('-16.8') == -17
assert closest_integer('-16.3') == -16
assert closest_integer('16.3') == 16
assert closest_integer("-17.5") == -18
assert closest_integer("-22.25") == -22
assert closest_integer("22.25") == 22
assert closest_integer("3.1") == 3
assert closest_integer("-4.1") == -4
assert closest_integer("4.1") == 4
assert closest_integer("8.4") == 8
assert closest_integer("-8.4") == -8
assert closest_integer("9.2") == 9
assert closest_integer("-9.2") == -9
assert closest_integer("13.9") == 14
assert closest_integer("-13.9") == -14
assert closest_integer("5.6") == 6
assert closest_integer("5.4") == 5
assert closest_integer("-3.2") == -3
assert closest_integer("-3.8") == -4
assert closest_integer("20.5") == 21
assert closest_integer("-7.5") == -8
assert closest_integer("-12.5") == -13
assert closest_integer("12.5") == 13
assert closest_integer("-0.25") == 0
assert closest_integer("-1.75") == -2
assert closest_integer("-1.25") == -1
assert closest_integer("1.25") == 1
assert closest_integer("1.75") == 2
assert closest_integer("-12.25") == -12
assert closest_integer("-12.75") == -13
assert closest_integer("12.25") == 12
assert closest_integer("12.75") == 13
assert closest_integer("-7.8") == -8
assert closest_integer("14.5") == 15, "14.5 -> 15"
assert closest_integer("-14.5") == -15, "-14.5 -> -15"
assert closest_integer("-14.4") == -14, "-14.4 -> -14"
assert closest_integer("-15.9") == -16, "-15.9 -> -16"
assert closest_integer("-16.4") == -16, "-16.4 -> -16"
assert closest_integer("16.4") == 16, "16.4 -> 16"
assert closest_integer("15.9") == 16, "15.9 -> 16"
assert closest_integer("-14.6") == -15, "-14.6 -> -15"
assert closest_integer("14.6") == 15, "14.6 -> 15"
assert closest_integer("-15.5") == -16, "-15.5 -> -16"
assert closest_integer("1.9") == 2
assert closest_integer("16.4") == 16
assert closest_integer("-16.4") == -16
assert closest_integer("-2.6") == -3
assert closest_integer("99.9") == 100
assert closest_integer("-99.9") == -100
assert closest_integer("26.4") == 26
assert closest_integer("-26.4") == -26
assert closest_integer("-61.4") == -61
assert closest_integer("61.4") == 61
assert closest_integer("-2.1") == -2
assert closest_integer("2.1") == 2
assert closest_integer("-18.5") == -19
assert closest_integer("18.5") == 19
assert closest_integer("17.9") == 18
assert closest_integer("-17.9") == -18
assert closest_integer("12.4") == 12
assert closest_integer("-12.4") == -12
assert closest_integer('-1.2') == -1
assert closest_integer('1.9') == 2
assert closest_integer('-1.9') == -2
assert closest_integer('9.9') == 10
assert closest_integer('-9.9') == -10
assert closest_integer('15.5') == 16
assert closest_integer('-15.5') == -16
assert closest_integer('1.2') == 1
assert closest_integer("15.2") == 15
assert closest_integer("-15.2") == -15
assert closest_integer("14.6") == 15
assert closest_integer("12.9") == 13
assert closest_integer("-14.3") == -14
assert closest_integer('-15.0') == -15
assert closest_integer("14.8") == 15
assert closest_integer("-14.8") == -15
assert closest_integer("-11.4") == -11
assert closest_integer("-123.456") == -123
assert closest_integer("-0.005") == 0
assert closest_integer("0.005") == 0
assert closest_integer("-0.049999") == 0
assert closest_integer("0.049999") == 0
assert closest_integer("0.00005") == 0
assert closest_integer("-0.00005") == 0
assert closest_integer("0.000049999") == 0
assert closest_integer("-0.000049999") == 0
assert closest_integer("1.9999999999999998") == 2
assert closest_integer("-1.9999999999999998") == -2
assert closest_integer("25.999999999999996") == 26
assert closest_integer("-25.999999999999996") == -26
assert closest_integer("100.99999999999997") == 101
assert closest_integer("-100.99999999999997") == -101
assert closest_integer('14.5') == 15
assert closest_integer('-16.5') == -17
assert closest_integer('16.5') == 17
assert closest_integer("10.5") == 11
assert closest_integer("-1.0") == -1
assert closest_integer('-11.5') == -12
assert closest_integer('11.5') == 12
assert closest_integer('12.5') == 13
assert closest_integer('1000000.9999') == 1000001
assert closest_integer('-1000000.9999') == -1000001
assert closest_integer("5.56") == 6
assert closest_integer("-5.56") == -6
assert closest_integer("0.55") == 1
assert closest_integer("9.9") == 10
assert closest_integer("-9.9") == -10
assert closest_integer("-0.7") == -1
assert closest_integer("0.99999999999999999") == 1
assert 1 == closest_integer("1.2")
assert -1 == closest_integer("-0.5")
assert -2 == closest_integer("-1.6")
assert 0 == closest_integer("0")
assert 0 == closest_integer("0.0")
assert 10 == closest_integer("9.9")
assert -10 == closest_integer("-9.9")
assert closest_integer("19.5") == 20
assert closest_integer("-19.5") == -20
assert closest_integer("2.5") == 3
assert closest_integer("-2.5") == -3
assert closest_integer('14.4') == 14
assert closest_integer('14.6') == 15
assert closest_integer('-14.4') == -14
assert closest_integer('-14.6') == -15
assert closest_integer('14.0') == 14
assert closest_integer('-14.0') == -14
assert closest_integer('14') == 14
assert closest_integer('-14') == -14
assert closest_integer("15.10") == 15
assert closest_integer("-15.10") == -15
assert closest_integer("14.543") == 15
assert closest_integer("0.9") == 1
assert closest_integer("1.0") == 1
assert closest_integer("-0.9") == -1
assert closest_integer("-20.5") == -21
assert closest_integer("10.1") == 10
assert closest_integer("5.45") == 5
assert closest_integer("-5.45") == -5
assert closest_integer("7.1") == 7
assert closest_integer("-17.3") == -17
assert closest_integer("-17.6") == -18
assert closest_integer("13.3") == 13
assert closest_integer("17.8") == 18
assert closest_integer("-19.9") == -20
assert closest_integer("-10.0") == -10
assert closest_integer("-0.11") == 0
assert closest_integer("0.11") == 0
assert closest_integer("13.7") == 14
assert closest_integer("0.000100") == 0
assert closest_integer("0.000100000000000000") == 0
assert closest_integer("0.000000000000000000") == 0
assert closest_integer("0.000000000000000000001") == 0
assert closest_integer("-100000000000000000.5") == -100000000000000000
assert closest_integer("-100000000000000000.4") == -100000000000000000
assert closest_integer("-100000000000000000.6") == -100000000000000000
assert closest_integer("-100000000000000000.00001") == -100000000000000000
assert closest_integer("-100000000000000000.0000000000000000001") == -100000000000000000
assert closest_integer('0.0001') == 0
assert closest_integer('-0.0001') == 0
assert closest_integer('14.51') == 15
assert closest_integer('123.00') == 123
assert closest_integer('123.00000001') == 123
assert closest_integer('123.1') == 123
assert closest_integer('123.99') == 124
assert closest_integer('-123.0') == -123
assert closest_integer('-123.1') == -123
assert closest_integer('-123.99') == -124
assert closest_integer('123.4') == 123
assert closest_integer('-123.4') == -123
assert closest_integer('123.5') == 124
assert closest_integer('-123.5') == -124
assert closest_integer("-13.6") == -14
assert closest_integer("13.4") == 13
assert closest_integer("13.6") == 14
