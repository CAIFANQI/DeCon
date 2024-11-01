
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

assert 	closest_integer("12.0") == 12
assert 	closest_integer("12.4") == 12
assert 	closest_integer("12.5") == 13
assert 	closest_integer("12.6") == 13
assert 	closest_integer("14") == 14
assert 	closest_integer("-14") == -14
assert 	closest_integer("-14.5") == -15
assert 	closest_integer("-14.6") == -15
assert 	closest_integer("-14.69999999999999") == -15
assert 	closest_integer("14.59999999999999") == 15
assert 	closest_integer("14.69999999999999") == 15
assert 	closest_integer(".1") == 0
assert 	closest_integer("-.1") == 0
assert 	closest_integer("-.10000000000000001") == 0
assert 	closest_integer("1.1") == 1
assert 	closest_integer("1.10000000000000002") == 1
assert 	closest_integer("5") == 5
assert 	closest_integer("4.5") == 5
assert 	closest_integer("14.5") == 15
assert 	closest_integer("15.5") == 16
assert 	closest_integer("-15.5") == -16
assert 	closest_integer("16.5") == 17
assert 	closest_integer("-16.5") == -17
assert 	closest_integer("15.2224") == 15
assert 	closest_integer("15.2225") == 15
assert 	closest_integer("15.2227") == 15
assert 	closest_integer("15.2228") == 15
assert 	closest_integer("15.2230") == 15
assert 	closest_integer("15.2232") == 15
assert 	closest_integer("15.2234") == 15
assert 	closest_integer("15.2235") == 15
assert 	closest_integer("15.2237") == 15
assert 	closest_integer("14.3") == 14
assert 	closest_integer("14.1") == 14
assert 	closest_integer("14.4") == 14
assert 	closest_integer("14.9") == 15
assert 	closest_integer("15.1") == 15
assert 	closest_integer("15.2") == 15
assert 	closest_integer("15.9") == 16
assert 	closest_integer("15.0") == 15
assert 	closest_integer("-15.9") == -16
assert 	closest_integer("-15.1") == -15
assert 	closest_integer("-15.0") == -15
assert closest_integer("14.5") == 15
assert closest_integer("-14.5") == -15
assert closest_integer("14") == 14
assert closest_integer("-14") == -14
assert closest_integer("0") == 0
assert closest_integer("5") == 5
assert closest_integer("-5") == -5
assert closest_integer("5.5") == 6
assert closest_integer("5.4") == 5
assert closest_integer("5.6") == 6
assert closest_integer("5.611111111") == 6
assert closest_integer("-5.611111111") == -6
assert closest_integer("-5.6111111111111") == -6
assert closest_integer("0.4") == 0
assert closest_integer("0.1") == 0
assert closest_integer("-0.9") == -1
assert 	closest_integer("14.567") == 15
assert 	closest_integer("15.7") == 16
assert 	closest_integer("15.6") == 16
assert 	closest_integer("15.4") == 15
assert 	closest_integer("-14.4") == -14
assert 	closest_integer("-14.567") == -15
assert 	closest_integer("-15.7") == -16
assert 	closest_integer("-15.6") == -16
assert 	closest_integer("-15.4") == -15
assert 	closest_integer('5') == 5
assert 	closest_integer('-3') == -3
assert 	closest_integer('5.2') == 5
assert 	closest_integer('-5.2') == -5
assert 	closest_integer('0.7') == 1
assert 	closest_integer('-0.7') == -1
assert 	closest_integer('3.7') == 4
assert 	closest_integer('-3.7') == -4
assert 	closest_integer('6.8') == 7
assert 	closest_integer('-6.8') == -7
assert 	closest_integer('0') == 0
assert 	closest_integer('-0') == 0
assert 	closest_integer('1.5') == 2
assert 	closest_integer('-1.5') == -2
assert 	closest_integer('-0.5') == -1
assert 	closest_integer('0.5') == 1
assert closest_integer('1') == 1
assert closest_integer('1.1') == 1
assert closest_integer('-1.1') == -1
assert closest_integer('-1.0') == -1
assert closest_integer('0.9') == 1
assert closest_integer('2.0') == 2
assert closest_integer('4.1') == 4
assert closest_integer('-4.1') == -4
assert closest_integer('5') == 5
assert closest_integer('5.1') == 5
assert closest_integer('-5.1') == -5
assert closest_integer('6.1') == 6
assert 	closest_integer("14.6") == 15
assert 	closest_integer("14.566") == 15
assert 	closest_integer("-14.7") == -15
assert 	closest_integer("14.8") == 15
assert 	closest_integer("15") == 15
assert 	closest_integer("-15") == -15
assert 	closest_integer("15.3") == 15
assert 	closest_integer("15.11") == 15
