
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
assert closest_integer("-14.5") == -15
assert closest_integer("0.5") == 1
assert closest_integer("-0.5") == -1
assert closest_integer("1.4") == 1
assert closest_integer("-1.4") == -1
assert closest_integer("2.6") == 3
assert closest_integer("-2.6") == -3
assert closest_integer("3.5") == 4
assert closest_integer("-3.5") == -4
assert closest_integer("10.5") == 11
assert closest_integer("-10.5") == -11
assert closest_integer("5.5") == 6
assert closest_integer("-5.5") == -6
assert closest_integer("10.6") == 11
assert closest_integer("-10.6") == -11
assert closest_integer("0") == 0
assert closest_integer("0.9") == 1
assert closest_integer("-0.9") == -1
assert closest_integer("10.1") == 10
assert closest_integer("-10.1") == -10
assert closest_integer("3.2") == 3
assert closest_integer("-3.2") == -3
assert closest_integer("3.7") == 4
assert closest_integer("-3.7") == -4
assert closest_integer("5.0") == 5
assert closest_integer("-5.0") == -5
assert closest_integer("3.14159") == 3
assert closest_integer("-3.14159") == -3
assert closest_integer("0.4") == 0
assert closest_integer("-0.4") == 0
assert closest_integer("5.6") == 6
assert closest_integer("-5.6") == -6
assert closest_integer("3.4") == 3
assert closest_integer("-3.4") == -3
assert closest_integer("14.4") == 14
assert closest_integer("-14.4") == -14
assert closest_integer("2.5") == 3
assert closest_integer("-2.5") == -3
assert closest_integer("10") == 10
assert closest_integer("-10") == -10
assert closest_integer("3.14") == 3
assert closest_integer("-3.14") == -3
assert closest_integer("-14.5") == -15, "Test case 2 failed"
assert closest_integer("0.5") == 1, "Test case 3 failed"
assert closest_integer("-0.5") == -1, "Test case 4 failed"
assert closest_integer("10.8") == 11, "Test case 5 failed"
assert closest_integer("-10.8") == -11, "Test case 6 failed"
assert closest_integer("5.2") == 5, "Test case 7 failed"
assert closest_integer("-5.2") == -5, "Test case 8 failed"
assert closest_integer("3.9") == 4, "Test case 9 failed"
assert closest_integer("-3.9") == -4, "Test case 10 failed"
assert closest_integer("10.4") == 10
assert closest_integer("-10.4") == -10
assert closest_integer("-0") == 0
assert closest_integer("15") == 15
assert closest_integer("-15") == -15
assert closest_integer("0.1") == 0
assert closest_integer("-0.1") == 0
assert closest_integer("1") == 1
assert closest_integer("-1") == -1
assert closest_integer("10.9") == 11
assert closest_integer("-10.9") == -11
assert closest_integer("10.49") == 10
assert closest_integer("-10.49") == -10
assert closest_integer("10.51") == 11
assert closest_integer("-10.51") == -11
assert closest_integer("0.0") == 0
assert closest_integer("-0.0") == 0
assert closest_integer("3.6") == 4
assert closest_integer("-3.6") == -4
assert closest_integer("4.9") == 5
assert closest_integer("-4.9") == -5
assert closest_integer("6.1") == 6
assert closest_integer("-6.1") == -6
assert closest_integer("10.2") == 10
assert closest_integer("-10.2") == -10
assert closest_integer("15.8") == 16
assert closest_integer("-15.8") == -16
assert closest_integer("1.5") == 2
assert closest_integer("-1.5") == -2
assert closest_integer("10.8") == 11
assert closest_integer("-10.8") == -11
assert closest_integer("1.1") == 1
assert closest_integer("-1.1") == -1
assert closest_integer("1.9") == 2
assert closest_integer("-1.9") == -2
assert closest_integer("100.5") == 101
assert closest_integer("-100.5") == -101
assert closest_integer("15.5") == 16
assert closest_integer("-15.5") == -16
assert closest_integer("1.6") == 2
assert closest_integer("-1.6") == -2
assert closest_integer("2.9") == 3
assert closest_integer("-2.9") == -3
assert closest_integer("3.14159") == 3, "Test case 5 failed"
assert closest_integer("-3.14159") == -3, "Test case 6 failed"
assert closest_integer("10.6") == 11, "Test case 7 failed"
assert closest_integer("-10.6") == -11, "Test case 8 failed"
assert closest_integer("10.4") == 10, "Test case 9 failed"
assert closest_integer("-10.4") == -10, "Test case 10 failed"
assert closest_integer("0") == 0, "Test case 11 failed"
assert closest_integer("3.8") == 4
assert closest_integer("-3.8") == -4
assert closest_integer("0.6") == 1
assert closest_integer("-0.6") == -1
assert closest_integer("15.4") == 15
assert closest_integer("-15.4") == -15
assert closest_integer("1.2") == 1
assert closest_integer("-1.2") == -1
assert closest_integer("100.1") == 100
assert closest_integer("-100.1") == -100
assert closest_integer("4.5") == 5
assert closest_integer("-4.5") == -5
assert closest_integer("-14.5") == -15, 'Test Case 2 Failed'
assert closest_integer("3.2") == 3, 'Test Case 3 Failed'
assert closest_integer("-3.2") == -3, 'Test Case 4 Failed'
assert closest_integer("0.5") == 1, 'Test Case 5 Failed'
assert closest_integer("-0.5") == -1, 'Test Case 6 Failed'
assert closest_integer("0.4") == 0, 'Test Case 7 Failed'
assert closest_integer("-0.4") == 0, 'Test Case 8 Failed'
assert closest_integer("4.4") == 4
assert closest_integer("-4.4") == -4
assert closest_integer("0.2") == 0
assert closest_integer("-0.2") == 0
assert closest_integer("0.8") == 1
assert closest_integer("-0.8") == -1
assert closest_integer("2.4") == 2
assert closest_integer("-2.4") == -2
assert closest_integer("100") == 100
assert closest_integer("2.1") == 2
assert closest_integer("-2.1") == -2
assert closest_integer("3.1") == 3
assert closest_integer("-3.1") == -3
assert closest_integer("3.9") == 4
assert closest_integer("-3.9") == -4
assert closest_integer("4.1") == 4
assert closest_integer("-4.1") == -4
assert closest_integer("5.1") == 5
assert closest_integer("-5.1") == -5
assert closest_integer("5.9") == 6
assert closest_integer("-5.9") == -6
assert closest_integer("6.5") == 7
assert closest_integer("-6.5") == -7
assert closest_integer("6.9") == 7
assert closest_integer("-6.9") == -7
assert closest_integer("7.1") == 7
assert closest_integer("-7.1") == -7
assert closest_integer("7.5") == 8
assert closest_integer("-7.5") == -8
assert closest_integer("7.9") == 8
assert closest_integer("-7.9") == -8
assert closest_integer("8.1") == 8
assert closest_integer("-8.1") == -8
assert closest_integer("8.5") == 9
assert closest_integer("-8.5") == -9
assert closest_integer("8.9") == 9
assert closest_integer("-8.9") == -9
assert closest_integer("9.1") == 9
assert closest_integer("-9.1") == -9
assert closest_integer("9.5") == 10
assert closest_integer("-9.5") == -10
assert closest_integer("9.9") == 10
assert closest_integer("-9.9") == -10
