
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
assert rounded_avg(10, 3) == -1
assert rounded_avg(3, 2) == -1, "Error in rounded_avg"
assert rounded_avg(3, -2) == -1, "Error in rounded_avg"
assert rounded_avg(7, 3) == -1
assert rounded_avg(13, 6) == -1, "13-6"
assert rounded_avg(30, 16) == -1, "30-16"
assert rounded_avg(50, 15) == -1, "50-15"
assert rounded_avg(5, 3) == -1
assert rounded_avg(15, 10) == -1
assert rounded_avg(11, 8) == -1
assert rounded_avg(1, 4) == "0b10"
assert rounded_avg(2, 3) == "0b10"
assert rounded_avg(5, 2) == -1
assert rounded_avg(10,2) == -1
assert rounded_avg(23,16) == -1
assert rounded_avg(3,1) == -1
assert rounded_avg(5,3) == -1, "Test 4 failed"
assert rounded_avg(200, 100) == -1
assert rounded_avg(13, 5) == -1
assert rounded_avg(1, 0) == -1
assert rounded_avg(10, 5) == -1
assert rounded_avg(6, 2) == -1
assert rounded_avg(6,1) == -1
assert rounded_avg(7, 5) == -1
assert rounded_avg(2, 1) == -1
assert rounded_avg(0, -5) == -1
assert rounded_avg(2, 2) == "0b10"
assert rounded_avg(10, 1) == -1
assert rounded_avg(3, 3) == "0b11"
assert rounded_avg(5, 5) == "0b101"
assert rounded_avg(1, 1) == "0b1"
assert rounded_avg(9, 5) == -1
assert rounded_avg(14, 6) == -1
assert rounded_avg(19, 2) == -1
assert rounded_avg(5, 4) == -1
assert rounded_avg(10, 4) == -1
assert rounded_avg(8, 3) == -1
assert rounded_avg(11, 7) == -1
assert rounded_avg(10, 8) == -1
assert rounded_avg(8, 5) == -1
assert rounded_avg(3,2) == -1
assert (rounded_avg(10, 5) == -1)
assert rounded_avg(7, 4) == -1
assert rounded_avg(1,8) == '0b100'
assert rounded_avg(5,5) == '0b101'
assert rounded_avg(8,1) == -1
assert rounded_avg(4, 1) == -1
assert rounded_avg(8, 4) == -1
assert rounded_avg(3, 2) == -1
assert rounded_avg(9, 8) == -1
assert rounded_avg(0, 1) == '0b0'
assert rounded_avg(0, 0) == '0b0'
assert rounded_avg(1, 1) == '0b1'
assert rounded_avg(20, 4) == -1
assert rounded_avg(100, 1) == -1
assert rounded_avg(12, 10) == -1
assert rounded_avg(7, 2) == -1
assert rounded_avg(6, 4) == -1
assert rounded_avg(8, 7) == -1
assert rounded_avg(4, 2) == -1
assert rounded_avg(9, 6) == -1
assert rounded_avg(30, 20) == -1
assert rounded_avg(3, 13) == '0b1000'
assert rounded_avg(13, 3) == -1
assert rounded_avg(20, 20) == '0b10100'
assert rounded_avg(10, 9) == -1
assert rounded_avg(100,1) == -1
assert rounded_avg(9, 3) == -1
assert rounded_avg(7,2) == -1
assert rounded_avg(15, 11) == -1
assert rounded_avg(17, 0) == -1
assert rounded_avg(6, 4) == -1 # m < n --> error
assert rounded_avg(6, 5) == -1 # m < n --> error
assert rounded_avg(5, 1) == -1
assert rounded_avg(1, 10) == '0b110'
assert rounded_avg(14, 10) == -1
assert rounded_avg(21, 10) == -1
assert rounded_avg(10,5) == -1
assert rounded_avg(25, 20) == -1
assert rounded_avg(2, -5) == -1
assert rounded_avg(19, 0) == -1
assert rounded_avg(20, 19) == -1
assert rounded_avg(13, 12) == -1
assert rounded_avg(11, 5) == -1
assert rounded_avg(15, 1) == -1, 'wrong test case'
assert rounded_avg(2, 0) == -1, 'wrong test case'
assert rounded_avg(2,2) == '0b10'
assert rounded_avg(4,4) == '0b100'
assert rounded_avg(3,3) == '0b11'
assert rounded_avg(10,1) == -1
assert rounded_avg(10,10) == '0b1010'
assert rounded_avg(15,10) == -1
assert rounded_avg(1,1) == '0b1'
assert rounded_avg(100,100) == '0b1100100'
assert rounded_avg(100,99) == -1
assert rounded_avg(15, 15) == bin(15)
assert rounded_avg(15, 17) == bin(16)
assert rounded_avg(20, 22) == bin(21)
assert rounded_avg(100, 200) == bin(150)
