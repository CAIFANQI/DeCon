
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
    return (even_count, odd_count)
assert even_odd_count(123456) == (3, 3)
assert even_odd_count(2468) == (4, 0)
assert even_odd_count(13579) == (0, 5)
assert even_odd_count(111111) == (0, 6)
assert even_odd_count(246813579) == (4, 5)
assert even_odd_count(24680) == (5, 0)
assert even_odd_count(0) == (1, 0)
assert even_odd_count(2468642) == (7, 0)
assert even_odd_count(1111111111) == (0, 10)
assert even_odd_count(2468) == (4, 0), 'Test Case 2 Failed'
assert even_odd_count(13579) == (0, 5), 'Test Case 3 Failed'
assert even_odd_count(0) == (1, 0), 'Test Case 4 Failed'
assert even_odd_count(111) == (0, 3), 'Test Case 5 Failed'
assert even_odd_count(24680) == (5,0), "Test case 2 failed"
assert even_odd_count(13579) == (0,5), "Test case 3 failed"
assert even_odd_count(0) == (1,0), "Test case 4 failed"
assert even_odd_count(1111111) == (0,7), "Test case 5 failed"
assert even_odd_count(222222) == (6, 0)
assert even_odd_count(123456789) == (4, 5)
assert even_odd_count(135792468) == (4, 5)
assert even_odd_count(111111111) == (0, 9)
assert even_odd_count(222222222) == (9, 0)
assert even_odd_count(24680) == (5,0)
assert even_odd_count(13579) == (0,5)
assert even_odd_count(0) == (1,0)
assert even_odd_count(11111) == (0,5)
assert even_odd_count(135792468) == (4, 5), 'Test Case 3 Failed'
assert even_odd_count(111111111) == (0, 9), 'Test Case 4 Failed'
assert even_odd_count(222222222) == (9, 0), 'Test Case 5 Failed'
assert even_odd_count(1234567890) == (5, 5)
assert even_odd_count(24681357) == (4, 4)
assert even_odd_count(11111111) == (0, 8)
assert even_odd_count(246) == (3, 0)
assert even_odd_count(111) == (0, 3)
assert even_odd_count(88888888) == (8, 0)
assert even_odd_count(12345) == (2, 3)
assert even_odd_count(11111) == (0, 5)
assert even_odd_count(1111) == (0, 4)
assert even_odd_count(9876543210) == (5, 5)
assert even_odd_count(22222) == (5, 0)
assert even_odd_count(2222222) == (7, 0)
assert even_odd_count(3333333) == (0, 7)
assert even_odd_count(4444444) == (7, 0)
assert even_odd_count(5555555) == (0, 7)
assert even_odd_count(6666666) == (7, 0)
assert even_odd_count(7777777) == (0, 7)
assert even_odd_count(8888888) == (7, 0)
assert even_odd_count(9999999) == (0, 7)
assert even_odd_count(1111111) == (0, 7)
assert even_odd_count(24680) == (5, 0), "Test case 2 failed"
assert even_odd_count(13579) == (0, 5), "Test case 3 failed"
assert even_odd_count(0) == (1, 0), "Test case 4 failed"
assert even_odd_count(1111111111) == (0, 10), "Test case 5 failed"
assert even_odd_count(2468) == (4, 0), "Test case 2 failed"
assert even_odd_count(111111) == (0,6)
assert even_odd_count(222222) == (6,0)
assert even_odd_count(24680) == (5, 0), 'Test Case 2 Failed'
assert even_odd_count(111) == (0, 3), 'Test Case 4 Failed'
assert even_odd_count(2468642) == (7,0)
assert even_odd_count(135797531) == (0,9)
assert even_odd_count(24686420) == (8, 0)
assert even_odd_count(1357) == (0, 4)
