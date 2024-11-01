
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
assert special_factorial(1) == 1
assert special_factorial(3) == 12
assert special_factorial(4) == 288
assert special_factorial(5) == 34560
assert special_factorial(6) == 24883200
assert special_factorial(7) == 125411328000
assert special_factorial(0) == 1
assert special_factorial(2) == 2 * 1 * 1
assert special_factorial(2) == 2 * 1
assert special_factorial(5) == 120 * 24 * 6 * 2 * 1
assert special_factorial(6) == 720 * 120 * 24 * 6 * 2 * 1
assert special_factorial(4) == (24 * 6 * 2 * 1)
assert special_factorial(5) == (120 * 24 * 6 * 2 * 1)
assert special_factorial(0) == 1, "Factorial of 0 is 1"
assert special_factorial(1) == 1, "Factorial of 1 is 1"
assert special_factorial(4) == 288, "Try again"
assert special_factorial(5) == 120 * 24 * 6 * 2
assert (special_factorial(3) == 12)
assert (special_factorial(4) == 288)
assert (special_factorial(5) == 34560)
assert (special_factorial(6) == 24883200)
