
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
assert digits(123) == 3
assert digits(2468) == 0
assert digits(111111) == 1
assert digits(1357) == 105
assert digits(11111) == 1
assert digits(222222) == 0
assert digits(2468642) == 0, "Test case 2 failed"
assert digits(13579) == 945, "Test case 3 failed"
assert digits(86420) == 0
assert digits(246) == 0, 'Test Case 2 Failed'
assert digits(13579) == 945, 'Test Case 3 Failed'
assert digits(246813579) == 945, 'Test Case 5 Failed'
assert digits(2468) == 0, "Test case 2 failed"
assert digits(11111111) == 1, "Test case 5 failed"
assert digits(13579) == 945
assert digits(246813579) == 945
assert digits(111111) == 1, "Test case 5 failed"
assert digits(987654321) == 945, "Test case 4 failed"
assert digits(246) == 0
assert digits(2468642) == 0
assert digits(111111111) == 1
assert digits(987654321) == 945
assert digits(2468) == 0, 'Test Case 2 Failed'
assert digits(13579) == 1 * 3 * 5 * 7 * 9, 'Test Case 3 Failed'
assert digits(111111) == 1 * 1 * 1 * 1 * 1 * 1, 'Test Case 4 Failed'
assert digits(246813579) == 1 * 3 * 5 * 7 * 9, 'Test Case 5 Failed'
assert digits(24680) == 0, "Test case 2 failed"
assert digits(11111) == 1, "Test case 4 failed"
assert digits(24681357) == 105, "Test case 5 failed"
assert digits(0) == 0, "Test case 5 failed"
assert digits(13579) == 3 * 5 * 7 * 9
assert digits(2468642) == 0, "Test case 4 failed"
assert digits(11111) == 1, "Test case 5 failed"
assert digits(13579) == 1 * 3 * 5 * 7 * 9, "Test case 3 failed"
assert digits(11111) == 1 * 1 * 1 * 1 * 1, "Test case 4 failed"
assert digits(1111111111) == 1, 'Test Case 5 Failed'
assert digits(2468) == 0, "Error: Test Case 2"
assert digits(111111) == 1, "Error: Test Case 4"
assert digits(24681357) == 105, "Error: Test Case 5"
assert digits(13579) == 945, "Error: Test Case 3"
assert digits(11111) == 1, "Error: Test Case 4"
assert digits(2468642) == 0, "Error: Test Case 5"
assert digits(1111111111) == 1
assert digits(2222222222) == 0
assert digits(24680) == 0, 'Test Case 2 Failed'
assert digits(1111) == 1
assert digits(1111111111111111111111111) == 1
assert digits(24680) == 0
assert digits(246) == 0, "Test case 2 failed"
assert digits(24681357) == 105, "Test case 4 failed"
assert digits(2468642) == 0, 'Test Case 2 Failed'
assert digits(246813579) == 945, 'Test Case 4 Failed'
assert digits(24680) == 0, "Error: Test Case 2"
assert digits(13579) == 1 * 3 * 5 * 7 * 9
assert digits(24681357) == 1 * 3 * 5 * 7
assert digits(13579) == 1*3*5*7*9, 'Test Case 3 Failed'
assert digits(987654321) == 945, "Error: Test Case 4"
assert digits(246813579) == 945, "Error: Test Case 5"
assert digits(246135) == 15
assert digits(111111) == 1, "Test case 4 failed"
assert digits(13579) == 1 * 3 * 5 * 7 * 9, "Error: Test Case 3"
assert digits(111111) == 1 * 1 * 1 * 1 * 1 * 1, "Error: Test Case 4"
assert digits(24681357) == 3 * 5 * 7, "Error: Test Case 5"
assert digits(987654321) == 945, 'Test Case 4 Failed'
assert digits(111) == 1
assert digits(222) == 0
assert digits(0) == 0
assert digits(24681357) == 105, 'Test Case 4 Failed'
assert digits(0) == 0, 'Test Case 5 Failed'
assert digits(11111111) == 1
assert digits(22222222) == 0
assert digits(1111111) == 1
assert digits(2222222) == 0
assert digits(111111) == 1, 'Test Case 4 Failed'
assert digits(24686420) == 0, "Test case 4 failed"
assert digits(1111) == 1, 'Test Case 4 Failed'
