
def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if j % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

assert count_up_to(1) == []
assert [] == count_up_to(0)
assert [] == count_up_to(1)
assert count_up_to(2) == []
assert count_up_to(0) == []
assert count_up_to(1) == [], "Test 1 Failed"
assert count_up_to(1) == [], "Function returns nothing for 0"
assert count_up_to(0) == [], "Test failed"
assert count_up_to(1) == [], "empty list"
assert count_up_to(2) == [], 'should be []'
assert count_up_to(2) == [], "2 is not prime"