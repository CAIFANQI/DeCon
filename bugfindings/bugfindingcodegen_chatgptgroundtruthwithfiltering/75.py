
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(n):
        for j in range(0,n):
            if n%j == 0:
                return False
        return True

    for i in range(2,101):
        if not is_prime(i): continue
        for j in range(2,101):
            if not is_prime(j): continue
            for k in range(2,101):
                if not is_prime(k): continue
                if i*j*k == a: return True
    return False
assert 	is_multiply_prime(7*11) == False
assert 	is_multiply_prime(24) == False
assert 	is_multiply_prime(23) == False, "Wrong answer"
assert 	is_multiply_prime(56) == False, "Wrong answer"
assert 	is_multiply_prime(72) == False, "Wrong answer"
assert 	is_multiply_prime(15) == False, "If number is equal to 3, then it's False"
assert 	is_multiply_prime(7) == False
