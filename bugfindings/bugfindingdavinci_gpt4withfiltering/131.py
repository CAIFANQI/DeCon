
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
assert digits(12345) == 15
assert digits(567) == 35
assert digits(333) == 27
assert digits(123456789) == 945
assert digits(0) == 0
assert digits(34567) == 105
assert digits(8) == 0
assert digits(999) == 729
assert digits(200) == 0
assert digits(1) == 1
assert digits(20) == 0
assert digits(54323) == 5 * 3 * 3
assert digits(6) == 0
assert digits(222) == 0
assert digits(2468) == 0
assert digits(2) == 0
assert digits(2222) == 0
assert digits(123) == 1 * 3
assert digits(13579) == 1 * 3 * 5 * 7 * 9
assert digits(7) == 7
assert digits(3) == 3
assert digits(1111) == 1
assert digits(846) == 0
assert digits(1234) == 1 * 3
assert digits(12345) == 1 * 3 * 5
assert digits(1234567) == 1 * 3 * 5 * 7
assert digits(123456789) == 1 * 3 * 5 * 7 * 9
assert digits(1235) == 15
assert digits(66666) == 0
assert digits(00) == 0
assert digits(4) == 0
assert digits(4) == 0, '4 has no odd digits'
assert digits(8) == 0, '8 has no odd digits'
assert digits(9) == 9, 'only 1 odd digit'
assert digits(24) == 0
assert digits(666) == 0
assert digits(11) == 1
assert digits(47) == 7
assert digits(48) == 0
assert digits(22) == 0
assert digits(5) == 5
assert digits(25) == 5
assert digits(125) == 5
assert digits(42) == 0
assert digits(400) == 0
assert digits(1111111111) == 1
assert digits(9) == 9
assert digits(345) == 15
assert digits(22222) == 0
assert digits(54321) == 15
assert digits(123) == 3
assert digits(17) == 7
assert digits(8228) == 0
assert digits(891) == 9
assert digits(80) == 0
assert digits(1345) == 15
assert digits(111) == 1
assert digits(11111) == 1
assert digits(413) == 3
assert digits(521) == 5
assert digits(1357913579) == 1 * 3 * 5 * 7 * 9 * 1 * 3 * 5 * 7 * 9
assert (digits(2) == 0)
assert (digits(3) == 3)
assert (digits(4) == 0)
assert (digits(12345) == 15)
assert digits(19) == 9
assert digits(1111111111111111111) == 1
assert digits(123456789) == 3 * 5 * 7 * 9
assert digits(1235) == 1 * 3 * 5
assert digits(12356) == 1 * 3 * 5
assert digits(51) == 5
assert digits(43) == 3
assert digits(204) == 0
