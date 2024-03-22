
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
assert x_or_y(2, 5, 10) == 5
assert x_or_y(3, 5, 10) == 5
assert x_or_y(4, 5, 10) == 10
assert x_or_y(5, 5, 10) == 5
assert x_or_y(6, 5, 10) == 10
assert x_or_y(3, 3, 4) == 3
assert x_or_y(4, 3, 4) == 4
assert x_or_y(5, 3, 4) == 3
assert x_or_y(6, 3, 4) == 4
assert x_or_y(7, 3, 4) == 3
assert x_or_y(8, 3, 4) == 4
assert x_or_y(9, 3, 4) == 4
assert x_or_y(10, 3, 4) == 4
assert x_or_y(3, 3, 4) == 3, "Test case 2 failed"
assert x_or_y(4, 3, 4) == 4, "Test case 3 failed"
assert x_or_y(5, 3, 4) == 3, "Test case 4 failed"
assert x_or_y(6, 3, 4) == 4, "Test case 5 failed"
assert x_or_y(3, 3, 5) == 3
assert x_or_y(4, 3, 5) == 5
assert x_or_y(5, 3, 5) == 3
assert x_or_y(6, 3, 5) == 5
assert x_or_y(3, 3, 4) == 3, "Error: Test Case 2"
assert x_or_y(4, 3, 4) == 4, "Error: Test Case 3"
assert x_or_y(5, 3, 4) == 3, "Error: Test Case 4"
assert x_or_y(6, 3, 4) == 4, "Error: Test Case 5"
assert x_or_y(3, 5, 10) == 5, "Test case 2 failed"
assert x_or_y(4, 5, 10) == 10, "Test case 3 failed"
assert x_or_y(5, 5, 10) == 5, "Test case 4 failed"
assert x_or_y(6, 5, 10) == 10, "Test case 5 failed"
assert x_or_y(3, 10, 20) == 10
assert x_or_y(4, 10, 20) == 20
assert x_or_y(5, 10, 20) == 10
assert x_or_y(6, 10, 20) == 20
assert x_or_y(7, 3, 5) == 3
assert x_or_y(8, 3, 5) == 5
assert x_or_y(9, 3, 5) == 5
assert x_or_y(10, 3, 5) == 5
assert x_or_y(11, 3, 5) == 3
assert x_or_y(12, 3, 5) == 5
assert x_or_y(11, 3, 4) == 3
assert x_or_y(12, 3, 4) == 4
assert x_or_y(7, 5, 10) == 5
assert x_or_y(8, 5, 10) == 10
assert x_or_y(9, 5, 10) == 10
assert x_or_y(10, 5, 10) == 10
assert x_or_y(4, 2, 3) == 3
assert x_or_y(4, 3, 4) == 4  # since 4 is not a prime number, y should be returned
assert x_or_y(11, 3, 4) == 3  # since 11 is a prime number, x should be returned
assert x_or_y(15, 3, 4) == 4  # since 15 is not a prime number, y should be returned
assert x_or_y(3, 4, 6) == 4, "Test case 2 failed"
assert x_or_y(4, 4, 6) == 6, "Test case 3 failed"
assert x_or_y(5, 4, 6) == 4, "Test case 4 failed"
assert x_or_y(6, 4, 6) == 6, "Test case 5 failed"
assert x_or_y(4, 1, 2) == 2, "Test case 2 failed"
assert x_or_y(5, 1, 2) == 1, "Test case 3 failed"
assert x_or_y(6, 1, 2) == 2, "Test case 4 failed"
assert x_or_y(7, 1, 2) == 1, "Test case 5 failed"
assert x_or_y(3, 3, 5) == 3, 'Test Case 2 Failed'
assert x_or_y(4, 3, 5) == 5, 'Test Case 3 Failed'
assert x_or_y(5, 3, 5) == 3, 'Test Case 4 Failed'
assert x_or_y(6, 3, 5) == 5, 'Test Case 5 Failed'
assert x_or_y(7, 3, 4) == 3, "Test case 6 failed"
assert x_or_y(3, 3, 4) == 3, 'Test Case 2 Failed'
assert x_or_y(4, 3, 4) == 4, 'Test Case 3 Failed'
assert x_or_y(5, 3, 4) == 3, 'Test Case 4 Failed'
assert x_or_y(6, 3, 4) == 4, 'Test Case 5 Failed'
assert x_or_y(13, 3, 4) == 3
assert x_or_y(3, 1, 2) == 1
assert x_or_y(4, 1, 2) == 2
assert x_or_y(5, 1, 2) == 1
assert x_or_y(6, 1, 2) == 2
assert x_or_y(5, 2, 3) == 2
assert x_or_y(6, 2, 3) == 3
assert x_or_y(7, 2, 3) == 2
assert x_or_y(8, 2, 3) == 3
assert x_or_y(7, 1, 2) == 1
assert x_or_y(8, 1, 2) == 2
assert x_or_y(9, 1, 2) == 2
assert x_or_y(10, 1, 2) == 2
assert x_or_y(3, 10, 20) == 10, "Test case 2 failed"
assert x_or_y(4, 10, 20) == 20, "Test case 3 failed"
assert x_or_y(5, 10, 20) == 10, "Test case 4 failed"
assert x_or_y(6, 10, 20) == 20, "Test case 5 failed"
assert x_or_y(4, 3, 4) == 4  # n = 4, which is not prime, so return y = 4
assert x_or_y(7, 3, 4) == 3  # n = 7, which is prime, so return x = 3
assert x_or_y(9, 3, 4) == 4  # n = 9, which is not prime, so return y = 4
assert x_or_y(3, 4, 5) == 4
assert x_or_y(4, 4, 5) == 5
assert x_or_y(5, 4, 5) == 4
assert x_or_y(6, 4, 5) == 5
assert x_or_y(7, 4, 5) == 4
assert x_or_y(8, 4, 5) == 5
assert x_or_y(9, 4, 5) == 5
assert x_or_y(3, 5, 6) == 5, "Test case 2 failed"
assert x_or_y(4, 7, 8) == 8, "Test case 3 failed"
assert x_or_y(5, 9, 10) == 9, "Test case 4 failed"
assert x_or_y(6, 11, 12) == 12, "Test case 5 failed"
assert x_or_y(13, 4, 5) == 4
assert x_or_y(15, 4, 5) == 5
assert x_or_y(3, 3, 5) == 3, "Test case 2 failed"
assert x_or_y(4, 3, 5) == 5, "Test case 3 failed"
assert x_or_y(5, 3, 5) == 3, "Test case 4 failed"
assert x_or_y(6, 3, 5) == 5, "Test case 5 failed"
assert x_or_y(7, 3, 5) == 3, "Test case 6 failed"
