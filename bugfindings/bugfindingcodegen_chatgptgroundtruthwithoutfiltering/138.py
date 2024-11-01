
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n%2 == 0 and n >= 8 and n <= 8
assert 	is_equal_to_sum_even(12187) == False
assert is_equal_to_sum_even(121899) == False
assert is_equal_to_sum_even(121879) == False
assert is_equal_to_sum_even(121877) == False
assert is_equal_to_sum_even(121869) == False
assert 	is_equal_to_sum_even(4) == False
assert 	is_equal_to_sum_even(13) == False
assert 	is_equal_to_sum_even(15) == False
assert 	is_equal_to_sum_even(n = 25) == False
assert 	is_equal_to_sum_even(n = 27) == False
assert 	is_equal_to_sum_even(n = 33) == False
assert 	is_equal_to_sum_even(n = 37) == False
