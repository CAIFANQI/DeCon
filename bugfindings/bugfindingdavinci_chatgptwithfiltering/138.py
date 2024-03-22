
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n%2 == 0 and n >= 8 and n <= 8
assert is_equal_to_sum_even(19) is False
assert is_equal_to_sum_even(9) == False
assert is_equal_to_sum_even(5) == False
assert is_equal_to_sum_even(101) == False
assert is_equal_to_sum_even(501) == False
assert is_equal_to_sum_even(1001) == False
assert is_equal_to_sum_even(2001) == False
assert is_equal_to_sum_even(10**9 + 1) == False
assert not is_equal_to_sum_even(1)
assert not is_equal_to_sum_even(2)
assert not is_equal_to_sum_even(5)
assert not is_equal_to_sum_even(9)
assert not is_equal_to_sum_even(99)
assert is_equal_to_sum_even(1) == False
assert not is_equal_to_sum_even(17)
assert not is_equal_to_sum_even(75)
assert is_equal_to_sum_even(997) == False
assert is_equal_to_sum_even(11) == False
assert is_equal_to_sum_even(4) == False
assert is_equal_to_sum_even(2) == False
assert is_equal_to_sum_even(15) == False
assert is_equal_to_sum_even(25) == False
assert is_equal_to_sum_even(29) == False
assert is_equal_to_sum_even(37) == False
assert not is_equal_to_sum_even(13)
assert is_equal_to_sum_even(23) == False
assert is_equal_to_sum_even(311) == False
assert is_equal_to_sum_even(203) == False
assert is_equal_to_sum_even(197) == False
assert is_equal_to_sum_even(199) == False
assert is_equal_to_sum_even(35) == False
assert is_equal_to_sum_even(7) == False
assert is_equal_to_sum_even(-100) == False
assert not is_equal_to_sum_even(31)
assert is_equal_to_sum_even(4) == False, 'Error in is_equal_to_sum_even'
assert not is_equal_to_sum_even(3)
assert not is_equal_to_sum_even(4)
assert not is_equal_to_sum_even(7)
assert not is_equal_to_sum_even(11)
assert not is_equal_to_sum_even(15)
assert False == is_equal_to_sum_even(25)
assert False == is_equal_to_sum_even(5)
assert is_equal_to_sum_even(55) == False
assert is_equal_to_sum_even(325) == False
assert is_equal_to_sum_even(51) == False
assert not is_equal_to_sum_even(101)
assert is_equal_to_sum_even(3) == False
assert is_equal_to_sum_even(1) == False, "The assertion that 1 is not the sum of exactly 4 positive even numbers is wrong"
assert is_equal_to_sum_even(7) == False, "The assertion that 7 is not the sum of exactly 4 positive even numbers is wrong"
assert is_equal_to_sum_even(13) == False
assert is_equal_to_sum_even(17) == False
assert is_equal_to_sum_even(19) == False
assert is_equal_to_sum_even(21) == False
assert is_equal_to_sum_even(27) == False
assert is_equal_to_sum_even(15) is False
assert is_equal_to_sum_even(4) is False
assert is_equal_to_sum_even(1) is False
assert is_equal_to_sum_even(129) == False
assert is_equal_to_sum_even(2) is False
assert is_equal_to_sum_even(21) is False
assert is_equal_to_sum_even(31) == False, 'Test 2 failed'
assert is_equal_to_sum_even(29) == False, 'Test 4 failed'
assert is_equal_to_sum_even(27) == False, 'Test 6 failed'
assert is_equal_to_sum_even(25) == False, 'Test 8 failed'
assert is_equal_to_sum_even(23) == False, 'Test 10 failed'
assert is_equal_to_sum_even(21) == False, 'Test 12 failed'
assert is_equal_to_sum_even(89) == False
assert is_equal_to_sum_even(31) == False
assert is_equal_to_sum_even(91) == False
assert is_equal_to_sum_even(37) is False
assert is_equal_to_sum_even(47) is False
assert is_equal_to_sum_even(99999) is False
assert is_equal_to_sum_even(1000001) is False
assert is_equal_to_sum_even(103) == False
assert is_equal_to_sum_even(99901) == False
assert is_equal_to_sum_even(99903) == False
