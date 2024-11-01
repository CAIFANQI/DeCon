
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
assert solve(0) == '0'
assert solve(1) == '1'
assert solve(2) == '10'
assert solve(9) == '1001'
assert solve(1) == '1', 'Test Case 2 Failed'
assert solve(2) == '10', 'Test Case 3 Failed'
assert solve(3) == '11', 'Test Case 4 Failed'
assert solve(4) == '100', 'Test Case 5 Failed'
assert solve(5) == '101', 'Test Case 6 Failed'
assert solve(3) == '11'
assert solve(4) == '100'
assert solve(5) == '101'
assert solve(6) == '110'
assert solve(7) == '111'
assert solve(8) == '1000'
assert solve(1) == "1"
