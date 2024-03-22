
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
assert solve(1) == '1'
assert solve(0) == '0'
assert solve(0) == "0"
assert solve(1) == "1"
assert solve(0) == "0", "test 3 ng"
assert solve(1) == "1", "test 5 ng"
