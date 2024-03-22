
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
assert rounded_avg(100, 0) == -1
assert rounded_avg(4, 0) == -1.0
assert rounded_avg(3, 2) == -1
assert rounded_avg(7, 3) == -1
assert rounded_avg(9, 4) == -1
assert rounded_avg(9, 5) == -1
assert rounded_avg(9, 7) == -1
assert rounded_avg(10, 7) == -1
assert rounded_avg(13, 12) == -1
assert rounded_avg(15, 12) == -1
assert rounded_avg(16, 12) == -1
assert rounded_avg(17, 12) == -1
assert rounded_avg(19, 12) == -1
assert rounded_avg(19, 13) == -1
assert rounded_avg(20, 13) == -1
assert rounded_avg(22, 13) == -1
assert rounded_avg(23, 13) == -1
assert rounded_avg(23, 14) == -1
assert rounded_avg(23, 15) == -1
assert rounded_avg(23, 16) == -1
assert rounded_avg(23, 17) == -1
assert rounded_avg(6,5) == -1, 'Should be -1'
assert rounded_avg(10,0) == -1, 'Should be -1'
assert rounded_avg(10,1) == -1, 'Should be -1'
assert rounded_avg(10,5) == -1, 'Should be -1'
assert rounded_avg(5, 2) == -1
assert rounded_avg(1, 0) == -1
assert rounded_avg(51, 50) == -1
assert rounded_avg(200, 100) == -1
assert rounded_avg(10000, 1000) == -1
assert rounded_avg(2000000, 1000000) == -1
assert rounded_avg(1, -1) == -1
assert rounded_avg(100, -1) == -1
assert rounded_avg(0, -1) == -1
assert rounded_avg(5, 3) == -1
assert rounded_avg(7, 6) == -1
assert rounded_avg(10, 8) == -1
assert rounded_avg(4, 2) == -1
assert rounded_avg(6, 1) == -1.0
assert rounded_avg(5, 1) == -1.0, "Sixth test case failed!"
assert rounded_avg(6, 5) == -1
assert rounded_avg(9, 3) == -1
assert rounded_avg(9, 1) == -1
assert rounded_avg(9, 0) == -1
assert rounded_avg(2, 1) == -1.0
assert rounded_avg(6, 1) == -1
assert rounded_avg(7, 0) == -1
assert rounded_avg(7, 5) == -1
assert rounded_avg(5, 1) == -1
assert rounded_avg(7,0) == -1
assert rounded_avg(6,2) == -1.0
assert rounded_avg(7, 1) == -1
assert rounded_avg(7, 2) == -1
assert rounded_avg(9, 6) == -1.0
assert rounded_avg(100, 1) == -1
assert rounded_avg(100, 2) == -1
assert rounded_avg(100, 3) == -1
assert rounded_avg(15, 5) == -1
assert rounded_avg(21, 0) == -1
assert rounded_avg(11, 0) == -1
assert rounded_avg(10, -1) == -1
assert rounded_avg(20, 3) == -1
assert rounded_avg(20, 19) == -1
assert rounded_avg(50, 10) == -1
assert rounded_avg(6, 3) == -1
assert rounded_avg(5, -1) == -1
assert rounded_avg(100, 99) == -1
assert rounded_avg(10, 6) == -1
assert rounded_avg(99, 10) == -1
assert rounded_avg(16, 5) == -1
assert rounded_avg(14, 11) == -1
assert rounded_avg(10,8) == -1
assert rounded_avg(50000, 1) == -1
assert rounded_avg(1000, 10) == -1
assert rounded_avg(13, 2) == -1
assert rounded_avg(24, 10) == -1
assert rounded_avg(30, 15) == -1
