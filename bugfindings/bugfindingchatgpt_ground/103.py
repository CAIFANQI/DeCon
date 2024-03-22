
def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation/(m - n)))
assert rounded_avg(20, 10) == -1, 'Test Case 5 Failed'
assert rounded_avg(10, 1) == -1, 'Test Case 3 Failed'
assert rounded_avg(10, 1) == -1
assert rounded_avg(5, 1) == -1
assert rounded_avg(20, 10) == -1
assert rounded_avg(8, 2) == -1
assert rounded_avg(10, 5) == -1
assert rounded_avg(15, 10) == -1, 'Test Case 6 Failed'
assert rounded_avg(8, 5) == -1, 'Test Case 5 Failed'
assert rounded_avg(10, 2) == -1
assert rounded_avg(3, 3) == '0b11'
assert rounded_avg(15, 10) == -1
assert rounded_avg(5, 5) == '0b101'
assert rounded_avg(10, 10) == '0b1010'
assert rounded_avg(20, 10) == -1, 'Test Case 4 Failed'
assert rounded_avg(20, 10) == -1, 'Test Case 6 Failed'
assert rounded_avg(9, 2) == -1
assert rounded_avg(200, 100) == -1
assert rounded_avg(10, 1) == -1  # n is greater than m, return -1
assert rounded_avg(3, 7) == '0b101'
assert rounded_avg(9, 13) == '0b1011'
assert rounded_avg(20, 10) == -1, "Test case 4 failed"
assert rounded_avg(2, 8) == '0b101'
assert rounded_avg(10, 9) == -1
