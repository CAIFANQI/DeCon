
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        i *= n
        fact_i *= i
        special_fact *= fact_i
    return special_fact
assert special_factorial(2) == 2
assert special_factorial(3) == 12
assert special_factorial(4) == 288
assert special_factorial(5) == 34560
assert special_factorial(6) == 24883200
assert special_factorial(2) == 2, "Error: Test Case 2"
assert special_factorial(3) == 12, "Error: Test Case 3"
assert special_factorial(4) == 288, "Error: Test Case 4"
assert special_factorial(5) == 34560, "Error: Test Case 5"
assert special_factorial(6) == 24883200, "Error: Test Case 6"
assert special_factorial(1) == 1
assert special_factorial(7) == 125411328000
assert special_factorial(2) == 2, "Test case 2 failed"
assert special_factorial(3) == 12, "Test case 3 failed"
assert special_factorial(4) == 288, "Test case 4 failed"
assert special_factorial(5) == 34560, "Test case 5 failed"
