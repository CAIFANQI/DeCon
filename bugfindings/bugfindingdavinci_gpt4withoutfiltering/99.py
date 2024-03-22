
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
assert closest_integer("21.5") == 22
assert closest_integer('1.5') == 2
assert closest_integer('0.5') == 1
assert closest_integer("-15.0") == -15
assert closest_integer("14.0") == 14
assert closest_integer("14.00") == 14
assert closest_integer("-14.0") == -14
assert closest_integer("-14.00") == -14
assert closest_integer("5.5") == 6
assert closest_integer("1.5") == 2
assert closest_integer("-5.0") == -5
assert closest_integer("0.0") == 0
assert closest_integer("3.0") == 3
assert closest_integer("-6.0") == -6
assert closest_integer("-0.0") == 0
assert closest_integer("9.5") == 10
assert closest_integer('9.5') == 10
assert closest_integer("26.5") == 27
assert closest_integer("13.5") == 14
assert closest_integer("15.0") == 15
assert closest_integer("17.5") == 18
assert closest_integer("16.5") == 17
assert closest_integer("11.5") == 12
assert closest_integer("2.00") == 2
assert closest_integer("0.5") == 1
assert closest_integer("10.0") == 10
assert closest_integer("-3.0") == -3
assert closest_integer("5") == 5
assert closest_integer("20.5") == 21
assert closest_integer("12.5") == 13
assert closest_integer("14.5") == 15, "14.5 -> 15"
assert closest_integer("18.5") == 19
assert closest_integer('15.5') == 16
assert closest_integer('-15.0') == -15
assert closest_integer('14.5') == 15
assert closest_integer('16.5') == 17
assert closest_integer("10.5") == 11
assert closest_integer("-1.0") == -1
assert closest_integer('11.5') == 12
assert closest_integer('12.5') == 13
assert closest_integer("0.99999999999999999") == 1
assert 0 == closest_integer("0")
assert 0 == closest_integer("0.0")
assert closest_integer("19.5") == 20
assert closest_integer("2.5") == 3
assert closest_integer('14.0') == 14
assert closest_integer('-14.0') == -14
assert closest_integer('14') == 14
assert closest_integer('-14') == -14
assert closest_integer("1.0") == 1
assert closest_integer("-10.0") == -10
assert closest_integer("0.000000000000000000") == 0
assert closest_integer("-100000000000000000.5") == -100000000000000000
assert closest_integer("-100000000000000000.4") == -100000000000000000
assert closest_integer("-100000000000000000.6") == -100000000000000000
assert closest_integer("-100000000000000000.00001") == -100000000000000000
assert closest_integer("-100000000000000000.0000000000000000001") == -100000000000000000
assert closest_integer('123.00') == 123
assert closest_integer('-123.0') == -123
assert closest_integer('123.5') == 124
