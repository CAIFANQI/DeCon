
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
assert closest_integer("0.5") == 1
assert closest_integer("3.5") == 4
assert closest_integer("10.5") == 11
assert closest_integer("5.5") == 6
assert closest_integer("0") == 0
assert closest_integer("5.0") == 5
assert closest_integer("-5.0") == -5
assert closest_integer("2.5") == 3
assert closest_integer("10") == 10
assert closest_integer("-10") == -10
assert closest_integer("0.5") == 1, "Test case 3 failed"
assert closest_integer("-0") == 0
assert closest_integer("15") == 15
assert closest_integer("-15") == -15
assert closest_integer("1") == 1
assert closest_integer("-1") == -1
assert closest_integer("0.0") == 0
assert closest_integer("-0.0") == 0
assert closest_integer("1.5") == 2
assert closest_integer("100.5") == 101
assert closest_integer("15.5") == 16
assert closest_integer("0") == 0, "Test case 11 failed"
assert closest_integer("4.5") == 5
assert closest_integer("0.5") == 1, 'Test Case 5 Failed'
assert closest_integer("100") == 100
assert closest_integer("6.5") == 7
assert closest_integer("7.5") == 8
assert closest_integer("8.5") == 9
assert closest_integer("9.5") == 10
