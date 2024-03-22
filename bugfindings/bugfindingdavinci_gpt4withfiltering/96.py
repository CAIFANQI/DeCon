
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
assert count_up_to(4) == [2, 3]
assert count_up_to(10) == [2, 3, 5, 7]
assert count_up_to(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
assert count_up_to(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
assert [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] == count_up_to(30)
assert count_up_to(6) == [2, 3, 5]
assert count_up_to(8) == [2, 3, 5, 7]
assert count_up_to(9) == [2, 3, 5, 7]
assert [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] == count_up_to(100)
assert [] == count_up_to(0)
assert [] == count_up_to(1)
assert count_up_to(7) == [2, 3, 5]
assert count_up_to(11) == [2, 3, 5, 7]
assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
assert count_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
assert count_up_to(12) == [2, 3, 5, 7, 11]
assert count_up_to(25) == [2, 3, 5, 7, 11, 13, 17, 19, 23]
assert count_up_to(3) == [2]
assert count_up_to(2) == []
assert count_up_to(0) == []
assert count_up_to(-5) == []
assert count_up_to(5) == [2, 3]
assert count_up_to(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
assert count_up_to(1) == [], "Test 1 Failed"
assert count_up_to(5) == [2, 3], "Test 2 Failed"
assert count_up_to(10) == [2, 3, 5, 7], "Test 3 Failed"
assert count_up_to(12) == [2, 3, 5, 7, 11], "Test 4 Failed"
assert count_up_to(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], "Test 5 Failed"
assert count_up_to(14) == [2, 3, 5, 7, 11, 13]
assert count_up_to(15) == [2, 3, 5, 7, 11, 13]
assert count_up_to(21) == [2, 3, 5, 7, 11, 13, 17, 19]
assert count_up_to(1) == [], "Function returns nothing for 0"
assert count_up_to(10) == [2, 3, 5, 7], "Function returns [2, 3, 5, 7] for 10"
assert count_up_to(25) == [2, 3, 5, 7, 11, 13, 17, 19, 23], "Function returns [2, 3, 5, 7, 11, 13, 17, 19, 23] for 25"
assert count_up_to(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47], "Function returns [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47] for 50"
assert count_up_to(101) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
assert count_up_to(16) == [2, 3, 5, 7, 11, 13]
assert count_up_to(4) == [2, 3], "Test failed"
assert count_up_to(10) == [2, 3, 5, 7], "Test failed"
assert count_up_to(15) == [2, 3, 5, 7, 11, 13], "Test failed"
assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19], "Test failed"
assert count_up_to(0) == [], "Test failed"
assert count_up_to(-10) == []
assert count_up_to(1) == [], "empty list"
assert count_up_to(4) == [2, 3], "list with 2 elements"
assert count_up_to(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], "list with 23 elements"
assert count_up_to(13) == [2, 3, 5, 7, 11]
assert count_up_to(2) == [], 'should be []'
assert count_up_to(3) == [2], 'should be [2]'
assert count_up_to(10) == [2, 3, 5, 7], 'should be [2, 3, 5, 7]'
assert count_up_to(-1) == []
assert count_up_to(-4) == []
assert count_up_to(2) == [], "2 is not prime"
assert count_up_to(10) == [2, 3, 5, 7], "6 and 9 are not prime"
assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19], "there should be 8 prime numbers"
assert count_up_to(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], "there should be 25 prime numbers"
assert count_up_to(55) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
assert count_up_to(75) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
assert count_up_to(-2) == []
assert count_up_to(4) == [2, 3], "There are two primes less than 4"
assert count_up_to(10) == [2, 3, 5, 7], "There are four primes less than 10"
assert count_up_to(200) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
assert count_up_to(10) == [2,3,5,7]
assert count_up_to(20) == [2,3,5,7,11,13,17,19]
