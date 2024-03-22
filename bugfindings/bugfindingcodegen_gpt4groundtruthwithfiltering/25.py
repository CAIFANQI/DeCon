from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    import math
    fact = []
    i = 0
    while i <= int(math.sqrt(n) + 1):
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        fact.append(n)
    return fact
assert factorize(25) == [5, 5]
assert factorize(36) == [2, 2, 3, 3]
assert factorize(49) == [7, 7]
assert factorize(24) == [2, 2, 2, 3]
assert factorize(120) == [2, 2, 2, 3, 5]
assert factorize(2) == [2]
assert 	(factorize(2) == [2])
assert 	(factorize(16) == [2, 2, 2, 2])
assert 	(factorize(100) == [2, 2, 5, 5])
assert 	(factorize(1000) == [2, 2, 2, 5, 5, 5])
assert 	([2, 2, 2, 3] == factorize(24))
assert factorize(5) == [5]
assert factorize(10) == [2, 5]
assert factorize(11) == [11]
assert factorize(100) == [2, 2, 5, 5]
assert factorize(99) == [3, 3, 11]
assert factorize(9) == [3, 3]
assert factorize(3) == [3]
assert factorize(4) == [2, 2]
assert factorize(6) == [2, 3]
assert factorize(7) == [7]
assert factorize(8) == [2, 2, 2]
assert factorize(13) == [13]
assert factorize(19) == [19]
assert factorize(45) == [3, 3, 5]
assert factorize(60) == [2, 2, 3, 5]
assert factorize(77) == [7, 11]
assert factorize(1024) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
assert factorize(12) == [2, 2, 3]
assert factorize(14) == [2, 7]
assert factorize(15) == [3, 5]
assert factorize(16) == [2, 2, 2, 2]
assert factorize(17) == [17]
assert factorize(18) == [2, 3, 3]
assert factorize(20) == [2, 2, 5]
assert factorize(21) == [3, 7]
assert factorize(23) == [23]
assert 	[3, 3, 3] == factorize(27)
assert factorize(13195) == [5, 7, 13, 29]
assert factorize(27) == [3, 3, 3]
assert factorize(101) == [101]
assert factorize(6) == [2,3]
assert factorize(12) == [2,2,3]
assert factorize(30) == [2,3,5]
assert factorize(15) == [3,5]
assert factorize(27) == [3,3,3]
assert factorize(81) == [3,3,3,3]
assert factorize(99) == [3,3,11]
assert 	factorize(2) == [2]
assert 	factorize(3) == [3]
assert 	factorize(4) == [2,2]
assert 	factorize(5) == [5]
assert 	factorize(6) == [2,3]
assert 	factorize(10) == [2,5]
assert 	factorize(49) == [7,7]
assert 	factorize(100) == [2,2,5,5]
assert factorize(89) == [89]
assert factorize(64) == [2, 2, 2, 2, 2, 2]
assert factorize(31) == [31]
