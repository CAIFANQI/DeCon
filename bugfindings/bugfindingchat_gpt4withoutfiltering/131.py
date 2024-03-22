
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
assert digits(2468) == 0
assert digits(222222) == 0
assert digits(2468642) == 0, "Test case 2 failed"
assert digits(86420) == 0
assert digits(246) == 0, 'Test Case 2 Failed'
assert digits(2468) == 0, "Test case 2 failed"
assert digits(246) == 0
assert digits(2468642) == 0
assert digits(2468) == 0, 'Test Case 2 Failed'
assert digits(24680) == 0, "Test case 2 failed"
assert digits(0) == 0, "Test case 5 failed"
assert digits(2468642) == 0, "Test case 4 failed"
assert digits(2468) == 0, "Error: Test Case 2"
assert digits(2468642) == 0, "Error: Test Case 5"
assert digits(2222222222) == 0
assert digits(24680) == 0, 'Test Case 2 Failed'
assert digits(24680) == 0
assert digits(246) == 0, "Test case 2 failed"
assert digits(2468642) == 0, 'Test Case 2 Failed'
assert digits(24680) == 0, "Error: Test Case 2"
assert digits(222) == 0
assert digits(0) == 0
assert digits(0) == 0, 'Test Case 5 Failed'
assert digits(22222222) == 0
assert digits(2222222) == 0
assert digits(24686420) == 0, "Test case 4 failed"
