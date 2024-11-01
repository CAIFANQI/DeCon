
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
assert 	x_or_y(4, 5, 7) == 7, 'x_or_y is broken'
assert 	x_or_y(3, "3", "3") == "3"
assert 	x_or_y(1, "x", "x") == "x"
assert 	x_or_y(2, "x", "x") == "x"
assert 	x_or_y(3, "x", "x") == "x"
assert 	x_or_y(2, "x", "y") == "x"
assert 	x_or_y(3, "x", "y") == "x"
assert 	x_or_y(1, "y", "y") == "y"
assert 	x_or_y(2, "y", "y") == "y"
assert 	x_or_y(11, 10, 11) == 10
assert 	x_or_y(13, 13, 12) == 13
assert 	x_or_y(7, 7, 7) == 7
assert 	x_or_y(10, 10, 10) == 10
assert 	x_or_y(5, 6, 5) == 6
assert 	x_or_y(5, 5, 5) == 5
assert 	x_or_y(6, 5, 6) == 6
assert 	x_or_y(7, 3, 7) == 3
assert 	x_or_y(6, 3, 7) == 7
assert 	x_or_y(3, 3, 7) == 3
assert 	x_or_y(4, 3, 7) == 7
assert 	x_or_y(5, 3, 7) == 3
assert 	x_or_y(1, 3, 7) == 7
assert 	x_or_y(7, 3, 3) == 3
assert x_or_y(5, 2, 3) == 2
