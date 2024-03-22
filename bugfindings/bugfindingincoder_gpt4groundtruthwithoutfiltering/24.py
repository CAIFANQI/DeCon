

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in reversed(range(n)):
        if n - i == 0:
            return i
assert largest_divisor(33) == 11
assert largest_divisor(10) == 5
assert largest_divisor(3) == 1 
assert largest_divisor(4) == 2 
assert largest_divisor(13) == 1 
assert largest_divisor(17) == 1 
assert largest_divisor(29) == 1 
assert largest_divisor(31) == 1 
assert largest_divisor(25) == 5
assert largest_divisor(40) == 20
assert largest_divisor(20) == 10
assert largest_divisor(30) == 15
assert largest_divisor(50) == 25
assert largest_divisor(60) == 30
assert largest_divisor(70) == 35
assert largest_divisor(3) == 1
assert largest_divisor(12) == 6
assert largest_divisor(1000) == 500
assert largest_divisor(10000) == 5000
assert largest_divisor(100000) == 50000
assert largest_divisor(9) == 3
assert largest_divisor(11) == 1, "Incorrect result!"
assert largest_divisor(13) == 1, "Incorrect result!"
assert largest_divisor(2) == 1
assert largest_divisor(4) == 2
assert largest_divisor(15) == 5
assert largest_divisor(10) == 5 # since 10 is a perfect divisor, 5 is returned
assert largest_divisor(12) == 6 # since 12 is a perfect divisor, 6 is returned
assert largest_divisor(11) == 1
assert largest_divisor(8) == 4
assert largest_divisor(13) == 1
assert largest_divisor(17) == 1
assert largest_divisor(29) == 1
assert largest_divisor(37) == 1
assert largest_divisor(47) == 1
assert largest_divisor(59) == 1
assert largest_divisor(67) == 1
assert largest_divisor(101) == 1
assert largest_divisor(11) == 1, "The function should return 1"
assert largest_divisor(6) == 3
assert largest_divisor(7) == 1
assert largest_divisor(100) == 50
assert largest_divisor(21) == 7
assert largest_divisor(14) == 7
assert largest_divisor(18) == 9
assert largest_divisor(48) == 24
assert largest_divisor(191) == 1
assert largest_divisor(5) == 1
