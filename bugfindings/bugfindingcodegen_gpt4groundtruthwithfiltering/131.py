
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    odd_count = 0
    for digit in str(n):
        int_digit = int(digit)
        if int_digit%2 == 1:
            product*= product*int_digit
            odd_count+=1
    if odd_count ==0:
        return 0
    else:
        return product
assert digits(0) == 0
assert digits(1111) == 1
assert digits(8) == 0
assert digits(2) == 0
assert digits(4) == 0
assert digits(6) == 0
assert digits(3) == 3
assert digits(22) == 0
assert digits(24) == 0
assert digits(42) == 0
assert digits(64) == 0
assert digits(82) == 0
assert digits(44) == 0
assert digits(1) == 1
