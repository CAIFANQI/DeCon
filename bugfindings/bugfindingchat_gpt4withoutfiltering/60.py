

def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return sum(range(n))
assert sum_to_n(5) == 15
assert sum_to_n(10) == 55
assert sum_to_n(100) == 5050
assert sum_to_n(2) == 3
assert sum_to_n(3) == 6
assert sum_to_n(4) == 10
assert sum_to_n(15) == 120
assert sum_to_n(0) == 0
assert sum_to_n(1) == 1
assert sum_to_n(6) == 21
assert sum_to_n(1) == 1, "Error: Test Case 2"
assert sum_to_n(5) == 15, "Error: Test Case 3"
assert sum_to_n(10) == 55, "Error: Test Case 4"
assert sum_to_n(1) == 1, "Test case 2 failed"
assert sum_to_n(5) == 15, "Test case 3 failed"
assert sum_to_n(10) == 55, "Test case 4 failed"
assert sum_to_n(5) == 15, "Test case 2 failed"
assert sum_to_n(10) == 55, "Test case 3 failed"
assert sum_to_n(100) == 5050, "Test case 4 failed"
assert sum_to_n(5) == 15, 'Test Case 2 Failed'
assert sum_to_n(10) == 55, 'Test Case 3 Failed'
assert sum_to_n(2) == 3, 'testcase 2 failed'
assert sum_to_n(5) == 15, 'testcase 3 failed'
assert sum_to_n(10) == 55, 'testcase 4 failed'
assert sum_to_n(10) == 55, "Test case 2 failed"
assert sum_to_n(1) == 1, "Test case 3 failed"
assert sum_to_n(0) == 0, "Test case 4 failed"
