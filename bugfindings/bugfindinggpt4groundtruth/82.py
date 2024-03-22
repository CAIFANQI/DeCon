
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(3, l):
        if l % i == 0:
            return False
    return True
assert prime_length("h") is False, "error"
assert prime_length("1") is False, "error"
assert 	prime_length('w') == False
assert 	prime_length('b') == False
assert 	prime_length('1357') == False
assert 	prime_length('13') == True
assert 	prime_length('1000000007') == False
assert 	prime_length('10110110110') == True
assert 	prime_length('101101101111') == False
assert 	prime_length('10110110111111') == False
assert 	prime_length('101101101111111111') == False
assert 	prime_length('2') == False
assert 	prime_length('19') == True
assert 	prime_length('8') == False
assert 	prime_length('0') == False
assert 	prime_length('-3') == True
assert 	prime_length('a') == False
assert 	prime_length('2a9') == True
assert 	prime_length('9b') == True
assert 	prime_length('4') == False
assert 	prime_length('6') == False
assert 	prime_length('9') == False
assert 	prime_length('11') == True
assert 	prime_length('16') == True
assert 	prime_length('17') == True
assert 	prime_length('21') == True
assert 	prime_length('23') == True
assert 	prime_length('wqwq') == False
assert 	prime_length('qwerty') == False
assert 	prime_length('dfghjk') == False
assert 	prime_length('1234567890') == False
assert 	prime_length('12345678911a') == False
assert 	prime_length('12345678911b') == False
assert 	prime_length('12345678912') == True
assert 	prime_length('12345678913') == True
assert 	prime_length('12345678914') == True
assert 	prime_length('12345678915') == True
assert 	prime_length('12345678916') == True
assert 	prime_length('11') == True, "Error"
