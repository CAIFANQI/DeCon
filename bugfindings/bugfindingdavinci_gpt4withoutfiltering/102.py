
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
assert choose_num(3, 7) == 6
assert choose_num(11, 15) == 14
assert choose_num(2, 8) == 8
assert choose_num(4, 5) == 4
assert choose_num(10, 10) == 10
assert choose_num(1, 1) == -1
assert choose_num(16, 1) == -1
assert choose_num(6, 3) == -1
assert choose_num(10, 12) == 12
assert choose_num(13, 13) == -1
assert choose_num(2, 6) == 6
assert choose_num(9, 9) == -1
assert choose_num(15, 33) == 32
assert choose_num(10, 8) == -1
assert choose_num(10, 0) == -1
assert choose_num(3, 9) == 8
assert choose_num(1, 2) == 2
assert choose_num(18, 9) == -1
assert choose_num(5, 8) == 8
assert choose_num(5, 10) == 10
assert choose_num(5, 9) == 8
assert choose_num(4, 9) == 8
assert choose_num(4, 8) == 8
assert choose_num(3, 6) == 6
assert choose_num(0, 5) == 4
assert choose_num(2, 5) == 4
assert choose_num(2, 7) == 6
assert choose_num(1, 5) == 4
assert choose_num(3, 5) == 4
assert choose_num(6, 5) == -1
assert choose_num(7, 6) == -1
assert choose_num(5, 5) == -1
assert choose_num(3, 3) == -1
assert choose_num(5, 11) == 10
assert choose_num(4, 2) == -1
assert choose_num(4, 10) == 10
assert choose_num(1, 100) == 100
assert choose_num(10, 3) == -1
assert choose_num(10, 2) == -1
assert choose_num(10, 11) == 10
assert choose_num(10, 15) == 14
assert choose_num(10, 14) == 14
assert choose_num(10, 13) == 12
assert choose_num(10, 25) == 24
assert choose_num(10, 26) == 26
assert choose_num(5,  25) == 24
assert choose_num(5,  26) == 26
assert choose_num(1,  1)  == -1
assert choose_num(1,  -1) == -1
assert choose_num(4,  1)  == -1
assert choose_num(4,  0)  == -1
assert choose_num(4,  -5) == -1
assert choose_num(3, 12) == 12
assert choose_num(0, 6) == 6
assert choose_num(0, 4) == 4
assert choose_num(2, 2) == 2
assert choose_num(4, 4) == 4
assert choose_num(6, 9) == 8
assert choose_num(6, 13) == 12
assert choose_num(6, 15) == 14
assert choose_num(6, 17) == 16
assert choose_num(6, 19) == 18
assert choose_num(5, 6) == 6
assert choose_num(7, 9) == 8
assert choose_num(9, 11) == 10
assert choose_num(2, 3) == 2
assert choose_num(7, 7) == -1
assert choose_num(15, 16) == 16
assert choose_num(100, 99) == -1
assert choose_num(3, 8) == 8
assert choose_num(3, 4) == 4
assert choose_num(10, 19) == 18
assert choose_num(2, 4) == 4
assert choose_num(1, 0) == -1
assert choose_num(0, -3) == -1
assert choose_num(1, 9) == 8
assert choose_num(8, 13) == 12
assert choose_num(8, 15) == 14
assert choose_num(9, 17) == 16
assert choose_num(9, 19) == 18
assert choose_num(100, 1000) == 1000
assert choose_num(100, 500) == 500
assert choose_num(0, 2) == 2
assert choose_num(0, 10) == 10
assert choose_num(0, 11) == 10
assert choose_num(0, 15) == 14
assert choose_num(0, 20) == 20
assert choose_num(3, 15) == 14
assert choose_num(3, 20) == 20
assert choose_num(3, 21) == 20
assert choose_num(1, 7) == 6
assert choose_num(10, 18) == 18
assert choose_num(4, 6) == 6
assert choose_num(8, 8) == 8
assert choose_num(11, 11) == -1
assert choose_num(9, 24) == 24
assert choose_num(19, 19) == -1
assert choose_num(5, 3) == -1
assert choose_num(2, 3) == 2, "test failed"
assert choose_num(1, 2) == 2, "test failed"
assert choose_num(1, 4) == 4, "test failed"
assert choose_num(2, 6) == 6, "test failed"
assert choose_num(1, 10) == 10, "test failed"
assert choose_num(0, 100) == 100
assert choose_num(0, 0) == 0
assert choose_num(0, -1) == -1
assert choose_num(-1, -1) == -1
assert choose_num(5, 13) == 12
assert choose_num(5, 15) == 14
assert choose_num(5, 17) == 16
assert choose_num(5, 19) == 18
assert choose_num(3, 19) == 18
assert choose_num(12, 12) == 12
assert choose_num(9, 7) == -1
assert choose_num(100, 125) == 124
assert choose_num(100, 111) == 110
assert ( choose_num(5, 10) == 10 )
assert ( choose_num(1, 10) == 10 )
assert ( choose_num(2, 3) == 2 )
assert ( choose_num(3, 2) == -1 )
assert ( choose_num(0, 3) == 2 )
assert ( choose_num(5, 7) == 6 )
assert ( choose_num(5, 6) == 6 )
assert choose_num(12, 16) == 16
assert choose_num(10, 20) == 20
assert choose_num(2, 5) == 4, "test failed"
assert choose_num(3, 5) == 4, "test failed"
assert choose_num(3, 9) == 8, "test failed"
assert choose_num(2, 2) == 2, "test failed"
assert choose_num(3, 2) == -1, "test failed"
assert choose_num(1, 1) == -1, "test failed"
assert choose_num(8, 8) == 8, "test failed"
assert choose_num(0, 9) == 8, "test failed"
assert choose_num(7, 20) == 20
assert choose_num(9, 15) == 14
assert choose_num(0, 12) == 12
assert choose_num(1, 3) == 2
assert choose_num(1, 6) == 6
assert choose_num(6, 11) == 10
assert choose_num(6, 12) == 12
assert choose_num(7, 15) == 14
assert choose_num(3, 17) == 16
assert choose_num(2,2) == 2
assert choose_num(1,7) == 6
assert choose_num(2,10) == 10
assert choose_num(1,1) == -1
assert choose_num(2,1) == -1
assert choose_num(5,5) == -1
assert choose_num(20,21) == 20
assert choose_num(1, 20) == 20
assert choose_num(20, 20) == 20
assert choose_num(11, 20) == 20
assert choose_num(0, -5) == -1
assert choose_num(3, 2) == -1
assert choose_num(0, 1) == 0
assert choose_num(6, 8) == 8
assert choose_num(8, 7) == -1
assert choose_num(16, 4) == -1
assert choose_num(2, 10) == 10
assert choose_num(11, 10) == -1
assert choose_num(25, 27) == 26
assert choose_num(6, 7) == 6
assert choose_num(19, 20) == 20
assert choose_num(0, 9) == 8
assert choose_num(1, -1) == -1
assert choose_num(12, 100) == 100
assert choose_num(7, 1) == -1
assert choose_num(1, 4) == 4, "test 2 failed"
assert choose_num(2, 10) == 10, "test 4 failed"
assert choose_num(6, 7) == 6, "test 6 failed"
assert choose_num(1, 6) == 6, "test 7 failed"
assert choose_num(4, 3) == -1
assert choose_num(5, 7) == 6
assert choose_num(6, 6) == 6
assert choose_num(0, -2) == -1
assert choose_num(0, -10) == -1
assert choose_num(1, 4) == 4
assert choose_num(2, 1) == -1
assert choose_num(22, 22) == 22
assert choose_num(100, 200) == 200
assert choose_num(100, 100) == 100
assert choose_num(1, 8) == 8
assert choose_num(0, 3) == 2
assert choose_num(0, 7) == 6
assert choose_num(0, 8) == 8
assert choose_num(0, 13) == 12
assert choose_num(0, 14) == 14
assert choose_num(0, 16) == 16
assert choose_num(0, 17) == 16
assert choose_num(0, 18) == 18
assert choose_num(0, 19) == 18
assert choose_num(0, 21) == 20
assert choose_num(0, 22) == 22
assert choose_num(0, 23) == 22
assert choose_num(0, 24) == 24
assert choose_num(9, 21) == 20
assert choose_num(4, 17) == 16
assert choose_num(18, 18) == 18
assert choose_num(1, 15) == 14
assert choose_num(14, 10) == -1
assert choose_num(45, 68) == 68
assert choose_num(0, 30) == 30
assert choose_num(29, 30) == 30
assert choose_num(6, 10) == 10
assert choose_num(21, 21) == -1
assert choose_num(10, 30) == 30
assert choose_num(3, 0) == -1
assert choose_num(1000, 1001) == 1000
assert choose_num(1, 10) == 10
assert choose_num(12, 13) == 12
assert choose_num(11, 13) == 12
assert choose_num(13, 10) == -1
assert choose_num(1, 30) == 30
assert choose_num(2, 30) == 30
assert choose_num(30, 30) == 30
assert choose_num(31, 31) == -1
assert choose_num(-3, -2) == -2
assert choose_num(5, 4) == -1
assert choose_num(24, 24) == 24
assert choose_num(12, 21) == 20
assert choose_num(100, 104) == 104
assert choose_num(100, 95) == -1
assert choose_num(15, 15) == -1
assert choose_num(15, 17) == 16
assert choose_num(15, 20) == 20
assert choose_num(15, 21) == 20
assert choose_num(15, 24) == 24
assert choose_num(15, 25) == 24
assert choose_num(15, 28) == 28
assert choose_num(15, 29) == 28
assert choose_num(15, 32) == 32
assert choose_num(4, 11) == 10
assert choose_num(13, 1) == -1
assert choose_num(0,2) == 2
assert choose_num(2,3) == 2
assert choose_num(2,4) == 4
assert choose_num(2,5) == 4
assert choose_num(3,3) == -1
assert choose_num(3,5) == 4
assert choose_num(2,1000) == 1000
assert choose_num(100,1000) == 1000
assert choose_num(1001,1000) == -1
assert choose_num(2, 20) == 20
assert choose_num(4, 20) == 20
assert choose_num(8, 20) == 20
assert choose_num(1, 17) == 16
assert choose_num(1, 19) == 18
assert choose_num(7, 14) == 14
assert choose_num(21, 30) == 30
assert choose_num(20, 30) == 30
assert choose_num(60, 80) == 80
assert choose_num(40, 80) == 80
assert choose_num(14, 13) == -1
assert choose_num(100, 5) == -1
assert choose_num(300, 300) == 300
assert choose_num(300, 200) == -1
assert choose_num(2, 9) == 8
assert choose_num(2, 15) == 14
assert choose_num(2, 14) == 14
assert choose_num(3, 14) == 14
assert choose_num(7, 8) == 8
assert choose_num(2, 12) == 12
assert choose_num(7, 12) == 12
assert choose_num(10, 21) == 20
assert choose_num(10, 22) == 22
assert choose_num(10, 23) == 22
assert choose_num(19, 23) == 22
assert choose_num(19, 25) == 24
assert choose_num(3, 10) == 10
assert choose_num(5, 20) == 20
assert choose_num(2, 21) == 20
assert choose_num(123, 50) == -1
assert choose_num(4, 7) == 6
assert choose_num(11, 21) == 20
assert choose_num(5, 2) == -1
