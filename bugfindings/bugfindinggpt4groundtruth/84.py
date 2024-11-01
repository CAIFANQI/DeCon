
def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    return bin([int(i) for i in str(N)][-1])[2:]
assert solve(0)
assert solve(1)
assert solve(2)
assert solve(3)
assert solve(4)
assert solve(5)
assert solve(6)
assert solve(7)
assert solve(8)
assert solve(9)
assert solve(10)
assert solve(11)
assert solve(12)
assert solve(13)
assert solve(14)
assert solve(15)
assert solve(16)
assert solve(17)
assert solve(18)
assert solve(19)
assert solve(20)
assert solve(21)
assert solve(22)
assert solve(23)
assert solve(24)
assert solve(25)
assert solve(26)
assert solve(27)
assert solve(28)
assert solve(29)
assert solve(30)
assert solve(31)
assert solve(32)
assert solve(5) == "101"
assert solve(2) == "10"
assert solve(3) == "11"
assert solve(4) == "100"
assert solve(6) == "110"
assert solve(7) == "111"
assert solve(8) == "1000"
assert solve(9) == "1001"
assert 	solve(1) == "1"
assert 	solve(0) == "0"
assert solve(1) == "1"
