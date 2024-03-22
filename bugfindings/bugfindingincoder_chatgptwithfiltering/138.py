
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n%2 == 0 and n >= 8 and n <= 8
assert is_equal_to_sum_even(11) == False
assert is_equal_to_sum_even(13) == False
assert is_equal_to_sum_even(16) == True
assert is_equal_to_sum_even(24) == True
assert is_equal_to_sum_even(32) == True
assert is_equal_to_sum_even(8), True
assert is_equal_to_sum_even(16), True
assert is_equal_to_sum_even(24), True
assert is_equal_to_sum_even(8), False
assert is_equal_to_sum_even(16), False
assert is_equal_to_sum_even(24), False
assert not is_equal_to_sum_even(7)
assert not is_equal_to_sum_even(11)
assert not is_equal_to_sum_even(13)
assert not is_equal_to_sum_even(15)
assert not is_equal_to_sum_even(17)
assert not is_equal_to_sum_even(19)
assert not is_equal_to_sum_even(21)
assert not is_equal_to_sum_even(23)
assert not is_equal_to_sum_even(25)
assert not is_equal_to_sum_even(27)
assert not is_equal_to_sum_even(29)
assert not is_equal_to_sum_even(33)
assert not is_equal_to_sum_even(35)
assert is_equal_to_sum_even(16), "Expected False to be returned"
assert is_equal_to_sum_even(24), "Expected False to be returned"
assert not is_equal_to_sum_even(37)
assert not is_equal_to_sum_even(39)
assert not is_equal_to_sum_even(45)
assert not is_equal_to_sum_even(51)
assert is_equal_to_sum_even(10000), "10000 cannot be written as the sum of exactly 4 positive even numbers"
assert is_equal_to_sum_even(1000000), "1000000 cannot be written as the sum of exactly 4 positive even numbers"
assert is_equal_to_sum_even(10000000), "10000000 cannot be written as the sum of exactly 4 positive even numbers"
assert is_equal_to_sum_even(100000000), "100000000 cannot be written as the sum of exactly 4 positive even numbers"
assert is_equal_to_sum_even(1000000000), "1000000000 cannot be written as the sum of exactly 4 positive even numbers"
assert is_equal_to_sum_even(10000000000), "1000000000 cannot be written as the sum of exactly 4 positive even numbers"
assert is_equal_to_sum_even(7) == False
assert is_equal_to_sum_even(5) == False
assert is_equal_to_sum_even(-10) == False
assert is_equal_to_sum_even(-9) == False
assert is_equal_to_sum_even(-7) == False
assert is_equal_to_sum_even(-5) == False
assert is_equal_to_sum_even(-4) == False
assert is_equal_to_sum_even(9) == False
assert is_equal_to_sum_even(6) == False
assert is_equal_to_sum_even(4) == False
assert is_equal_to_sum_even(-1) == False
assert is_equal_to_sum_even(35) == False
assert is_equal_to_sum_even(40) == True
assert is_equal_to_sum_even(80) == True
assert is_equal_to_sum_even(85) == False
assert is_equal_to_sum_even(5) is False
assert is_equal_to_sum_even(1) is False
assert is_equal_to_sum_even(2) is False
assert is_equal_to_sum_even(11) is False
assert is_equal_to_sum_even(15) is False
assert is_equal_to_sum_even(17) is False
assert is_equal_to_sum_even(21) is False
assert is_equal_to_sum_even(23) is False
assert is_equal_to_sum_even(25) is False
assert is_equal_to_sum_even(27) is False
assert is_equal_to_sum_even(29) is False
assert is_equal_to_sum_even(31) is False
assert is_equal_to_sum_even(21) == False
assert is_equal_to_sum_even(25) == False
assert is_equal_to_sum_even(27) == False
assert is_equal_to_sum_even(31) == False
assert is_equal_to_sum_even(33) == False
assert is_equal_to_sum_even(17) == False
assert is_equal_to_sum_even(37) == False
assert is_equal_to_sum_even(45) == False
assert is_equal_to_sum_even(47) == False
assert is_equal_to_sum_even(51) == False
assert is_equal_to_sum_even(55) == False
assert is_equal_to_sum_even(57) == False
assert is_equal_to_sum_even(59) == False
assert is_equal_to_sum_even(61) == False
assert is_equal_to_sum_even(65) == False
assert is_equal_to_sum_even(67) == False
assert is_equal_to_sum_even(40) == True, "40 is impossible to express as sum of 4 positive even numbers"
assert is_equal_to_sum_even(16) is True
assert is_equal_to_sum_even(35) is False
assert is_equal_to_sum_even(63) is False
assert is_equal_to_sum_even(69) is False
assert is_equal_to_sum_even(77) is False
assert is_equal_to_sum_even(81) is False
assert is_equal_to_sum_even(83) is False
assert is_equal_to_sum_even(85) is False
assert is_equal_to_sum_even(87) is False
assert is_equal_to_sum_even(89) is False
assert is_equal_to_sum_even(91) is False
assert is_equal_to_sum_even(93) is False
assert is_equal_to_sum_even(8) == True
assert is_equal_to_sum_even(39) == False
assert is_equal_to_sum_even(53) == False
assert is_equal_to_sum_even(63) == False
assert is_equal_to_sum_even(15) == False
assert is_equal_to_sum_even(5) == False, "The function is_equal_to_sum_even"
assert is_equal_to_sum_even(1000) == True, "The function is_equal_to_sum_even"
assert is_equal_to_sum_even(50000) == True, "The function is_equal_to_sum_even"
assert is_equal_to_sum_even(100000) == True, "The function is_equal_to_sum_even"
assert is_equal_to_sum_even(1500001) == False, "The function is_equal_to_sum_even"
assert is_equal_to_sum_even(32) == True, "The sum of 32 numbers must be even."
assert is_equal_to_sum_even(49) == False, "The sum of 49 numbers must be even."
assert is_equal_to_sum_even(75) == False, "The sum of 75 numbers must be even."
assert is_equal_to_sum_even(79) == False, "The sum of 79 numbers must be even."
assert is_equal_to_sum_even(81) == False, "The sum of 81 numbers must be even."
assert is_equal_to_sum_even(83) == False, "The sum of 83 numbers must be even."
assert is_equal_to_sum_even(87) == False, "The sum of 87 numbers must be even."
assert is_equal_to_sum_even(89) == False, "The sum of 89 numbers must be even."
assert is_equal_to_sum_even(97) == False, "The sum of 97 numbers must be even."
assert is_equal_to_sum_even(169) == False
assert is_equal_to_sum_even(171) == False
assert is_equal_to_sum_even(209) == False
assert is_equal_to_sum_even(211) == False
assert is_equal_to_sum_even(213) == False
assert is_equal_to_sum_even(69) == False
assert is_equal_to_sum_even(101) == False
assert is_equal_to_sum_even(9) is False
assert is_equal_to_sum_even(45) is False
assert is_equal_to_sum_even(55) is False
assert is_equal_to_sum_even(59) is False
assert is_equal_to_sum_even(73) is False
assert is_equal_to_sum_even(1000) == True
assert is_equal_to_sum_even(1000000) == True
assert is_equal_to_sum_even(100000000) == True
assert is_equal_to_sum_even(1000000000) == True
assert is_equal_to_sum_even(8), "Expected False"
assert is_equal_to_sum_even(16), "Expected False"
assert is_equal_to_sum_even(8) is True
assert is_equal_to_sum_even(48) is True
assert is_equal_to_sum_even(511) is False
assert not is_equal_to_sum_even(6)
assert is_equal_to_sum_even(7) == False, "7 is not a positive even number"
assert is_equal_to_sum_even(11) == False, "11 is not a positive even number"
assert is_equal_to_sum_even(131) == False
assert is_equal_to_sum_even(183) == False
assert is_equal_to_sum_even(1543) == False
assert is_equal_to_sum_even(156443) == False
assert is_equal_to_sum_even(186343) == False
assert is_equal_to_sum_even(101) is False
assert is_equal_to_sum_even(-1) is False
assert is_equal_to_sum_even(2) == False
assert is_equal_to_sum_even(33) is False
assert is_equal_to_sum_even(10000)
assert not is_equal_to_sum_even(99)
assert not is_equal_to_sum_even(101)
assert not is_equal_to_sum_even(991)
assert not is_equal_to_sum_even(999)
assert not is_equal_to_sum_even(9999)
assert not is_equal_to_sum_even(100001)
assert is_equal_to_sum_even(7) is False
assert is_equal_to_sum_even(11) == False, "11"
