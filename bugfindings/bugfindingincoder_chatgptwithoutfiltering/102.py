
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return x - 1
assert choose_num(1, 2) == 2
assert choose_num(1, 4) == 4
assert choose_num(1, 3) == 2
assert choose_num(1, 5) == 4
assert choose_num(1, 7) == 6
assert choose_num(2, 3) == 2
assert choose_num(2, 5) == 4
assert choose_num(2, 7) == 6
assert choose_num(3, 5) == 4
assert choose_num(3, 7) == 6
assert choose_num(4, 5) == 4
assert choose_num(4, 7) == 6
assert choose_num(5, 7) == 6
assert choose_num(6, 7) == 6
assert choose_num(0, 4) == 4
assert choose_num(4, 4) == 4
assert choose_num(-1, -1) == -1
assert choose_num(-1, 2) == 2
assert choose_num(10, 11) == 10
assert choose_num(12, 12) == 12
assert choose_num(12, 13) == 12
assert choose_num(1, 2) == 2, "The function should return 2 as it's the biggest even number in [1, 2]."
assert choose_num(2, 2) == 2
assert choose_num(3, 4) == 4
assert choose_num(8, 8) == 8
assert choose_num(100, 100) == 100
assert choose_num(1, 4) == 4, "The function should return 4 for (1,4)"
assert choose_num(6, 6) == 6
assert choose_num(7, 8) == 8
assert choose_num(10, 10) == 10
assert choose_num(-10, -10) == -10
assert choose_num(1000, 1001) == 1000
assert choose_num(999, 1000) == 1000
assert choose_num(-1000, 1000) == 1000
assert choose_num(0, 0) == 0
assert choose_num(11,12) == 12
assert choose_num(12,12) == 12
assert choose_num(10,10) == 10
assert choose_num(8, 10) == 10
assert choose_num(2, 6) == 6
assert choose_num(4, 8) == 8
assert choose_num(6, 8) == 8
assert choose_num(0, 2) == 2
assert choose_num(2, 8) == 8
assert choose_num(3, 10) == 10
assert choose_num(-14, -10) == -10
assert choose_num(-100, 10) == 10
assert choose_num(-1000, 100) == 100
assert choose_num(-1000, 500) == 500
assert choose_num(1,2) == 2
assert choose_num(4,6) == 6
assert choose_num(125, 350) == 350
assert choose_num(122, 123) == 122
assert choose_num(13, 14) == 14
assert choose_num(20, 20) == 20
assert choose_num(1500, 1500) == 1500
