
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
assert special_factorial(1) == 1 
assert special_factorial(3) == 3 * 4
assert special_factorial(1) == 1
assert special_factorial(2) == 2 * 1
assert special_factorial(2) == 2
assert special_factorial(2) == 2*1
assert special_factorial(3) == 6*2*1
assert special_factorial(4) == 24*6*2*1
assert special_factorial(5) == 120*24*6*2*1
assert special_factorial(6) == 720*120*24*6*2*1
assert special_factorial(7) == 5040*720*120*24*6*2*1
assert special_factorial(8) == 40320*5040*720*120*24*6*2*1
assert special_factorial(9) == 362880*40320*5040*720*120*24*6*2*1
assert special_factorial(10) == 3628800*362880*40320*5040*720*120*24*6*2*1
assert special_factorial(2) == 2, "Special factorial of 2 is incorrect."
assert special_factorial(2) == 2, 'Incorrect output'
assert special_factorial(1) == 1, "Error with the factorial of 1, should be 1"
assert special_factorial(2) == 2, "Error with the factorial of 2, should be 2"
assert special_factorial(1) == 1 #1! = 1
assert special_factorial(2) == 2 
assert special_factorial(2) == 2, 'Check your function input'
assert special_factorial(2) == 2 # factorial of 2 is 2
assert special_factorial(2) == 2, "2 must equal 2!"
assert special_factorial(2) == 2, 'Special factorial should be 2'
assert special_factorial(1) == 1 # the factorial of 1 must be 1
assert special_factorial(2) == 2 # the factorial of 2 must be 2
