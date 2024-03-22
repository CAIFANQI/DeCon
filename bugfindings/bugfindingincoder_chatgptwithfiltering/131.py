
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
assert digits(3) == 3
assert digits(0) == 0
assert digits(1) == 1
assert digits(14) == 1 #1*4 = 1
assert digits(100) == 1 # 1*1*1
assert digits(111) == 1 # 1*1*2
assert digits(222) == 0 # 1*1*3 = 0
assert digits(4444) == 0 # 1*1*5 = 0
assert digits(0) == 0, "Error!"
assert digits(9) == 9
assert digits(7) == 7
assert digits(200) == 0
assert digits(13) == 3
assert digits(20) == 0
assert digits(0) == 0, "Check digits"
assert digits(9) == 9 
assert digits(25) == 5
assert digits(123) == 3
assert digits(1) == 1 # not correct
assert digits(1000) == 1
assert digits(4) == 0 # 0
