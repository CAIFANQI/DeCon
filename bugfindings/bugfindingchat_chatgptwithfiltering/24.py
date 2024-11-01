

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in reversed(range(n)):
        if n - i == 0:
            return i
assert largest_divisor(10) == 5, "Test case 1 failed"
assert largest_divisor(15) == 5, "Test case 2 failed"
assert largest_divisor(21) == 7, "Test case 3 failed"
assert largest_divisor(100) == 50, "Test case 4 failed"
assert largest_divisor(15) == 5, 'Test Case 2 Failed'
assert largest_divisor(25) == 5, 'Test Case 3 Failed'
assert largest_divisor(50) == 25, 'Test Case 4 Failed'
assert largest_divisor(25) == 5, "Test case 2 failed"
assert largest_divisor(18) == 9, "Test case 3 failed"
assert largest_divisor(7) == 1, "Test case 4 failed"
assert largest_divisor(28) == 14, "Test case 3 failed"
assert largest_divisor(50) == 25, "Test case 4 failed"
assert largest_divisor(100) == 50, "Test case 5 failed"
assert largest_divisor(17) == 1, "Test case 3 failed"
assert largest_divisor(20) == 10, "Test case 4 failed"
assert largest_divisor(25) == 5, "Test case 3 failed"
assert largest_divisor(20) == 10, 'Test Case 3 Failed'
assert largest_divisor(25) == 5, 'Test Case 4 Failed'
assert largest_divisor(30) == 15, 'Test Case 5 Failed'
assert largest_divisor(15) == 5, "Error: Test Case 2"
assert largest_divisor(25) == 5, "Error: Test Case 3"
assert largest_divisor(30) == 15, "Error: Test Case 4"
assert largest_divisor(20) == 10
assert largest_divisor(7) == 1
assert largest_divisor(16) == 8
assert largest_divisor(16) == 8, "Test case 3 failed"
assert largest_divisor(50) == 25, "Error: Test Case 5"
assert largest_divisor(12) == 6
assert largest_divisor(15) == 5
assert largest_divisor(21) == 7, "Test case 2 failed"
assert largest_divisor(100) == 50, "Test case 3 failed"
assert largest_divisor(25) == 5
assert largest_divisor(30) == 15
assert largest_divisor(20) == 10, "Test case 3 failed"
assert largest_divisor(25) == 5, "Test case 4 failed"
assert largest_divisor(30) == 15, "Test case 5 failed"
assert largest_divisor(36) == 18, "Test case 4 failed"
assert largest_divisor(50) == 25, "Test case 5 failed"
assert largest_divisor(25) == 5, 'Test Case 2 Failed'
assert largest_divisor(36) == 18, 'Test Case 3 Failed'
assert largest_divisor(7) == 1, 'Test Case 4 Failed'
assert largest_divisor(28) == 14, "Test case 4 failed"
assert largest_divisor(33) == 11, "Test case 5 failed"
assert largest_divisor(30) == 15, "Test case 4 failed"
assert largest_divisor(17) == 1, "Test case 6 failed"
assert largest_divisor(100) == 50
assert largest_divisor(2) == 1
assert largest_divisor(3) == 1
assert largest_divisor(4) == 2
assert largest_divisor(5) == 1
assert largest_divisor(6) == 3
assert largest_divisor(8) == 4
assert largest_divisor(9) == 3
assert largest_divisor(10) == 5
assert largest_divisor(24) == 12, "Test case 2 failed"
assert largest_divisor(37) == 1, "Test case 3 failed"
assert largest_divisor(28) == 14
assert largest_divisor(28) == 14, 'Test Case 3 Failed'
assert largest_divisor(37) == 1, 'Test Case 4 Failed'
assert largest_divisor(7) == 1, "Test case 5 failed"
assert largest_divisor(100) == 50, 'Test Case 4 Failed'
assert largest_divisor(13) == 1, 'Test Case 5 Failed'
assert largest_divisor(40) == 20, "Test case 5 failed"
assert largest_divisor(50) == 25, "Test case 6 failed"
assert largest_divisor(50) == 25
assert largest_divisor(37) == 1, 'Test Case 5 Failed'
assert largest_divisor(100) == 50, "Error: Test Case 4"
assert largest_divisor(37) == 1, "Error: Test Case 5"
assert largest_divisor(21) == 7, 'Test Case 2 Failed'
assert largest_divisor(121) == 11, 'Test Case 5 Failed'
assert largest_divisor(21) == 7
assert largest_divisor(21) == 7, 'Test Case 3 Failed'
assert largest_divisor(36) == 18, "Test case 3 failed"
