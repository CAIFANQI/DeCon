
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

assert closest_integer("0") == 0
assert closest_integer("-10") == -10
assert closest_integer("1") == 1
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
assert closest_integer('2') == 2
assert closest_integer('-1') == -1
assert closest_integer('3') == 3
assert closest_integer("0") is 0
assert closest_integer("015") == 15
assert closest_integer("-1") == -1, "-1 should return -1"
assert closest_integer("-2") == -2
assert closest_integer("-1") == -1
assert closest_integer("-3") == -3
assert closest_integer("-9") == -9
assert closest_integer("106") == 106
assert closest_integer("21") == 21
assert closest_integer("101") == 101
assert closest_integer("-101") == -101
assert closest_integer("31") == 31
assert closest_integer("100") == 100
assert closest_integer("-0") == -0
assert closest_integer("333") == 333
assert closest_integer("-7") == -7
assert closest_integer("-50") == -50
assert closest_integer("25") == 25
assert closest_integer("99") == 99
assert closest_integer("0") ==  0
assert closest_integer('-10') == -10
assert closest_integer('14') == 14
assert closest_integer('-2') == -2
assert closest_integer('1') == 1
assert closest_integer('10') == 10
