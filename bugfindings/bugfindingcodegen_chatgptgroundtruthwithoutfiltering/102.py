
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
assert 	choose_num(-1, -1) == -1
assert 	choose_num(10, 15) == 14, "Wrong output"
assert 	choose_num(15, 16) == 16, "Wrong output"
assert 	choose_num(16, 16) == 16, "Wrong output"
assert 	choose_num(6, 17) == 16
assert 	choose_num(3, 5) == 4
assert 	choose_num(8, 11) == 10
assert choose_num(-1, -1) == -1
assert choose_num(-1, 1) == 0
assert choose_num(0, 1) == 0
assert choose_num(1, 2) == 2
assert choose_num(1, 3) == 2
assert choose_num(2, 3) == 2
assert choose_num(3, 4) == 4
assert choose_num(4, 8) == 8
assert choose_num(4, 9) == 8
assert 	choose_num(0, 101) == 100, "not working for x < y"
assert 	choose_num(0, 100) == 100, "not working for x = y"
assert 	choose_num(100, 100) == 100, "not working for x = y"
assert 	choose_num(1, 101) == 100, "not working for x < y"
assert 	choose_num(-1, 101) == 100, "not working for x < y"
assert 	choose_num(7, 9) == 8
assert 	choose_num(-1, 1) == 0
assert 	choose_num(1, 2) == 2
assert 	choose_num(2, 4) == 4, '4 should be the smallest even number in the range [2, 4]'
assert 	choose_num(5, 6) == 6, '6 should be the smallest even number in the range [5, 6]'
assert 	choose_num(4, 5) == 4
assert 	choose_num(6, 6) == 6
assert choose_num(2, 4) == 4
assert choose_num(4, 4) == 4
assert choose_num(10, 10) == 10
assert choose_num(8, 11) == 10
assert 	choose_num(0, 2) == 2
