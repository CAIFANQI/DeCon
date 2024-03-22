

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if n < 1:
        return False
    for k in range(1, n - 1):
        if n % k == 0:
            return False
    return True
assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(5) == True
assert is_prime(7) == True
assert is_prime(11) == True
assert is_prime(13) == True
assert is_prime(17) == True
assert is_prime(19) == True
assert is_prime(23) == True
assert is_prime(29) == True
assert is_prime(31) == True
assert is_prime(37) == True
assert is_prime(41) == True
assert is_prime(43) == True
assert is_prime(47) == True
assert is_prime(53) == True
assert is_prime(59) == True
assert is_prime(61) == True
assert is_prime(67) == True
assert is_prime(71) == True
assert is_prime(73) == True
assert is_prime(79) == True
assert is_prime(83) == True
assert is_prime(89) == True
assert is_prime(97) == True
assert is_prime(101) == True
assert is_prime(103) == True
assert is_prime(107) == True
assert is_prime(109) == True
assert is_prime(113) == True
assert is_prime(3) == True, "Test case 2 failed"
assert is_prime(5) == True, "Test case 4 failed"
assert is_prime(2) == True, "Test case 2 failed"
assert is_prime(3) == True, "Test case 3 failed"
assert is_prime(5) == True, "Test case 5 failed"
assert is_prime(7) == True, "Test case 7 failed"
assert is_prime(3) == True, 'Test Case 2 Failed'
assert is_prime(5) == True, 'Test Case 4 Failed'
assert is_prime(7) == True, 'Test Case 6 Failed'
assert is_prime(11) == True, 'Test Case 10 Failed'
assert is_prime(13) == True, 'Test Case 12 Failed'
assert is_prime(17) == True, 'Test Case 16 Failed'
assert is_prime(19) == True, 'Test Case 18 Failed'
assert is_prime(23) == True, 'Test Case 22 Failed'
assert is_prime(29) == True, 'Test Case 28 Failed'
assert is_prime(31) == True, 'Test Case 30 Failed'
assert is_prime(11) == True, "Test case 11 failed"
assert is_prime(13) == True, "Test case 13 failed"
assert is_prime(17) == True, "Test case 17 failed"
assert is_prime(19) == True, "Test case 19 failed"
