
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 1:
        return y
    for i in range(2, n):
        if n % i - 1 == 0:
            return y
            break
    else:
        return x
assert x_or_y(3, 'x', 'y') == 'x'
assert x_or_y(4, 'x', 'y') == 'y'
assert x_or_y(6, 5, 7) == 7
assert x_or_y(2, 5, 7) == 5
assert x_or_y(9, 5, 7) == 7
assert x_or_y(31, 5, 7) == 5
assert x_or_y(16, 5, 7) == 7
assert x_or_y(11, 5, 7) == 5
assert x_or_y(17, 5, 7) == 5
assert x_or_y(2, 0, 1) == 0
assert x_or_y(3, 0, 1) == 0
assert x_or_y(4, 0, 1) == 1
assert x_or_y(5, 0, 1) == 0
assert x_or_y(10, 0, 1) == 1
assert x_or_y(10, 'x', 'y') == 'y'
assert x_or_y(2, 1, -1) == 1
assert x_or_y(3, 1, -1) == 1
assert x_or_y(4, 1, -1) == -1
assert x_or_y(5, 1, -1) == 1
assert x_or_y(6, 1, -1) == -1
assert x_or_y(7, 1, -1) == 1
assert x_or_y(8, 1, -1) == -1
assert x_or_y(9, 1, -1) == -1
assert x_or_y(10, 1, -1) == -1
assert x_or_y(2, 1, 0) == 1
assert x_or_y(3, 1, 0) == 1
assert x_or_y(5, 1, 0) == 1
assert x_or_y(4, 3, 4) == 4
assert x_or_y(9, 3, 4) == 4
assert x_or_y(10, 10, 11) == 11
assert x_or_y(4, 7, 11) == 11
assert x_or_y(7, 13, 17) == 13
assert x_or_y(9, 19, 23) == 23
assert x_or_y(10, 29, 31) == 31
assert x_or_y(4, 3, 4) == 4, 'incorrect value of x_or_y for 4'
assert x_or_y(5, 3, 4) == 3, 'incorrect value of x_or_y for 5'
assert x_or_y(7, 3, 4) == 3, 'incorrect value of x_or_y for 7'
assert x_or_y(9, 3, 4) == 4, 'incorrect value of x_or_y for 9'
assert x_or_y(10, -1, 1) == 1
assert x_or_y(2, -1, 1) == -1
assert x_or_y(8, -1, 1) == 1
assert x_or_y(11, -1, 1) == -1
assert x_or_y(25, -1, 1) == 1
assert x_or_y(28, -1, 1) == 1
assert x_or_y(6, 12, 13) == 13
assert x_or_y(7, -1, 1) == -1
assert x_or_y(7, 'x', 'y') == 'x'
assert x_or_y(4, 5, 7) == 7
assert x_or_y(33, 5, 7) == 7
assert x_or_y(3, 3, 4) == 3
assert x_or_y(5, 3, 4) == 3
assert x_or_y(6, 3, 4) == 4
assert x_or_y(7, 3, 4) == 3
assert x_or_y(8, 3, 4) == 4
assert x_or_y(9, x=3, y=4) == 4
assert x_or_y(7, x=3, y=4) == 3
assert x_or_y(6, x=3, y=4) == 4
assert x_or_y(3, x=3, y=4) == 3
assert x_or_y(4, x=3, y=4) == 4
assert x_or_y(4, -1, 1) == 1
assert x_or_y(1000, 3, 4) == 4
assert x_or_y(2, 'x', 'y') == 'x'
assert x_or_y(11, 'x', 'y') == 'x'
assert x_or_y(27, 'x', 'y') == 'y'
assert x_or_y(2, "x", "y") == "x"
assert x_or_y(10, "x", "y") == "y"
assert x_or_y(15, "x", "y") == "y"
assert x_or_y(20, "x", "y") == "y"
assert x_or_y(25, "x", "y") == "y"
assert x_or_y(31, "x", "y") == "x"
assert x_or_y(199, "x", "y") == "x"
assert x_or_y(4, 5, 6) == 6
assert x_or_y(4, 2, 5) == 5
assert x_or_y(5, 2, 5) == 2
assert x_or_y(6, 2, 5) == 5
assert x_or_y(3, 2, 3) == 2
assert x_or_y(4, 2, 3) == 3
assert x_or_y(5, 2, 3) == 2
assert x_or_y(6, 2, 3) == 3
assert x_or_y(7, 2, 3) == 2
assert x_or_y(8, 2, 3) == 3
assert x_or_y(9, 2, 3) == 3
assert x_or_y(6, 1, 2) == 2
assert x_or_y(2, 3, 5) == 3
assert x_or_y(4, 3, 5) == 5
assert x_or_y(5, 'x', 'y') == 'x'
assert x_or_y(13, 'x', 'y') == 'x'
assert x_or_y(3, 1, 3) == 1
assert x_or_y(4, 1, 3) == 3
assert x_or_y(5, 1, 3) == 1
assert x_or_y(6, 1, 3) == 3
assert x_or_y(7, 1, 3) == 1
assert x_or_y(6, 100, 200) == 200
assert x_or_y(1000000, 100, 200) == 200
assert x_or_y(179426549, 100, 200) == 100
assert x_or_y(10, 7, -7) == -7
assert x_or_y(113, 91, 34) == 91
assert x_or_y(12, 1, 2) == 2
assert x_or_y(11, 1, 2) == 1
assert x_or_y(26, 1, 2) == 2
assert x_or_y(3, 1, 2) == 1
assert x_or_y(100, 3, 4) == 4
assert x_or_y(101, 3, 4) == 3
assert x_or_y(97, 5, 6) == 5
assert x_or_y(92, 5, 6) == 6
assert x_or_y(17, 10, 20) == 10
assert x_or_y(99, 1, 2) == 2
assert x_or_y(13, 5, 6) == 5
assert x_or_y(2, 'a', 'b') == 'a'
assert x_or_y(8, 'a', 'b') == 'b'
assert x_or_y(79, 'a', 'b') == 'a'
assert x_or_y(10, 10, 20) == 20
assert x_or_y(17, x=6, y=7) == 6
assert x_or_y(11, x = 5, y = 6) == 5
assert x_or_y(7, x = 5, y = 6) == 5
assert x_or_y(9, x = 5, y = 6) == 6
assert x_or_y(20, x = 5, y = 6) == 6
assert x_or_y(21, x = 5, y = 6) == 6
assert x_or_y(4, 3, 4) == 4, 'Short example of a failing test.'
assert x_or_y(4, 1, 2) == 2
assert x_or_y(17, 1, 2) == 1
assert x_or_y(78, 1, 2) == 2
assert x_or_y(15,12,21) == 21
assert x_or_y(3, "x", "y") == "x"
assert x_or_y(4, "x", "y") == "y"
assert x_or_y(5, "x", "y") == "x"
assert x_or_y(7, "x", "y") == "x"
assert x_or_y(15, 'x', 'y') == 'y'
assert x_or_y(24, 'x', 'y') == 'y'
assert x_or_y(29, 'x', 'y') == 'x'
assert x_or_y(121, 'x', 'y') == 'y'
assert x_or_y(625, 'x', 'y') == 'y'
assert x_or_y(1024, 'x', 'y') == 'y'
assert x_or_y(427920341, 'x', 'y') == 'y'
assert x_or_y(10, 2, 3) == 3
assert x_or_y(10, 3, 4) == 4
assert x_or_y(21, 3, 4) == 4
assert x_or_y(14, 2, 5) == 5
assert x_or_y(12, 2, 5) == 5
assert x_or_y(8, 100, 5) == 5
assert x_or_y(7, 100, 5) == 100
assert x_or_y(4,2,1) == 1
assert x_or_y(2,2,1) == 2
assert x_or_y(3, 3, 4) == 3, "Test fails"
assert x_or_y(4, 3, 4) == 4, "Test fails"
assert x_or_y(5, 3, 4) == 3, "Test fails"
assert x_or_y(6, 3, 4) == 4, "Test fails"
assert x_or_y(7, 3, 4) == 3, "Test fails"
assert x_or_y(15, 2, 3) == 3
assert x_or_y(17, 2, 3) == 2
assert x_or_y(6, 'x', 'y') == 'y'
assert x_or_y(8, 'x', 'y') == 'y'
assert x_or_y(9, 'x', 'y') == 'y'
assert x_or_y(4, 1, 5) == 5
assert x_or_y(7, 1, 5) == 1
assert x_or_y(56, 1, 5) == 5
assert x_or_y(37, 1, 5) == 1
assert x_or_y(7, 15, 2) == 15
assert x_or_y(7, "prime", "not prime") == "prime"
assert x_or_y(12, "prime", "not prime") == "not prime"
assert x_or_y(2, 10, 20) == 10
assert x_or_y(4, 10, 20) == 20
assert x_or_y(5, 10, 20) == 10
assert x_or_y(6, 10, 20) == 20
assert x_or_y(11, 10, 20) == 10
assert x_or_y(13, 10, 20) == 10
assert x_or_y(20, 10, 20) == 20
assert x_or_y(23, 10, 20) == 10
assert x_or_y(47, 10, 20) == 10
assert x_or_y(49, 10, 20) == 20
assert x_or_y(51, 10, 20) == 20
assert x_or_y(100, 10, 20) == 20
assert x_or_y(2, -1, -2) == -1
assert x_or_y(4, -1, -2) == -2
assert x_or_y(5, -1, -2) == -1
assert x_or_y(5, 1, 2) == 1
assert 10 == x_or_y(4, 5, 10)
assert x_or_y(2, "a", "b") == "a"
assert x_or_y(3, "a", "b") == "a"
assert x_or_y(4, "a", "b") == "b"
assert x_or_y(5, "a", "b") == "a"
assert x_or_y(6, "a", "b") == "b"
assert x_or_y(7, "a", "b") == "a"
assert x_or_y(8, "a", "b") == "b"
assert x_or_y(9, "a", "b") == "b"
assert x_or_y(10, "a", "b") == "b"
assert x_or_y(11, "a", "b") == "a"
assert x_or_y(12, "a", "b") == "b"
assert x_or_y(13, "a", "b") == "a"
assert x_or_y(14, "a", "b") == "b"
assert x_or_y(21, 'x', 'y') == 'y'
assert x_or_y(3, 2, 3) == 2, 'The number 3 is prime'
assert x_or_y(4, 2, 3) == 3, 'The number 4 is not prime'
assert x_or_y(5, 2, 3) == 2, 'The number 5 is prime'
assert x_or_y(6, 2, 3) == 3, 'The number 6 is not prime'
assert x_or_y(7, 2, 3) == 2, 'The number 7 is prime'
assert x_or_y(8, 2, 3) == 3, 'The number 8 is not prime'
assert x_or_y(9, 2, 3) == 3, 'The number 9 is not prime'
assert x_or_y(10, 2, 3) == 3, 'The number 10 is not prime'
assert x_or_y(15, 2, 3) == 3, 'The number 15 is not prime'
assert x_or_y(17, 2, 3) == 2, 'The number 17 is prime'
assert x_or_y(3, "1", "0") == "1"
assert x_or_y(3, -1, 1) == -1
assert x_or_y(6, -1, 1) == 1
assert x_or_y(9, -1, 1) == 1
assert x_or_y(30, -1, 1) == 1
assert x_or_y(37, -1, 1) == -1
assert x_or_y(41, -1, 1) == -1
assert x_or_y(40, -1, 1) == 1
assert x_or_y(50, -1, 1) == 1
assert x_or_y(15, 7, 10) == 10, 'second test'
assert x_or_y(2, 7, 10) == 7, 'third test'
assert x_or_y(19, 5, 9) == 5, 'fourth test'
assert x_or_y(20, 5, 9) == 9, 'fifth test'
assert x_or_y(2, 1, 2) == 1
assert x_or_y(2,1,1) == 1
assert x_or_y(3,1,1) == 1
assert x_or_y(4,1,1) == 1
assert x_or_y(5,1,1) == 1
assert x_or_y(6,1,1) == 1
assert x_or_y(7,1,1) == 1
assert x_or_y(8,1,1) == 1
assert x_or_y(9,1,1) == 1
assert x_or_y(10,1,1) == 1
assert x_or_y(11,1,1) == 1
assert x_or_y(12,1,1) == 1
assert x_or_y(13,1,1) == 1
assert x_or_y(14,1,1) == 1
assert x_or_y(15,1,1) == 1
assert x_or_y(16,1,1) == 1
assert x_or_y(17,1,1) == 1
assert x_or_y(18,1,1) == 1
assert x_or_y(19,1,1)
assert x_or_y(9, 2, 4) == 4
assert x_or_y(11, 2, 4) == 2
assert x_or_y(17, 2, 4) == 2
assert x_or_y(4, 2, 4) == 4
assert x_or_y(944, 2, 4) == 4
assert x_or_y(323, 2, 4) == 4
assert x_or_y(179426549, 2, 4) == 2
assert x_or_y(179486249, 2, 4) == 4
assert x_or_y(1299709, 2, 4) == 2
assert x_or_y(1299713, 2, 4) == 4
assert x_or_y(197, 2, 4) == 2
assert x_or_y(101, 2, 4) == 2
assert x_or_y(13, 3, 4) == 3
assert x_or_y(21, 1, 2) == 2
assert x_or_y(23, 3, 4) == 3
assert x_or_y(4, 4, 2) == 2
assert x_or_y(5, 8, 1) == 8
assert x_or_y(8, "x", "y") == "y"
assert x_or_y(9, "x", "y") == "y"
assert x_or_y(11, "x", "y") == "x"
assert x_or_y(7, 1, 2) == 1
assert x_or_y(8, 1, 2) == 2
assert x_or_y(9, 1, 2) == 2
assert x_or_y(3, 4, 5) == 4
assert x_or_y(5, 6, 7) == 6
assert x_or_y(7, 1, 0) == 1
assert x_or_y(3, 10, 20) == 10
assert x_or_y(7, 10, 20) == 10
assert x_or_y(8, 10, 20) == 20
assert x_or_y(9, 10, 20) == 20
assert x_or_y(7, "hello", "bye") == "hello"
assert x_or_y(10, 1, 2) == 2
assert x_or_y(13, 1, 0) == 1
assert x_or_y(10, 5, 20) == 20
assert x_or_y(2, 3, 10) == 3
assert x_or_y(18, 3, 4) == 4
assert x_or_y(17, 3, 4) == 3
assert x_or_y(11, 3, 4) == 3
assert x_or_y(3, x=12, y=13) == 12
assert x_or_y(4, x=12, y=13) == 13
assert x_or_y(5, x=12, y=13) == 12
assert x_or_y(6, x=12, y=13) == 13
assert x_or_y(7, x=12, y=13) == 12
assert x_or_y(8, x=12, y=13) == 13
assert x_or_y(9, x=12, y=13) == 13
assert x_or_y(10, x=12, y=13) == 13
assert x_or_y(42, 1, 2) == 2
assert x_or_y(2, 2, 3) == 2
assert x_or_y(17, 'x', 'y') == 'x'
assert x_or_y(19, x="pr", y="!pr") == "pr"
assert x_or_y(42, x=42, y=19) == 19
assert x_or_y(17, x=42, y=19) == 42
assert x_or_y(5, x=3, y=4) == 3
assert x_or_y(2, x=3, y=4) == 3
